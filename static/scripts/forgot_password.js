document.getElementById("forgot-password-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const emailInput = document.getElementById("fp-email");
    const email = emailInput.value.trim();
    const messageDiv = document.getElementById("reset-message");

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
            messageDiv.textContent = "A password reset link has been sent to your email.";
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