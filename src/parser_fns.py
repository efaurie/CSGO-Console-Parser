def parse(log_line, scoreboard):
    if 'connected' in log_line:
        player_connected(log_line, scoreboard)
    elif 'Damage' in log_line:
        damage_report(log_line, scoreboard)
    elif 'EVERYONE' in log_line:
        scoreboard.start_round()

def player_connected(log_line, scoreboard):
    split_line = log_line.split(' ')
    scoreboard.add_player(split_line[0])

def damage_report(log_line, scoreboard):
    if 'Damage Taken from' in log_line:
        damage_received(log_line, scoreboard)
    elif 'Damage Given to' in log_line:
        damage_given(log_line, scoreboard)


def damage_given(log_line, scoreboard):
    split_line = log_line.split(' ')
    given_to = split_line[3][1:-1]
    scoreboard.damage_given(given_to, split_line[5], split_line[7])

def damage_received(log_line, scoreboard):
    split_line = log_line.split(' ')
    given_by = split_line[3][1:-1]
    scoreboard.damage_received(given_by, split_line[5], split_line[7])
