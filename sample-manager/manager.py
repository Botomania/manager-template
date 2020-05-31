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
        return json.dumps({"state": self.state})

    def manage(self, player, action):
        """
        Player player made an action

        Returns: dict
            {"error": "message"} if error
            {"state": ..., "next": <id>}
        """
        if action != self.state + 1:
            return json.dumps({"error": "Illegal move"})

        self.state = action
        next = action % len(self.players)

        return json.dumps({"state": self.state, "next": self.players[next]["id"]})
