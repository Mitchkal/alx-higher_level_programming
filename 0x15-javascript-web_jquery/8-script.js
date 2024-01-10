$(document).ready(function () {
  $.get(
    'https://swapi-api.alx-tools.com/api/films/?format=json',
    function (response) {
      const listMovies = $('#list_movies');
      response.results.forEach(function (movie) {
        listMovies.append('<li>' + movie.title + '</li>');
      });
    }
  );
});
