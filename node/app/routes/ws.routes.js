const {
  modelsController,
  yearsController,
  trimsController,
  searchController,
  makesController,
} = require("../controllers/ws.controllers");

const router = require("express").Router();

router.get("/makes", makesController);
router.get("/models/:make", modelsController);
router.get("/years/:make/:model", yearsController);
router.get("/trims/:make/:model/:year", trimsController);
router.get("/search", searchController);

module.exports = router;
