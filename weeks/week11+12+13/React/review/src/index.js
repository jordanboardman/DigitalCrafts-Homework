import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import {
  BrowserRouter as Router,
  Routes as Switch,
  Route,
} from "react-router-dom";
import BaseLayout from "./components/layout/BaseLayout";
import Forms from "./components/Forms";
import FormsClass from "./components/FormsClass";
import News from "./components/News";
import ShoppingList from "./components/ShoppingList";
import AddressBook from "./components/AddressBook";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Router>
      <BaseLayout>
        <Switch>
          <Route path="/" element={<App />} />
          <Route path="/forms" element={<Forms />} />
          <Route path="/class" element={<FormsClass />} />
          <Route path="/news" element={<News />} />
          <Route path="/shoppinglist" element={<ShoppingList />} />
          <Route path="/addressbook" element={<AddressBook />} />
        </Switch>
      </BaseLayout>
    </Router>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
