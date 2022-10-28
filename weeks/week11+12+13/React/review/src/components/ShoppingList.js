import React from "react";
import { useState } from "react";

const ShoppingList = () => {
  const [text, setText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    let shopList = {
      text,
    };
    let addItem = shopList.text;
    let newElement = makeElement();
    document.body.append(newElement);
    newElement.append(addItem);
  };

  function makeElement() {
    return document.createElement("li");
  }

  return (
    <>
      <h2>Shopping List</h2>
      <br />

      <h3>Add new item:</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <br />
      </form>

      <input type="submit">Submit</input>
    </>
  );
};

export default ShoppingList;

// YOU CAN DO IT THIS WAY TOO. VERONICA'S WAY.

// import React, {useState} from 'react'

// const ShoppingList = () => {
//   const [item, setItem] = useState("");
//   const [list, setList] = useState([]);

//   const handleSubmit = (e) => {
//     e.preventDefault();
//     let newList = [item, ...list]
//     setList(newList)
//     setItem("")

//     console.log(list);
//   }

//   return (
//     <>
//       <h2>Shopping List</h2>
//       <br />

//       <h3>Add new Item:</h3>

//       <form onSubmit={handleSubmit}>
//         <input type="text" value={item} onChange={e=>setItem(e.target.value)}/>
//         <br />

//         <input type="submit" />
//       </form>

//     <ul>

//        {list.map(listItem =>{
//            return <li key={listItem}>{listItem}</li>
//        })}
//     </ul>

//     </>
//   )
// }

// export default ShoppingList

//CURSOR PARKING: *************
// Click here
