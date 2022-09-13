// Create a card match game. The game should display 6 pairs of matching cards. When a two cards are picked that match, they should disappear from the screen.

// Display 12 facedown cards on the screen
// At the beginning of the game, randomly generate the order of 6 different cards (there will be two of each)
// The player clicks on two cards, if they don't match, they both go back to being facedown (reset?)
// If the player selects two matching pairs, those two cards disappear.
//

// Array of Cards with pairs included
let pairList = [
  "2_of_clubs.png",
  "jack_of_diamonds.png",
  "10_of_hearts.png",
  "7_of_spades.png",
  "9_of_clubs.png",
  "ace_of_diamonds.png",
  "2_of_clubs.png",
  "jack_of_diamonds.png",
  "10_of_hearts.png",
  "7_of_spades.png",
  "9_of_clubs.png",
  "ace_of_diamonds.png",
];

// Maybe use this?
// let pairList = [
//   card1,
//   card2,
//   card3,
//   card4,
//   card5,
//   card6,
//   card7,
//   card8,
//   card10,
//   card11,
//   card12,
// ];

let card1 = document.getElementById("card1");
let card2 = document.getElementById("card2");
let card3 = document.getElementById("card3");
let card4 = document.getElementById("card4");
let card5 = document.getElementById("card5");
let card6 = document.getElementById("card6");
let card7 = document.getElementById("card7");
let card8 = document.getElementById("card8");
let card9 = document.getElementById("card9");
let card10 = document.getElementById("card10");
let card11 = document.getElementById("card11");
let card12 = document.getElementById("card12");

function shuffle(pairList) {
  let currentIndex = pairList.length,
    randomIndex;

  // While there remain elements to shuffle.
  while (currentIndex != 0) {
    // Pick a remaining element.
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    // And swap it with the current element.
    [pairList[currentIndex], pairList[randomIndex]] = [
      pairList[randomIndex],
      pairList[currentIndex],
    ];
  }

  return pairList;
}
console.log(pairList);
shuffle(pairList);
console.log(pairList);

function displayCards() {
  let cardImg = document.createElement("img");
  let card = deck.pop();
  cardImg.src = card;
}

// Write a function to fill every face up div with one of the cards in pairList
// document.getElementById("card1").src = "./PNG-cards-1.3/" + pairList[0];
function faceup(images) {
  for (i = 0; (i = images.length); i++) {
    document.getElementById("card" + (i + 1)).src =
      "./PNG-cards-1.3/" + images[i];
  }
}

faceup(pairList);

const cards = document.querySelectorAll(".cardbox");

function flipCard() {
  this.pairList.toggle("flip"); // "this" is a keyword, used to refer to an object which depends on how this is being invoked (used or called).
}

cards.forEach((card) => card.addEventListener("click", flipCard));
