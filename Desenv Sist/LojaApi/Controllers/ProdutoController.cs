using Microsoft.AspNetCore.Mvc;
using LojaApi.Services;

namespace LojaApi.Controllers
{
    [ApiController]
[Route("api/produto")] // Forçamos a rota a ser exatamente isso
public class ProdutoController : ControllerBase
    {
        private readonly ProdutoService _service = new ProdutoService();

        [HttpGet("{tipo}/{nome}/{preco}")]
        public IActionResult Get(string tipo, string nome, decimal preco)
        {
            var resultado = _service.ObterDetalhes(tipo, nome, preco);
            return Ok(resultado);
        }
    }
}