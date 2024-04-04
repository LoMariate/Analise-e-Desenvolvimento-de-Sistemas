// Importe de classes
import { Personagem } from "./classes/Personagem";
import { treinar } from "./classes/Personagem";

import Prompt from "prompt-sync";

const teclado = Prompt();

// Criando objetos, utilizando a classe
let personagem: Personagem = new Personagem(teclado("Informe o nome do primeiro personagem: "));


// Atribuido valores no objeto



// Apresenta o objeto

while(true) {
console.log("+---------------------------------------------------+")
console.log("| 1. Treinar                                        |")
console.log("| 2. Info Personagem                                |")
console.log("| 0. Sair                                           |")
console.log("+---------------------------------------------------+")

let escolha: number = +teclado("Informe sua escolha: ")

if (escolha == 0){
    break;
}

switch (escolha) {
    case 1:
        treinar()
        break;
    case 2:
        console.table(personagem)
        break;
    case 0:
        break;
}

}