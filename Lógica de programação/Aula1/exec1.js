const prompt = require ('prompt-sync')()

const fruta = prompt("Digite o nome da fruta: ")
const quant = prompt("Quantidade de frutas colhidas: ")

console.log(`Foram colhidas ${quant} unidades de ${fruta}.`)