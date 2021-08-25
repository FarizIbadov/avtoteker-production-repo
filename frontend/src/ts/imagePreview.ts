class ImagePreview {
  modalImg = document.querySelector("#imagePreview img");
  constructor() {
    const images = document.querySelectorAll<HTMLElement>(".main-list__col-sm");

    images.forEach(image => {
      image.addEventListener("click", e => {
        const target = e.target as HTMLDivElement;
        const container = target.closest(".main-list__col-sm") as HTMLElement;
        const { src, alt } = container.querySelector(
          ".main-list__img",
        ) as HTMLImageElement;

        if (this.modalImg) {
          this.modalImg.setAttribute("src", src);
          this.modalImg.setAttribute("alt", alt);
        }
      });
    });
  }
}

new ImagePreview();
