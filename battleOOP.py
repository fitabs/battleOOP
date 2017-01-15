class Board():

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def setBoard(self):
		self.board = [['O'] * self.y for _ in range(self.x)]
		return self.board

	def changeBoardMiss(self, row, col):
		self.board[row][col] = 'X'

	def changeBoardWin(self, row, col):
		self.board[row][col] = '*'

	def printBoard(self):
		print('  ', end = ' ')
		for i in range(self.y):
			print (string.ascii_letters[i], end = ' ')
		print()
		for i,j in enumerate(self.board):
			if i < 9:
				print('0' + str(i + 1), ' '.join(j))
			else:
				print(i + 1, ' '.join(j))

	def setShip(self):
		self.ship_col = random.randint(0, len(self.board[0]) - 1)
		self.ship_row = random.randint(0, len(self.board) - 1)
		return (self.ship_col, self.ship_row)
		
class Player(Board):

	def __init__(self, name, x, y):
		super().__init__(x, y)
		self.name = name
		self.status = False

	def getMove(self, ship_row, ship_col):

		print('\n', ship_col + 1, ship_row + 1)
		move = input('Ход игрока {} (пример ввода: а-4): '.format(self.name)).split('-')

		if len(move) < 2 or len(move[0]) > 1 or len(move[1]) > 2 or move[0] not in string.ascii_letters or not move[1].isdigit() or move[1] == 0:
			print('Неверный ввод!')
			cont()
			return False
			
		i = 1
		for letter in string.ascii_letters:
			if move[0] == letter:
				move[0] = i
				break
			i += 1

		if int(move[1]) > self.x or int(move[0]) - 1 > self.y:
			print('Вы вышли за границу поля')
			cont()
			return False
			
		else:
			if int(move[1]) - 1 == ship_row and int(move[0]) - 1 == ship_col:
				clear()
				print('Поздравляю {}. Ты победил!'.format(self.name))
				self.status = True
				return (int(move[1]) - 1, int(move[0]) - 1)
			else:
				return (int(move[1]) - 1, int(move[0]) - 1)

class Game():

	def setPlayers(self):
		try:
			num_of_players = int(input('Введите количество игроков (до 5): '))
		except ValueError:
			print('Введите число!')
			cont()
		if num_of_players < 1 or num_of_players > 5:
			print('Необходимо ввести число от 1 до 5!')
			cont()
			sys.exit()

		players = []
		for count in range(1, num_of_players + 1):
			name = input('Введите имя игрока {0} (player{0}): '.format(count))
			if name == '':
				name = 'player{}'.format(count)
			players.append(name)
		return players
	
	def startGame(self):
		clear()
		def loop():
			size = input('Введите размер доски (пример: 10х10): ').split('x')
			if len(size) != 2 or not size[0].isdigit() or not size[1].isdigit() or int(size[0]) > 26 or int(size[1]) > 26 or int(size[0]) <= 0 or int(size[1]) <= 0:
				print('Неверный ввод!')
				loop()

			else:
				players = self.setPlayers()
				board = Board(int(size[0]), int(size[1]))
				board.setBoard()
				ship_col, ship_row = board.setShip()
				done = False
				while not done:
					for name in players:
						def main():
							clear()
							board.printBoard()
							player = Player(name, int(size[0]), int(size[1]))
							try:
								row, col = player.getMove(ship_row, ship_col)
							except TypeError:
								main()

							if player.status == True:
								board.changeBoardWin(row, col)
								board.printBoard()
								print('\n...Конец игры...')
								cont()
								done = True
								sys.exit()
							else:
								clear()
								board.changeBoardMiss(row, col)
								board.printBoard()
								print('\nПромах!')
								cont()
						main()
		loop()

if __name__ == '__main__':
	import sys, os, random, string
	def cont(): return input('\n.....Введите символ чтобы продолжить.....')
	def clear(): 
		if sys.platform.startswith('win'):
			return os.system('cls')
		else:
			return os.system('clear')

	game = Game()
	game.startGame()



