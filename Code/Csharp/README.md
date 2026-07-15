# Learn C#

## Features
- [Automatic Memory Management](https://learn.microsoft.com/en-us/dotnet/standard/automatic-memory-management)
- Strongly Type
- NuGet Packages Download

## Installation
``` bash
# Create the console in a new folder
dotnet new console -n abc
# Create the console in the current folder
dotnet new console

dotnet new apicontroller -n api
```

## Run
``` bash
dotnet run
dotnet run hello-world.cs
```

## Package Usage
``` c#
# with using 
using System;
Console.WriteLine("Hello, World");

# withou using
System.Console.WriteLine("Hello, World");
```

## Entry point of C# program
``` c#
using System;
﻿namespace TourOfCsharp;

class Program
{
    static void Main()
    {
        // This line prints "Hello, World" 
        Console.WriteLine("Hello, World");
    }
}
```

## Namespace

## Value Types and Reference Types

## Asynchronous Programming
async, await

## Lambda Operator =>
``` c#
x => x * 2

app.UseEndpoints(endpoints =>
{
    endpoints.MapControllers();
    endpoints.MapPersonalChatbotMcp();
});

app.UseEndpoints(
    delegate(IEndpointRouteBuilder endpoints)
    {
        endpoints.MapControllers();
        endpoints.MapPersonalChatbotMcp();
    });
```

## Delegate

## Interface & Abstract

