const sendButton = document.getElementById('send-button');
const chatInput = document.getElementById('chat-input');
const chatContainer = document.getElementById('chat-container');

function sendMessage() {
    const message = chatInput.value.trim();
    if (message) {
        // Añadir mensaje del usuario
        const userBubble = document.createElement('div');
        userBubble.className = 'user-message';
        userBubble.innerText = message;
        chatContainer.appendChild(userBubble);

        // Añadir respuesta simulada del bot
        const botBubble = document.createElement('div');
        botBubble.className = 'bot-message';
        botBubble.innerText = "🧙‍♂️ Respuesta automática simulada...";
        chatContainer.appendChild(botBubble);

        // Limpiar textarea
        chatInput.value = '';

        // Scroll automático al fondo
        chatContainer.scrollTo({
            top: chatContainer.scrollHeight,
            behavior: 'smooth'
        });

        // Ajustar altura después de enviar
        autoResize();
    }
}

// Enviar al pulsar el botón
sendButton.addEventListener('click', sendMessage);

// Enviar al pulsar "Enter" sin Shift
chatInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// Función para ajustar la altura automáticamente
function autoResize() {
    chatInput.style.height = 'auto'; // resetea primero
    chatInput.style.height = chatInput.scrollHeight + 'px'; // ajusta a su contenido
}

// Detectar cambios mientras escribe
chatInput.addEventListener('input', autoResize);

// Ajuste inicial
autoResize();