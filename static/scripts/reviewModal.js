var modal = document.getElementById("reviewModal");
var closeBtn = document.querySelector(".close");

function openModal() {
    modal.classList.add("show");
}

closeBtn.onclick = function() {
    modal.classList.remove("show");
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.classList.remove("show");
    }
}

const textarea = document.getElementById("text");

textarea.addEventListener("input", function() {
    this.style.height = "auto";
    this.style.height = this.scrollHeight + "px";
});
