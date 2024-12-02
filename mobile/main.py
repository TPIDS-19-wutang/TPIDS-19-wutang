import requests
from datetime import datetime
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget

# Use this URL to connect the app to the local server from an Android emulator.
# API_BASE_URL = "http://10.0.2.2:5001"
API_BASE_URL = "http://127.0.0.1:5001"

class Navbar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 60
        self.padding = [20, 10]
        self.spacing = 10
        self.canvas.before.clear()

        with self.canvas.before:
            Color(0.85, 0.65, 0.13, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        title = Label(
            text="Hotel Trivium",
            font_size=30,
            color=(1, 1, 1, 1),
            bold=True
        )
        self.add_widget(title)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos


class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", spacing=10)
        self.layout.canvas.before.clear()

        with self.layout.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        self.navbar = Navbar()
        self.main_content = BoxLayout(orientation="vertical", padding=[30, 20], spacing=20)

        self.layout.add_widget(self.navbar)
        self.layout.add_widget(self.main_content)
        self.add_widget(self.layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def create_label(self, text, font_size=20, color=(0.2, 0.2, 0.2, 1), **kwargs):
        return Label(text=text, font_size=font_size, color=color, **kwargs)

    def create_button(self, text, on_press_callback, height=50, **kwargs):
        button = Button(
            text=text,
            size_hint_y=None,
            height=height,
            background_color=(0.85, 0.65, 0.13, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        button.bind(on_press=on_press_callback)
        return button


class HomeScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_content.add_widget(self.create_label("Buscar Reserva", font_size=38, bold=True))

        self.reservation_input = TextInput(
            hint_text="Código de reserva",
            multiline=False,
            size_hint_y=None,
            height=60,
            padding_y=[10, 10],
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.lastname_input = TextInput(
            hint_text="Apellido",
            multiline=False,
            size_hint_y=None,
            height=60,
            padding_y=[10, 10],
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.error_label = self.create_label("", font_size=18, color=(1, 0, 0, 1))

        self.search_button = self.create_button("Buscar Reserva", self.validate_reservation)

        self.main_content.add_widget(self.reservation_input)
        self.main_content.add_widget(self.lastname_input)
        self.main_content.add_widget(self.error_label)
        self.main_content.add_widget(self.search_button)

    def validate_reservation(self, instance):
        reservation_id = self.reservation_input.text.strip()
        lastname = self.lastname_input.text.strip().lower()

        try:
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
        except requests.exceptions.RequestException:
            self.error_label.text = "Error de conexión con el servidor."


class ServicesScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_content.spacing = 20

        self.location_label = self.create_label(
            "Lugar: Hotel Trivium",
            font_size=38,
            size_hint_y=None,
            height=30,
            color=(0, 0, 0, 1),
            halign="left",
            valign="middle",
            bold=True
        )

        self.dates_label = self.create_label(
            "Fechas: Check-in - Check-out",
            font_size=38,
            size_hint_y=None,
            height=30,
            color=(0, 0, 0, 1),
            halign="left",
            valign="middle",
            bold=True
        )

        self.main_content.add_widget(self.location_label)
        self.main_content.add_widget(self.dates_label)
        self.main_content.add_widget(Widget(size_hint_y=None, height=5))
        self.main_content.add_widget(self.create_label("Servicios Contratados", font_size=34, size_hint_y=None, height=50))

        self.contracted_services_list = self._create_service_list()
        self.main_content.add_widget(self.contracted_services_list)
        self.main_content.add_widget(Widget(size_hint_y=None, height=5))
        self.main_content.add_widget(self.create_label("Servicios Disponibles", font_size=34, size_hint_y=None, height=50))
        self.available_services_list = self._create_service_list()
        self.main_content.add_widget(self.available_services_list)

        bottom_spacer = Widget(size_hint_y=1)
        self.main_content.add_widget(bottom_spacer)

        button_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=60)
        button_layout.add_widget(self.create_button("Contratar Servicios", self.confirm_services))
        button_layout.add_widget(self.create_button("Volver al Menú Principal", self.go_back_to_main))
        self.main_content.add_widget(button_layout)

        self.selected_services = []
        self.contracted_services = []
        self.available_services = []
        self.newly_added_services = []

    def _create_service_list(self):
        service_list = BoxLayout(orientation="vertical", spacing=5, size_hint_y=None)
        service_list.bind(minimum_height=service_list.setter('height'))
        return service_list
    
    def on_enter(self, *args):
        self.selected_services = []

    def format_date(self, date_string):
        if not date_string:
            return "N/A"
        try:
            parsed_date = datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %Z")
            return parsed_date.strftime("%d/%m/%Y")
        except ValueError:
            try:
                dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
                return dt.strftime("%d/%m/%Y")
            except ValueError:
                return "N/A"
        
    def load_services(self, id_reservation):
        response = requests.get(f"{API_BASE_URL}/services/{id_reservation}")
        services = response.json().get("data", {})
        self.contracted_services = services.get("contracted_services", [])
        self.available_services = services.get("available_services", [])

        app = App.get_running_app()
        check_in_raw = app.current_reservation.get("check_in", None)
        check_out_raw = app.current_reservation.get("check_out", None)
        check_in = self.format_date(check_in_raw)
        check_out = self.format_date(check_out_raw)
        location = app.current_reservation.get("location")

        self.location_label.text = f"Lugar: Hotel Trivium {location}"
        self.dates_label.text = f"Fechas: {check_in} - {check_out}"

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
        for service in services:
            if contracted:
                service_list.add_widget(self.create_label(service["name"], font_size=30, size_hint_y=None, height=30))
            else:
                button = self.create_button(
                    f'{service["name"]} - ${service["price"]}',
                    lambda instance, srv=service: self.toggle_service_selection(srv, instance),
                    height=50
                )
                service_list.add_widget(button)

    def toggle_service_selection(self, service, button):
        if service in self.selected_services:
            self.selected_services.remove(service)
            button.background_color = (0.85, 0.65, 0.13, 1)
        else:
            self.selected_services.append(service)
            button.background_color = (0, 1, 0, 1)

    def confirm_services(self, instance):
        app = App.get_running_app()
        id_reservation = app.current_reservation.get('id_reservation')

        contracted_service_ids = [service["id_service"] for service in self.contracted_services]
        selected_service_ids = [service["id_service"] for service in self.selected_services]

        combined_service_ids = list(set(contracted_service_ids + selected_service_ids))

        payload = {"services": combined_service_ids}

        payload = {"services": combined_service_ids}

        try:
            response = requests.put(f"{API_BASE_URL}/services/{id_reservation}", json=payload)
            response_data = response.json()

            if response.status_code == 200 and response_data.get("status") == "success":
                app.show_confirmation_screen(self.selected_services)
            else:
                error_message = response_data.get("message", "Error al actualizar los servicios.")
                self.main_content.add_widget(self.create_label(error_message, font_size=24, color=(1, 0, 0, 1)))

        except requests.exceptions.RequestException:
            error_label = self.create_label("Error de conexión con el servidor.", font_size=24, color=(1, 0, 0, 1))
            self.main_content.add_widget(error_label)

    def go_back_to_main(self, instance):
        self.manager.current = "home"


class ConfirmationScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_content.padding = [20, 20, 20, 20]

        self.success_label = self.create_label("", font_size=32, halign="center", valign="middle")
        
        self.main_content.add_widget(self.create_label("Confirmación", font_size=38, size_hint_y=None, height=50, bold=True))
        self.main_content.add_widget(self.success_label)
        self.main_content.add_widget(Widget(size_hint_y=None, height=20))
        self.main_content.add_widget(self.create_button("Volver al Menú Principal", self.go_back_to_main))

    def display_confirmation(self, selected_services):
        service_names = [service["name"] for service in selected_services]
        total_price = sum(float(service.get("price", 0)) for service in selected_services)
        self.success_label.text = (
            f"¡Servicios Contratados con Éxito!\n\n"
            f"Servicios: {', '.join(service_names)}\n"
            f"Precio Total: ${total_price:.2f}"
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
    def show_confirmation_screen(self, selected_services):
        self.sm.get_screen("confirmation").display_confirmation(selected_services)
        self.sm.current = "confirmation"


if __name__ == "__main__":
    HotelApp().run()
