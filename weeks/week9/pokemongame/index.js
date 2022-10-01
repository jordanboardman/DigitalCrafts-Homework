const axios = require("axios").default;
const { pokemon } = require("./models");
const express = require("express");
const app = express();

app.use(express.json());

// 1). Modify the code so that the drawPokemon function gets 5 cards and stores them to the database
// 2). Convert this into an API, so each function will be called by its corresponding (use express)
// 3). Add additional safeguards to make sure the API calls do not crash the server

// Draws a random pokecard
app.post("/pokemon", (req, res) => {
  pokemon.findAll();
  let draw = drawPokemon();
  console.log("endpoint draw", draw);
  res.send(draw);
});

async function drawPokemon() {
  let draw = [];
  // Make an API call to get a list of cards
  await axios
    .get(
      "https://api.pokemontcg.io/v2/cards?q=nationalPokedexNumbers:[1 TO 151]"
    )
    .then(function (response) {
      for (let i = 0; i < 5; i++) {
        // We pick at random one of the cards in the list
        let cardNum = Math.round(Math.random() * response.data.count);

        // Place desired card attributes into an object and add to the db
        let card = {
          id: response.data.data[cardNum].id,
          name: response.data.data[cardNum].name,
          type: response.data.data[cardNum].types[0],
          level: response.data.data[cardNum].level,
          hp: response.data.data[cardNum].hp,
          images: response.data.data[cardNum].images.large,
        };
        // console.log(card);
        draw.push(card);
      }
      console.log("function draw", draw);
      pokemon.bulkCreate(draw);
      return draw();
    })
    .catch(function (error) {
      // handle error
      console.log(error);
    })
    .then(function () {
      // always executed
    });
}

async function deletePokemon(id) {
  // Check if card exists in db
  let pokeDelete = await pokemon.findOne({
    where: {
      id: id,
    },
  });

  if (pokeDelete == null) {
    console.error("Card does not exist");
  } else {
    // Remove card from db
    pokemon.destroy({
      where: {
        id: id,
      },
    });
  }
}

function getDeck() {
  pokemon.findAll();
}

drawPokemon();
// deletePokemon();

app.listen(4000, () => {
  console.log("Server is running on port 4000");
});
