from CSGORound import CSGORound

class CSGOGame:
    def __init__(self, verbose=True):
        self.map = None
        self.current_round = -1
        self.players = []
        self.rounds = []
        self.game_active = True
        self.verbose = verbose
        if self.verbose:
            print '---- New Game Initialized ----'
        self.start_round()

    def set_map(self, map_name):
        self.map = map_name

    def start_round(self):
        if self.current_round > -1:
            self.rounds[self.current_round].generate_round_report()

        self.current_round += 1
        self.rounds.append(CSGORound(self.current_round, self.players, self.verbose))

    def register_player_if_unseen(self, player_name):
        if player_name not in self.players:
            self.players.append(player_name)
            self.rounds[self.current_round].register_unseen_player(player_name)

    def damage_given(self, given_to, amount, hits):
        self.register_player_if_unseen(given_to)
        self.rounds[self.current_round].damage_given(given_to, amount, hits)

    def damage_received(self, received_from, amount, hits):
        self.register_player_if_unseen(received_from)
        self.rounds[self.current_round].damage_received(received_from, amount, hits)

    def end_last_round(self):
        if self.game_active:
            self.rounds[self.current_round].generate_round_report()
            self.game_active = False
