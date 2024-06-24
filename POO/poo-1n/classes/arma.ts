export class Arma {
    dano: number = 0;
    durabilidade: number = 0;
    raridade: string;
    armaDefesa: number = 0;

    constructor(){
        this.dano = Math.floor(Math.random() * 40) + 10;
        this.armaDefesa = Math.floor(Math.random() * 10) + 1;
        this.durabilidade = Math.floor(Math.random() * 90) + 10
        this.raridade = gerarRaridade()
    }
}

function gerarRaridade() {
    let numAleatorio = Math.random() * 1;

    if (numAleatorio < 0.6) {
        return "Comum";
    } else if (numAleatorio < 0.8){
        return "Incomum";
    } else if (numAleatorio < 0.95){
        return "Raro";
    } else {
        return "Épico";
    }

}