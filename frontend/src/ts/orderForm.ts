import axios from "axios";

class OrderForm {
  private data = {};
  form?: HTMLFormElement;
  constructor(private formClass: string, private formFields: Field[]) {
    this.initForm();
  }

  initForm = () => {
    this.form = document.querySelector(this.formClass) as HTMLFormElement;
    if (this.form) {
      this.form.addEventListener("submit", this.handleSubmit);
    }
  };

  handleSubmit = (e: Event) => {
    e.preventDefault();
    if (this.form!.checkValidity()) {
      this.getFormData();
      this.postData();
    }
  };

  getFormData = () => {
    for (const field of this.formFields) {
      const fieldValue = this.getFieldValue(field);
      this.data = {
        ...this.data,
        ...fieldValue,
      };
    }
  };

  getFieldValue = (field: Field): FieldData => {
    const { value } = document.getElementById(field.id) as HTMLInputElement;
    const name = field.id.replace("id_", "");
    return { [name]: field.type(value) };
  };

  postData = () => {
    const action = this.form!.getAttribute("action")!;
    const config = this.getConfig();
    const orderModalFooter = document.getElementById("order-modal-footer")!;
    const orderModalBody = document.getElementById("order-modal-body")!;
    const modalForm = document.getElementById("modal-form");

    orderModalFooter.classList.add("d-none");

    const loadingSpinner = `
      <div class="text-center text-my-secondary" id="spinner">
        <div class="spinner-border" style="width: 5rem; height: 5rem;" role="status">
          <span class="sr-only">Loading...</span>
        </div>
      </div>
    `;

    orderModalBody.insertAdjacentHTML("afterbegin", loadingSpinner);
    modalForm!.classList.add("d-none");

    axios
      .post(action, this.data, config)
      .then(() => {
        this.removeSpinner();
        modalForm!.classList.remove("d-none");
        orderModalFooter.classList.remove("d-none");
      })
      .catch(e => {
        console.log(e.response.data);
        this.removeSpinner();
        modalForm!.classList.remove("d-none");
        orderModalFooter.classList.remove("d-none");
      });
  };

  getConfig = () => {
    const { value: csrftoken } = document.querySelector(
      "[name=csrfmiddlewaretoken]",
    ) as HTMLInputElement;
    return { headers: { "X-CSRFToken": csrftoken } };
  };

  removeSpinner = () => {
    const spinner = document.getElementById("spinner")!;
    spinner.remove();
  };
}

new OrderForm(".tire-order", [
  { id: "id_quantity", type: Number },
  { id: "id_payment_type", type: Number },
  { id: "id_phone", type: String },
  { id: "id_name", type: String },
  { id: "id_tire", type: Number },
]);

new OrderForm(".oil-order", [
  { id: "id_note", type: String },
  { id: "id_payment_type", type: Number },
  { id: "id_phone", type: String },
  { id: "id_name", type: String },
  { id: "id_oil", type: Number },
]);
