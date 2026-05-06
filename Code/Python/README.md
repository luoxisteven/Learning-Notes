## Dunder (Double Underscore)
``` python
def search(query: str, max_results: int = 5) -> str:
    """Search the web for information."""
    return "result"

print(search.__doc__) # Search the web for information.
print("--------------------------------")
print(search.__annotations__) # {'query': <class 'str'>, 'max_results': <class 'int'>, 'return': <class 'str'>}
print(type(search.__annotations__)) # <class 'dict'>
```

``` python
# Only run this code when this file is executed directly, not when it is imported by another file.
if __name__ == "__main__":
```