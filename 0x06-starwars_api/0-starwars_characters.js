#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let result = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const abc = JSON.parse(body).characters;
    for (let i = 0; i < abc.length; i++) {
      request(abc[i], function (error, response, content) {
        if (error) {
          console.log(error);
        } else {
          result = JSON.parse(content);
          console.log(result.name);
        }
      });
    }
  }
});