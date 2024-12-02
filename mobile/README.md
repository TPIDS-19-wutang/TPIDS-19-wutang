# Hotel Trivium

## Introducción
Hotel Trivium es una aplicación basada en Kivy para la gestión de servicios y reservas de hotel.

## Requisitos
- Python 3.x
- Kivy

## Instalación

1. **Clonar el repositorio**
   ```bash
   git clone git@github.com:TPIDS-19-wutang/TPIDS-19-wutang.git
   cd mobile
   ```

2. **Instalar dependencias**
   ```bash
   # Para la mayoría de los sistemas:
   python -m pip install kivy
   ```

   Adicionalmente, instalá la librería `requests`:
   ```bash
   python -m pip install requests
   ```

## Ejecución de la App Localmente

Para ejecutar la app en tu máquina local, ejecutá:

```bash
python main.py
```

Donde `main.py` es el archivo de Python que ejecuta la aplicación Kivy.

## Construcción para Android (APK)

Para construir la app para Android, necesitarás usar [Buildozer](https://buildozer.readthedocs.io/es/latest/). Instalá Buildozer con:

```bash
python -m pip install buildozer
```

1. **Crear un archivo de configuración de Buildozer**
   - Inicializá Buildozer en tu directorio del proyecto:
   ```bash
   buildozer init
   ```

3. **Construir el APK**
   - Ejecutá Buildozer para crear el APK:
   ```bash
   buildozer -v android debug
   ```

   Este comando compilará tu app y producirá un archivo `.apk` que podes instalar en dispositivos Android.

4. **Desplegar el APK**
   - Después de construir, podes desplegar el APK directamente en un dispositivo Android conectado:
   ```bash
   buildozer android deploy run
   ```

## Cómo Correr el APK en Android Studio

Para probar y ejecutar el APK de la aplicación Kivy en Android Studio, seguí estos pasos:

1. **Instala Android Studio**
   Si aún no tienes Android Studio instalado, podes descargarlo desde [aquí](https://developer.android.com/studio). Seguí las instrucciones de instalación proporcionadas en el sitio web.

2. **Abrir Android Studio**
   Iniciá Android Studio y en la pantalla de bienvenida, seleccioná "Profile or debug APK".

3. **Selecciona el APK**
   Buscá y seleccioná el archivo APK que has generado con Buildozer. Android Studio cargará el APK y preparará el entorno para probar la aplicación.

4. **Configura un Dispositivo Virtual**
   Podes configurar un dispositivo virtual:
   - Ve a **AVD Manager** (Administrador de Dispositivos Virtuales) en Android Studio.
   - Haz clic en "Create Virtual Device" (Crear Dispositivo Virtual), elegí un modelo de teléfono y descarga la imagen del sistema que prefieras.
   - Una vez creado el dispositivo virtual, inicialo.

5. **Ejecuta el APK**
   Con el dispositivo virtual en ejecución:
   - Arrastrá el archivo apk al dispositivo virtual.
   - Android Studio instalará el APK en el dispositivo seleccionado y empezará a ejecutar la aplicación.

## Solución de Problemas

- **Asegurate de que todas las dependencias estén instaladas**, ya que la falta de paquetes puede causar fallos en el build.
- **Consultá la documentación de Kivy y Buildozer** para guías detalladas y consejos de solución de problemas.
