!function(c){function e(e){for(var t,n,r=e[0],i=e[1],a=e[2],o=0,s=[];o<r.length;o++)n=r[o],Object.prototype.hasOwnProperty.call(u,n)&&u[n]&&s.push(u[n][0]),u[n]=0;for(t in i)Object.prototype.hasOwnProperty.call(i,t)&&(c[t]=i[t]);for(m&&m(e);s.length;)s.shift()();return d.push.apply(d,a||[]),l()}function l(){for(var e,t=0;t<d.length;t++){for(var n=d[t],r=!0,i=1;i<n.length;i++){var a=n[i];0!==u[a]&&(r=!1)}r&&(d.splice(t--,1),e=o(o.s=n[0]))}return e}var n={},u={1:0},d=[];function o(e){if(n[e])return n[e].exports;var t=n[e]={i:e,l:!1,exports:{}};return c[e].call(t.exports,t,t.exports,o),t.l=!0,t.exports}o.m=c,o.c=n,o.d=function(e,t,n){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},o.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)o.d(n,r,function(e){return t[e]}.bind(null,r));return n},o.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="";var t=window.webpackJsonp=window.webpackJsonp||[],r=t.push.bind(t);t.push=e,t=t.slice();for(var i=0;i<t.length;i++)e(t[i]);var m=r;d.push([37,0]),l()}({13:function(e,t,n){},15:function(e,t,n){"use strict";function r(e,t){var n;if("undefined"==typeof Symbol||null==e[Symbol.iterator]){if(Array.isArray(e)||(n=function(e,t){if(!e)return;if("string"==typeof e)return s(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);"Object"===n&&e.constructor&&(n=e.constructor.name);if("Map"===n||"Set"===n)return Array.from(e);if("Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return s(e,t)}(e))||t&&e&&"number"==typeof e.length){n&&(e=n);var r=0,t=function(){};return{s:t,n:function(){return r>=e.length?{done:!0}:{done:!1,value:e[r++]}},e:function(e){throw e},f:t}}throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}var i,a=!0,o=!1;return{s:function(){n=e[Symbol.iterator]()},n:function(){var e=n.next();return a=e.done,e},e:function(e){o=!0,i=e},f:function(){try{a||null==n.return||n.return()}finally{if(o)throw i}}}}function s(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}new function t(){var i=this;!function(e){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this),this.map=null,this.maps=null,this.currentTarget=null,this.mapTabs=document.querySelectorAll(".map-item"),this.mainTab=document.getElementById("main-map"),this.mapContainer=document.getElementById("map"),this.setMapTabs=function(){i.mapTabs.forEach(function(e){e.addEventListener("click",function(e){i.mapTabs.forEach(function(e){e.classList.remove("map-active")});var t=e.target.closest("button");t.classList.add("map-active");e=t.getAttribute("map-href"),t=t.getAttribute("map-url");i.setImage(e,t)})})},this.setDefaultMap=function(){var t=r(i.mapTabs);try{for(t.s();!(n=t.n()).done;){var e=n.value;if(e.classList.contains("map-active")){var n=e.getAttribute("map-href"),e=e.getAttribute("map-url");i.setImage(n,e);break}}}catch(e){t.e(e)}finally{t.f()}},this.setImage=function(e,t){i.mapContainer.innerHTML="";var n=document.createElement("img"),r=document.createElement("a");r.classList.add("w-100","h-100"),r.setAttribute("target","blank"),n.classList.add("w-100","h-100","object-fit-cover"),e&&r.setAttribute("href",e),t&&(n.setAttribute("src",t),n.setAttribute("alt",t)),r.insertAdjacentElement("beforeend",n),i.mapContainer.insertAdjacentElement("beforeend",r)},this.setDefaultMap(),this.setMapTabs()}},16:function(e,t){function i(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}new(function(){function n(){var t=this;!function(e){if(!(e instanceof n))throw new TypeError("Cannot call a class as a function")}(this),this.price=null,document.querySelectorAll(".main-list__cart-btn").forEach(function(e){return e.addEventListener("click",t.configBtn.bind(t))});var e=document.getElementById("order-btn");e&&e.addEventListener("click",this.gtag_report_conversion.bind(this))}var e,t,r;return e=n,(t=[{key:"configBtn",value:function(e){e=e.target.closest(".main-list__cart-btn");this.price=+e.getAttribute("data-price")}},{key:"gtag_report_conversion",value:function(){return gtag("event","conversion",{send_to:"AW-748783498/HaZ5CKmw7u8BEIqPhuUC",value:this.price,currency:"USD",event_callback:function(){}}),!1}}])&&i(e.prototype,t),r&&i(e,r),n}())},35:function(e,t,n){"use strict";new function t(){var n=this;!function(e){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this),this.modalImg=document.querySelector("#imagePreview img"),document.querySelectorAll(".main-list__col-sm").forEach(function(e){e.addEventListener("click",function(e){var t=e.target.closest(".main-list__col-sm").querySelector(".main-list__img"),e=t.src,t=t.alt;n.modalImg&&(n.modalImg.setAttribute("src",e),n.modalImg.setAttribute("alt",t))})})}},36:function(e,t,n){"use strict";var r=document.querySelectorAll(".kredit-taksit-qtn-btn"),i=document.querySelectorAll(".kredit-taksit-qtn-with-price");0<r.length&&r.forEach(function(e){e.addEventListener("click",function(e){r.forEach(function(e){e.classList.remove("active")});e=e.target;e.classList.add("active");var n=+e.getAttribute("data-qtn");0<i.length&&i.forEach(function(e){var t=+(e.getAttribute("data-total")||"0").replace(",",".");n*t==0?e.innerHTML="0":(t=(n*t).toFixed(2),e.innerHTML=String(t))})})})},37:function(e,t,n){"use strict";n.r(t);n(13),n.p,n.p,n.p,n.p,n(14),n(15),n(16);var t=n(2),r=n.n(t);r()(document).ready(function(){r()(".customer-logos").slick({slidesToShow:6,slidesToScroll:1,autoplay:!0,autoplaySpeed:1500,arrows:!1,dots:!1,pauseOnHover:!1,responsive:[{breakpoint:768,settings:{slidesToShow:4}},{breakpoint:520,settings:{slidesToShow:2}}]})});var t=n(1),l=n.n(t);function s(e){return function(e){if(Array.isArray(e))return i(e)}(e)||function(e){if("undefined"!=typeof Symbol&&Symbol.iterator in Object(e))return Array.from(e)}(e)||function(e,t){if(!e)return;if("string"==typeof e)return i(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);"Object"===n&&e.constructor&&(n=e.constructor.name);if("Map"===n||"Set"===n)return Array.from(e);if("Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return i(e,t)}(e)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function i(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}function a(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}new(function(){function r(){var t=this;!function(e){if(!(e instanceof r))throw new TypeError("Cannot call a class as a function")}(this),this.tireSearchSubmitBtn=document.getElementById("tire-search-submit-btn"),this.make="",this.model="",this.year="",this.size="",this.actionVals=["_","_","_"],this.state="size",this.settedUp=!1;var e=document.getElementById("size-tab"),n=document.getElementById("car-tab");e&&e.addEventListener("click",function(e){e=e.target;t.setFormAction(e),t.tireSearchSubmitBtn.removeAttribute("disabled"),t.removeName("make","model","year","trim"),t.resetSelect("make","model","year","trim"),t.state="size",t.sizeSearch()}),n&&n.addEventListener("click",function(e){e=e.target;t.setFormAction(e),t.tireSearchSubmitBtn.setAttribute("disabled",""),t.setName("make","model","year","trim"),t.carSearch()}),this.onResetForm(),this.sizeSearch()}var e,t,n;return e=r,(t=[{key:"resetSelect",value:function(){for(var e=arguments.length,t=new Array(e),n=0;n<e;n++)t[n]=arguments[n];for(var r=0,i=t;r<i.length;r++)!function(){var e=i[r],t=document.getElementById(e);t.querySelectorAll("option").forEach(function(e){e.value&&t.removeChild(e)}),t.setAttribute("disabled","")}()}},{key:"setName",value:function(){for(var e=arguments.length,t=new Array(e),n=0;n<e;n++)t[n]=arguments[n];for(var r=0,i=t;r<i.length;r++){var a=i[r],o=document.getElementById(a),a=o.getAttribute("data-name");o.setAttribute("name",a)}}},{key:"removeName",value:function(){for(var e=arguments.length,t=new Array(e),n=0;n<e;n++)t[n]=arguments[n];for(var r=0,i=t;r<i.length;r++){var a=i[r];document.getElementById(a).removeAttribute("name")}}},{key:"setFormAction",value:function(e){var t=document.getElementById("tire-search"),e=e.closest("li").getAttribute("data-action");t.setAttribute("action",e)}},{key:"handleSizeSelectEvent",value:function(e){e=e.target.value;return e||"_"}},{key:"sizeSearch",value:function(){var n,e,r=this,t=document.getElementById("width"),i=document.getElementById("height"),a=document.getElementById("radius"),o=document.getElementById("tire-search");o&&((e=o.getAttribute("action"))!==(n=o.getAttribute("data-action"))&&(e=(e=e.split("/").filter(function(e){return e}))[e.length-1].split("-"),this.actionVals=s(e)),t&&t.addEventListener("change",function(e){r.actionVals[0]=r.handleSizeSelectEvent(e)}),i&&i.addEventListener("change",function(e){r.actionVals[1]=r.handleSizeSelectEvent(e)}),a&&a.addEventListener("change",function(e){r.actionVals[2]=r.handleSizeSelectEvent(e)}),o.addEventListener("submit",function(e){var t;"size"===r.state&&"/oil-list/"!==o.getAttribute("action")&&("___"!==r.actionVals.join("")?(t=n+r.actionVals.join("-"),o.setAttribute("action",t)):(t=n.substr(0,n.length),o.setAttribute("action",t)))}))}},{key:"carSearch",value:function(){var r=this,t=document.getElementById("make"),n=document.getElementById("model"),i=document.getElementById("year"),a=document.getElementById("trim"),e=t.getAttribute("data-url"),o=n.getAttribute("data-url"),s=i.getAttribute("data-url"),c=a.getAttribute("data-url");"size"===this.state&&(l.a.get(e).then(function(e){r.resetSelect("make","model","year","trim"),r.putOptions(t,e.data),t.removeAttribute("disabled")}).catch(console.log),this.settedUp||t.addEventListener("change",function(e){n.setAttribute("disabled",""),r.tireSearchSubmitBtn.setAttribute("disabled",""),r.resetSelect("model","year","trim");e=e.target;r.make=e.value,l.a.get(o,{params:{make:r.make}}).then(function(e){r.putOptions(n,e.data),n.removeAttribute("disabled")}).catch(console.log)}),this.settedUp||n.addEventListener("change",function(e){i.setAttribute("disabled",""),r.tireSearchSubmitBtn.setAttribute("disabled",""),r.resetSelect("year","trim");var t=e.target;r.model=t.value;e=r.model,t=r.make;l.a.get(s,{params:{make:t,model:e}}).then(function(e){r.putOptions(i,e.data),i.removeAttribute("disabled")}).catch(console.log)}),this.settedUp||i.addEventListener("change",function(e){a.setAttribute("disabled",""),r.tireSearchSubmitBtn.setAttribute("disabled",""),r.resetSelect("trim");var t=e.target;r.year=t.value;var n=r.model,e=r.make,t=r.year;l.a.get(c,{params:{model:n,make:e,year:t}}).then(function(e){r.putOptions(a,e.data),a.removeAttribute("disabled")}).catch(console.log)}),this.settedUp||a.addEventListener("change",function(e){var t=e.target.value,e=r.tireSearchSubmitBtn;t?e.removeAttribute("disabled"):e.setAttribute("disabled","")})),this.settedUp=!0,this.state="car"}},{key:"putOptions",value:function(n,e){e.forEach(function(e){var t=document.createElement("option");t.value=e.slug,t.innerText=e.name,n.insertAdjacentElement("beforeend",t)})}},{key:"onResetForm",value:function(){var t=this,n=document.getElementById("tire-search");n&&n.addEventListener("reset",function(){var e;"size"===t.state&&(document.querySelectorAll(".size-select").forEach(function(e){e.querySelectorAll("option").forEach(function(e){e.removeAttribute("selected")})}),e=n.getAttribute("data-action"),n.setAttribute("action",e),t.actionVals=["_","_","_"]),"car"===t.state&&(t.tireSearchSubmitBtn.setAttribute("disabled",""),t.resetSelect("model","year","trim"),document.getElementById("make").setAttribute("value",""))})}}])&&a(e.prototype,t),n&&a(e,n),r}());n(35);function o(t,e){var n,r=Object.keys(t);return Object.getOwnPropertySymbols&&(n=Object.getOwnPropertySymbols(t),e&&(n=n.filter(function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable})),r.push.apply(r,n)),r}function c(t){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{};e%2?o(Object(n),!0).forEach(function(e){u(t,e,n[e])}):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach(function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(n,e))})}return t}function u(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function d(e,t){var n;if("undefined"==typeof Symbol||null==e[Symbol.iterator]){if(Array.isArray(e)||(n=function(e,t){if(!e)return;if("string"==typeof e)return m(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);"Object"===n&&e.constructor&&(n=e.constructor.name);if("Map"===n||"Set"===n)return Array.from(e);if("Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return m(e,t)}(e))||t&&e&&"number"==typeof e.length){n&&(e=n);var r=0,t=function(){};return{s:t,n:function(){return r>=e.length?{done:!0}:{done:!1,value:e[r++]}},e:function(e){throw e},f:t}}throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}var i,a=!0,o=!1;return{s:function(){n=e[Symbol.iterator]()},n:function(){var e=n.next();return a=e.done,e},e:function(e){o=!0,i=e},f:function(){try{a||null==n.return||n.return()}finally{if(o)throw i}}}}function m(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}t=function t(e,n){var a=this;!function(e){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this),this.formClass=e,this.formFields=n,this.data={},this.errorMessageIds=[],this.initForm=function(){var e,t,n;a.form=document.querySelector(a.formClass),a.cancelBtn=document.getElementById("cancel-btn"),a.cancelBtn&&a.cancelBtn.addEventListener("click",function(){a.resetHandler()}),a.form&&(a.modalTitle=a.form.querySelector(".modal-title"),a.disableFormBtn(),a.form.addEventListener("click",function(e){e.target===a.form&&a.resetHandler()}),a.form.addEventListener("input",a.disableFormBtn),a.form.addEventListener("submit",a.handleSubmit),".tire-order"===a.formClass&&(e=document.getElementById("id_payment_type"),t=document.getElementById("id_email").closest(".col-md"),n=document.getElementById("id_taksit_choice").closest(".col-md"),e.addEventListener("change",function(e){e=e.target.value;"4"===e||"2"===e?("4"===e?n.classList.remove("d-none"):n.classList.add("d-none"),t.classList.remove("d-none")):t.classList.add("d-none")})))},this.resetHandler=function(){var e,t,n,r;a.form&&a.form.reset(),a.disableFormBtn(),a.cancelBtn.innerHTML="İmtina",a.orderBtn&&a.orderBtn.classList.remove("d-none"),a.removeResultView(),a.removeErrors(),a.modalTitle&&a.modalTitle.classList.remove("non-visible"),a.modalForm&&a.modalForm.classList.remove("d-none"),".tire-order"===a.formClass&&(e=document.getElementById("id_taksit_choice"),t=document.getElementById("id_email"),n=e.closest(".col-md"),r=t.closest(".col-md"),n.classList.add("d-none"),r.classList.add("d-none"),e.setAttribute("value","0"),t.setAttribute("value",""))},this.disableFormBtn=function(){a.form&&(a.orderBtn=a.form.querySelector("#order-btn"),a.orderBtn.setAttribute("disabled",""),a.form.checkValidity()?a.orderBtn.removeAttribute("disabled"):a.orderBtn.setAttribute("disabled",""))},this.handleSubmit=function(e){e.preventDefault(),a.form.checkValidity()&&(a.getFormData(),a.postData())},this.getFormData=function(){var t=d(a.formFields);try{for(t.s();!(e=t.n()).done;){var e=e.value,e=a.getFieldValue(e);a.data=c(c({},a.data),e)}}catch(e){t.e(e)}finally{t.f()}},this.getFieldValue=function(e){var t=document.getElementById(e.id).value,n=e.id.replace("id_",""),r="";return t&&(r=e.type(t)),u({},n,r)},this.postData=function(){var e=a.form.getAttribute("action"),t=a.getConfig(),n=document.getElementById("order-modal-footer"),r=document.getElementById("order-modal-body");a.modalForm=document.getElementById("modal-form"),n.classList.add("d-none"),a.modalTitle.classList.add("non-visible");r.insertAdjacentHTML("afterbegin",'\n      <div class="text-center text-secondary-1" id="spinner">\n        <div class="spinner-border" style="width: 5rem; height: 5rem;" role="status">\n          <span class="sr-only">Loading...</span>\n        </div>\n      </div>\n    '),a.modalForm.classList.add("d-none"),l.a.post(e,a.data,t).then(function(e){a.removeSpinner();var t=e.data.order_id;a.putResultView(r,t,e.data.result),a.orderBtn.classList.add("d-none"),a.cancelBtn.innerText=e.data.result.message,n.classList.remove("d-none")}).catch(function(e){a.removeSpinner(),a.modalTitle.classList.remove("non-visible"),a.modalForm.classList.remove("d-none"),n.classList.remove("d-none"),a.putErrors(e.response.data)})},this.getConfig=function(){return{headers:{"X-CSRFToken":document.querySelector("[name=csrfmiddlewaretoken]").value}}},this.removeSpinner=function(){var e=document.getElementById("spinner");e&&e.remove()},this.putErrors=function(e){for(var t in e){var n=e[t],r=n[n.length-1],i="id_"+t,n=document.getElementById(i);n&&(n.classList.remove("is-valid"),n.classList.add("is-invalid"),n=n.closest("div"),r=a.createFeedback(i,r),n.insertAdjacentElement("beforeend",r))}},this.createFeedback=function(e,t){var n=document.createElement("div");n.id=e+"_feedback";e=document.getElementById(n.id);return e&&e.remove(),a.errorMessageIds.push(n.id),n.classList.add("invalid-feedback"),n.innerText=t,n},this.removeErrors=function(){var t=d(a.errorMessageIds);try{for(t.s();!(n=t.n()).done;){var e=n.value,n=document.getElementById(e);n&&n.remove();e=e.replace("_feedback","");document.getElementById(e).classList.remove("is-invalid")}}catch(e){t.e(e)}finally{t.f()}},this.putResultView=function(e,t,n){a.removeResultView();t='\n          <div id="order-success">\n            <p class="h2 text-center">'.concat(n.head,'</p>\n            <p class="h5 font-weight-normal text-center">').concat(n.sub,'</p>\n            <hr>\n            <p class="h4 font-weight-normal text-center">\n              ').concat(n.order_id_part," - ").concat(t,"\n            </p>\n          </div>\n        ");e.insertAdjacentHTML("afterbegin",t)},this.removeResultView=function(){var e=document.getElementById("order-success");e&&e.remove()},this.initForm()};function f(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}new t(".tire-order",[{id:"id_quantity",type:Number},{id:"id_payment_type",type:Number},{id:"id_phone",type:String},{id:"id_name",type:String},{id:"id_email",type:String},{id:"id_tire",type:Number},{id:"id_taksit_choice",type:String}]),new t(".oil-order",[{id:"id_note",type:String},{id:"id_payment_type",type:Number},{id:"id_phone",type:String},{id:"id_name",type:String},{id:"id_oil",type:Number}]),new(function(){function n(e){var t=this;!function(e){if(!(e instanceof n))throw new TypeError("Cannot call a class as a function")}(this),this.loaded=!1,this.isFullscreen=!1,this.loadingSpinner='\n      <div class="text-center text-light video-spinner" id="video-spinner">\n        <div class="spinner-border" style="width: 5rem; height: 5rem;" role="status">\n          <span class="sr-only">Loading...</span>\n        </div>\n      </div>\n    ',this.setPlayPause=function(){t.video.paused?t.setPlay():t.setPause()},this.setPlay=function(){var e=t.video.play();null!=e&&e.then(function(){t.playPauseBtn.innerHTML='<i class="bi bi-pause-fill d-flex align-items-center h-100"></i>'})},this.setPause=function(){t.video.pause(),t.playPauseBtn.innerHTML='<i class="bi bi-play-fill d-flex align-items-center h-100"></i>'},this.configRange=function(){var e;t.range=t.videoContainer.querySelector(".video-progress"),t.range&&(e=t.range.value,t.setInputBackground(e),t.range.addEventListener("input",t.rangeHandler))},this.rangeHandler=function(e){e=e.target.value;t.setInputBackground(e);e=+e/100*t.duration;isFinite(e)&&(t.video.load(),t.video.currentTime=e)},this.setInputBackground=function(e){t.range.style.background="linear-gradient(to right, #fb0 0% ".concat(e,"%, #fff ").concat(e,"% 100%)")},this.configureBlobUrl=function(){var e=t.source.getAttribute("src");t.videoContainer.insertAdjacentHTML("afterbegin",t.loadingSpinner),l.a.get(e,{responseType:"blob"}).then(function(e){return t.setObjectUrl(e.data)}).catch(function(e){console.log(e)})},this.setObjectUrl=function(e){e=URL.createObjectURL(e);t.source.setAttribute("src",e)},this.configFullscreen=function(){t.fullscreenBtn=t.videoContainer.querySelector(".fullscreen-btn"),t.fullscreenBtn&&t.fullscreenBtn.addEventListener("click",t.setFullscreen),document.addEventListener("fullscreenchange",function(e){document.fullscreenElement?(t.isFullscreen=!0,t.fullscreenBtn.innerHTML="<i class='bi bi-fullscreen-exit'></i>"):(t.isFullscreen=!1,t.fullscreenBtn.innerHTML="<i class='bi bi-fullscreen'></i>")})},this.setFullscreen=function(){t.isFullscreen?document.exitFullscreen():t.videoContainer.requestFullscreen()},this.videoContainer=document.querySelector(".".concat(e)),this.videoContainer&&(this.video=this.videoContainer.querySelector("video"),this.videoToolContainer=this.videoContainer.querySelector(".video-tool-container"),this.video&&(this.source=this.video.querySelector("source"),this.configureBlobUrl(),this.configFullscreen(),this.configVideo(),this.configPlayPause()))}var e,t,r;return e=n,(t=[{key:"configPlayPause",value:function(){var t=this;this.playPauseBtn=this.videoContainer.querySelector(".video-play-pause"),this.playPauseBtn&&this.playPauseBtn.addEventListener("click",function(){t.setPlayPause()}),document.addEventListener("keyup",function(e){switch(e.preventDefault(),e.code){case"Space":return void t.setPlayPause();case"KeyF":return void t.setFullscreen();default:return}})}},{key:"configVideo",value:function(){var n=this;this.video&&(this.video.addEventListener("timeupdate",function(e){e.preventDefault();var t=n.video,e=t.duration,e=t.currentTime/(n.duration=e)*100;e<=100&&(n.range.value=String(e),n.setInputBackground(e))}),this.video.addEventListener("loadedmetadata",function(e){e.preventDefault(),n.setPlayPause(),n.configRange();e=document.getElementById("video-spinner");e&&e.remove(),n.videoToolContainer&&(n.videoToolContainer.classList.remove("d-none"),n.videoToolContainer.classList.add("d-flex")),n.loaded||(window.matchMedia("(min-width: 768px)").matches&&n.video.addEventListener("click",function(){n.setPlayPause()}),n.loaded=!0)}),this.video.addEventListener("ended",function(){n.video.currentTime=0,n.video.play()}))}}])&&f(e.prototype,t),r&&f(e,r),n}())("video-player");n(36);function v(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}var h,y=document.querySelector(".needs-validation"),n=document.querySelectorAll(".order-btn"),b=document.getElementById("id_tire"),p=document.getElementById("id_oil"),g=document.getElementById("id_taksit_choice"),E=[];g&&(h=g.querySelectorAll("option"),E=function(e){if(Array.isArray(e))return v(e)}(h)||function(e){if("undefined"!=typeof Symbol&&Symbol.iterator in Object(e))return Array.from(e)}(h)||function(e,t){if(!e)return;if("string"==typeof e)return v(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);"Object"===n&&e.constructor&&(n=e.constructor.name);if("Map"===n||"Set"===n)return Array.from(e);if("Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return v(e,t)}(h)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}());var S=document.getElementById("id_quantity");n.forEach(function(e){e.addEventListener("click",function(e){var t=e.target.closest(".order-btn"),e=t.getAttribute("data-id"),n=t.getAttribute("data-taksit-list").split(",");g.innerHTML="",E.forEach(function(e){!n.includes(e.value)&&"0"!==e.value||g.insertAdjacentElement("beforeend",e)}),b?(t=t.getAttribute("data-max"),b.setAttribute("value",e),S.setAttribute("max",t)):p&&p.setAttribute("value",e)})}),y&&y.addEventListener("submit",function(e){!1===y.checkValidity()&&(e.preventDefault(),e.stopPropagation(),y.classList.add("was-validated"))});var A=document.getElementById("lang-dropdown"),w=document.getElementById("nav-burger"),B=document.getElementById("nav-list");window.addEventListener("scroll",function(){43<=window.scrollY?(A.classList.add("d-none"),w.classList.remove("toggler-extra"),B.classList.remove("nav-extra")):(A.classList.remove("d-none"),w.classList.add("toggler-extra"),B.classList.add("nav-extra"))})}});