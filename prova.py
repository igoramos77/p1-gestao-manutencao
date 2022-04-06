LOVE = 0
FIFTEEN = 1
THIRTY = 2
FORTY = 3
WIN = 4

class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points

        def increase_points(self):
            self.points += 1

        def decrease_points(self):
            self.points -= 1
        
        def get_player_points(self):
            self.points

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def score(self):
        result = ""
        
        if (self.player1.points == self.player2.poits and self.player1.points < 3):
            if (self.player1.points == LOVE):  # 0
                result = "Love"
                
            if (self.player1.points == FIFTEEN): # 1
                result = "Fifteen"
                
            if (self.player1.points == THIRTY): # 2
                result = "Thirty"
                
            result += "-All"
            
        if (self.player1.points == self.player2.points and self.player1.points > 2):
            result = "Deuce"

        P1res = ""
        P2res = ""
        
        if (self.player1.points > LOVE and self.player2.points == LOVE):
            if (self.player1.points == FIFTEEN):
                P1res = "Fifteen"
                
            if (self.player1.points == THIRTY):
                P1res = "Thirty"
                
            if (self.player1.points == FORTY):
                P1res = "Forty"

            P2res = "Love"
            
            result = P1res + "-" + P2res
            
        if (self.player2.points > LOVE and self.player1.points == LOVE):
            if (self.player2.points == FIFTEEN):
                P2res = "Fifteen"
            if (self.player2.points == THIRTY):
                P2res = "Thirty"
            if (self.player2.points == FORTY):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if (self.player1.points > self.player2.points and self.player1.points < 4):
            if (self.player1.points == THIRTY):
                P1res = "Thirty"
                
            if (self.player1.points == FORTY):
                P1res = "Forty"
                
            if (self.player2.points == FIFTEEN):
                P2res = "Fifteen"
                
            if (self.player2.points == THIRTY):
                P2res = "Thirty"
                
            result = P1res + "-" + P2res
            
        if (self.player2.points > self.player1.points and self.player2.points < WIN):
            if (self.player2.points == THIRTY):
                P2res = "Thirty"
                
            if (self.player2.points == FORTY):
                P2res = "Forty"
                
            if (self.player1.points == FIFTEEN):
                P1res = "Fifteen"
                
            if (self.player1.points == THIRTY):
                P1res = "Thirty"
                
            result = P1res + "-" + P2res

        if (self.player1.points > self.player2.points and self.player2.points >= FORTY):
            result = "Advantage " + self.player1.name

        if (self.player2.points > self.player1.points and self.player1.points >= FORTY):
            result = "Advantage " + self.player2.name

        if (self.player1.points >= WIN and self.player2.points >= LOVE and (self.player1.points - self.player2.points) >= THIRTY):
            result = "Win for " + self.player1.name
            
        if (self.player2.points >= WIN and self.player1.points >= LOVE and (self.player2.points - self.player1.points) >= THIRTY):
            result = "Win for " + self.player2.name
            
        return result

    def set_p1_score(self, number):
        for i in range(number):
            self.P1Score()

    def set_pw_score(self, number):
        for i in range(number):
            self.P2Score()

    def p1_score(self):
        self.player1.points += 1

    def p2_score(self):
        self.player2.points += 1


### Client
p1 = Player("Igor", 0)
p2 = Player("Tassio", 0)

game1 = Game(p1, p2)

game1.score()
