class ticTacToe:
	def __init__(self):
		self.player = '0'
		self.players = {
		'0': 'X',
		'X': '0',
		}
		self.board = {
			1: '1',
			2: '2',
			3: '3',
			4: '4',
			5: '5',
			6: '6',
			7: '7',
			8: '8',
			9: '9',
		}

	def showBoard(self):
		print(f"""
		Player 1: 0
		Player 2: X

			{self.board[1]}|{self.board[2]}|{self.board[3]}
			-----
			{self.board[4]}|{self.board[5]}|{self.board[6]}
			-----
			{self.board[7]}|{self.board[8]}|{self.board[9]}
			""")

	def move(self):
		self.choice = input("What's your move?")
		self.board[int(self.choice)] = self.player

	def changePlayer(self):
		self.player = self.players[self.player]

	def winner(self):
		if(
			(self.board[1] == self.board[2] and self.board[1] == self.board[3]) or
			(self.board[4] == self.board[5] and self.board[4] == self.board[6]) or
			(self.board[7] == self.board[8] and self.board[7] == self.board[9]) or
			(self.board[1] == self.board[4] and self.board[1] == self.board[7]) or
			(self.board[2] == self.board[5] and self.board[2] == self.board[8]) or
			(self.board[3] == self.board[6] and self.board[3] == self.board[9]) or
			(self.board[1] == self.board[5] and self.board[1] == self.board[9]) or
			(self.board[3] == self.board[5] and self.board[3] == self.board[7])
		):
			return True
		else:
			return False

	def checkWinner(self):
		if(self.winner()):
			print(f"{self.players[self.player]} won")
			return True
		else:
			return False

	def start(self):
		self.showBoard()
		while(not self.checkWinner()):
			self.move()
			self.changePlayer()
			self.showBoard()