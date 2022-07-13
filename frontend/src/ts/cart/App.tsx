import React from "react";
import ReactDOM from "react-dom";
import { Routes, Route, BrowserRouter } from "react-router-dom";

import CartPage from "./views/CartPage";
import OrderPage from "./views/OrderPage";

const cartContainer = document.getElementById("cart");

const App: React.FC<CartSettings> = props => {
  return (
    <div className="container">
      <Routes>
        <Route path={props.path} element={<CartPage />} />
        <Route path={props.path + "order"} element={<OrderPage />} />
      </Routes>
    </div>
  );
};

const path = cartContainer!.getAttribute("data-path")!;

ReactDOM.render(
  <BrowserRouter>
    <App path={path} />
  </BrowserRouter>,
  cartContainer,
);
