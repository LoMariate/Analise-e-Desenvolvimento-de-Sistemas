const prompt = require('prompt-sync')()

const cid1 = prompt("Digite o nome da 1º cidade: ")
const cid2 = prompt("Digite o nome da 2º cidade: ")
const dist = prompt("Informe a distância entre elas: ")

console.log(`A distância entre ${cid1} e ${cid2} é de ${dist} km`)