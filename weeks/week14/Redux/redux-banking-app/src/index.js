// import React from 'react';
// import ReactDOM from 'react-dom/client';
// import './index.css';
// import App from './App';
// import reportWebVitals from './reportWebVitals';

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );

// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();

import { createStore } from "redux";

console.log("Starting banking app");

const defaultState = {
  balance: 0,
};

const actionIncrement = {
  type: "increment",
};

const actionDecrement = {
  type: "decrement",
};

function account(state = defaultState, action) {
  switch (action.type) {
    case "increment":
      return {
        balance: state.balance + 1,
      };
    case "decrement":
      {
        return {
          balance: state.balance - 1,
        };
      }
      return state;
  }
}

const store = createStore(account);
