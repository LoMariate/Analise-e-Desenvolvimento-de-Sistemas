import prompt from 'prompt-sync'
import { Livro } from './classes/livros'
import { Membro } from './classes/membros'



const teclado = prompt()

const interfaceBiblio = "|---------------Sistema de Biblioteca---------------|"
const interfaceLivro = "|----------------Cadastro de livros-----------------|"
const interfaceMembro = "|----------------Cadastro de membros----------------|"
const interfaceEmprestimo = "|-----------Gerenciamento de empréstimos------------|"
const interfaceFinal = "|---------------------------------------------------|"

while (true) {
    console.log(interfaceBiblio)
    console.log("| 1. Cadastro de livros                             |")
    console.log("| 2. Cadastro de membros                            |")
    console.log("| 3. Gerenciamento de empréstimos                   |")
    console.log("| 0. Sair                                           |")
    console.log(interfaceFinal)
    
    let escolha: number = +teclado("Informe sua escolha: ")
    
    switch (escolha) {
        case 1:
            while (true) {
                console.clear()
                console.log(interfaceLivro)
                console.log("| 1. Adicionar novo livro                           |")
                console.log("| 2. Listar todos os livros cadastrados             |")
                console.log("| 3. Atualizar informações de um livro              |")
                console.log("| 4. Remover um livro do cadastro                   |")
                console.log("| 0. Voltar                                         |")
                console.log(interfaceFinal)

                let escolhaLivro: number = +teclado("Informe sua escolha: ")

                switch (escolhaLivro) {
                    case 1:
                        console.log(interfaceLivro)

                        const novoLivro = Livro.cadastrarLivro()
                        Livro.salvarLivroCSV(novoLivro)
                        
                        console.log("| Livro cadastrado com sucesso!                     |")
                        novoLivro.exibirLivro()
                        console.log(interfaceFinal)
                        teclado("Pressione Enter para continuar...")
                        break;
                    case 2:
                        console.log(interfaceLivro)
                        
                        console.log("| Listagem de livros cadastrados                    |")
                        Livro.carregarLivrosCSV()
                        
                        console.log(interfaceFinal)
                        teclado("Pressione Enter para continuar...")
                        break;
                    case 3:
                        console.log("Atualizar informações de um livro")
                        break;
                    case 4:
                        console.log("Remover um livro do cadastro")
                        break;
                    case 0:
                        console.clear()
                        break;    
                }
            
                if (escolhaLivro === 0) {
                    break;
                }
            }
            
        break;    
        case 2:
            console.clear()
            console.log(interfaceMembro)
            console.log("| 1. Adicionar novo membro                          |")
            console.log("| 2. Listar todos os membros cadastrados            |")
            console.log("| 3. Atualizar informações de um membro             |")
            console.log("| 4. Remover um membro do cadastro                  |")
            console.log("| 0. Voltar                                         |")
            console.log(interfaceFinal)

            let escolhaMembro: number = +teclado("Informe sua escolha: ")

            switch (escolhaMembro) {
                case 1:
                    console.log(interfaceMembro)

                    const novoMembro = Membro.CadastrarMembro()
                    // SalvarSVCMembro

                    console.log("Membro cadastrado com sucesso!")
                    novoMembro.exibirMembro()

                    console.log(interfaceFinal)
                    teclado("Pressione Enter para continuar")
                    break;
                case 2:
                    console.log(interfaceMembro)
                        
                    console.log("| Listagem de Membros cadastrados                   |")
                    // Membro.carregarMembrosCSV()
                    
                    console.log(interfaceFinal)
                    teclado("Pressione Enter para continuar...")
                    break;
                case 3:
                    console.log("Atualizar informações de um membro")
                    break;
                case 4:
                    console.log("Remover um membro do cadastro")
                    break;
                case 0:
                    console.clear()
                    break;
            }

        break;
        case 3:
            console.clear()
            console.log(interfaceEmprestimo)
            console.log("| 1. Realizar empréstimo de um livro para um membro |")
            console.log("| 2. Listar todos os empréstimos ativos             |")
            console.log("| 3. Registrar devolução de um livro                |")
            console.log("| 4. Listar histórico de empréstimos                |")
            console.log("| 0. Voltar                                         |")
            console.log(interfaceFinal)

            let escolhaEmprestimo: number = +teclado("Informe sua escolha: ")

            switch (escolhaEmprestimo) {
                case 1:
                    console.log("Realizar empréstimo de um livro para um membro")
                    break;
                case 2:
                    console.log("Listar todos os empréstimos ativos")
                    break;
                case 3:
                    console.log("Registrar devolução de um livro")
                    break;
                case 4:
                    console.log("Listar histórico de empréstimos")
                    break;
                case 0:
                    console.clear()
                    break;
            }

            break;
        case 0:
            console.log("Saindo do sistema...")
            process.exit();
    }
}
