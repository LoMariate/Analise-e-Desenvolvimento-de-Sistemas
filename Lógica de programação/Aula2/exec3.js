const prompt = require('prompt-sync')()

const veic = Number(prompt("Informe o valor do veículo: "))

console.log(`Com a promoção a compra fica da seguinte forma\nValor de entrada: ${(veic/2).toFixed(2)}\nRestante parcelado em 12x: ${((veic/2)/12).toFixed(2)}`)