from CSGOGame import CSGOGame

class ConsoleParser:
    def __init__(self, console_tailer):
        self.console_tailer = console_tailer
        self.csgo_game = None

    def listen(self):
        try:
            while True:
                next_line = self.console_tailer.poll()
                self.handle(next_line)
        except KeyboardInterrupt:
            self.console_tailer.stop()

    def handle(self, log_line):
        if 'Counter-Strike: Global Offensive' in log_line:
            self.csgo_game = CSGOGame()
        elif 'Map:' in log_line:
            self.csgo_game.set_map(log_line.split(' ')[1])
        elif 'connected' in log_line:
            self.player_connected(log_line)
        elif 'Damage' in log_line:
            self.damage_report(log_line)
        elif 'EVERYONE' in log_line:
            self.csgo_game.start_round()

    def player_connected(self, log_line):
        split_line = log_line.split(' ')
        self.csgo_game.register_player(split_line[0])

    def damage_report(self, log_line):
        if 'Damage Taken from' in log_line:
            self.damage_received(log_line)
        elif 'Damage Given to' in log_line:
            self.damage_given(log_line)

    def damage_given(self, log_line):
        split_line = log_line.split(' ')
        given_to = split_line[3][1:-1]
        self.csgo_game.damage_given(given_to, split_line[5], split_line[7])

    def damage_received(self, log_line):
        split_line = log_line.split(' ')
        given_by = split_line[3][1:-1]
        self.csgo_game.damage_received(given_by, split_line[5], split_line[7])
