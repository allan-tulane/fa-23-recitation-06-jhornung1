def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    if n <= 1:
      return n
    else:
      return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    
def fib_top_down(n, fibs):
  """
  Return the nth Fibonacci number using top-down dynamic programming with memoization.
  fibs is a list to store precomputed Fibonacci values.
  """
  # Check if F_n has already been computed
  if fibs[n] != -1:
      return fibs[n]

  # Compute F_n using recursion
  if n <= 1:
      fibs[n] = n
  else:
      fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)

  return fibs[n]


def fib_bottom_up(n):
  """
  Return the nth Fibonacci number using a bottom-up iterative approach.
  """
  if n <= 1:
      return n

  # Initialize a list to store the Fibonacci sequence up to F_n
  fibs = [0] * (n + 1)
  fibs[0] = 0
  fibs[1] = 1

  # Fill in the list with Fibonacci values from F_2 to F_n
  for i in range(2, n + 1):
      fibs[i] = fibs[i - 1] + fibs[i - 2]

  # Return the last value, which is F_n
  return fibs[n]


n = 20
counts = [0] * (n+1)
fib_recursive(n, counts)
print(counts)
print(sum(counts))