# Documentacion Tecnica Inicial - T7AIChatModular

## Arquitectura del Interfaz

La arquitectura del proyecto **T7AIChatModular** se basa en una separacion modular de responsabilidades, permitiendo una evolucion sencilla y ordenada.

### Estructura General del Proyecto

- **Servidor Backend (app.py)**: Utiliza Flask como microframework para gestionar las rutas web. Recibe las solicitudes desde el navegador, procesa los mensajes enviados por el usuario y devuelve la respuesta correspondiente. 

- **Motor de Logica (main.py)**: Se encarga de procesar el contenido de los mensajes recibidos. Incluye la logica principal del chatbot, que podra ser expandida con futuras mejoras modulares.

- **Frontend Web (HTML + CSS + JS)**: 
  - **HTML**: Define la estructura basica de la interfaz de usuario, incluyendo el cuadro de chat, la caja de texto para introducir mensajes y el boton para enviar.
  - **CSS**: Estiliza la apariencia de la interfaz, asegurando un diseño limpio y responsive que se adapta a diferentes dispositivos.
  - **JavaScript**: Gestiona la interaccion en tiempo real. Captura el mensaje del usuario, lo envia al servidor via fetch API, recibe la respuesta y actualiza dinamicamente la interfaz.

- **Carpeta static/**: Contiene los archivos estaticos como hojas de estilo (CSS) y scripts de cliente (JS).

- **Carpeta templates/**: Contiene las plantillas HTML que renderiza Flask al servir las paginas web.

- **Carpeta docs/tecnico/**: Contendra la documentacion tecnica detallada del proyecto, para mantener la trazabilidad y facilitar la escalabilidad futura.

### Flujo de Datos

1. El usuario introduce un mensaje en el cuadro de texto de la web.
2. JavaScript captura el mensaje y realiza una solicitud POST a la ruta `/chat` del servidor.
3. Flask recibe el mensaje y lo envia al motor de logica (`main.py`).
4. El motor analiza el mensaje y genera una respuesta.
5. Flask devuelve la respuesta al frontend.
6. JavaScript actualiza el chat en pantalla mostrando la respuesta del bot.

### Ventajas de esta Arquitectura

- Separacion clara entre frontend y backend.
- Modularidad que facilita el mantenimiento y la expansion.
- Uso de tecnologias ligeras y ampliamente soportadas.
- Flujo de interaccion simple y eficiente.

---

**Nota:** Esta documentacion resume la base tecnica construida hasta ahora. A partir de aqui se podran ir integrando modulos adicionales, mejoras visuales y nuevas funcionalidades en el chatbot.

