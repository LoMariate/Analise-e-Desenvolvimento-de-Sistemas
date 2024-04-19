"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var jogador_1 = require("./classes/jogador");
var prompt_sync_1 = require("prompt-sync");
var teclado = (0, prompt_sync_1.default)();
while (true) {
    console.log("+---------------------------------------------------+");
    console.log("| 1. Info Personagem                                |");
    console.log("| 2. Ver Monstros de bolso                          |");
    console.log("| 0. Sair                                           |");
    console.log("+---------------------------------------------------+");
    var escolha = +teclado("Informe sua escolha: ");
    switch (escolha) {
        case 1:
            var jogador = new jogador_1.Jogador(teclado("Informe o nome do jogador: "));
            console.table(jogador);
            break;
        case 2:
            console.log("Ver monstros");
            break;
        case 0:
            break;
    }
}
