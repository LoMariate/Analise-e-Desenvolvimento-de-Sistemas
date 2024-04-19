import { Jogador } from "./classes/jogador"
import prompt from "prompt-sync"

const teclado = prompt()

while(true) {
    console.log("+---------------------------------------------------+")
    console.log("| 1. Info Personagem                                |")
    console.log("| 2. Ver Monstros de bolso                          |")
    console.log("| 0. Sair                                           |")
    console.log("+---------------------------------------------------+")

    let escolha: number = +teclado("Informe sua escolha: ")
    switch (escolha) { 
        case 1:
            let jogador: Jogador = new Jogador(teclado("Informe o nome do jogador: "))
            console.table(jogador)
            break;
        case 2:
            console.log("Ver monstros")
            break;
        case 0:
            process.exit(); // Encerra o programa
    }
}
