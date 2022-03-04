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

  load() {
    this.currentTarget = this.mainTab;

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
