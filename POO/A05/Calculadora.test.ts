import { Calculadora } from "./Calculadora";

describe("Somar", () => {
    it("Deve ser possível somar dois números", () => {
        const calc: Calculadora = new Calculadora();
        const resultado:number = calc.somar(10, 20);
        expect(resultado).toBe(30);
    });
})



