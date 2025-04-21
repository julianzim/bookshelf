document.getElementById("forgot-password-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const emailInput = document.getElementById("fp-email");
    const email = emailInput.value.trim();
    const messageDiv = document.getElementById("reset-message");
    const form = document.getElementById("forgot-password-form");

    messageDiv.textContent = "Sending form...";
    messageDiv.style.color = "blue";
    messageDiv.style.display = "block";

    if (!email) {
        messageDiv.textContent = "Please enter your email.";
        messageDiv.style.color = "red";
        messageDiv.style.display = "block";
        return;
    }

    try {
        const response = await fetch("/auth/forgot-password", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email: email })
        });

        const result = await response.json();

        if (response.ok) {
            form.style.display = "none";
            messageDiv.innerHTML = "✓ A password reset link has been successfully sent to your email.";
            messageDiv.style.color = "green";
        } else {
            messageDiv.textContent = "Error: " + (result.detail || "Failed to send reset email");
            messageDiv.style.color = "red";
        }
    } catch (error) {
        console.error("Fetch error:", error);
        messageDiv.textContent = "Network error. Try again later.";
        messageDiv.style.color = "red";
    }

    messageDiv.style.display = "block";
});