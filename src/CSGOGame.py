from CSGORound import CSGORound

class CSGOGame:
    def __init__(self):
        self.map = None
        self.current_round = -1
        self.players = []
        self.rounds = []

    def set_map(self, map_name):
        self.map = map_name

    def register_player(self, player_name):
        self.players.append(player_name)

    def start_round(self):
        if self.current_round > -1:
            self.rounds[self.current_round].generate_round_report()

        self.current_round += 1
        self.rounds.append(CSGORound(self.current_round + 1, self.players))

    def damage_given(self, given_to, amount, hits):
        self.rounds[self.current_round].damage_given(given_to, amount, hits)

    def damage_received(self, received_from, amount, hits):
        self.rounds[self.current_round].damage_received(received_from, amount, hits)
