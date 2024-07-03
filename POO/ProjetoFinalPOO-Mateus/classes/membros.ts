// 2. **Cadastro de Membros**
//      - Adicionar novo membro (com atributos como nome, número de matrícula, endereço, telefone).
//      - Listar todos os membros cadastrados.
//      - Atualizar informações de um membro.
//      - Remover um membro do cadastro.

import prompt from 'prompt-sync'
import fs from 'fs'
import path from 'path'

const teclado = prompt()

class Membro {
    private _nome: string;
    private _NumMatricula: number;
    private _endereco: string;
    private _telefone: number;

    constructor(nome: string, NumMatricula: number, endereco: string, telefone: number){
        this._nome = nome
        this._NumMatricula = NumMatricula
        this._endereco = endereco
        this._telefone = telefone
    }

    static CadastrarMembro(){
        let nome: string
            while (true){
                nome = teclado("Informe o nome do membro novo: ")               
                if (nome.length > 0){
                    break;
                }else{
                    console.log("Nome Inválido, por favor insira um novo nome")
                }
            }
        let NumMatricula: number
            while (true){
                // Matricula deve ser um número inteiro  aleatorio entre 1 e 10000 e não pode ser repetido
                NumMatricula = Math.floor(Math.random() * 10000) + 1
                if (NumMatricula > 0){
                    break;
                }
            }

        let endereco: string
            while (true){
                endereco = teclado("Informe o endereço do membro novo: ")               
                if (endereco.length > 0){
                    break;
                }else{
                    console.log("Endereço Inválido, por favor insira um novo endereço")
                }
            }
        let telefone: number
           while (true){
                telefone = +teclado("Informe um Nº de telefone (9 Digitos): ")
                if (telefone.toString().length === 9){
                    break;
                } else {
                    console.log("Telefone inválido! Deve conter 9 dígitos.")
                }
        }
        return new Membro(nome, NumMatricula, endereco, telefone)
    }

    exibirMembro() {
        console.log("Nome: ", this._nome)
        console.log("Nº de Matrícula: ", this._NumMatricula)
        console.log("Endereço: ", this._endereco)
        console.log("Telefone: ", this._telefone)
    }

    // Método para salvar os membros cadastrados
    static salvarMembrosCSV(membros: Membro) {
        const pastaData = path.join('.', 'data')
        const caminhoArquivo = path.join(pastaData, 'membros.csv')

        if (!fs.existsSync(pastaData)) {
            fs.mkdirSync(pastaData)
        }

        const dados = `${membros._nome},${membros._NumMatricula},${membros._endereco},${membros._telefone}\n`
        fs.appendFileSync(caminhoArquivo, dados, 'utf-8')
    }

    static carregarMembrosCSV(){
        const caminhoArquivo = path.join('.', 'data', 'membros.csv')
        const membros: any[] = []
        let indice = 1

        if (fs.existsSync(caminhoArquivo)){
            const data = fs.readFileSync(caminhoArquivo, 'utf-8')
            const linhas = data.split('\n')
            linhas.forEach(linha => {
                if (linha) {
                    const [NOME, NumMatricula, ENDERECO, TELEFONE] = linha.split(',')
                    membros.push({'#': indice++, NOME, NumMatricula, ENDERECO, TELEFONE });
                }
            })

            console.table(membros)
        } else {
            console.log("Ainda não existem membros cadastrados")
        }
    }
}

export  { Membro }