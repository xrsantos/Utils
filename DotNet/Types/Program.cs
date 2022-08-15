using System;

namespace Types
{
    class Program
    {
        static void Main(string[] args)
        {
            //Value Types - Stack Memory  
            Boolean boolean = true;
            Int16 integer = 32767;
            Int32 integer2 = 2147483647;
            Int64 integer3 = 9223372036854775807;
            UInt16 integer4 = 65535;
            UInt32 integer5 = 4294967295;
            UInt64 integer6 = 18446744073709551615;
            Double double   = 1.7976931348623157E+308;
            Single single = 3.40282347E+38F;
            Decimal decimal1 = 79228162514264337593543950335M;
            Decimal decimal2 = decimal.MaxValue;
            Decimal decimal3 = decimal.MinValue;
            Decimal decimal4 = decimal.One;
            Decimal decimal5 = decimal.Zero;
            
            //Alias Types 
            string text = string.Empty;
            char character = ' ';
            short integer7 = 0;
            int integer8 = 0;
            long integer9 = 0;
            ushort integer10 = 0;
            uint integer11 = 0;
            ulong integer12 = 0;
            float single1 = 0;
            double double1 = 0;
            decimal decimal6 = 0;

            DateTime dateTime = DateTime.Now;
            TimeSpan timeSpan = TimeSpan.Zero;
            Guid guid = Guid.NewGuid();
            object object1 = new object();
            dynamic dynamic = new dynamic();
            var var = new var();


            Console.WriteLine(boolean);
            Console.WriteLine(integer);
            Console.WriteLine(integer2);


        }
    }
}
