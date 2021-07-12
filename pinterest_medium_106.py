# Given an integer list where each number represents 
# the number of hops you can make, 
# determine whether you can reach to the last index starting at index 0.

# For example, [2, 0, 1, 0] 
# returns True while [1, 1, 0, 1] returns False.


def can_reach(hops):

	i = 0
	while i < len(hops):

		if i == len(hops) - 1:
			return True

		if hops[i] == 0:
			return False
		i += hops[i]


print(can_reach([2, 0, 1, 0]))
print(can_reach([1, 1, 0, 1] ))




