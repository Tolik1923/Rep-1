using System;

namespace Лаб_3
{
    class Program
    {
        static void Main(string[] args)
        {
           Lab_3 l = new Lab_3();
            l.read_1();
            l.read_2();
            l.call();
            l.maximum();
            l.search();
            l.sum_of_elements();
            l.sorting();
        }
    }

    class Lab_3
    {
        private int i;
        private double max;
        public int d_1, d_2, n;
        public double[] m;

        public void read_1()
        {
             Console.Write("size ");
             n = Convert.ToInt32(Console.ReadLine());
             Console.WriteLine();
            m = new double[n];
        }

        public void read_2()
        {
            Console.WriteLine("enter an array");

            for (i = 0; i < n; i++)
                m[i] = Convert.ToDouble(Console.ReadLine());
        }

        public void maximum()
        {
            max = 0;

            for(i = 0; i < n; i++)
            {
                if (Math.Abs(max) < Math.Abs(m[i]))
                    max = m[i];
            }

            Console.WriteLine();
            Console.WriteLine("the maximum modulo element = " + (max));
        }

        public void search()
        {
            for (d_1 = 0; d_1 < n; d_1++)
            {
                if (m[d_1] > 0) break;
            }
            
            for (d_2 = (d_1 + 1); d_2 < n; d_2++)
            {
                if (m[d_2] > 0) break;
            }
        }

        public void sum_of_elements()
        {
            double sum = 0;

            for (i = (d_1 + 1); i < d_2; i++)
                sum += m[i];

            Console.WriteLine();
            Console.Write("the sum of the elements between the positive elements = " + (sum));
            Console.WriteLine();
        }

        public void sorting()
        {
            double[] new_m = new double[n];
            int k = 0;  

            for (i = 0; i < n; i++)
            {
                if (m[i] != 0)
                {
                    new_m[k] = m[i];
                    k++;
                }
            }

            Console.WriteLine();
            Console.Write("New array");
            for (i = 0; i < n; i++)
                Console.Write("\t" + new_m[i]);

            Console.WriteLine();

        }

        public void call()
        {
            Console.WriteLine();
            Console.Write("refer to the array element ");
            i = Convert.ToInt32(Console.ReadLine());
 
            try
            {
                Console.Write(m[i]);
            }
            catch
            {
                Console.Write("Maximum index " + (n-1));
                Console.Write(" Тhe index entered is larger");
            }

            Console.WriteLine();
        }
    }
}
