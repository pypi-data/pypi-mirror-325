from typing import Optional, Tuple, List, Dict, Any
import textarena as ta
import random
import re

class MastermindEnv(ta.Env):
    """
    Environment for Mastermind game.
    """
    def __init__(
        self,
        difficulty: Optional[str] = "easy",
    ):
        """
        Initializes the Mastermind environment.
        
        Parameters:
        - difficulty: The difficulty level of the game (easy, medium, hard).
        """
        super().__init__()
        self.environment_name = "Mastermind"
        self.difficulty = difficulty

        ## initializa the properties of the game
        if self.difficulty == "easy":
            self.code_length = 4
            self.num_numbers = 6
            self.max_turns = 20
            self.duplicate_numbers = False
        elif self.difficulty == "medium":
            self.code_length = 4
            self.num_numbers = 8
            self.max_turns = 30
            self.duplicate_numbers = False
        elif self.difficulty == "hard":
            self.code_length = 4
            self.num_numbers = 10
            self.max_turns = 50
            self.duplicate_numbers = True
        else:
            raise ValueError(f"Invalid difficulty level: {difficulty}")
        
        ## inistialize the game state
        self.state = ta.State(
            num_players=2,
            max_turns=self.max_turns,
        )
    
    @property
    def terminal_render_keys(self):
        return ["rendered_view"]

    def reset(
        self,
        seed: Optional[int] = None
    ) -> Optional[ta.Observations]:
        """
        Resets the environment to its initial state.
        
        Args:
            seed (int): Optional random seed for reproducibility.
            
        Returns:
            Observations: Initial observations for all players.
        """
        if seed is not None:
            random.seed(seed)
        else:
            random.seed()

        ## initialize the game objects
        self.secret_codes = self._generate_secret_codes()
        self.guesses = {0: [], 1: []}

        ## return the initial observations
        return self.state.reset(
            game_state={
                "rendered_view": self._render_view()
            },
            player_prompt_function=self._generate_player_prompt
        )
    
    def _generate_secret_codes(self) -> Dict[List[int], List[int]]:
        """
        Generates secret codes for both players based on the difficulty level.

        Returns:
            Dict[int, List[int]]: Secret codes for both players.
        """

        available_numbers = list(range(1, self.num_numbers + 1))
        if self.duplicate_numbers:
            player1_code = random.choices(available_numbers, k=self.code_length)
            player2_code = random.choices(available_numbers, k=self.code_length)
        else:
            player1_code = random.sample(available_numbers, k=self.code_length)
            player2_code = random.sample(available_numbers, k=self.code_length)
        
        secret_codes = {
            0: player1_code,
            1: player2_code
        }

        return secret_codes
    
    def _render_view(self) -> str:
        """
        Renders the game view for both players. It shows their secret codes against the opponent's guesses.
        """
        view = "Player 0's Guess: " + " ".join(map(str, self.guesses[0]) if self.guesses[0] else ["-"] * self.code_length) + "\n"
        view += "Player 1's Guess: " + " ".join(map(str, self.guesses[1]) if self.guesses[1] else ["-"] * self.code_length) + "\n"

        return view

    def _generate_player_prompt(self, player_id: int, game_state: Dict[int, Any]) -> str:
        """
        Generates the initial prompt for a player.
        
        Args:
            player_id (int): ID of the player (0 or 1).
        
        Returns:
            str: Initial prompt for the player.
        """
        prompt = (
            f"You are Player {player_id}. You are playing Mastermind ({self.difficulty} level).\n"
            f"Your goal is to guess the other player's secret code that is {self.code_length} digits long, where each digit ranges from 1 to {self.num_numbers}, and the are {'' if self.duplicate_numbers else 'no '}duplicate digits.\n"
            "In your response, you can mention any code or previously submitted code in the format of 1 2 3 4. Only when you have decided to make your guess, then you must strictly enter the code in square brackets like [2 1 4 5]. This is to avoid submitting a wrong code to the game environment.\n"
            "Hence, if you are quoting a recent guess, you must mention the numbers without the square brackets.\n"
            "After each guess, you will receive feedback in the form of black and white pegs.\n"
            "A black peg indicates a correct digit in the correct position, while a white peg indicates a correct digit in the wrong position.\n"
            f"You have only {self.max_turns/2:.0f} turns to guess the code.\n"
        )

        return prompt
    
    def step(
        self,
        action: str,
    ) -> Tuple[
        ta.Observations,
        ta.Rewards,
        bool,
        bool,
        ta.Info
    ]:
        """
        Process the player's action and update the game state.

        Args:
            player_id (int): The player's ID (0 or 1).
            action (str): The player's action (guess).

        Returns:
            Observations: Observations for all players.
            Rewards: Rewards for all players.
            bool: Whether the game is truncated.
            bool: Whether the game is terminated.
            Info: Additional information.
        """
        player_id = self.state.current_player_id

        ## update the observations
        self.state.add_observation(
            from_id=player_id,
            to_id=player_id, ## send the observation to the same player
            message=action,
            for_logging=True
        )

        ## search for the action pattern
        action_search_pattern = re.compile(r"\[(\d+(?:\s+\d+)*)\]") ## e.g., [1 2 3 4]
        match = action_search_pattern.search(action)

        if match is None:
            self.state.set_invalid_move(
                player_ids=[player_id],
                reasons=[f"Invalid move format. Player {player_id}, did not respond with a space-separated list of numbers wrapped in square brackets."]
            )

        else:
            ## extract the numbers from the action
            player_guess = list(map(int, match.group(1).split()))

            ## check if the guess is valid
            if len(player_guess) != self.code_length:
                self.state.set_invalid_move(
                    player_ids=[player_id],
                    reasons=[f"Invalid move format. Player {player_id}, the guess should contain {self.code_length} numbers."]
                )
            else:
                ## evaluate the guess
                black_pegs, white_pegs = self._evaluate_guess(player_id, player_guess)

                ## check if the player has won
                if any(num > self.num_numbers for num in player_guess):
                    self.state.set_invalid_move(
                        player_ids=[player_id],
                        reasons=[f"Invalid move format. Player {player_id}, the guess should contain numbers between 1 and {self.num_numbers}."]
                    )
                elif black_pegs == self.code_length:
                    self.state.set_winners(
                        player_ids=[player_id],
                        reason=f"Player {player_id} has cracked the code!"
                    )
                else:
                    self.state.add_observation(
                        from_id=ta.GAME_ID,
                        to_id=player_id, ## send the observation to the player
                        message=f"You have submitted [{match.group(1)}]. Feedback: {black_pegs} black peg(s), {white_pegs} white peg(s).",
                        for_logging=False
                    )

                ## update the guesses
                self.guesses[player_id] = player_guess

        ## update the rendered view
        self.state.game_state["rendered_view"] = self._render_view()

        return self.state.step()
    
    def _evaluate_guess(self, player_id: int, player_guess: List[int]) -> Tuple[int, int]:
        """
        Evaluates the player's guess and returns the number of black and white pegs.
        
        Args:
            player_id (int): ID of the player making the guess.
            player_guess (List[int]): The player's guess.
        
        Returns:
            Tuple[int, int]: Number of black and white pegs.
        """
        black_pegs = 0
        white_pegs = 0
        matched_code = [False] * self.code_length
        opponent_code = self.secret_codes[1 - player_id]

        for i in range(self.code_length):
            if player_guess[i] == opponent_code[i]:
                black_pegs += 1
                matched_code[i] = True
            else:
                for j in range(self.code_length):
                    if not matched_code[j] and player_guess[i] == opponent_code[j]:
                        white_pegs += 1
                        matched_code[j] = True
                        break

        return black_pegs, white_pegs
    
    def render(self):
        """
        Renders the minimal game state.
        """
        print(f"Turn: {self.state.turn}")
        print("\nRecent Game Logs:")
        recent_logs = self.state.logs[-5:]

        for sender_id, log in recent_logs:
            if sender_id == ta.GAME_ID:
                print(f"[GAME] {log}")
            else:
                print(f"[Player {sender_id}] {log}")