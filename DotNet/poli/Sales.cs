using System;

namespace poli
{
    public abstract class Sales
    {
        public string Descriptions { get; set; }
        public string Customer { get; set; }
        public double Amount { get; set; }
        public TypeSales Type { get; set; }
        public override string ToString()
        {
            return $"{Descriptions} - {Customer} - {Amount} - {Type}";
        }

        public abstract void Execute();
    }
}