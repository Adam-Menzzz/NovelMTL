fetch('../navbar.html')
  .then(response => response.text())
  .then(navbarHtml => {
  document.getElementById('navbar-placeholder').innerHTML = navbarHtml;
  }); 