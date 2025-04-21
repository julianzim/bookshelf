document.addEventListener('DOMContentLoaded', function () {
    const leftButton = document.querySelector('.scroll-button.blog.left');
    const rightButton = document.querySelector('.scroll-button.blog.right');
    const blogGrid = document.querySelector('.grid-in-wrapper.blog');

    const articleItemWidth = document.querySelector('.card.article').offsetWidth * 4;
    console.log("Article item width: ", articleItemWidth);
    let scrollBlogAmount = 0;

    leftButton.addEventListener('click', function () {
        scrollBlogAmount -= articleItemWidth;
        scrollBlogAmount = Math.max(scrollBlogAmount, 0);
        blogGrid.scrollTo({ left: scrollBlogAmount, behavior: 'smooth' });
        console.log("scrollAmount after left click", scrollBlogAmount);
        toggleButtons();
    });

    rightButton.addEventListener('click', function () {
        scrollBlogAmount += articleItemWidth;
        const maxScrollLeft = blogGrid.scrollWidth - blogGrid.clientWidth;
        scrollBlogAmount = Math.min(scrollBlogAmount, maxScrollLeft);
        blogGrid.scrollTo({ left: scrollBlogAmount, behavior: 'smooth' });
        console.log("scrollAmount after right click", scrollBlogAmount);
        toggleButtons();
    });

    function toggleButtons() {
        const maxScrollLeft = blogGrid.scrollWidth - blogGrid.clientWidth;
        console.log("Toggling buttons");
        console.log("scrollAmount", scrollBlogAmount, "maxScrollLeft", maxScrollLeft);
        if (scrollBlogAmount <= 0) {
            leftButton.disabled = true;
        } else {
            leftButton.disabled = false;
        }
        if (scrollBlogAmount >= maxScrollLeft) {
            rightButton.disabled = true;
        } else {
            rightButton.disabled = false;
        }
    }

    toggleButtons();
});