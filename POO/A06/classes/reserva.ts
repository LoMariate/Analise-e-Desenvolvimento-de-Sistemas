import { Quadra } from "./quadra"; 

class Reserva {
    public cliente: string
    public quadra: Quadra
    public data: Date

    constructor(cliente: string, quadra: Quadra, data: Date) {
        this.cliente = cliente
        this.quadra = quadra
        this.data = data
    }
}

export { Reserva };