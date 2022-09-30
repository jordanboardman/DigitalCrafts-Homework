const axios = require("axios").default;
const { Sequelize } = require("sequelize");
const { pokemon } = require("./models");

// Make a request for a user with a given ID
axios
  .get("https://api.pokemontcg.io/v2/cards?q=name:charizard")
  .then(function (response) {
    // handle success
    let cardNum = Math.round(Math.random() * response.data.totalCount);

    pokemon.create({
      id: response.data.data[cardNum].id,
      name: response.data.data[cardNum].name,
      type: response.data.data[cardNum].types[0],
      level: response.data.data[cardNum].level,
      hp: response.data.data[cardNum].hp,
      images: response.data.data[cardNum].images.large,
    });
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
