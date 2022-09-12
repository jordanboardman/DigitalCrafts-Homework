const dealerHand = document.getElementById("dealer-hand");
const playerHand = document.getElementById("player-hand");
const dealButton = document.getElementById("dealButton");

dealButton.addEventListener("click", function () {
  dealButton();
});

function dealButton() {
  const newCard = document.createElement("img");
  newCard.src = "PNG-cards-1.3/2_of_clubs.png";
  const card = document.getElementById("card");
  card.appendChild(newCard.src);
  console.log(newCard.src);
}

// const deck = [];
// const suits = ["hearts", "spades", "clubs", "diamonds"];
// const ranks = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"];
// const makeDeck = (rank, suit) => {
//   const card = {
//     rank: rank,
//     suit: suit,
//     pointValue: rank > 10 ? 10 : rank,
//   };
//   deck.push(card);
// };

// for (let suit of suits) {
//   for (const rank of ranks) {
//     makeDeck(rank, suit);
//   }
// }

// var deck;

// function buildDeck() {
//   const suits = ["hearts", "spades", "clubs", "diamonds"];
//   const ranks = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"];
//   deck = [];

//   for (let i=0, i < suits.length; i++) { // For each suits
//     for (let j=0; j < ranks.length; j++) { // For each ranks
//       deck.push(ranks[j] + "_of_" + suits.[i]); // Create an arry of each card, named in that img filename format
//     }
//   }
// }

// function shuffleDeck () {
//   for (let i=0, i < deck.length, i++) {
//     let j = Math.floor(Math.random() * deck.length);
//     let tempDeck = deck[i];
//     deck[i] = deck[j];
//     deck[j] = tempDeck
//   }
// }

// window.addEventListener("DOMContentLoaded", () => {
//   // Execute after page load
// });

// fuction calc
