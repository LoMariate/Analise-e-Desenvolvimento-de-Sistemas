const prompt = require('prompt-sync')()

const num = Number(prompt("Informe o número: "))

console.log(`número à esquerda: ${num - 1}`)
console.log(`número à direita: ${num + 1}`)