from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        sorted_desc = sorted(self.players, key=lambda l: l.assists+l.goals, reverse=True)
        by_nat = filter(lambda p: p.nationality=="FIN", sorted_desc)
        return by_nat
    