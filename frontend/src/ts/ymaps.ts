import ymaps from "ymaps/dist/ymaps.esm.js";

class Ymaps {
  map: any = null;
  maps: any = null;
  currentTarget: Element | null = null;
  mapTabs = document.querySelectorAll(".map-item");
  mainTab = document.getElementById("main-map");

  mapContainer = document.getElementById("map");

  constructor() {
    this.load();
  }

  init() {
    this.setTargetMap(this.mainTab);
  }

  setMap(lon: number, lat: number) {
    if (this.mapContainer) {
      this.mapContainer.innerHTML = "";
    }
    this.map = new this.maps.Map("map", {
      center: [lon, lat],
      zoom: 17,
      controls: ["zoomControl"],
      behaviors: ["drag"],
    });

    const placemark = new this.maps.Placemark([lon, lat], {
      hintContent: "Avtotəkər",
    });

    this.map.geoObjects.add(placemark);
  }

  setTargetMap(target: Element | null) {
    if (target) {
      const lon = +target.getAttribute("data-lon")!;
      const lat = +target.getAttribute("data-lat")!;
      this.setMap(lon, lat);
    }
  }

  // setLoadingTemplate() {
  //   if (this.mapContainer) {
  //     this.mapContainer.innerHTML = "";
  //     const loader = document.createElement("div");
  //     loader.classList.add("loader");
  //     this.mapContainer.insertAdjacentElement("beforeend", loader);
  //   }
  // }

  // setError() {
  //   if (this.mapContainer) {
  //     this.mapContainer.innerHTML = `
  //       <div>
  //         <svg class="map-repeat-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-counterclockwise" viewBox="0 0 16 16">
  //           <path fill-rule="evenodd" d="M8 3a5 5 0 1 1-4.546 2.914.5.5 0 0 0-.908-.417A6 6 0 1 0 8 2v1z"/>
  //           <path d="M8 4.466V.534a.25.25 0 0 0-.41-.192L5.23 2.308a.25.25 0 0 0 0 .384l2.36 1.966A.25.25 0 0 0 8 4.466z"/>
  //         </svg>
  //         <p class="text-center text-danger font-weight-bold">Xəta baş verdi</p>
  //       </div>
  //     `;

  //     // this.mapContainer
  //     //   .querySelector(".map-repeat-icon")!
  //     //   .addEventListener("click", this.load.bind(this));
  //   }
  // }

  load() {
    this.currentTarget = this.mainTab;
    // this.setLoadingTemplate();

    ymaps
      .load()
      .then((maps: any) => {
        this.maps = maps;
        this.init();

        this.mapTabs.forEach(tab => {
          tab.addEventListener("click", e => {
            const element = e.target as Element;
            if (!element.classList.contains("map-active")) {
              this.currentTarget!.classList.remove("map-active");
              const target = e.target as Element;
              this.setTargetMap(target as Element);
              target!.classList.add("map-active");
              this.currentTarget = target;
            }
          });
        });
      })
      .catch(() => {
        // this.setError();
      });
  }
}

new Ymaps();
