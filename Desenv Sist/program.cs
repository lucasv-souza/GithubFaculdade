public class dois_parametros
{
    public static void Main(string[] args)
    {
        // 1. Pega a quantidade de parâmetros e calcula o dobro
        int quantidade = args.Length;
        System.Console.WriteLine(quantidade * 2);

        // 2. Repete cada parâmetro recebido duas vezes
        foreach (string item in args)
        {
            System.Console.WriteLine(item);
            System.Console.WriteLine(item);
        }
    }
}