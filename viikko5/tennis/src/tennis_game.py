class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0
        self.score_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
            4: "Deuce"
        }

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def get_score(self):
        if self.players_are_tied():
            return self.get_tied_score(self.player1_points)
        elif self.a_player_scored_more_than_four_points():
            return self.get_advantage_score(self.player1_points, self.player2_points)
        else:
            return self.get_regular_score(self.player1_points, self.player2_points)
    
    def players_are_tied(self):
        return self.player1_points == self.player2_points

    def get_tied_score(self, points):
        result = self.score_names[points] + "-All"
        if points > 3:
            result = "Deuce"
        return result

    def a_player_scored_more_than_four_points(self):
        return self.player1_points >= 4 or self.player2_points >= 4

    def get_advantage_score(self, points1, points2):
        point_difference = abs(points1 - points2)
        result = ""
        
        if point_difference == 1:
            result += "Advantage "
        else:
            result += "Win for "
        
        if points1 > points2:
            result += "player1"
        else:
            result += "player2"
        
        return result
    
    def get_regular_score(self, points1, points2):
        return self.score_names[points1] + "-" + self.score_names[points2]