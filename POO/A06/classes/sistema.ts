import { Quadra } from './quadra';
import { Reserva } from './reserva';

class Sistema {
    private static quadras: Quadra[] = []
    private static reservas: Reserva[] = []

    public static cadastrarQuadra(nome: string, esporte: string): void {
        Sistema.quadras.push(new Quadra(nome, esporte))
    }

    public static listarQuadrasDisponiveis(): Quadra[] {
        return Sistema.quadras
    }

    public static reservarQuadra(cliente: string, quadra: Quadra, data: Date): void {
        Sistema.reservas.push(new Reserva(cliente, quadra, data));
        const index = Sistema.quadras.indexOf(quadra);
        if (index !== -1) {
            Sistema.quadras.splice(index, 1);
        }
    }

    public static listarReservas(): Reserva[] {
        return Sistema.reservas
    }

    public static cancelarReserva(reserva: Reserva): void {
        Sistema.reservas.push(reserva);
        const index = Sistema.reservas.indexOf(reserva);
        if (index !== -1) {
            Sistema.reservas.splice(index, 1);
        }
        Sistema.cadastrarQuadra(reserva.quadra.nome, reserva.quadra.esporte);
    }
}

export { Sistema };