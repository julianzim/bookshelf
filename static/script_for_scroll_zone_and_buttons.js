document.addEventListener('DOMContentLoaded', () => {
    console.log("Script loaded");

    const leftZone = document.querySelector('.scroll-zone.left');
    const rightZone = document.querySelector('.scroll-zone.right');
    const leftButton = document.querySelector('.scroll-button.left');
    const rightButton = document.querySelector('.scroll-button.right');
    const bookGrid = document.querySelector('.book-grid-in-wrapper');

    if (!leftZone || !rightZone || !leftButton || !rightButton || !bookGrid) {
        console.error("Scroll zones or buttons or book grid not found");
        return;
    }

    const bookItemWidth = document.querySelector('.book-item-in-wrapper').offsetWidth * 5; // Ширина элемента + отступы
    console.log("Book item width: ", bookItemWidth);

    let scrollAmount = 0;

    const scrollToPosition = (position) => {
        bookGrid.scrollTo({ left: position, behavior: 'smooth' });
    };

    let scrollInterval;

    const startScrollLeft = () => {
        scrollInterval = setInterval(() => {
            scrollAmount = Math.max(scrollAmount - 5, 0);
            scrollToPosition(scrollAmount);
            toggleButtons();
        }, 70);
    };
    const startScrollRight = () => {
        const maxScrollLeft = bookGrid.scrollWidth - bookGrid.clientWidth;
        scrollInterval = setInterval(() => {
            scrollAmount = Math.min(scrollAmount + 5, maxScrollLeft);
            scrollToPosition(scrollAmount);
            toggleButtons();
        }, 70);
    };

    const stopScroll = () => {
        clearInterval(scrollInterval);
    };

    leftZone.addEventListener('mouseenter', startScrollLeft);
    leftZone.addEventListener('mouseleave', stopScroll);
    rightZone.addEventListener('mouseenter', startScrollRight);
    rightZone.addEventListener('mouseleave', stopScroll);

    leftButton.addEventListener('click', () => {
        scrollAmount = Math.max(scrollAmount - bookItemWidth, 0);
        scrollToPosition(scrollAmount);
        toggleButtons();
    });

    rightButton.addEventListener('click', () => {
        const maxScrollLeft = bookGrid.scrollWidth - bookGrid.clientWidth;
        scrollAmount = Math.min(scrollAmount + bookItemWidth, maxScrollLeft);
        scrollToPosition(scrollAmount);
        toggleButtons();
    });

    const toggleButtons = () => {
        const maxScrollLeft = bookGrid.scrollWidth - bookGrid.clientWidth;
        console.log("scrollAmount", scrollAmount, "maxScrollLeft", maxScrollLeft);
        leftButton.disabled = scrollAmount <= 0;
        rightButton.disabled = scrollAmount >= maxScrollLeft;
    };

    toggleButtons(); // Check buttons on load
});