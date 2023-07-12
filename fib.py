MAX_RECURSION: int = 10


def fib(n: int) -> int:
    if n > MAX_RECURSION:
        raise ValueError(f"Error: MAX_RECURSION limit of {MAX_RECURSION} exceeded.")
    if n < 0:
        raise ValueError(f"Lowest possible input value is zero; {n} input.")
    return n if n <= 1 else (fib(n - 1) + fib(n - 2))
