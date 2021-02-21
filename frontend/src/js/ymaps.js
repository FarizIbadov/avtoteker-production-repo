ymaps.ready(init);

const center = [40.40432361546929, 49.877367169701486];

function init() {
  var map = new ymaps.Map("map", {
    center,
    zoom: 17,
    controls: ["zoomControl"],
    behaviors: ["drag"],
  });

  const placemark = new ymaps.Placemark(center, {
    hintContent: "Avtotəkər",
  });

  map.geoObjects.add(placemark);
}
