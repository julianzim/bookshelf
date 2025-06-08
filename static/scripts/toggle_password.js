function togglePassword(fieldId, showIconId, hideIconId) {
    const field = document.getElementById(fieldId);
    const showIcon = document.getElementById(showIconId);
    const hideIcon = document.getElementById(hideIconId);

    const isPassword = field.type === "password";
    field.type = isPassword ? "text" : "password";
    showIcon.style.display = isPassword ? "none" : "inline";
    hideIcon.style.display = isPassword ? "inline" : "none";
}
