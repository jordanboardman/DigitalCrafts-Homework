import React from "react";
import { Link } from "react-router-dom";

// anchor Link

// create 2 components: Forms, FormsClass, News
// add components to react-router index.js
// add the links to baselayout
const BaseLayout = (props) => {
  return (
    <>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/forms">Forms</Link>
        </li>
        <li>
          <Link to="/classlass">Forms for Class</Link>
        </li>
        <li>
          <Link to="/news">News</Link>
        </li>
        <li>
          <Link to="/shoppinglist">Shopping List</Link>
        </li>
        <li>
          <Link to="/addressbook">Address Book</Link>
        </li>
      </ul>

      {props.children}
    </>
  );
};

export default BaseLayout;
