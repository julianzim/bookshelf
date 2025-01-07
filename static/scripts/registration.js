document.getElementById('auth-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const form = event.target;
    const data = {
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
        repeat_password: document.getElementById('repeat-password').value
    };

    document.getElementById('email-error').textContent = '';
    document.getElementById('repeat-password-error').textContent = '';
    document.getElementById('password-strength').textContent = '';

    if (data.password !== data.repeat_password) {
        document.getElementById('repeat-password-error').textContent = 'Passwords do not match';
        return;
    }

    const response = await fetch('/auth/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    if (response.ok) {
        // window.location.href = '/auth/login';
        document.getElementById('registerModal').style.display = 'none';
        document.getElementById('loginModal').style.display = 'block';
    } else {
        const result = await response.json();
        console.error('Registration failed:', result);
        if (result.message) {
            document.getElementById('email-error').textContent = result.message;
        }
    }
});

document.getElementById('password').addEventListener('input', function() {
    const password = this.value;
    const strength = getPasswordStrength(password);
    document.getElementById('password-strength').textContent = strength;
});

function getPasswordStrength(password) {
    if (password.length < 6) return 'Weak';
    if (password.length < 12) return 'Medium';
    return 'Strong';
}