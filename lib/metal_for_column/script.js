"use strict";
let items = () => {
  let NameKolumn = document.getElementById("name_products").value;
  let NameZD = document.getElementById("name_item").value;
  let HowManyZD = +document.getElementById("how_much_items").value;
  return [NameKolumn, NameZD, HowManyZD];
};

let database = [
  ["ЗД4", { ф20АIII: 19.8, "пластина 16": 342.9 }], //+
  ["ЗД5", { ф20АIII: 16.2, "пластина 16": 53.1 }], //+
  ["ЗД6", { ф20АIII: 23.7, "пластина 16": 265 }], //+
  ["ЗД7", { ф20АIII: 16.2, "пластина 16": 41 }], //+
  ["ЗД8", { ф20АIII: 16.2, "пластина 16": 31.8 }], //+
  ["ЗД11", { ф20АIII: 17.8, "пластина 16": 92.3 }], //+
  ["ЗД12", { ф20АIII: 9.7, "пластина 16": 16.1 }], //+
  ["ЗД13", { ф20АIII: 8.9, "пластина 16": 71.7 }], //+
  ["ЗД14", { ф20АIII: 7.7, "пластина 16": 12.5 }], //+
  ["ЗД15", { ф20АIII: 3, "пластина 16": 68.3 }], //+
  ["ЗД17", { ф20АIII: 23.7, "пластина 16": 97.9 }], //+
  ["ЗД18", { ф20АIII: 12.2, "пластина 16": 21.7 }], //+
  ["ЗД19", { ф20АIII: 11.9, "пластина 16": 76.1 }], //+
  ["ЗД20", { ф20АIII: 12.2, "пластина 16": 16.9 }], //+
  ["ЗД21", { ф20АIII: 15.8, "пластина 16": 146.7 }], //+
  ["ЗД25", { ф20АIII: 13.4, "пластина 16": 112.7 }], //+
  ["ЗД1", { ф6АI: 0.7, "уголок 75х5": 19.5 }], //+
  ["ЗД2", { ф6АI: 0.51, "уголок 75х5": 15 }], //+
  ["ЗД3", { ф6АI: 0.37, "уголок 75х5": 10.9 }], //+
  ["ЗД9", { ф6АI: 0.44, "уголок 75х5": 12 }], //+
  ["ЗД10", { ф6АI: 0.66, "уголок 75х5": 19.31 }], //+
  ["ЗД16", { ф6АI: 0.73, "уголок 75х5": 22.8 }], //+
  ["ЗД22", { ф6АI: 0.66, "уголок 75х5": 20.8 }], //+
  ["ЗД23", { ф6АI: 0.6, "уголок 75х5": 17.3 }], //+
  ["ЗД24", { ф6АI: 0.6, "уголок 75х5": 17.2 }], //+
  ["ЗД27", { ф6АI: 0.51, "уголок 75х5": 15.5 }], //+
  ["ЗД29", { ф6АI: 0.7, "уголок 75х5": 18.7 }], //+
  ["ЗД32", { ф6АI: 0.7, "уголок 75х5": 20.2 }], //+
  ["ЗД35", { ф6АI: 0.51, "уголок 75х5": 14.9 }], //+
  ["ЗД36", { ф6АI: 0.51, "уголок 75х5": 14.3 }], //+
  ["ЗД37", { ф6АI: 0.07, "уголок 75х5": 0.73 }], //+
  ["ЗД26", { ф20АIII: 7.9, "пластина 16": 19.6 }], //+
  ["ЗД28", { ф20АIII: 11.9, "пластина 16": 119.6 }], //+
  ["ЗД30", { ф20АIII: 11.9, "пластина 16": 130.5 }], //+
  ["ЗД31", { ф20АIII: 12.2, "пластина 16": 29 }], //+
  ["ЗД33", { ф20АIII: 23.7, "пластина 16": 239.3 }], //+
  ["ЗД34", { ф20АIII: 16.2, "пластина 16": 53.1 }], //+
  ["ЗД38", { ф20АIII: 15.8, "пластина 16": 155.5 }], //+
  ["ЗД39", { ф20АIII: 16.2, "пластина 16": 34.5 }], //+
  ["ЗД38.1", { ф20АIII: 15.8, "пластина 16": 155.5 }], //+
  ["ЗД39.1", { ф20АIII: 12.3, "пластина 16": 34.5 }], //+
  ["ЗД40.1", { ф20АIII: 1.6, "пластина 16": 2.5 }], //+
  ["ЗД40.2", { ф20АIII: 1.6, "пластина 16": 2.5 }], //+
  ["ЗД40.3", { ф20АIII: 0.8, "пластина 16": 2.5 }], //+
  ["ЗД40.4", { ф20АIII: 1.6, "пластина 16": 2.5 }], //+
  ["ЗД43", { ф20АIII: 11.9, "пластина 16": 64.2 }], //+
  ["ЗД51.1", { ф16АIII: 2.46, "пластина 16": 3.3 }], //+
  ["ЗД51.2", { ф16АIII: 1.23, "пластина 16": 3.3 }], //+
  ["ЗД51.3", { ф16АIII: 2.5, "пластина 16": 3.3 }], //+
  ["ЗД52", { ф20АIII: 23.7, "пластина 16": 184.9 }], //+
  ["ЗД53", { ф20АIII: 16.2, "пластина 16": 41 }], //+
  ["ЗД41", { ф6АI: 1.1, "уголок 75х5": 33.2 }], //+
  ["ЗД42", { ф16АIII: 0.22, "пластина 16": 7.02 }], //+
  ["ЗД44", { ф16АIII: 0.9, "пластина 16": 26.5 }], //+
  ["ЗД45", { ф16АIII: 0.4, "пластина 16": 11.5 }], //+
  ["ЗД46", { ф16АIII: 0.3, "пластина 16": 8.5 }], //+
  ["ЗД47", { ф16АIII: 0.4, "пластина 16": 10 }], //+
  ["ЗД48", { ф16АIII: 0.2, "пластина 16": 2.1 }], //+
  ["ЗД49", { ф16АIII: 0.6, "пластина 16": 16.5 }], //+
  ["ЗД50", { ф16АIII: 0.7, "пластина 16": 19 }], //+
  ["ЗД54", { ф16АIII: 0.3, "пластина 16": 8.6 }], //+
  ["ЗДТ1", { ф22АIII: 74.5, "пластина 20": 80.1 }], //1275*400
  ["ЗДТ2", { ф22АIII: 40, "пластина 20": 41.7 }], //850*300
  ["ЗДТ3", { ф22АIII: 59.6, "пластина 20": 56.5 }], //900*400
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
  let writeRes = "<p>Масса закладных:</p>";
  for (let key in fullObject) {
    writeRes +=
      "<p>" + key + " весом " + fullObject[key].toFixed(2) + " кг</p>";
  }
  result.innerHTML = writeRes;
};

window.onload = () => {
  let fullObject = {};
  let button = document.getElementById("submit");
  button.onclick = () => {
    let NameZD = findItem()[0];
    let obj = findItem()[1];
    let output = document.getElementById("createInput");
    let writeNameZD =
      "<p>" + NameZD + " в количестве " + items()[2] + "шт.</p>";
    output.innerHTML += writeNameZD;

    for (let key in obj) {
      if (key in fullObject) {
        fullObject[key] += obj[key] * items()[2];
      } else {
        fullObject[key] = obj[key] * items()[2];
      }
    }

    result(fullObject);
  };
};
