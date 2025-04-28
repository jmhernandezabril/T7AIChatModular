const sendButton    = document.getElementById('send-button');
const chatInput     = document.getElementById('chat-input');
const chatContainer = document.getElementById('chat-container');

async function sendMessage() {
    const message = chatInput.value.trim();
    if (!message) return;

    // Añadir mensaje del usuario
    const userBubble = document.createElement('div');
    userBubble.className = 'user-message';
    userBubble.innerText = message;
    chatContainer.appendChild(userBubble);

    // Limpiar textarea y ajustar scroll/altura
    chatInput.value = '';
    autoScroll();
    autoResize();

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });
        const data    = await response.json();
        const resp    = data.response;
        const columns = data.columns;

        if (Array.isArray(resp)) {
            const headerCols = Array.isArray(columns) && columns.length
                ? columns
                : Object.keys(resp[0] || {});

            const table = document.createElement('table');
            table.className = 'bot-table';

            const thead     = document.createElement('thead');
            const headerRow = document.createElement('tr');
            headerCols.forEach(col => {
                const th = document.createElement('th');
                th.innerText = col;
                headerRow.appendChild(th);
            });
            thead.appendChild(headerRow);
            table.appendChild(thead);

            const tbody = document.createElement('tbody');
            resp.forEach(row => {
                const tr = document.createElement('tr');
                headerCols.forEach(col => {
                    const td = document.createElement('td');
                    td.innerText = row[col] ?? '';
                    tr.appendChild(td);
                });
                tbody.appendChild(tr);
            });
            table.appendChild(tbody);

            chatContainer.appendChild(table);

            // Añadir enlace al nuevo panel Dash
            const linkWrapper = document.createElement('div');
            linkWrapper.className = 'dash-link';
            linkWrapper.innerHTML = `
                <a href="/dash/" target="_blank">
                    🔗 Abrir panel avanzado
                </a>
            `;
            chatContainer.appendChild(linkWrapper);

        } else {
            const botBubble = document.createElement('div');
            botBubble.className = 'bot-message';
            botBubble.innerText = resp;
            chatContainer.appendChild(botBubble);
        }

        autoScroll();

    } catch (error) {
        const errorBubble = document.createElement('div');
        errorBubble.className = 'bot-message';
        errorBubble.innerText = "❌ Error de comunicacion.";
        chatContainer.appendChild(errorBubble);
        autoScroll();
    }
}

// Helpers
function autoScroll() {
    chatContainer.scrollTo({
        top: chatContainer.scrollHeight,
        behavior: 'smooth'
    });
}

function autoResize() {
    chatInput.style.height = 'auto';
    chatInput.style.height = chatInput.scrollHeight + 'px';
}

// Listeners
sendButton.addEventListener('click', sendMessage);
chatInput.addEventListener('keypress', e => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});
chatInput.addEventListener('input', autoResize);
autoResize();