document.getElementById('register-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const form = event.target;
    const data = {
        username: document.getElementById('register-username').value,
        email: document.getElementById('register-email').value,
        password: document.getElementById('register-password').value,
        repeat_password: document.getElementById('register-repeat-password').value
    };

    document.getElementById('register-email-error').textContent = '';
    document.getElementById('register-repeat-password-error').textContent = '';
    document.getElementById('register-password-strength').textContent = '';

    if (data.password !== data.repeat_password) {
        document.getElementById('register-repeat-password-error').textContent = 'Passwords do not match';
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
        if (window.location.pathname === '/auth/register') {
            window.location.href = '/auth/login';
        } else {
            document.getElementById('registerModal').style.display = 'none';
            document.getElementById('loginModal').style.display = 'block';
        }
    } else {
        const result = await response.json();
        console.error('Registration failed:', result);
        if (result.message) {
            document.getElementById('register-email-error').textContent = result.message;
        }
    }
});

document.getElementById('register-password').addEventListener('input', function() {
    const password = this.value;
    const strength = getPasswordStrength(password);
    document.getElementById('register-password-strength').textContent = strength;
});

function getPasswordStrength(password) {
    if (password.length < 6) return 'Weak';
    if (password.length < 12) return 'Medium';
    return 'Strong';
}