using LojaApi.Models;

namespace LojaApi.Services
{
    public class ProdutoService
    {
        public object ObterDetalhes(string tipo, string nome, decimal preco)
        {
            Produto p;

            // INSTANCIANDO OBJETOS conforme o tipo
            if (tipo.ToLower() == "digital")
                p = new ProdutoDigital { Nome = nome, PrecoBase = preco };
            else
                p = new ProdutoFisico { Nome = nome, PrecoBase = preco };

            return new
            {
                Nome = p.Nome,
                Tipo = p.GetType().Name,
                PrecoOriginal = preco,
                PrecoFinal = p.CalcularPrecoFinal() // Aqui acontece o Polimorfismo
            };
        }
    }
}