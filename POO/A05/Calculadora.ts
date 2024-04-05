export class Calculadora{
    dividir(arg0: number, arg1: number): number {

        if (arg1 === 0) {
            throw new Error("Não é possível dividir por zero");
        }
        return arg0 / arg1;
    }

    somar(arg0: number, arg1: number): number {
        return arg0 + arg1;
    }
}