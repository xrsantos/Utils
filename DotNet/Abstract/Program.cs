using System;

namespace Abstract
{
    class Program
    {
        static void Main(string[] args)
        {
            var nota = new NfeFactory().CreateNfe(3);
            nota.GerarNotaFiscal();

        }
    }
}
