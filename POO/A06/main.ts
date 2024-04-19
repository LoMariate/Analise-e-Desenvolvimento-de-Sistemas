import { Sistema } from "./classes/sistema"
import prompt from "prompt-sync"

const teclado = prompt()

while (true) {
    console.log("+---------------------------------------------------+")
    console.log("| 1. Cadastrar Quadra                               |")
    console.log("| 2. Reservar Quadra                                |")
    console.log("| 3. Listar Quadras Disponíveis                     |")
    console.log("| 4. Listar Reservas                                |")
    console.log("| 5. Cancelar Reserva                               |")
    console.log("| 0. Sair                                           |")
    console.log("+---------------------------------------------------+")

    let escolha: number = +teclado("Informe sua escolha: ")
    let quadrasDisponiveis: any[];

    switch (escolha) {
        case 1:
            let nome: string = teclado("Informe o nome da quadra: ")
            let esporte: string = teclado("Informe o esporte da quadra: ")
            Sistema.cadastrarQuadra(nome, esporte)
            break;
        case 2:
            if (Sistema.listarQuadrasDisponiveis().length === 0){
                console.log("Não há quadras disponíveis")
                break;
            }

            let cliente: string = teclado("Informe o nome do cliente: ")
            quadrasDisponiveis = Sistema.listarQuadrasDisponiveis()

            console.log("Quadras disponíveis:")
            quadrasDisponiveis.forEach((quadra, index) => {console.log(`${index + 1}. ${quadra.nome} (${quadra.esporte})`)})

            let quadraEscolhida: number = +teclado("Escolha a quadra: ") - 1
            Sistema.reservarQuadra(cliente, quadrasDisponiveis[quadraEscolhida], new Date())
            break;
        case 3:
            if (Sistema.listarQuadrasDisponiveis().length === 0){
                console.log("Não há quadras disponíveis")
                break;
            }

            quadrasDisponiveis = Sistema.listarQuadrasDisponiveis()
            console.log("Quadras disponíveis:")
            quadrasDisponiveis.forEach((quadra) => {
                console.log(`- ${quadra.nome} (${quadra.esporte})`)
            })
            break;
        case 4:
            let reservas = Sistema.listarReservas()

            if (reservas.length === 0){
                console.log("Não há reservas feitas")
                break;
            }

            console.log("Reservas feitas:")
            reservas.forEach((reserva) => {
                console.log(`- ${reserva.cliente} reservou a quadra ${reserva.quadra.nome} (${reserva.quadra.esporte}) em ${reserva.data}`)
            })
            break;
        case 5:
            let reservasFeitas = Sistema.listarReservas()
            console.log("Reservas feitas:")
            reservasFeitas.forEach((reserva, index) => {
                console.log(`${index}. ${reserva.cliente} reservou a quadra ${reserva.quadra.nome} (${reserva.quadra.esporte}) em ${reserva.data}`)
            })
            let reservaCancelada: number = +teclado("Escolha a reserva a ser cancelada: ")
            let reservaSelecionada = reservasFeitas[reservaCancelada]
            if (reservaSelecionada) {
                Sistema.cancelarReserva(reservaSelecionada)
                reservasFeitas.splice(reservaCancelada, 1)
            } else {
                console.log("Reserva inválida")
            }
            break;
        case 0:
            process.exit();
    }
}