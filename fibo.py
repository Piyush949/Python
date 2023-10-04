def generate_fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

# Example usage
n_terms = 10
fibonacci_sequence = generate_fibonacci(n_terms)
print(f"Fibonacci Sequence (first {n_terms} terms): {fibonacci_sequence}")
