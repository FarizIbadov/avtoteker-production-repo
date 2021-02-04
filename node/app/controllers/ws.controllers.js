const ws_api_client = require("ws-api-client-nodejs");
const uuid = require('uuid').v4;

exports.makesController = (req, res, next) => {
  try {
    const apiInstance = new ws_api_client.MakesApi();
    const callback = (error, data, response) => {
      if (error) {
        throw error;
      } else {
        res.json(data);
      }
    };
    apiInstance.makesList({}, callback);
  } catch (err) {
    next(err);
  }
};

exports.modelsController = (req, res, next) => {
  try {
    const apiInstance = new ws_api_client.ModelsApi();
    const make = req.params.make;

    const callback = getCallback(res, next);
    apiInstance.modelsList(make, {}, callback);
  } catch (err) {
    next(err);
  }
};

exports.yearsController = (req, res, next) => {
  try {
    const apiInstance = new ws_api_client.YearsApi();

    const { make, model } = req.params;

    const opts = {
      model,
    };

    const callback = getCallback(res, next);
    apiInstance.yearsList(make, opts, callback);
  } catch (err) {
    next(err);
  }
};

exports.trimsController = (req, res, next) => {
  try {
    const apiInstance = new ws_api_client.TrimsApi();

    const { make, model } = req.params;
    const year = +req.params.year;

    const callback = (error, data, response) => {
      if (error) {
        throw error;
      } else {
        const customDataArray = [];
        const uniqueNames = [];

        for (const trimData of data) {
          const customData = {};
          if (!uniqueNames.includes(trimData.trim)) {
            customData["slug"] = trimData.slug;
            customData["name"] = trimData.trim;
            customDataArray.push(customData);
            uniqueNames.push(trimData.trim);
          }
        }
        res.json(customDataArray);
      }
    };
    apiInstance.trimsList(make, model, year, callback);
  } catch (err) {
    next(err);
  }
};

exports.searchController = (req, res, next) => {
  try {
    const apiInstance = new ws_api_client.SearchApi();

    const { make, model, trim, year } = req.query;
    const callback = (error, data, response) => {
      if (error) {
        throw error;
      } else {
        const tires = []

        for (const dataItem of data) {
          for (const wheel of dataItem.wheels) {
            const wheelId = uuid();
            const pressure = []
  
            if (wheel.front.tire) {
              if (wheel.front.tire_pressure){
                const bar = wheel.front.tire_pressure.bar + ' bar';
                const kPa =  wheel.front.tire_pressure.kPa + ' kPa';
                pressure.push(bar,kPa);
              } else {
                pressure.push('-','-');
              }

              const tireType = !wheel.rear.tire ? 3 : 1;
              const tireObj = {
                "wheel_id":wheelId,
                "rim":wheel.front.rim,
                "tire_type":tireType,
                "tire":wheel.front.tire,
                "pressure":pressure.join(" / ")
              }
              tires.push(tireObj);
            }

            if (wheel.rear.tire) {
              if (wheel.rear.tire_pressure){
                const bar = wheel.rear.tire_pressure.bar + ' bar';
                const kPa =  wheel.rear.tire_pressure.kPa + ' kPa';
                pressure.push(bar,kPa);
              } else {
                pressure.push('-','-');
              }

              const tireObj = {
                "wheel_id":wheelId,
                "rim":wheel.rear.rim,
                "tire_type":2,
                "tire":wheel.rear.tire,
                "pressure":pressure.join(" / ")
              }
              tires.push(tireObj);
            }
          }
        }
        res.json(tires);
        }
      
    }
    
    apiInstance.searchByModelList(make, model, +year, { trim }, callback);
  } catch (err) {
    next(err);
  }
};

const getCallback = (res, next) => (error, data, response) => {
  if (error) {
    throw error;
  } else {
    res.json(data);
  }
};
