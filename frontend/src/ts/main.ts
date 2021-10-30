import "../sass/main.scss";
import "../img/logo.svg";
import "../img/icons.svg";
import "../img/cart.svg";
import "../img/manat.png";
import "../fonts/Averta_Avto.ttf";
import "../fonts/346526_2_0-b68b923f95695860fef4e27dbe4c742c.woff2";
import "../fonts/346526_C_0-2698ac8eb8035cbb2f4007204717b111.woff2";
import "../fonts/346526_C_0-d543b03fa0c0fb9a4f9f156b4facf083.woff2";
import "bootstrap";
import "slick-carousel";

import "./ymaps";
import "./brandCarousel";
import "./tireSearch";
import "./imagePreview";
import "./orderForm";
import "./videoPlayer";

const form = document.querySelector<HTMLFormElement>(".needs-validation");
const listCartBtns = document.querySelectorAll<HTMLButtonElement>(".order-btn");
const tireInput = document.getElementById("id_tire") as HTMLInputElement;
const oilInput = document.getElementById("id_oil") as HTMLInputElement;

const quantityInput = document.getElementById(
  "id_quantity",
) as HTMLInputElement;

listCartBtns.forEach(listCartBtn => {
  listCartBtn.addEventListener("click", e => {
    const target = e.target as HTMLElement;
    const btn = target.closest(".order-btn") as HTMLButtonElement;
    const id = btn.getAttribute("data-id")!;
    if (tireInput) {
      const max = btn.getAttribute("data-max")!;
      tireInput.setAttribute("value", id);
      quantityInput.setAttribute("max", max);
    } else if (oilInput) {
      oilInput.setAttribute("value", id);
    }
  });
});

if (form) {
  form.addEventListener("submit", e => {
    if (form.checkValidity() === false) {
      e.preventDefault();
      e.stopPropagation();
      form.classList.add("was-validated");
    }
  });
}

const langDropDown = document.getElementById("lang-dropdown")!;
const navBurger = document.getElementById("nav-burger")!;
const navList = document.getElementById("nav-list")!;

window.addEventListener("scroll", () => {
  if (window.scrollY >= 43) {
    langDropDown.classList.add("d-none");
    navBurger.classList.remove("toggler-extra");
    navList.classList.remove("nav-extra");
  } else {
    langDropDown.classList.remove("d-none");
    navBurger.classList.add("toggler-extra");
    navList.classList.add("nav-extra");
  }
});
