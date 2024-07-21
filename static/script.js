document.addEventListener('DOMContentLoaded', function () {
    console.log("Script loaded");

    const leftButton = document.querySelector('.scroll-button.left');
    const rightButton = document.querySelector('.scroll-button.right');
    const bookGrid = document.querySelector('.book-grid-in-wrapper');

    if (!leftButton || !rightButton || !bookGrid) {
        console.error("Scroll buttons or book grid not found");
        return;
    }

    const bookItemWidth = document.querySelector('.book-item-in-wrapper').offsetWidth + 20; // Ширина элемента + отступы
    console.log("Book item width: ", bookItemWidth);
    let scrollAmount = 0;

    leftButton.addEventListener('click', function () {
        scrollAmount -= bookItemWidth;
        scrollAmount = Math.max(scrollAmount, 0);
        bookGrid.scrollTo({ left: scrollAmount, behavior: 'smooth' });
        console.log("scrollAmount after left click", scrollAmount);
        toggleButtons();
    });

    rightButton.addEventListener('click', function () {
        scrollAmount += bookItemWidth;
        const maxScrollLeft = bookGrid.scrollWidth - bookGrid.clientWidth;
        scrollAmount = Math.min(scrollAmount, maxScrollLeft);
        bookGrid.scrollTo({ left: scrollAmount, behavior: 'smooth' });
        console.log("scrollAmount after right click", scrollAmount);
        toggleButtons();
    });

    function toggleButtons() {
        const maxScrollLeft = bookGrid.scrollWidth - bookGrid.clientWidth;
        console.log("Toggling buttons");
        console.log("scrollAmount", scrollAmount, "maxScrollLeft", maxScrollLeft);
        if (scrollAmount <= 0) {
            leftButton.disabled = true;
        } else {
            leftButton.disabled = false;
        }
        if (scrollAmount >= maxScrollLeft) {
            rightButton.disabled = true;
        } else {
            rightButton.disabled = false;
        }
    }

    toggleButtons(); // Check buttons on load
});