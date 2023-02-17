using System;

namespace Abstract 
{
    public class NfeFactory: INfeCreate
    {
        public INfe CreateNfe(int versao)
        {
            switch (versao)
            {
                case 3:
                    return new NfeVersao3();
                case 4:
                    return new NfeVersao4();
                default:
                    return null;
            }
        }
    }
}
