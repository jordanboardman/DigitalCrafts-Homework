const getUsers = () => {
  fetch("https://random-data-api.com/api/v2/users?size=1")
    .then((response) => {
      return response.json();
    })
    .then((userData) => {
      //console.log(userData);
      let userTitle = document.createElement("h5"); // GrandChild
      userTitle.classList.add("card-title");
      userTitle.appendChild(document.createTextNode(userData.username));
      //console.log(userTitle.innerText)
      const cIndex = document.getElementById("userCard");

      let userOverview = document.createElement("p"); // GrandChild
      userOverview.classList.add("card-text");
      userOverview.appendChild(
        document.createTextNode(
          "Hi my name is " +
            userData.first_name +
            " " +
            userData.last_name +
            " I am a " +
            userData.employment.title
        )
      );

      let userButton = document.createElement("button"); // GrandChild
      userButton.classList.add("btn-primary");
      userButton.appendChild(document.createTextNode("More Info"));

      let cardBody = document.createElement("div"); // Parent
      cardBody.classList.add("card-body");
      cardBody.append(userTitle);
      cardBody.append(userOverview);
      cardBody.append(userButton);
      console.log(cardBody.innerHTML);

      let cardImage = document.createElement("img"); // Uncle
      cardImage.classList.add("card-img-top");
      cardImage.src = userData.avatar;

      let cardBox = document.createElement("div"); // GrandParent
      cardBox.classList.add("card");
      cardBox.append(cardImage);
      cardBox.append(cardBody);

      document.body.insertBefore(cardBox, cIndex);
    });
};
