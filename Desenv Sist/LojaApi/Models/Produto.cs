namespace LojaApi.Models
{
    // ABSTRAÇÃO: Classe base que não pode ser instanciada
    public abstract class Produto
    {
        public string Nome { get; set; } = string.Empty;
        public decimal PrecoBase { get; set; }

        // POLIMORFISMO: Método que será calculado de formas diferentes
        public abstract decimal CalcularPrecoFinal();
    }

    // HERANÇA: ProdutoFisico herda de Produto
    public class ProdutoFisico : Produto
    {
        public decimal Frete { get; set; } = 20.00m;
        
        public override decimal CalcularPrecoFinal()
        {
            return PrecoBase + Frete; // Preço com frete
        }
    }

    // HERANÇA: ProdutoDigital herda de Produto
    public class ProdutoDigital : Produto
    {
        public override decimal CalcularPrecoFinal()
        {
            return PrecoBase * 0.90m; // 10% de desconto (sem frete)
        }
    }
}