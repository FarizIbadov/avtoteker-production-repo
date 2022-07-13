const kreditTaksitQtnBtns = document.querySelectorAll(".kredit-taksit-qtn-btn");
const kreditTaksitTotals = document.querySelectorAll(
  ".kredit-taksit-qtn-with-price",
);

if (kreditTaksitQtnBtns.length > 0) {
    kreditTaksitQtnBtns.forEach(btn => {
        btn.addEventListener('click', e => {
            kreditTaksitQtnBtns.forEach(btn => {
                btn.classList.remove('active');
            })
            const button = e.target as HTMLButtonElement;
            button.classList.add('active')
            const qtn = +button.getAttribute('data-qtn')!

            if (kreditTaksitTotals.length > 0) {
              kreditTaksitTotals.forEach(total => {
                const rawTotalPrice = total.getAttribute("data-total") || "0";
                const totalPrice = +rawTotalPrice.replace(",", ".");

                if (qtn * totalPrice == 0) {
                  total.innerHTML = "0";
                }
                else {
                  const price = (qtn * totalPrice).toFixed(2);
                  total.innerHTML = String(price);
                }
              });
            }
        })
    })
}