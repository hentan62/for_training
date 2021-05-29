"use strict";
let items = () => {
  let NameKolumn = document.getElementById("name_products").value;
  let NameZD = document.getElementById("name_item").value;
  let HowManyZD = +document.getElementById("how_much_items").value;
  return [NameKolumn, NameZD, HowManyZD];
};

let database = [
  ["М1", { ф20АI: 8.4, "пластина 20": 39.3 }], //+
  ["М2", { ф12АIII: 0.4, "пластина 8": 3.3 }], //+
  ["М3", { ф12АIII: 0.2, "уголок 100х7": 1.1 }], //+
  ["М4", { ф16АIII: 3.2, "пластина 12": 7.5 }], //+
  ["М5", { ф16АIII: 1.6, "пластина 12": 3.8 }], //+
  ["М6", { ф20АIII: 9.9, "пластина 20": 25.2 }], //+
  ["М7", { ф16АIII: 4.7, "пластина 20": 25.2 }], //+
  ["М8", { ф16АIII: 4.8, "пластина 12": 11.3 }], //+
  ["М8а", { ф16АIII: 4.8, "пластина 12": 18.9 }], //+
  ["М8б", { ф16АIII: 1.6, "пластина 12": 2.8 }], //+
  ["Тр1", { "Труба 76х3": 2.7 }], //+
  ["Тр1", { "Труба 83х3": 10.1 }], //+
];

let findItem = () => {
  let NameZD = items()[1];
  let HowManyZD = items()[2];
  for (let keys of database) {
    if (keys[0] == NameZD) {
      return [keys[0], keys[1]];
    }
  }
};

let result = (fullObject) => {
  let result = document.getElementById("result");
  let writeRes = "<table><tr><td colspan='2'>Масса закладных:</td></tr>";
  writeRes += "<tr><td>Название детали</td><td>Масса детали</td></tr>";
  let arrOfKeys = [];
  for (let k in fullObject) {
    if (fullObject.hasOwnProperty(k)) arrOfKeys.push(k);
  }
  arrOfKeys.sort();
  for (let i = 0; i < arrOfKeys.length; i++) {
    let kf = arrOfKeys[i];
    writeRes +=
      "<tr><td>" + kf + "</td><td>" + fullObject[kf].toFixed(2) + "</td></tr>";
  }
  writeRes += "</table>";
  result.innerHTML = writeRes;
};

function output(NameZD, obj) {
  let output = document.getElementById("createInput");
  let writeNameZD = "<p>" + NameZD + " в количестве " + items()[2] + "шт.</p>";
  output.innerHTML += writeNameZD;
}

function multiply(obj, fullObject) {
  for (let key in obj) {
    if (key in fullObject) {
      fullObject[key] += obj[key] * items()[2];
    } else {
      fullObject[key] = obj[key] * items()[2];
    }
  }
  return fullObject;
}

window.onload = () => {
  let fullObject = {};
  let button = document.getElementById("submit");
  let NameItem = items()[0];
  let placeItem = document.getElementById("nameKol");
  placeItem.innerHTML = "<b>" + NameItem + "</b>";
  button.onclick = () => {
    let obj = findItem()[1];
    output(findItem()[0], obj);
    multiply(obj, fullObject);
    result(fullObject);
  };
};
