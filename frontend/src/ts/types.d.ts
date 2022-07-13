declare module "ymaps/dist/ymaps.esm.js";

interface FieldData {
  [string]: string;
}

interface Field {
  id: string;
  type: NumberConstructor | StringConstructor;
}

interface ErrorData {
  [key: string]: string[];
}

interface OrderResult {
  [key: string]: string;
}

interface CartSettings {
  path: string;
}
