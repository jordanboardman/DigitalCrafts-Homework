import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { createStore } from "redux";
import counterReducer from "./reducers/counter";
import { Provider } from "react-redux";

const store = createStore(
  counterReducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);

// // STORE -> GLOBALIZED ACTION

// const store = createStore(counter);

// // Display in console
// store.subscribe(() => console.log(store.getState()));

// // ACTIONN INCREMENT
// const increment = () => {
//   return {
//     type: "INCREMENT",
//   };
// };
// const decrement = () => {
//   return {
//     type: "DECREMENT",
//   };
// };

// // REDUCER
// const counter = (state = 0, action) => {
//   switch (action.type) {
//     case "INCREMENT":
//       return state + 1;
//     case "DECREMENT":
//       return state - 1;
//   }
// };

// // DISPATCH
// store.dispatch(increment());
// store.dispatch(decrement());
// store.dispatch(decrement());

// const root = ReactDOM.createRoot(document.getElementById("root"));
ReactDOM.render(
  <Provider store={store}>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </Provider>,
  document.getElementById("root")
);
