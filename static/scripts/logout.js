document.getElementById('logout-button').addEventListener('click', async () => {
    const lastVisitedPage = window.location.href;
    localStorage.setItem('lastVisitedPage', lastVisitedPage);

    const response = await fetch('/auth/logout', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      credentials: 'include'
    });

    if (response.ok) {
      const redirectUrl = localStorage.getItem('lastVisitedPage') || '/';
      window.location.href = redirectUrl;
    } else {
      alert('Logout failed');
    }
});