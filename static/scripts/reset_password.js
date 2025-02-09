document.getElementById("reset-password-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const token = document.getElementById("token").value;
    const password = document.getElementById("new-password").value.trim();
    const confirmPassword = document.getElementById("confirm-password").value.trim();
    const messageDiv = document.getElementById("reset-message");

    if (!password || !confirmPassword) {
        messageDiv.textContent = "Please enter and confirm your new password.";
        messageDiv.style.color = "red";
        messageDiv.style.display = "block";
        return;
    }

    if (password !== confirmPassword) {
        messageDiv.textContent = "Passwords do not match. Please try again.";
        messageDiv.style.color = "red";
        messageDiv.style.display = "block";
        return;
    }

    try {
        const response = await fetch("/auth/reset-password", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ token: token, password: password })
        });

        const result = await response.json();
        console.log("Response:", result);

        if (response.ok) {
            messageDiv.textContent = "Your password has been reset successfully.";
            messageDiv.style.color = "green";
            setTimeout(() => window.location.href = "/", 2000);
        } else {
            messageDiv.textContent = "Error: " + (result.detail || "Failed to reset password.");
            messageDiv.style.color = "red";
        }
    } catch (error) {
        console.error("Fetch error:", error);
        messageDiv.textContent = "Network error. Try again later.";
        messageDiv.style.color = "red";
    }

    messageDiv.style.display = "block";
});