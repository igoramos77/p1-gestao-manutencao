#LOVE = 0
#FIFTEEN = 1
#THIRTY = 2
#FORTY = 3
#WIN = 4

class Tenis():
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, playerName):
        if playerName == self.player1_name:
            self.p1_score()
        else:
            self.p2_score()

    def p1_score(self):
        self.p1_points +=1


    def p2_score(self):
        self.p2_points +=1

    def is_deuce(self):
        return self.p1_points==self.p2_points

    def deuce_score(self, points):
        if points < 3:
            return {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }[points]

        return "Deuce"

    def is_win_or_advantage(self):
        return self.p1_points >= 4 or self.p2_points >= 4

    def win_or_advantage_score(self, p1_points, p2_points):
        points_difference = p1_points - p2_points

        if (points_difference == 1):
          return "Vantagem para: " + self.player1_name
        elif (points_difference <= 1):
            return "Vantagem para: " + self.player2_name
        elif (points_difference >= 2):
            return  "Vitoria de: " + self.player1_name
        else:
            return "Vitoria de: " + self.player2_name

    def points(self, p1_points, p2_points):
        names = {
            0 : "Love",
            1 : "Fifteen",
            2 : "Thirty",
            3 : "Forty",
        }

        p1_name = names[p1_points]
        p2_name = names[p2_points]

        return p1_name + "-" + p2_name
