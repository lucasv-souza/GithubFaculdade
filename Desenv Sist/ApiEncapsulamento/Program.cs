using Microsoft.AspNetCore.Mvc;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// ==========================================
// 1. SIMULAÇÃO DE BANCO DE DADOS
// ==========================================
var myAccount = new BankAccount(100.00m);

// ==========================================
// 2. ROTAS DA API
// ==========================================
app.MapGet("/conta/saldo", () => 
{
    return Results.Ok(new { SaldoAtual = myAccount.Balance });
});

app.MapPost("/conta/depositar", ([FromBody] decimal amount) => 
{
    try
    {
        myAccount.Deposit(amount);
        return Results.Ok(new { Mensagem = "Depósito realizado!", SaldoAtual = myAccount.Balance });
    }
    catch (Exception ex)
    {
        return Results.BadRequest(new { Erro = ex.Message });
    }
});

app.MapPost("/conta/sacar", ([FromBody] decimal amount) => 
{
    try
    {
        myAccount.Withdraw(amount);
        return Results.Ok(new { Mensagem = "Saque realizado!", SaldoAtual = myAccount.Balance });
    }
    catch (Exception ex)
    {
        return Results.BadRequest(new { Erro = ex.Message });
    }
});

// Essa linha liga o servidor
app.Run();


// ==========================================
// 3. DOMÍNIO: A Classe com Encapsulamento
// (Sempre no final do arquivo no C# moderno!)
// ==========================================
public class BankAccount
{
    private decimal _balance;
    public decimal Balance => _balance;

    public BankAccount(decimal initialBalance = 0)
    {
        _balance = initialBalance;
    }

    public void Deposit(decimal amount)
    {
        if (amount <= 0)
            throw new ArgumentException("O valor do depósito deve ser maior que zero.");
        
        _balance += amount; 
    }

    public void Withdraw(decimal amount)
    {
        if (amount <= 0)
            throw new ArgumentException("O valor do saque deve ser maior que zero.");
        
        if (amount > _balance)
            throw new InvalidOperationException("Saldo insuficiente para o saque.");
        
        _balance -= amount; 
    }
}