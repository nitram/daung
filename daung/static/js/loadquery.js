const searchBar = document.getElementById('search-bar');

searchBar.addEventListener('keyup', function() {
    const query = searchBar.value.toLowerCase();
    const qdata = document.querySelectorAll('.qdata');

    qdata.forEach(function(data) {
        const dataText = data.querySelector('.qtext').textContent.toLowerCase();
        if (dataText.includes(query)) {
            data.style.display = '';
        } else {
            data.style.display = 'none';
        }
    });
});
