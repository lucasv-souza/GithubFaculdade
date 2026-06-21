using System.Text.RegularExpressions;
using CadastroValidaCpfApi.Models;

namespace CadastroValidaCpfApi.Services
{
    public class PessoaService
    {
        // CONTEMPLANDO O DRY: Um único método centralizado para validar o CPF.
        // Evita copiar e colar este bloco matemático no "Cadastrar" e no "Atualizar".
        private bool ValidarCpf(string cpf)
        {
            if (string.IsNullOrWhiteSpace(cpf)) return false;

            // CONTEMPLANDO O KISS: Limpeza simples da string com Regex nativo.
            // (Evita loops complexos caracter por caracter ou conversões manuais de ASCII)
            string cpfLimpo = Regex.Replace(cpf, @"[^\d]", "");

            if (cpfLimpo.Length != 11) return false;

            // Impede CPFs com todos os números iguais (ex: 111.111.111-11)
            if (new string(cpfLimpo[0], 11) == cpfLimpo) return false;

            return true; // Simulação direta e legível (KISS)
        }

        public void CadastrarPessoa(Pessoa pessoa)
        {
            // Reutilizando a função (DRY) de forma simples (KISS)
            if (!ValidarCpf(pessoa.Cpf))
            {
                throw new ArgumentException("O CPF informado é inválido.");
            }

            Console.WriteLine($"[Banco LocalDB] Pessoa {pessoa.Nome} salva com sucesso!");
        }

        public void AtualizarPessoa(Pessoa pessoa)
        {
            // Reutilizando o mesmo método sem duplicar linhas de código (DRY)
            if (!ValidarCpf(pessoa.Cpf))
            {
                throw new ArgumentException("O CPF informado é inválido.");
            }
        }
    }
}