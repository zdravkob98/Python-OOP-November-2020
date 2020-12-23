

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if not player.guild == "Unaffiliated" and not player.guild == self.name:
            return f"Player {player.name} is in another guild."
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        #if player_name not in map(lambda x: x.name, self.players):
        if player_name not in [x.name for x in self.players]:
            return f"Player {player_name} is not in the guild."
        #self.players.remove(next(filter(lambda x: x.name == player_name, self.players)))
        del self.players[player_name.index(player_name)]
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        data = f"Guild: {self.name}\n"
        for p in self.players:
            data += p.player_info()
        return data


