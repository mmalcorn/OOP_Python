def magic(n):
  # nRange is a range of numbers: takes a number, "n", and creates an array from 1 to the parameterized number.
  nRange = range(1, n)
  divisors = []

  for i in nRange:
    if n % i == 0:
      divisors.append(i)

  # Print a boolean. True if all of the even divisors add to the entered number, false otherwise.
  print(sum(divisors) == n)
  return sum(divisors) == n

#### For testing, call the function ####
magic(496)