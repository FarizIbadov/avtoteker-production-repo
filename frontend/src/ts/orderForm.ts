import axios from "axios";

class OrderForm {
  private data = {};
  errorMessageIds: string[] = [];
  form?: HTMLFormElement;
  orderBtn?: HTMLButtonElement;
  modalForm?: HTMLElement;
  cancelBtn?: HTMLButtonElement;
  modalTitle?: HTMLElement;

  constructor(private formClass: string, private formFields: Field[]) {
    this.initForm();
  }

  initForm = () => {
    this.form = document.querySelector(this.formClass) as HTMLFormElement;
    this.cancelBtn = document.getElementById("cancel-btn") as HTMLButtonElement;

    if (this.cancelBtn) {
      this.cancelBtn.addEventListener("click", () => {
        this.resetHandler();
      });
    }

    if (this.form) {
      this.modalTitle = this.form.querySelector(".modal-title") as HTMLElement;
      this.disableFormBtn();
      this.form.addEventListener("click", e => {
        if (e.target === this.form) {
          this.resetHandler();
        }
      });
      this.form.addEventListener("input", this.disableFormBtn);
      this.form.addEventListener("submit", this.handleSubmit);
    }
  };

  resetHandler = () => {
    if (this.form) {
      this.form.reset();
    }
    this.disableFormBtn();
    this.cancelBtn!.innerHTML = "İmtina";
    if (this.orderBtn) {
      this.orderBtn!.classList.remove("d-none");
    }
    this.removeResultView();
    this.removeErrors();
    if (this.modalTitle) {
      this.modalTitle!.classList.remove("non-visible");
    }
    if (this.modalForm) {
      this.modalForm!.classList.remove("d-none");
    }
  };

  disableFormBtn = () => {
    if (this.form) {
      this.orderBtn = this.form!.querySelector(
        "#order-btn",
      ) as HTMLButtonElement;
      this.orderBtn!.setAttribute("disabled", "");

      if (this.form!.checkValidity()) {
        this.orderBtn!.removeAttribute("disabled");
      } else {
        this.orderBtn!.setAttribute("disabled", "");
      }
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
    this.modalForm = document.getElementById("modal-form") as HTMLElement;

    orderModalFooter.classList.add("d-none");
    this.modalTitle!.classList.add("non-visible");

    const loadingSpinner = `
      <div class="text-center text-my-secondary" id="spinner">
        <div class="spinner-border" style="width: 5rem; height: 5rem;" role="status">
          <span class="sr-only">Loading...</span>
        </div>
      </div>
    `;

    orderModalBody.insertAdjacentHTML("afterbegin", loadingSpinner);
    this.modalForm!.classList.add("d-none");

    axios
      .post(action, this.data, config)
      .then(res => {
        this.removeSpinner();
        const orderId = res.data["order_id"];

        this.putResultView(orderModalBody, orderId, res.data.result);
        this.orderBtn!.classList.add("d-none");
        this.cancelBtn!.innerText = res.data.result["message"];
        orderModalFooter.classList.remove("d-none");
      })
      .catch(e => {
        this.removeSpinner();
        this.modalTitle!.classList.remove("non-visible");
        this.modalForm!.classList.remove("d-none");
        orderModalFooter.classList.remove("d-none");
        this.putErrors(e.response!.data);
      });
  };

  getConfig = () => {
    const { value: csrftoken } = document.querySelector(
      "[name=csrfmiddlewaretoken]",
    ) as HTMLInputElement;
    return { headers: { "X-CSRFToken": csrftoken } };
  };

  removeSpinner = () => {
    const spinner = document.getElementById("spinner");
    if (spinner) {
      spinner.remove();
    }
  };

  putErrors = (errorData: ErrorData) => {
    for (const field in errorData) {
      const value = errorData[field];
      const message = value[value.length - 1];
      const fieldId = "id_" + field;
      const input = document.getElementById(fieldId) as HTMLInputElement;
      input.classList.remove("is-valid");
      input.classList.add("is-invalid");

      const inputContainer = input.closest("div");
      const feedback = this.createFeedback(fieldId, message);

      inputContainer!.insertAdjacentElement("beforeend", feedback);
    }
  };

  createFeedback = (fieldId: string, message: string) => {
    const feedback = document.createElement("div");
    feedback.id = fieldId + "_feedback";
    const existingFeedback = document.getElementById(feedback.id);

    if (existingFeedback) {
      existingFeedback.remove();
    }

    this.errorMessageIds.push(feedback.id);
    feedback.classList.add("invalid-feedback");

    feedback.innerText = message;

    return feedback;
  };

  removeErrors = () => {
    for (const feedbackId of this.errorMessageIds) {
      const element = document.getElementById(feedbackId) as HTMLElement;
      element.remove();
      const fieldId = feedbackId.replace("_feedback", "");
      const input = document.getElementById(fieldId) as HTMLInputElement;
      input.classList.remove("is-invalid");
    }
  };

  putResultView = (
    container: HTMLElement,
    orderId: string,
    result: OrderResult,
  ) => {
    this.removeResultView();

    const resultView = `
          <div id="order-success">
            <p class="h2 text-center">${result.head}</p>
            <p class="h5 font-weight-normal text-center">${result.sub}</p>
            <hr>
            <p class="h4 font-weight-normal text-center">
              ${result.order_id_part} - ${orderId}
            </p>
          </div>
        `;
    container.insertAdjacentHTML("afterbegin", resultView);
  };

  removeResultView = () => {
    const existingResultView = document.getElementById("order-success");
    if (existingResultView) {
      existingResultView.remove();
    }
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
