class CSGORound:
    def __init__(self, round_id, players, verbose=True):
        self.round_id = round_id
        self.verbose = verbose
        self.total_damage = {'given': {'damage': 0, 'hits': 0}, 'received': {'damage': 0, 'hits': 0}}

        self.player_stats = dict()
        self.init_player_stats(players)

    def init_player_stats(self, players):
        for player in players:
            self.register_unseen_player(player)

    def register_unseen_player(self, player_name):
        self.player_stats[player_name] = {'given': {'damage': 0, 'hits': 0}, 'received': {'damage': 0, 'hits': 0}}

    def damage_given(self, given_to, amount, hits):
        self.player_stats[given_to]['received']['damage'] += int(amount)
        self.player_stats[given_to]['received']['hits'] += int(hits)

        self.total_damage['given']['damage'] += int(amount)
        self.total_damage['given']['hits'] += int(hits)

        if self.verbose:
            self.generate_live_player_report(given_to)

    def damage_received(self, received_from, amount, hits):
        self.player_stats[received_from]['given']['damage'] += int(amount)
        self.player_stats[received_from]['given']['hits'] += int(hits)

        self.total_damage['received']['damage'] += int(amount)
        self.total_damage['received']['hits'] += int(hits)

    def generate_round_report(self):
        print '\n---- Round {0} Report ----'.format(self.round_id)
        self.generate_round_subreport('given')
        self.generate_round_subreport('received')
        print '\n'

    def generate_round_subreport(self, key):
        if key is 'received':
            subkey = 'given'
        else:
            subkey = 'received'

        print 'Damage {0}:'.format(key.capitalize())
        for player, reports in self.player_stats.iteritems():
            if reports[subkey]['damage'] > 0:
                print '\t{0}: {1} in {2} hits'.format(player, reports[subkey]['damage'], reports[subkey]['hits'])

        print '\tTotal Damage: {0} in {1} hits'.format(self.total_damage[key]['damage'], self.total_damage[key]['hits'])

    def generate_live_player_report(self, player_name):
        damage_given = self.player_stats[player_name]['received']['damage']
        hits_landed = self.player_stats[player_name]['received']['hits']
        print 'Damage Given: [{0}] {1} in {2} hits'.format(player_name, damage_given, hits_landed)
