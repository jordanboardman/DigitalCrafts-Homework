import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { increment } from "./actions/index.js";
import { decrement } from "./actions/index.js";

const App = () => {
  const counter = useSelector((state) => state.payload);
  // const isLogged = useSelector((state) => state.isLogged);
  const dispatch = useDispatch();

  return (
    <div className="App">
      <h1>Counter {counter}</h1>
      <button onClick={() => dispatch(increment(5))}>+</button>
      <button onClick={() => dispatch(decrement())}>-</button>
      {/* <h3>{isLogged ? <h3>Valuable Information I Shouldn't See</h3> : ""}</h3> */}
    </div>
  );
};

export default App;
