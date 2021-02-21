require("dotenv").config();
const path = require("path");
const express = require("express");
const ws_api_client = require("ws-api-client-nodejs");
const wsRouters = require("./routes/ws.routes");

const defaultClient = ws_api_client.ApiClient.instance;
const userKey = defaultClient.authentications["user_key"];
userKey.apiKey = process.env.WHEEL_SIZE_KEY;

const app = express();

app.use(express.json());

app.use("/", wsRouters);

app.use((error, req, res, next) => {
  console.log(error);
  res.status(500).json({ message: "Error!" });
});

app.listen(80, "0.0.0.0", () => {
  console.log("App is running on http://localhost:80/");
});
