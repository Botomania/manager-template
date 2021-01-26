import json


class Manager:
    def __init__(self, players):
        """
        Initialize state
        Get list of players

        example:
        ---
        players: [
            {
                "id": 1,
                "name": "test1"
            },
            {
                "id": 2,
                "name": "test2"
            }
        ]
        """
        self.players = players
        self.state = 0

    def get_state(self):
        """
        Return current state

        State can be as complex as you want to,
        but should follow the following style:
        {"state": ...}

        The value of key "state" will be sent (or printed) at the player's side
        """
        return {"state": self.state}

    def invalidate(self, player_id):
        """
        This player_id made an invalid move
        OR timeout
        OR other error

        remove from active list
        """
        del self.players[
            self.players.index(
                list(filter(lambda x: x["id"] == player_id, self.players))[0]
            )
        ]

    def manage(self, player, action):
        """
        Player player made an action

        Returns: dict
            {"error": "message"} if error
            {"winner": [<id>, <id>, ...]} if game over
            {"state": ..., "next": <id>}
        """
        if action != self.state + 1:
            return {"error": "Illegal move"}

        if len(self.players) == 1:
            return {"winner": [self.players[0]["id"]]}

        self.state = action
        next = action % len(self.players)

        return {"state": self.state, "next": self.players[next]["id"]}
