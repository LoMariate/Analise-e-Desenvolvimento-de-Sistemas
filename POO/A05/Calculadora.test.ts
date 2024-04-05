import { Calculadora } from "./Calculadora";

// Install type definitions for test runner
// npm i --save-dev @types/jest

let calc: Calculadora;

beforeAll(() => {
    console.log("Before All");
}

beforeEach(() => {
    calc = new Calculadora();
}



describe("Soma", () => {
    it("Deve ser possível somar dois números", () => {
        const resultado:number = calc.somar(10, 20);
        expect(resultado).toBe(30);
    });
})

describe("Divisão", () => {
    it("Deve ser possível dividir dois números", () => {
        const resultado:number = calc.dividir(10, 2);
        expect(resultado).toBe(5);
    });

    
    it("Deve ser possivel dividir por zero", () => {
        expect(() => calc.dividir(10, 0)).toThrow();
    });

    
    it("Deve apresentar mensagem de erro quando dividir por zero", () => {
        expect(() => calc.dividir(10, 0)).toThrow("Não é possível dividir por zero");
    });
})


