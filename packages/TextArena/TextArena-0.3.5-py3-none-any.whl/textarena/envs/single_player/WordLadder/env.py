from typing import Any, Dict, List, Tuple, Optional, Union
import copy
import random
import textarena as ta
import re
import networkx as nx

## use nltk to get the words
import nltk
from nltk.corpus import words
nltk.download('words')

class WordLadderEnv(ta.Env):
    """
    Word Ladder environment.
    """

    def __init__(
        self,
        hardcore: Optional[bool] = False,
        word_len: int = 4
    ):
        """
        Initialize the Word Ladder environment.

        Args:
            hardcore: Whether to play in hardcore mode.
            word_len: The length of the words to use.

        """

        super().__init__()
        self.environment_name = "WordLadder"
        self.hardcore = hardcore
        self.word_len = word_len

        ## initialize the game state
        self.state = ta.State(
            num_players=1,
            max_turns=10 ## TODO - is 10 enough? Is max_turns or max_lives better?
        )

        ## load the word list (to be sampled from)
        if hardcore:
            self.word_list = words.words("en")
        else:
            self.word_list = words.words("en-basic")

    @property
    def offline_renderer(self):
        pass

    @property
    def terminal_render_keys(self):
        return ["rendered_text"]

    def reset(
        self,
        seed: Optional[int] = None
    ) -> Optional[ta.Observations]:
        """
        Reset the environment to its initial state.

        Args:
            seed (int): Random seed for the environment.

        Returns:
            Observations: Initial observations for the player.

        """

        ## seed the random number generator
        if seed is not None:
            random.seed(seed)
        else:
            random.seed()

        ## initialize the game state
        self.word_graph = self._generate_word_graph(word_len = self.word_len)
        self.start_word, self.target_word = self._generate_words()
        self.current_word = self.start_word
        self.history = [self.start_word]

        ## reset the game state
        return self.state.reset(
            game_state={
                "start_word": self.start_word,
                "target_word": self.target_word,
                "rendered_text": self._render_text() 
            },
            player_prompt_function=self._generate_player_prompt
        )
    
    def _generate_player_prompt(self, player_id: int, game_state: Dict[int, Any]) -> str:
        """
        Generate the prompt for the player based on the current state of the game.

        Args:
            player_id: The player id.

        Returns:
            str: The prompt for the player.

        """
        prompt = (
            f"You are Player {player_id}. You are playing Word Ladder ({'Hardcore' if self.hardcore else 'basic'}).\n"
            "The objective of the game is to convert the start word to the target word by changing one letter at a time.\n"
            f"The start word is: {self.start_word}\n"
            f"The target word is: {self.target_word}\n"
            "To submit your word, you must wrap it in square brackets, e.g. [word].\n"
            "As you play, the history of your choices will be appended below. Use the information to win the game.\n"
        )

        return prompt
    
    def _render_text(self) -> str:
        """
        Render the text for the player based on the current state of the game.

        Returns:
            str: The rendered text for the player.

        """
        ## render the history and also the target words
        return (
            f"Word Ladder History: {' -> '.join(self.history)}. Target Word: {self.target_word}\n", 
        )

    def _generate_word_graph(self, word_len: int) -> Any:
        """
        Builds a graph where each word is a node and two words are connected
        if they differ by exactly one letter.

        Args:
            word_len: The length of the words to use.

        Returns:
            Any: A networkx graph representing the word ladder.

        """
        graph = nx.Graph()
        self.k_len_words = [word for word in self.word_list if len(word) == word_len]
        graph.add_nodes_from(self.k_len_words)
        for i, word in enumerate(self.k_len_words):
            for other_word in self.k_len_words[i + 1 :]:
                if sum(a != b for a, b in zip(word, other_word)) == 1: ## check if the words differ by exactly one letter
                    graph.add_edge(word, other_word)
        # remove any isolated nodes
        graph.remove_nodes_from(list(nx.isolates(graph)))
        
        return graph
    
    # def _generate_words(self) -> Tuple[str, str]:
    #     """
    #     Generate the start and target words for the game.

    #     Returns:
    #         Tuple[str, str]: The start and target words.

    #     """
    #     start_word, target_word = random.sample(self.k_len_words, 2)
        
    #     while not self._validate_solution_existence(self.word_graph, start_word, target_word):
    #         start_word = random.choice(self.k_len_words).lower()
    #         target_word = random.choice(self.k_len_words).lower()
    #         while target_word == start_word:
    #             target_word = random.choice(self.k_len_words).lower()

    #     return start_word, target_word

    def _generate_words(self) -> Tuple[str, str]:
        """
        Generate a start and target word pair with exactly 10 steps between them.

        Returns:
            Tuple[str, str]: The start and target words.
        """
        while True:
            start_word = random.choice(self.k_len_words)
            
            # Ensure start_word is in the graph (in case of isolates removal)
            if start_word not in self.word_graph:
                continue
            
            # Get all nodes with exactly 10 steps from start_word
            path_lengths = nx.single_source_shortest_path_length(self.word_graph, start_word)
            candidates = [word for word, distance in path_lengths.items() if distance == 5]
            
            # If there are any candidates exactly 10 steps away, select one as target_word
            if candidates:
                target_word = random.choice(candidates)
                return start_word, target_word


    
    def _validate_solution_existence(self, graph, start_word, target_word) -> bool:
        """
        Check if there is a path from start_word to target_word in the graph.
        
        Args:
            graph: The graph to search.
            start_word: The start word.
            target_word: The target word.
            
        Returns:
            bool: Whether a path exists between the two words.
        """
        return nx.has_path(graph, start_word, target_word)
    
    def step(
        self,
        action: str
    ) -> Tuple[
        Optional[ta.Observations], # observations
        Optional[ta.Rewards], # reward
        bool, # truncated
        bool, # terminated
        ta.Info # info
    ]:
        """
        Process the player's action and update the environment state.

        Args:
            player_id (int): The ID of the player making the move.
            action (str): The action taken by the player.

        Returns:
            Observations: Observations for the player after the action.
            Rewards: Rewards for the player after the action.
            bool: Whether the game was truncated.
            bool: Whether the game is terminated.
            Info: Additional information about the game state

        """
        player_id = self.state.current_player_id

        ## update the observation
        self.state.add_observation(
            from_id=player_id,
            to_id=-1,
            message=action,
            for_logging=True
        )

        ## validate the action
        action_search_pattern = re.compile(r"\[([a-zA-Z]+)\]") # e.g. [word]
        match = action_search_pattern.search(action)


        if match is None:
            self.state.set_invalid_move(
                player_ids= [player_id],
                reasons=[f"Invalid move format. Player {player_id} did not respond with a valid word format in square brackets."]
            )

        else:
            next_word = match.group(1)
            if len(next_word) != len(self.target_word):
                ## check if the word is of the correct length
                self.state.set_invalid_move(
                    player_ids= [player_id],
                    reasons=[f"Invalid move format. Player {player_id} did not respond with a word of the correct length."]
                )
            elif not self.word_graph.has_node(next_word):
                ## check if the word is in the word list
                self.state.set_invalid_move(
                    player_ids= [player_id],
                    reasons=[f"Invalid move format. Player {player_id} did not respond with a valid word."]
                )
            elif not self._is_valid_move(next_word):
                ## check if word is a move that is one letter away from the current word
                self.state.add_observation(
                    from_id=-1,
                    to_id=player_id,
                    message="You have provided an invalid word! The word must differ by exactly one letter.",
                    for_logging=False
                )

            else:
                ## is a valid move
                self.current_word = next_word
                self.history.append(next_word)
                if next_word == self.target_word:
                    ## player found the target word - game is over
                    self.state.set_winners(
                        player_ids=[player_id],
                        reason=f"Congratulations! Player {player_id} has found the target word."
                    )
                else:
                    ## game is not over
                    self.state.add_observation(
                        from_id=-1,
                        to_id=player_id,
                        message=f"You've selected a valid word.\n{self._render_text()}",
                        for_logging=False
                    )

            ## update the game board
            self.state.game_state["rendered_text"] = self._render_text()

        return self.state.step()            
    
    def _is_valid_move(self, next_word: str) -> bool:
        """
        Attempts to change the current word to `next_word` if valid.
        
        Args:
            next_word: The word to change to.
            
        Returns:
            bool: Whether the move is valid.

        """
        next_word = next_word.lower()
        
        if not self.word_graph.has_edge(self.current_word, next_word):
            return False
        
        return True

    def render(self):
        """
        Render the current state of the environment.

        Returns:
            str: The rendered state of the environment.
            
        """
        print(f"Start word: {self.start_word}")
        print(f"Target word: {self.target_word}")
        print(f"Current word: {self.current_word}")
        print(f"History: {self.history}")
