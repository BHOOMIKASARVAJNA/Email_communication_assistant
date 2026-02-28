function send(){
  const chat = document.getElementById("chat");
  const text = document.getElementById("context").value;
  const tone = document.getElementById("tone").value;

  if (text.trim() === "") return;

  // User message
    chat.innerHTML += `<div class="message user">${text}</div>`;

    // Call backend
    fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ context: text, tone })
    })
    .then(res => res.json())
    .then(data => {
        const formatted = data.response
            .replace(/\n/g, "<br>")
            .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

        chat.innerHTML += `
            <div class="email-output">
                ${formatted}
            </div>
        `;
        chat.scrollTop = chat.scrollHeight;
    });

    document.getElementById("context").value = "";
}

  
