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
   Instala Kivy siguiendo la [guía oficial de instalación de Kivy](https://kivy.org/doc/stable/gettingstarted/installation.html) para tu sistema operativo. Esto generalmente implica:

   ```bash
   # Para la mayoría de los sistemas:
   python -m pip install kivy
   ```

   Adicionalmente, instala la librería `requests`:
   ```bash
   python -m pip install requests
   ```

## Ejecución de la App Localmente

Para ejecutar la app en tu máquina local, ejecuta:

```bash
python main.py
```

Donde `main.py` es el archivo de Python que ejecuta la aplicación Kivy.

## Construcción para Android (APK)

Para construir la app para Android, necesitarás usar [Buildozer](https://buildozer.readthedocs.io/es/latest/). Instala Buildozer con:

```bash
python -m pip install buildozer
```

1. **Crear un archivo de configuración de Buildozer**
   Inicializa Buildozer en tu directorio del proyecto:
   ```bash
   buildozer init
   ```

3. **Construir el APK**
   Ejecuta Buildozer para crear el APK:
   ```bash
   buildozer -v android debug
   ```

   Este comando compilará tu app y producirá un archivo `.apk` que puedes instalar en dispositivos Android.

4. **Desplegar el APK**
   Después de construir, puedes desplegar el APK directamente en un dispositivo Android conectado:
   ```bash
   buildozer android deploy run
   ```

## Cómo Correr el APK en Android Studio

Para probar y ejecutar el APK de tu aplicación Kivy en Android Studio, sigue estos pasos:

1. **Instala Android Studio**
   Si aún no tienes Android Studio instalado, puedes descargarlo desde [aquí](https://developer.android.com/studio). Sigue las instrucciones de instalación proporcionadas en el sitio web.

2. **Abrir Android Studio**
   Inicia Android Studio y en la pantalla de bienvenida, selecciona "Profile or debug APK".

3. **Selecciona el APK**
   Busca y selecciona el archivo APK que has generado con Buildozer. Android Studio cargará el APK y preparará el entorno para probar la aplicación.

4. **Configura un Dispositivo Virtual**
   Si no tienes un dispositivo Android físico, puedes configurar un dispositivo virtual:
   - Ve a **AVD Manager** (Administrador de Dispositivos Virtuales) en Android Studio.
   - Haz clic en "Create Virtual Device" (Crear Dispositivo Virtual), elige un modelo de teléfono que se ajuste a las características de prueba que necesitas y descarga la imagen del sistema que prefieras.
   - Una vez creado el dispositivo virtual, inícialo.

5. **Ejecuta el APK**
   Con el dispositivo virtual en ejecución o un dispositivo físico conectado:
   - Haz clic derecho sobre el proyecto en el que cargaste el APK.
   - Selecciona 'Run' (Ejecutar) desde el menú contextual.
   - Android Studio instalará el APK en el dispositivo seleccionado y empezará a ejecutar la aplicación.

6. **Monitorea la Salida**
   Observa la consola de Android Studio para cualquier mensaje de salida o error que pueda surgir mientras pruebas la aplicación. Esto es especialmente útil para depurar problemas específicos de la aplicación en dispositivos Android.

## Solución de Problemas

- **Asegúrate de que todas las dependencias estén instaladas**, ya que la falta de paquetes puede causar fallos en el build.
- **Consulta la documentación de Kivy y Buildozer** para guías detalladas y consejos de solución de problemas.
