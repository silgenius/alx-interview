#!/usr/bin/node

/* a script that prints all characters of a Star Wars movie */

const request = require('request');
const util = require('util');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, async (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const resp = JSON.parse(body);
    const requestUtil = util.promisify(request);
    for (const character of resp.characters) {
      try {
        const res = await requestUtil(character);
        const data = await JSON.parse(res.body);
        console.log(data.name);
      } catch (err) {
        console.error(err);
      }
    }
  }
});
