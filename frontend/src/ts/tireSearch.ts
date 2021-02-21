import axios, { AxiosResponse } from "axios";

interface ResData {
  name: string;
  slug: string;
}

class TireSearch {
  tireSearchSubmitBtn: HTMLButtonElement = document.getElementById(
    "tire-search-submit-btn",
  ) as HTMLButtonElement;

  make = "";
  model = "";
  year = "";

  state: "size" | "car" = "size";
  settedUp = false;

  constructor() {
    const sizeTab = document.getElementById("size-tab");
    const carTab = document.getElementById("car-tab");

    if (sizeTab) {
      sizeTab.addEventListener("click", e => {
        const target = e.target as HTMLElement;
        this.setFormAction(target);
        this.tireSearchSubmitBtn!.removeAttribute("disabled");
        this.setName("width", "height", "radius");
        this.removeName("make", "model", "year", "trim");
        this.resetSelect("make", "model", "year", "trim");
        this.state = "size";
      });
    }

    if (carTab) {
      carTab.addEventListener("click", e => {
        const target = e.target as HTMLElement;
        this.setFormAction(target);
        this.tireSearchSubmitBtn!.setAttribute("disabled", "");
        this.removeName("width", "height", "radius");
        this.setName("make", "model", "year", "trim");
        this.carSearch();
      });
    }

    this.onResetForm();
  }

  resetSelect(...elementIds: string[]) {
    for (const elementId of elementIds) {
      const select = document.getElementById(elementId) as HTMLSelectElement;
      select.querySelectorAll("option").forEach(option => {
        if (option.value) {
          select.removeChild(option);
        }
      });
      select.setAttribute("disabled", "");
    }
  }

  setName(...elementIds: string[]) {
    for (const elementId of elementIds) {
      const select = document.getElementById(elementId) as HTMLSelectElement;
      const name = select.getAttribute("data-name")!;
      select.setAttribute("name", name);
    }
  }

  removeName(...elementIds: string[]) {
    for (const elementId of elementIds) {
      const select = document.getElementById(elementId) as HTMLSelectElement;
      select.removeAttribute("name");
    }
  }

  setFormAction(element: HTMLElement) {
    const form = document.getElementById("tire-search") as HTMLFormElement;
    const closestListItem = element.closest("li");
    const action = closestListItem!.getAttribute("data-action")!;
    form.setAttribute("action", action);
  }

  carSearch() {
    const make = document.getElementById("make") as HTMLSelectElement;
    const model = document.getElementById("model") as HTMLSelectElement;
    const year = document.getElementById("year") as HTMLSelectElement;
    const trim = document.getElementById("trim") as HTMLSelectElement;

    if (this.state === "size") {
      axios
        .get<any, AxiosResponse<ResData[]>>("/api/makes/")
        .then(res => {
          this.resetSelect("make", "model", "year", "trim");
          this.putOptions(make, res.data);
          make.removeAttribute("disabled");
        })
        .catch(console.log);

      !this.settedUp &&
        make.addEventListener("change", e => {
          model.setAttribute("disabled", "");
          this.tireSearchSubmitBtn.setAttribute("disabled", "");
          this.resetSelect("model", "year", "trim");
          const target = e.target as HTMLSelectElement;
          this.make = target.value;
          axios
            .get<any, AxiosResponse<ResData[]>>(
              `/api/models/?make=${this.make}`,
            )
            .then(res => {
              this.putOptions(model, res.data);
              model.removeAttribute("disabled");
            })
            .catch(console.log);
        });

      !this.settedUp &&
        model.addEventListener("change", e => {
          year.setAttribute("disabled", "");
          this.tireSearchSubmitBtn.setAttribute("disabled", "");
          this.resetSelect("year", "trim");
          const target = e.target as HTMLSelectElement;
          this.model = target.value;
          const { model, make } = this;
          axios
            .get<any, AxiosResponse<ResData[]>>(
              `/api/years/?model=${model}&make=${make}`,
            )
            .then(res => {
              this.putOptions(year, res.data);
              year.removeAttribute("disabled");
            })
            .catch(console.log);
        });

      !this.settedUp &&
        year.addEventListener("change", e => {
          trim.setAttribute("disabled", "");
          this.tireSearchSubmitBtn.setAttribute("disabled", "");
          this.resetSelect("trim");
          const target = e.target as HTMLSelectElement;
          this.year = target.value;
          const { model, make, year } = this;
          axios
            .get<any, AxiosResponse<ResData[]>>(
              `/api/trims/?model=${model}&make=${make}&year=${year}`,
            )
            .then(res => {
              this.putOptions(trim, res.data);
              trim.removeAttribute("disabled");
            })
            .catch(console.log);
        });

      !this.settedUp &&
        trim.addEventListener("change", e => {
          const { value } = e.target as HTMLSelectElement;
          const button = this.tireSearchSubmitBtn;
          if (value) {
            button.removeAttribute("disabled");
          } else {
            button.setAttribute("disabled", "");
          }
        });
    }

    this.settedUp = true;
    this.state = "car";
  }

  putOptions(element: HTMLSelectElement, dataList: ResData[]) {
    dataList.forEach(data => {
      const option = document.createElement("option");
      option.value = data.slug;
      option.innerText = data.name;
      element.insertAdjacentElement("beforeend", option);
    });
  }

  onResetForm() {
    const form = document.getElementById("tire-search") as HTMLFormElement;
    if (form) {
      form.addEventListener("reset", () => {
        if (this.state === "size") {
          const selects = document.querySelectorAll<HTMLSelectElement>(
            ".size-select",
          );
          selects.forEach(select => {
            select.querySelectorAll("option").forEach(option => {
              option.removeAttribute("selected");
            });
          });
        }
        if (this.state === "car") {
          this.tireSearchSubmitBtn.setAttribute("disabled", "");
          this.resetSelect("model", "year", "trim");
          const make = document.getElementById("make") as HTMLSelectElement;
          make.setAttribute("value", "");
        }
      });
    }
  }
}

new TireSearch();
