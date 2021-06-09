declare module "ymaps/dist/ymaps.esm.js";

interface FieldData {
  [string]: string;
}

interface Field {
  id: string;
  type: NumberConstructor | StringConstructor;
}
