import React from "react";

/**
 * {
 * id
 * item
 * }
 */
const ShoppingDetails = ({ itemDetailObject }) => {
  return (
    <>
      <li key={itemDetailObject.id}> {itemDetailObject.item}</li>
    </>
  );
};

export default ShoppingDetails;
