document.addEventListener('DOMContentLoaded', function () {
    const leftButton = document.querySelector('.scroll-button.books.left');
    const rightButton = document.querySelector('.scroll-button.books.right');
    const bookGrid = document.querySelector('.grid-in-wrapper.books');

    const bookItemWidth = document.querySelector('.book-item-in-wrapper').offsetWidth * 5;
    console.log("Book item width: ", bookItemWidth);
    let scrollBooksAmount = 0;

    leftButton.addEventListener('click', function () {
        scrollBooksAmount -= bookItemWidth;
        scrollBooksAmount = Math.max(scrollBooksAmount, 0);
        bookGrid.scrollTo({ left: scrollBooksAmount, behavior: 'smooth' });
        console.log("scrollAmount after left click", scrollBooksAmount);
        toggleButtons();
    });

    rightButton.addEventListener('click', function () {
        scrollBooksAmount += bookItemWidth;
        const maxScrollLeft = bookGrid.scrollWidth - bookGrid.clientWidth;
        scrollBooksAmount = Math.min(scrollBooksAmount, maxScrollLeft);
        bookGrid.scrollTo({ left: scrollBooksAmount, behavior: 'smooth' });
        console.log("scrollAmount after right click", scrollBooksAmount);
        toggleButtons();
    });

    function toggleButtons() {
        const maxScrollLeft = bookGrid.scrollWidth - bookGrid.clientWidth;
        console.log("Toggling buttons");
        console.log("scrollAmount", scrollBooksAmount, "maxScrollLeft", maxScrollLeft);
        if (scrollBooksAmount <= 0) {
            leftButton.disabled = true;
        } else {
            leftButton.disabled = false;
        }
        if (scrollBooksAmount >= maxScrollLeft) {
            rightButton.disabled = true;
        } else {
            rightButton.disabled = false;
        }
    }

    toggleButtons();
});