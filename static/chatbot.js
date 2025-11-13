document.getElementById('pdf-input').addEventListener('change', function() {
    const fileNameDiv = document.getElementById('file-name');
    if (this.files.length > 0) {
        fileNameDiv.textContent = this.files[0].name;
    } else {
        fileNameDiv.textContent = "Nenhum arquivo escolhido";
    }
});

document.querySelector('.custom-file-label').addEventListener('click', function() {
    document.getElementById('pdf-input').click();
});

document.getElementById('pdf-form').onsubmit = async function(e) {
    e.preventDefault();
    const input = document.getElementById('pdf-input');
    const status = document.getElementById('upload-status');
    if (!input.files.length) {
        status.textContent = "Selecione um arquivo PDF.";
        return;
    }
    const formData = new FormData();
    formData.append('pdf', input.files[0]);
    const response = await fetch('/upload', { method: 'POST', body: formData });
    const result = await response.json();
    status.textContent = result.mensagem;
};

async function sendMessage() {
    const input = document.getElementById('user-input');
    const chatWindow = document.getElementById('chat-window');
    const message = input.value.trim();
    if (message === "") return;

    const userMsg = document.createElement('div');
    userMsg.textContent = "Você: " + message;
    userMsg.className = "user-message";
    chatWindow.appendChild(userMsg);

    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    });
    const data = await response.json();

    const botMsg = document.createElement('div');
    botMsg.textContent = "Chatbot: " + data.response;
    botMsg.className = "bot-message";
    chatWindow.appendChild(botMsg);

    chatWindow.scrollTop = chatWindow.scrollHeight;
    input.value = "";
    input.focus();
}