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
                NumMatricula = +teclado("Infrome o Nº de Matricula: ")
                if (NumMatricula > 0){
                    break;
                } else{
                    console.log("Nº de Matricula Invalido, por favor insira novamente")
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
                if (telefone == 9){
                    break;
                } else{
                    console.log("Nº de telefone inválido, por favor insira novamente")
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
}

export  { Membro }