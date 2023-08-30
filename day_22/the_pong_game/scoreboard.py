from turtle import Turtle

ALIGNMENT = "center"
SCOREBOARD_FONT = ("Courier", 48, "bold")
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """creates a scoreboard with the current score of 0."""
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the scoreboard with the current score.
        """
        self.clear()
        self.write(f"{self.score1}    {self.score2}", align=ALIGNMENT, font=SCOREBOARD_FONT)

    def increase_score1(self):
        """
        Increase the score by 1 and update the scoreboard.
        """
        self.score1 += 1
        self.update_scoreboard()

    def increase_score2(self):
        """
        Increase the score by 1 and update the scoreboard.
        """
        self.score2 += 1
        self.update_scoreboard()

    def game_over(self, player):
        """
        Display the game over message.

        Parameters:
        - player (str): The name of the winning player.

        Returns:
        - None
        """
        self.goto(0, 0)
        self.write(f"GAME OVER. {player} WINS!", align=ALIGNMENT, font=FONT)
