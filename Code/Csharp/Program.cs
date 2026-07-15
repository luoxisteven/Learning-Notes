// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

// Lambda Function
int x = 4;

// Lambda
int TimesTwo(int a)
{
    return a * 2;
}

int TimesTwo2(int a) => a * 2;
Console.WriteLine(TimesTwo(x));
Console.WriteLine(TimesTwo2(x));

Func<int, int> TimesTwo3 = n => n * 2;
Console.WriteLine(TimesTwo3(x));