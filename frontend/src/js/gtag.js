class GoogleConversion {
  price = null;

  constructor() {
    const cartBtns = document.querySelectorAll(".main-list__cart-btn");
    cartBtns.forEach(cartBtn =>
      cartBtn.addEventListener("click", this.configBtn.bind(this)),
    );
    const orderBtn = document.getElementById("order-btn");
    if (orderBtn) {
      orderBtn.addEventListener(
        "click",
        this.gtag_report_conversion.bind(this),
      );
    }
  }

  configBtn(event) {
    const target = event.target;
    const button = target.closest(".main-list__cart-btn");
    this.price = +button.getAttribute("data-price");
  }

  gtag_report_conversion() {
    var callback = function () {};
    gtag("event", "conversion", {
      send_to: "AW-748783498/HaZ5CKmw7u8BEIqPhuUC",
      value: this.price,
      currency: "USD",
      event_callback: callback,
    });
    return false;
  }
}

new GoogleConversion();
