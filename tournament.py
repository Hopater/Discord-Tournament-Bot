# tournament.py
import math
import random

class TournamentManager:
    def __init__(self):
        self.players = []
        self.rounds = []
        self.current_round = 0
        self.registration_message_id = None
        self.channel_id = None
        self.host_id = None

    def reset(self):
        self.__init__()

    def add_player(self, name):
        if name not in self.players:
            self.players.append(name)

    def generate_bracket(self):
        shuffled = self.players[:]
        if len(shuffled) % 2 != 0:
            shuffled.append("BYE")
        random.shuffle(shuffled)
        matches = [(shuffled[i], shuffled[i+1]) for i in range(0, len(shuffled), 2)]
        self.rounds = [matches]
        self.current_round = 0

    def get_next_match(self):
        if self.current_round >= len(self.rounds):
            return None
        for match in self.rounds[self.current_round]:
            if isinstance(match, tuple):
                return match
        return None

    def record_result(self, p1, p2, winner):
        round_matches = self.rounds[self.current_round]
        for i, match in enumerate(round_matches):
            if (p1, p2) == match or (p2, p1) == match:
                round_matches[i] = winner
                break

        if all(isinstance(m, str) for m in round_matches):
            if len(round_matches) == 1:
                return  # Tournament over
            next_round = [(round_matches[i], round_matches[i+1]) for i in range(0, len(round_matches), 2)]
            self.rounds.append(next_round)
            self.current_round += 1

    def get_all_rounds(self):
        return self.rounds