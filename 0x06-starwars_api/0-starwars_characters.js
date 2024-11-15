#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, body) => {
      if (err) {
        console.error(err);
      } else {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      }
    });
  });
});

