const kreditTaksitQtnBtns = document.querySelectorAll(".kredit-taksit-qtn-btn");
const kreditTaksitTotals = document.querySelectorAll(".kredit-taksit-total");

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
                const rawTotalPrice = total.getAttribute("data-total")!;
                const totalPrice = +rawTotalPrice.replace(",", ".");
          
                total.innerHTML = String(qtn * totalPrice)
              });
            }
        })
    })
}