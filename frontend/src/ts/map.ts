
class AvtoMap {
  map: any = null;
  maps: any = null;
  currentTarget: Element | null = null;
  mapTabs = document.querySelectorAll(".map-item");
  mainTab = document.getElementById("main-map");

  mapContainer = document.getElementById("map");

  constructor() {
    this.setDefaultMap();
    this.setMapTabs();
  }

  setMapTabs = () => {
    this.mapTabs.forEach(tab => {
      tab.addEventListener('click', (e) => {
        const target = e.target as HTMLElement
        const currentTab = target.closest("button") as HTMLButtonElement;
        const link = currentTab.getAttribute("map-href");
        const image = currentTab.getAttribute("map-url");
        this.setImage(link, image);
      })
    })
  };

  setDefaultMap = () => {
    for (const tab of this.mapTabs) {
      if (tab.classList.contains("map-active")) {
        const link = tab.getAttribute("map-href");
        const image = tab.getAttribute("map-url");
        this.setImage(link, image);
        break;
      }
    }
  };

  setImage = (link: string | null, image: string | null) => {
    this.mapContainer!.innerHTML = "";
    const img = document.createElement("img");
    const a = document.createElement("a");
    a.classList.add("w-100", "h-100");
    img.classList.add("w-100", "h-100", "object-fit-cover");

    if (link) {
      a.setAttribute("href", link);
    }

    if (image) {
      img.setAttribute("src", image);
      img.setAttribute("alt", image);
    }

    a.insertAdjacentElement("beforeend", img);
    this.mapContainer!.insertAdjacentElement("beforeend", a);
  };
}

new AvtoMap();
