using System;

namespace ConsoleAppCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Bem-vindo a Calculadora!");

            Console.Write("Digite o primeiro numero: ");
            string? input1 = Console.ReadLine();
            double num1 = 0;
            if (!double.TryParse(input1, out num1))
            {
                Console.WriteLine("Numero invalido.");
                return;
            }

            Console.Write("Digite o segundo numero: ");
            string? input2 = Console.ReadLine();
            double num2 = 0;
            if (!double.TryParse(input2, out num2))
            {
                Console.WriteLine("Numero invalido.");
                return;
            }

            Console.Write("Digite a operacao desejada (+, -, *, /): ");
            string? operacao = Console.ReadLine();

            double resultado = 0;
            bool operacaoValida = true;

            switch (operacao)
            {
                case "+":
                    resultado = num1 + num2;
                    break;
                case "-":
                    resultado = num1 - num2;
                    break;
                case "*":
                    resultado = num1 * num2;
                    break;
                case "/":
                    if (num2 == 0)
                    {
                        Console.WriteLine("Erro: Divisao por zero nao permitida.");
                        operacaoValida = false;
                    }
                    else
                    {
                        resultado = num1 / num2;
                    }
                    break;
                default:
                    Console.WriteLine("Operacao invalida.");
                    operacaoValida = false;
                    break;
            }

            if (operacaoValida)
            {
                Console.WriteLine($"A resposta da operacao {num1} {operacao} {num2} eh igual a: {resultado}");
            }
        }
    }
}
