// 1. **Cadastro de Livros**
//      - Adicionar novo livro (com atributos como título, autor, ISBN, ano de publicação).
//      - Listar todos os livros cadastrados.
//      - Atualizar informações de um livro.
//      - Remover um livro do cadastro.

// - **Manipulação de Arquivos:**
// - Salvar e carregar os dados dos livros, membros e empréstimos de/para arquivos para garantir a persistência dos dados.
// - Utilizar arquivos de texto ou CSV para armazenamento.

// Importa os módulos necessários
import prompt from 'prompt-sync' 
import fs from 'fs'
import path from 'path'

const teclado = prompt()

// Criando a classe livro
class Livro {
    private _titulo: string
    private _autor: string
    private _isbn: number
    private _anoPublicacao: number

    constructor(titulo: string, autor: string, isbn: number, anoPublicacao: number) { // Construtor da classe para inicializar os atributos
        this._titulo = titulo
        this._autor = autor
        this._isbn = isbn
        this._anoPublicacao = anoPublicacao
    }

    // Método para cadastrar um livro
    static cadastrarLivro() {
        let titulo: string;  // Armazena o título do livro, é utilizado um "WHILE" para garantir que o título tenha ao menos um caracterer
            while (true) {
                titulo = teclado("Informe o título do livro: ")
                if (titulo.length > 0) {
                    break;
                } else {
                    console.log("Título inválido! Deve conter ao menos um caractere.")
                }
            }

        let autor: string; // Armazena o autor do livro, é utilizado um "WHILE" para garantir que o autor tenha ao menos um caracterer
            while (true) {
                autor = teclado("Informe o autor do livro: ")
                if (autor.length > 0) {
                    break;
                } else {
                    console.log("Autor inválido! Deve conter ao menos um caractere.")
                }
            }

        let isbn: number; // Armazena o ISBN do livro, é utilizado um "WHILE" para garantir que o ISBN tenha 10 ou 13 dígitos
            while (true) {
                isbn = +teclado("Informe o ISBN do livro: ")
                if (isbn.toString().length === 10 || isbn.toString().length === 13) {
                    break;
                } else {
                    console.log("ISBN inválido! Deve conter 10 ou 13 dígitos.")
                }
            }

        let anoPublicacao: number; // Armazena o ano de publicação do livro, é utilizado um "WHILE" para garantir que o ano seja menor ou igual ao ano atual
        const anoAtual = new Date().getFullYear()
            while (true) {
                anoPublicacao = +teclado("Informe o ano de publicação do livro: ")
                if (anoPublicacao <= anoAtual) {
                    break;
                } else {
                    console.log("Ano de publicação inválido! Deve ser menor ou igual ao ano atual.")
                }
            }

        return new Livro(titulo, autor, isbn, anoPublicacao)  
    }

    // Método para exibir o livro na hora do cadastro
    exibirLivro() {
        console.log("Título: ", this._titulo)
        console.log("Autor: ", this._autor)
        console.log("ISBN: ", this._isbn)
        console.log("Ano de publicação: ", this._anoPublicacao)
    }

    // Método para salvar o livro no arquivo CSV
    static salvarLivroCSV(livro: Livro){
        const pastaData = path.join('.', 'data')                       // Determinando o caminho para a pasta data onde será salvo o arquivo CSV
        const caminhoArquivo = path.join(pastaData, 'livros.csv')

        if (!fs.existsSync(pastaData)){                                // Verifica se a pasta data já existe, se não existir, cria a pasta
            fs.mkdirSync(pastaData)
        }

        const dados = `${livro._titulo},${livro._autor},${livro._isbn},${livro._anoPublicacao}\n`
        fs.appendFileSync(caminhoArquivo, dados, 'utf-8')
    }

    static carregarLivrosCSV(){
        const caminhoArquivo = path.join('.', 'data', 'livros.csv')
        const livros: any[] = []
        let indice = 1

        if (fs.existsSync(caminhoArquivo)){
            const data = fs.readFileSync(caminhoArquivo, 'utf-8')
            const linhas = data.split('\n')
            linhas.forEach(linha => {
                if (linha) {
                    const [TITULO, AUTOR, ISBN, ANO_DE_PUBLICACAO] = linha.split(',')
                    livros.push({'#': indice++, TITULO, AUTOR, ISBN, ANO_DE_PUBLICACAO: parseInt(ANO_DE_PUBLICACAO) });
                }
            })

            console.table(livros)
        } else {
            console.log("Ainda não existem livros cadastrados!")
        }
    }

}

export { Livro }
