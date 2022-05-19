#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const abc = JSON.parse(body).characters;
    for (let i = 0; i < abc.length; i++) {
      await request(abc[i], function (error, response, content) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(content).name);
        }
      });
    }
  }
});
