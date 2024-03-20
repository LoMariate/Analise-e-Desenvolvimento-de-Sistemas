import { Arma } from "./arma"

export class Personagem {
    nome: string;
    energia: number;
    ataque: number;
    defesa: number;

    constructor(nome: string){
        this.nome = nome;
        this.energia = Math.floor(Math.random() * 99) + 1;
        this.ataque = Math.floor(Math.random() * 40) + 10;
        this.defesa = Math.floor(Math.random() * 40) + 10;
    }
}


function gerarArma() {
    let arma: Arma = new Arma();
}

