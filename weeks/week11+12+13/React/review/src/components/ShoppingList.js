import React, { useState } from "react";
import ShoppingDetails from "./ShoppingDetails";
import { v4 as uuidv4 } from "uuid";

/**
 * {
 *  id: uuid
 *  item: Item
 *
 * }
 */
const ShoppingList = () => {
  const [item, setItem] = useState("");
  const [list, setList] = useState([]); //["". "", ""]   // [{}, {}, {}, {}]

  const handleSubmit = (e) => {
    e.preventDefault();

    let newItemObj = {
      id: uuidv4(),
      item,
    };
    // let newList = [item, ...list] //array of strings
    let newList = [newItemObj, ...list]; //array of objs

    setList(newList);
    setItem(""); //reset our input field

    console.log(list);
  };

  return (
    <>
      <h2>Shopping List</h2>
      <br />

      <h3>Add new Item:</h3>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={item}
          onChange={(e) => setItem(e.target.value)}
        />
        <br />

        <input type="submit" />
      </form>

      <ul>
        {list.map((listItem) => {
          return (
            <ShoppingDetails key={listItem.id} itemDetailObject={listItem} />
          );
        })}
      </ul>
    </>
  );
};

export default ShoppingList;

//CURSOR PARKING: *************
// Click here
