class Crossword:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.words = []

    def add_word(self, word, row, col, direction):
        if direction == 'horizontal':
            if col + len(word) > self.size:
                return False
            for i in range(len(word)):
                if self.board[row][col + i] != ' ' and self.board[row][col + i] != word[i]:
                    return False
            for i in range(len(word)):
                self.board[row][col + i] = word[i]
        elif direction == 'vertical':
            if row + len(word) > self.size:
                return False
            for i in range(len(word)):
                if self.board[row + i][col] != ' ' and self.board[row + i][col] != word[i]:
                    return False
            for i in range(len(word)):
                self.board[row + i][col] = word[i]
        else:
            return False
        self.words.append(word)
        return True

    def is_valid_word(self, word):
        return word in self.words

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
    def display_words(self):
        print(self.words)