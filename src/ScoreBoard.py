class ScoreBoard:
    def __init__(self):
        self.round = 0
        self.player_name = None
        self.other_players = dict()
        self.add_player('World')

    def start_round(self):
        if self.round != 0:
            self.end_round()
        else:
            self.round += 1

        for player, reports in self.other_players.iteritems():
            reports.append([[0, 0], [0, 0]])

    def end_round(self):
        self.print_report()
        self.round += 1

    def print_report(self):
        print '---- Round {0} Report ----'.format(self.round)

        print 'Damage Given:'
        given_total = 0
        for player, reports in self.other_players.iteritems():
            if reports[self.index][0][0] > 0:
                print '\t{0}: {1} in {2} hits'.format(player, reports[self.round - 1][0][0], reports[self.index][0][1])
                given_total += reports[self.index][0][0]
        print '\tTotal Damage: {0}'.format(given_total)

        print '\nDamage Received:'
        received_total = 0
        for player, reports in self.other_players.iteritems():
            if reports[self.index][1][0] > 0:
                print '\t{0}: {1} in {2} hits'.format(player, reports[self.index][1][0], reports[self.index][1][1])
                received_total += reports[self.index][1][0]
        print '\tTotal Damage: {0}'.format(received_total)
        print '\n'

    def damage_given(self, given_to, amount, hits):
        given_pair = self.other_players[given_to][self.index][0]
        given_pair[0] += int(amount)
        given_pair[1] += int(hits)

    def damage_received(self, received_from, amount, hits):
        received_pair = self.other_players[received_from][self.index][1]
        received_pair[0] += int(amount)
        received_pair[1] += int(hits)

    def add_player(self, player_name):
        self.other_players[player_name] = []

    @property
    def index(self):
        return self.round - 1
