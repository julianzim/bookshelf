document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        const requiredInputs = form.querySelectorAll('input[required], textarea[required], select[required]');
        const submitButton = form.querySelector('button[type="submit"]');

        if (!submitButton) return;

        function updateButtonState() {
            const allFilled = Array.from(requiredInputs).every(input => input.value.trim() !== '');
            submitButton.disabled = !allFilled;
        }

        requiredInputs.forEach(input => {
            input.addEventListener('input', updateButtonState);
        });

        updateButtonState();

        form.addEventListener('submit', (e) => {
            submitButton.disabled = true;
        });
    });
});