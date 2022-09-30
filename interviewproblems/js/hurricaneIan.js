// [DRE HAS SAID THAT IF YOU CAN DO EACH OF THESE STEPS BELOW, YOU CAN HANDLE THE BACK END PROJECT ALONE IF YOU HAD TO, BUT IT IS GOING TO BE A GROUP PROJECT]

// Hurricane Ian has caused massive power outages across FL and we need to determine how many people are without power. Using the random data API, create a database that holds customers of Florida Power and store their name, phone number, and address. Only people with FL, GA, SC, and NC addresses should be stored. Add to each customer a field that indicates if they have power or not. Write db query that retrieves all users from the db without power.

// 1). Make API call that gets 1000 random users (DONE)
// 2). Filter out anyone not in the affected states
// 3). Remove unnecessary fields of info
// 4). Randomly assign if person has power
// 5). Using sequelize, create a db and table for storing customers
// 6). Store those customers in the db
// 7). Write a separate function that only retrieves customers without power

// import axios from "axios";

function generateUsers() {
  const fetch = require("node-fetch");
  fetch("https://random-data-api.com/api/v2/users?size=100")
    .then((response) => response.json())
    .then((data) => {
      for (i = 0; i < data.length; i++) {
        resident = {
          first_name: data[i].first_name,
          last_name: data[i].last_name,
          state: data[i].address.state,
        };
      }
      console.log(data);
    });
}

// const affStates = resident.filter(function (states) {
//   return states.state == "Florida";
// });

// console.log(affStates);
