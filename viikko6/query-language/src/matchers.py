


class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self):
        pass

    def matches(self, player):
        return True

class Not:
    def __init__(self, matcher):
        self._matcher = matcher
    
    def matches(self, player):
        return not self._matcher.matches(player)

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr
    
    def matches(self, player):
        player_value = getattr(player, self._attr)
        
        return player_value < self._value

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        
        return False

class QueryBuilder:
    def __init__(self, query = All()):
        self.query = query
    
    def playsIn(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query, HasFewerThan(value, attr)))

    def oneOf(self, *queries):
        return QueryBuilder(And(self.query, Or(*queries)))
    
    def build(self):
        return self.query