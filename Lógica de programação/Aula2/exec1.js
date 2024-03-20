const prompt = require('prompt-sync')()

const name = prompt("Informe o nome do aluno: ")
const nota1 = Number(prompt("Digite a 1ª nota: "))
const nota2 = Number(prompt("Digite a 2ª nota: "))

console.log(`A média do(a) ${name} é de ${(nota1 + nota2)/2 }`)
