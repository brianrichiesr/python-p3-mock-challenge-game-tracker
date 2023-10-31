from statistics import mean

class Game:
    flag = False
    original_value = None
    def __init__(self, title):
        if not self.flag:
            self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not self.flag:
            if hasattr(self, f"{title}"):
                raise ValueError("Title already exists")
            elif not isinstance(f"{title}", str):
                raise TypeError("Title must be a string")
            else:
                self._title = title
                self.flag = True
                self.original_value = title
        else:
            self._title = self.original_value

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({game.player for game in self.results()})

    def average_score(self, player):
        return mean([result.score for result in self.results()])

class Player:

    original_value = None

    def __init__(self, username):
        self.username = username
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if not isinstance(username, str):
            self._username = self.original_value
            # raise Exception("Username must be a string")
        elif not 2 <= len(username) <= 16:
            self._username = self.original_value
            # raise ValueError("Username either too long or too short")
        else:
            self._username = username
            self.original_value = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result.game for result in self.results() if result.game == game])

class Result:
    flag = False
    original_value = None
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if not self.flag:
            if hasattr(self, f"{score}"):
                raise ValueError("Score already exists")
            elif not type(score) in (int,):
                raise TypeError("score must be an Integer")
            else:
                self._score = score
                self.flag = True
                self.original_value = score
        else:
            self._score = self.original_value
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if not isinstance(game, Game):
            raise TypeError("Game needs to be type Game")
        else:
            self._game = game
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if not isinstance(player, Player):
            raise TypeError("Player needs to be type Player")
        else:
            self._player = player