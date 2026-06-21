var builder = WebApplication.CreateBuilder(args);

// 1. HABILITA O USO DE CONTROLLERS (Essencial para achar seu PessoaController)
builder.Services.AddControllers();

builder.Services.AddOpenApi();
var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseHttpsRedirection();

// 2. MAPEIA AS ROTAS DOS CONTROLLERS
app.MapControllers();

app.Run();