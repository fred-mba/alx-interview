#!/usr/bin/node
/*
 * The script prints all characters of a Star Wars movie
 * The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi"
 * Display one character name per line in the same order as the “characters” list in the /films/ endpoint
 * Must use the request module
 */

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});

const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
