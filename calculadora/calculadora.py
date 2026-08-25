class calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def somar(self):
        self.resultado = self.numero1 + self.numero2

    def subtrair(self):
        self.resultado = self.numero1 - self.numero2

    def multiplicar(self):
        self.resultado = self.numero1 * self.numero2

    def dividir(self):
        if self.numero2 != 0:
            self.resultado = self.numero1 / self.numero2
        else:
            raise ValueError("O denominador não pode ser zero.")


resultado1 = calculadora(10, 5)
resultado1.somar()
print(f"Resultado da soma: {resultado1.resultado}")
resultado2 = calculadora(9, 3)
resultado2.subtrair()
print(f"Resultado da subtração: {resultado2.resultado}")
resultado3 = calculadora(8, 2)
resultado3.multiplicar()
print(f"Resultado da multiplicação: {resultado3.resultado}")
resultado4 = calculadora(12, 4)
resultado4.dividir()
print(f"Resultado da divisão: {resultado4.resultado}")

