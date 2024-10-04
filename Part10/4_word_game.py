# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return 0

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        player_1_vowels = [i for i in player1_word if i in vowels]
        player_2_vowels = [i for i in player2_word if i in vowels]

        if len(player_1_vowels) > len(player_2_vowels):
            return 1
        elif len(player_2_vowels) > len(player_1_vowels):
            return 2
        else:
            return 0

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        self.valid_answers = ["rock", "paper", "scissors"]
    
    def round_winner(self, player1_word:str, player2_word:str):
        if player1_word.lower() in self.valid_answers and player2_word in self.valid_answers: #check that both players answered with a correct option
            if player1_word.lower() == "rock":
                if player2_word.lower() == "scissors":
                    return 1
                elif player2_word.lower() == "paper":
                    return 2
                else:
                    return 0
                
            elif player1_word.lower() == "paper":
                if player2_word.lower() == "rock":
                    return 1
                elif player2_word == "scissors":
                    return 2
                else:
                    return 0

            elif player1_word.lower() == "scissors":
                if player2_word.lower() == "rock":
                    return 2
                elif player2_word.lower() == "paper":
                    return 1
                else:
                    return 0
                
        elif player1_word.lower() not in self.valid_answers and player2_word in self.valid_answers:
            return 2
        elif player1_word.lower() in self.valid_answers and player2_word not in self.valid_answers:
            return 1
        else:
            return 0


p = LongestWord(4)
p.play() 