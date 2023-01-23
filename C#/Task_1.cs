using System;

namespace Task_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Task_1 t = new Task_1();
            t.read();
            t.calculator();
        }
    }

    class Task_1
    {
        private double a, b, h, x, res;

        public void read()
        {
            Console.WriteLine("enter a value");
            Console.WriteLine("interval");
            a = Convert.ToDouble(Console.ReadLine());
            b = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("step");
            h = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("\n");
        }

        public void calculator()
        {
            for (x = a; x < 4.51; x = x + h)
            {
                res = 1 / Math.Cos(x * Math.Cos(x));
                Console.WriteLine("X= " + (x));
                Console.WriteLine("Result = " + (res));
                Console.WriteLine("\n");
            }

            for (x = 4.5; x < 6.1; x = x + h)
            {
                res = Math.Pow(x, 3.0) + 4;
                Console.WriteLine("X= " + (x));
                Console.WriteLine("Result = " + (res));
                Console.WriteLine("\n");
            }

            for (x = 6; x < (b+0.1); x = x + h)
            {
                res = Math.Log10(Math.Exp(x));
                Console.WriteLine("X= " + (x));
                Console.WriteLine("Result = " + (res));
                Console.WriteLine("\n");
            }
        }
    }
}
