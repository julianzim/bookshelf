function toggleMobMenu() {
    const menu = document.querySelector('.mobile-menu');
    menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';
}
document.addEventListener('click', function (event) {
    const menu = document.querySelector('.mobile-menu');
    const button = document.querySelector('.menu-button');

    if (!menu.contains(event.target) && !button.contains(event.target)) {
        menu.style.display = 'none';
    }
});
