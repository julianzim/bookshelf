var register_modal = document.getElementById("registerModal");
var closeBtnRegister = document.querySelector(".register-close");
var login_modal = document.getElementById("loginModal");
var closeBtnLogin = document.querySelector(".login-close");

function openRegisterModal() {
    login_modal.classList.remove("show");
    register_modal.classList.add("show");
}

closeBtnRegister.onclick = function() {
    register_modal.classList.remove("show");
}

window.onclick = function(event) {
    if (event.target == register_modal) {
        register_modal.classList.remove("show");
    }
}


function openLoginModal() {
    register_modal.classList.remove("show");
    login_modal.classList.add("show");
}

closeBtnLogin.onclick = function() {
    login_modal.classList.remove("show");
}

window.onclick = function(event) {
    if (event.target == login_modal) {
        login_modal.classList.remove("show");
    }
}

