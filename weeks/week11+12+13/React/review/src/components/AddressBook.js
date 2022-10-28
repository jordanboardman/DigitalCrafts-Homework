import React from "react";
import { useState } from "react";

const AddressBook = () => {
  const [nameAdd, setNameAdd] = useState("");
  const [emailAdd, setEmailAdd] = useState("");
  const [phoneAdd, setPhoneAdd] = useState("");
  const [list, setList] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    let newList = [nameAdd, emailAdd, phoneAdd, ...list];
    setList(newList);
    setNameAdd("");
    setEmailAdd("");
    setPhoneAdd("");

    console.log(list);
  };

  return (
    <>
      <h2>Address Book</h2>
      <br />

      <h3>Add a new Contact</h3>
      <br />

      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input
            type="text"
            value={nameAdd}
            onChange={(e) => setNameAdd(e.target.value)}
          />
        </label>
        <label>
          Email:
          <input
            type="text"
            value={emailAdd}
            onChange={(e) => setEmailAdd(e.target.value)}
          />
        </label>
        <label>
          Phone:
          <input
            type="text"
            value={phoneAdd}
            onChange={(e) => setPhoneAdd(e.target.value)}
          />
        </label>
        <input type="submit" />
      </form>

      <h3>Contacts</h3>

      <ul>
        {list.map((listItem) => {
          return <li key={listItem}>{listItem}</li>;
        })}
      </ul>
      <br />

      <input type="submit" />
    </>
  );
};

export default AddressBook;
