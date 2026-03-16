using System;

namespace ConsoleAppMaxNumber
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Bem-vindo! Vamos encontrar o maior numero.");
            
            int? maiorNumero = null;

            for (int i = 1; i <= 5; i++)
            {
                Console.Write($"Digite o {i}º número inteiro: ");
                string? input = Console.ReadLine();
                
                if (int.TryParse(input, out int numeroDaVez))
                {
                    if (maiorNumero == null || numeroDaVez > maiorNumero)
                    {
                        maiorNumero = numeroDaVez;
                    }
                }
                else
                {
                    Console.WriteLine("Entrada inválida. Por favor, digite um número inteiro.");
                    i--; // Decrementa para repetir a leitura
                }
            }

            if (maiorNumero != null)
            {
                Console.WriteLine($"\nO maior número digitado foi: {maiorNumero}");
            }
        }
    }
}
