class ImagePreview {
  modalImg = document.querySelector("#imagePreview img");
  constructor() {
    const images = document.querySelectorAll<HTMLImageElement>(
      ".main-list__img",
    );

    images.forEach(image => {
      image.addEventListener("click", e => {
        const target = e.target as HTMLImageElement;
        const { src, alt } = target;
        if (this.modalImg) {
          this.modalImg.setAttribute("src", src);
          this.modalImg.setAttribute("alt", alt);
        }
      });
    });
  }
}

new ImagePreview();
