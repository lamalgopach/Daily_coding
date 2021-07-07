# Given an even number (greater than 2), return two prime numbers 
# whose sum will be equal to the given number.

# A solution will always exist. See Goldbach’s conjecture.

# Example:

# Input: 4
# Output: 2 + 2 = 4
# If there are more than one solution possible, 
# return the lexicographically smaller solution.

# If [a, b] is one solution with a <= b, and [c, d] 
# is another solution with c <= d, then
# [a, b] < [c, d]
# If a < c OR a==c AND b < d.

def is_prime(n):

	for i in range(4, n // 2 + 1):
		if n % i == 0:
			return False
	return True

def return_primes(num):

	primes = set()

	for i in range(1, num // 2 + 1):

		if i in primes and (num - i) in primes:
			return i, num - i
		elif is_prime(i):
			primes.add(i)
			if is_prime(num - i):
				return i, num - i
		elif is_prime(num - i):
			primes.add(num - i)


print(return_primes(4))
print(return_primes(20)) # 3, 17
print(return_primes(40)) # 17, 23 || 3, 37
print(return_primes(39)) # 2, 37 
print(return_primes(42)) # 1, 41 












