using System;

namespace poli
{
    class Program
    {
        static void Main(string[] args)
        {
            var sales = new Cartao();
            sales.Descriptions = "TV";
            sales.Customer = "João";
            sales.Amount = 100;
            sales.Type = TypeSales.Cartao;
            Console.WriteLine(sales.ToString());

            sales.Execute();

            
        }
    }
}
