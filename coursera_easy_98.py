# Given a 2D board of characters and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# For example, given the following board:

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, 
# exists(board, "ABCB") returns false.
def next_move(i, j, board):
	if j + 1 < len(board[0]):
		j += 1
	else:
		i += 1
		j = 0
	return i, j


def is_in_board(i, j, board):
	return 0 <= i < len(board) and 0 <= j < len(board[0])

def check_next_letter(i, j, board, letter, letters_map):

	moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

	for move in moves:
		new_i = i + move[0]
		new_j = j + move[1]

		if (is_in_board(new_i, new_j, board) 
			and (new_i, new_j) not in letters_map
			and board[new_i][new_j] == letter):
			return True, new_i, new_j
	return False, i, j


def exists(board, word):
	# does_exists

	i, j, k = 0, 0, 0

	letters_map = []

	while i < len(board) and j < len(board[0]):

		if board[i][j] != word[k]:
			i, j = next_move(i, j, board)

		elif k < len(word) - 1:
			point = (i, j)
			letters_map.append(point)
			next_letter, i_t, j_t = check_next_letter(i, j, board, word[k + 1], letters_map)

			if next_letter:
				i, j = i_t, j_t
				k += 1
			else:
				i, j = next_move(i, j, board)
		elif k == len(word) - 1:
			return True
	return False			




board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(exists(board, "ABCCED"))
print(exists(board, "SEE"))
print(exists(board, "ABCB"))



