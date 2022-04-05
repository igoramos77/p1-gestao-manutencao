class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points

        def increase_points(self):
            self.points += 1

        def decrease_points(self):
            self.points -= 1



class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def score(self, player):
        result = ""
        if (self.player1.points == self.player2.poits and self.player1TotalPoints < 3):
            if (self.player1TotalPoints == 0):
                result = "Love"
            if (self.player1TotalPoints == 1):
                result = "Fifteen"
            if (self.player1TotalPoints == 2):
                result = "Thirty"
            result += "-All"
        if (self.player1TotalPoints == self.player2TotalPoints and self.player1TotalPoints > 2):
            result = "Deuce"

        P1res = ""
        P2res = ""
        if (self.player1TotalPoints > 0 and self.player2TotalPoints == 0):
            if (self.player1TotalPoints == 1):
                P1res = "Fifteen"
            if (self.player1TotalPoints == 2):
                P1res = "Thirty"
            if (self.player1TotalPoints == 3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.player2TotalPoints > 0 and self.player1TotalPoints == 0):
            if (self.player2TotalPoints == 1):
                P2res = "Fifteen"
            if (self.player2TotalPoints == 2):
                P2res = "Thirty"
            if (self.player2TotalPoints == 3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if (self.player1TotalPoints > self.player2TotalPoints and self.player1TotalPoints < 4):
            if (self.player1TotalPoints == 2):
                P1res = "Thirty"
            if (self.player1TotalPoints == 3):
                P1res = "Forty"
            if (self.player2TotalPoints == 1):
                P2res = "Fifteen"
            if (self.player2TotalPoints == 2):
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if (self.player2TotalPoints > self.player1TotalPoints and self.player2TotalPoints < 4):
            if (self.player2TotalPoints == 2):
                P2res = "Thirty"
            if (self.player2TotalPoints == 3):
                P2res = "Forty"
            if (self.player1TotalPoints == 1):
                P1res = "Fifteen"
            if (self.player1TotalPoints == 2):
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if (self.player1TotalPoints > self.player2TotalPoints and self.player2TotalPoints >= 3):
            result = "Advantage " + self.player1Name

        if (self.player2TotalPoints > self.player1TotalPoints and self.player1TotalPoints >= 3):
            result = "Advantage " + self.player2Name

        if (self.player1TotalPoints >= 4 and self.player2TotalPoints >= 0 and (
                self.player1TotalPoints - self.player2TotalPoints) >= 2):
            result = "Win for " + self.player1Name
        if (self.player2TotalPoints >= 4 and self.player1TotalPoints >= 0 and (
                self.player2TotalPoints - self.player1TotalPoints) >= 2):
            result = "Win for " + self.player2Name
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.player1TotalPoints += 1

    def P2Score(self):
        self.player2TotalPoints += 1


p1 = Player("Igor", 0)
p2 = Player("Tassio", 0)

game1 = Game(p1, p2)

game1.score()
