using System;

namespace Task_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Task_2 t = new Task_2();
            t.read();
            t.calculator();
        }
    }

    class Task_2
    {
        private double a, b, h, d, k, x, res, res_1;

        public void read ()
        {
            Console.WriteLine("enter a value");
            Console.WriteLine("interval");
            a = Convert.ToDouble(Console.ReadLine());
            b = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("step");
            h = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("error");
            d = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("\n");
        }

        public void calculator()
        {
            res = 0; k = 0;
            for (x = a; x < (b + 0.2*h); x = x + h)
            {
                do
                {
                    res_1 = (x / Math.Pow((2 * k + 1), 3.0)) * Math.Sin(2 * k + 1);
                    k++;
                    res += res_1;
                } while(res_1 > d);

                Console.WriteLine("X = " + (x));
                Console.WriteLine("Result = " + (res));
                Console.WriteLine("\n");

                res = 0; k = 0;
            }
        }
    }
}
