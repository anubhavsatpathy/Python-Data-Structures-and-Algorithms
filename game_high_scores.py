class GameEntry:
    def __init__(self, score, name):
        """
        Constructor for a particular game entry
        :param score: The score of the game
        :param name: The name of the player who registered the score
        """
        self._score = score
        self._name = name

    def get_score(self):

        return self._score

    def get_name(self):

        return self._name

    def __str__(self):

        return "{} ------------------- {}\n".format(self._name,self._score)

class ScoreBoard:

    def __init__(self, capacity = 10):
        """
        Constructor for a scoreboard object that stores the high scores
        :param capacity: The number of high scores maintained on the scoreboard
        """
        self._capacity = capacity
        self._highScores = self._capacity * [None]
        self._n = 0

    def __getitem__(self, item):

        if self._n == 0:
            raise Exception("No High Scores Registered")
        else:
            if item < 0 or item >= self._n:
                raise IndexError("Index Out of Bounds")
            else:
                return self._highScores[item]

    def add_score(self,entry):
        """
        Checks if a GameEntry object qualifies as a high score
        :param entry: The GameEntry that needs to be checked
        :return: Void - Modifies self.-highScores
        """

        is_qualified = (self._n < self._capacity) or (entry.get_score() > self._highScores[-1].get_score())

        if is_qualified:

            if self._n < self._capacity:
                self._n += 1

            last = self._n - 1

            while last > 0 and self._highScores[last - 1].get_score() < entry.get_score():
                self._highScores[last] = self._highScores[last - 1]
                last -= 1
            self._highScores[last] = entry

    def __len__(self):
        return self._n

    def __str__(self):

        s = "\n".join(str(self._highScores[i]) for i in range(self._n))
        return s



if __name__ == '__main__':
    
    board = ScoreBoard()

    for i in range(10):
        entry = GameEntry(i * 10, "Player" + str(i))
        board.add_score(entry)

    print(board)





