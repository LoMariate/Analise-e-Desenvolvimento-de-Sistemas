const prompt = require('prompt-sync')()

const filme = prompt("Informe o nome do filme: ")
const duracao = prompt("Informe a duração do filme em minutos: ")

console.log(`O filme ${filme} tem duração de ${duracao} min. `)