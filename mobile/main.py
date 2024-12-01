import requests
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

API_BASE_URL = "http://127.0.0.1:5001"

class BaseScreen(Screen):
    def create_label(self, text, font_size=30, color=(1, 1, 1, 1), **kwargs):
        return Label(text=text, font_size=font_size, color=color, **kwargs)

    def create_button(self, text, on_press_callback, height=100, **kwargs):
        button = Button(text=text, size_hint_y=None, height=height, **kwargs)
        button.bind(on_press=on_press_callback)
        return button


class HomeScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.reservation_input = TextInput(hint_text="Código de reserva", multiline=False)
        self.lastname_input = TextInput(hint_text="Apellido", multiline=False)
        self.error_label = self.create_label("", font_size=30, color=(1, 0, 0, 1))

        self.search_button = self.create_button("Buscar Reserva", self.validate_reservation)

        self.layout.add_widget(self.create_label("Buscar Reserva", font_size=40))
        self.layout.add_widget(self.reservation_input)
        self.layout.add_widget(self.lastname_input)
        self.layout.add_widget(self.error_label)
        self.layout.add_widget(self.search_button)

        self.add_widget(self.layout)

    def validate_reservation(self, instance):
        reservation_id = self.reservation_input.text.strip()
        lastname = self.lastname_input.text.strip().lower()

        response = requests.get(
            f"{API_BASE_URL}/reservation/{reservation_id}",
            params={"lastname": lastname}
        )
        reservation = response.json()

        if reservation.get("status") == "success":
            self.error_label.text = ""
            app = App.get_running_app()
            app.current_reservation = reservation.get("data", {})
            app.show_services_screen()
        else:
            self.error_label.text = "Reserva no encontrada."


class ServicesScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=20)

        self.contracted_services_list = self._create_service_list()
        self.available_services_list = self._create_service_list()

        self.layout.add_widget(self.create_label("Reserva", font_size=40, size_hint_y=None, height=50))
        self.layout.add_widget(self.create_label("Servicios Contratados", font_size=34, size_hint_y=None, height=50))
        self.layout.add_widget(self.contracted_services_list)

        self.layout.add_widget(Widget(size_hint_y=None, height=20))

        self.layout.add_widget(self.create_label("Servicios Disponibles", font_size=34, size_hint_y=None, height=50))
        self.layout.add_widget(self.available_services_list)

        button_layout = BoxLayout(orientation="vertical", spacing=10)
        button_layout.add_widget(self.create_button("Contratar Servicios", self.confirm_services))
        button_layout.add_widget(self.create_button("Volver al Menú Principal", self.go_back_to_main))

        self.layout.add_widget(button_layout)
        self.add_widget(self.layout)

        self.selected_services = []
        self.contracted_services = []
        self.available_services = []
        self.newly_added_services = []

    def _create_service_list(self):
        service_list = BoxLayout(orientation="vertical", spacing=10, size_hint_y=None)
        service_list.bind(minimum_height=service_list.setter('height'))
        return service_list

    def load_services(self, id_reservation):
        response = requests.get(f"{API_BASE_URL}/services/{id_reservation}")
        services = response.json().get("data", {})
        self.contracted_services = services.get("contracted_services", [])
        self.available_services = services.get("available_services", [])

        self.contracted_services_list.clear_widgets()
        self.available_services_list.clear_widgets()

        if not self.contracted_services:
            self.contracted_services_list.add_widget(
                self.create_label("No hay servicios contratados.", font_size=24, color=(1, 0, 0, 1))
            )

        if not self.available_services:
            self.available_services_list.add_widget(
                self.create_label("No hay servicios disponibles.", font_size=24, color=(1, 0, 0, 1))
            )

        self._populate_services(self.contracted_services_list, self.contracted_services, contracted=True)
        self._populate_services(self.available_services_list, self.available_services, contracted=False)

    def _populate_services(self, service_list, services, contracted):
        service_list.clear_widgets()
        for service in services:
            if contracted:
                service_list.add_widget(self.create_label(service["name"], font_size=30, size_hint_y=None, height=30))
            else:
                button = self.create_button(
                    f'{service["name"]} - ${service["price"]}',
                    lambda instance, srv=service["name"]: self.toggle_service_selection(srv, instance),
                    height=50
                )
                service_list.add_widget(button)

    def toggle_service_selection(self, service, button):
        if service in self.selected_services:
            self.selected_services.remove(service)
            button.background_color = (1, 1, 1, 1)
        else:
            self.selected_services.append(service)
            button.background_color = (0, 1, 0, 1)

    def confirm_services(self, instance):
        app = App.get_running_app()
        id_reservation = app.current_reservation.get('id_reservation')

        contracted_service_ids = [
            service["id_service"] for service in self.contracted_services
        ]

        selected_service_ids = [
            service["id_service"]
            for service in self.available_services
            if service["name"] in self.selected_services
        ]

        combined_service_ids = list(set(contracted_service_ids + selected_service_ids))

        self.newly_added_services = [
            service["name"]
            for service in self.available_services
            if service["id_service"] in selected_service_ids and service["id_service"] not in contracted_service_ids
        ]

        payload = {
            "services": combined_service_ids
        }

        try:
            response = requests.put(f"{API_BASE_URL}/services/{id_reservation}", json=payload)
            response_data = response.json()

            if response.status_code == 200 and response_data.get("status") == "success":
                app.show_confirmation_screen()
            else:
                error_message = response_data.get("message", "Error al actualizar los servicios.")
                self.layout.add_widget(self.create_label(error_message, font_size=24, color=(1, 0, 0, 1)))

        except requests.exceptions.RequestException as e:
            error_label = self.create_label("Error de conexión con el servidor.", font_size=24, color=(1, 0, 0, 1))
            self.layout.add_widget(error_label)

    def go_back_to_main(self, instance):
        self.manager.current = "home"


class ConfirmationScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=20)
        self.success_label = self.create_label("", font_size=30, halign="center", valign="middle", color=(0, 1, 0, 1))

        self.layout.add_widget(self.create_label("Confirmación", font_size=40, size_hint_y=None, height=50))
        self.layout.add_widget(self.success_label)
        self.layout.add_widget(Widget(size_hint_y=None, height=20))
        self.layout.add_widget(self.create_button("Volver al Menú Principal", self.go_back_to_main))

        self.add_widget(self.layout)

    def display_confirmation(self, newly_selected_services):
        total_price = len(newly_selected_services) * 10
        self.success_label.text = (
            f"¡Servicios Contratados con Éxito!\n\n"
            f"Servicios: {', '.join(newly_selected_services)}\n"
            f"Precio Total: ${total_price}"
        )

    def go_back_to_main(self, instance):
        self.manager.current = "home"


class HotelApp(App):
    def build(self):
        self.current_reservation = {}
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(ServicesScreen(name="services"))
        self.sm.add_widget(ConfirmationScreen(name="confirmation"))
        return self.sm

    def show_services_screen(self):
        id_reservation = self.current_reservation.get('id_reservation')
        self.sm.get_screen("services").load_services(id_reservation)
        self.sm.current = "services"

    def show_confirmation_screen(self):
        newly_selected_services = self.sm.get_screen("services").newly_added_services
        self.sm.get_screen("confirmation").display_confirmation(newly_selected_services)
        self.sm.current = "confirmation"


if __name__ == "__main__":
    HotelApp().run()
