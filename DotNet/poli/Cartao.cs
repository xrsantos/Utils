using System;

namespace poli
{
    public class Cartao: Sales
    {
        public override void Execute()
        {
            Console.WriteLine("Pagamento com cartão");
        }
    }
}