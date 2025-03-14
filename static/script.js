async function generateResponse() {
    let prompt = document.getElementById("prompt").value;
    let responseElement = document.getElementById("response");

    let response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: prompt }),
    });

    let data = await response.json();
    responseElement.innerText = data.response || data.error;
}