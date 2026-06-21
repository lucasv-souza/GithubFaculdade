using Microsoft.AspNetCore.Mvc;
using CadastroValidaCpfApi.Models;
using CadastroValidaCpfApi.Services;

namespace CadastroValidaCpfApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PessoaController : ControllerBase
    {
        private readonly PessoaService _service = new PessoaService();

        [HttpPost]
        public IActionResult Cadastrar([FromBody] Pessoa pessoa)
        {
            try
            {
                _service.CadastrarPessoa(pessoa);
                return Ok(new { mensagem = "Cadastro realizado com sucesso no LocalDB!" });
            }
            catch (ArgumentException ex)
            {
                return BadRequest(new { erro = ex.Message });
            }
        }
    }
}