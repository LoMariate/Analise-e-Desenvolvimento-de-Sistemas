const prompt = require('prompt-sync')()

const jantar = prompt("Informe o valor do jantar: ")

console.log(`O valor total a ser pago é de ${(jantar * 1.1).toFixed(2)}`)
console.log(`A taxa do garçom é de 10%, então é ${((jantar*1.1)-jantar).toFixed(2)}`)
