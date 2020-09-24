$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  const films = data.results;
  for (const film of films) {
    $('UL#list_movies').append(`<li>${film.title}</li>`);
  }
});
