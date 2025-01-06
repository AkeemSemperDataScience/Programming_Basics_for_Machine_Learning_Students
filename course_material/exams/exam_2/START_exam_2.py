import pandas as pd
import seaborn as sns
import numpy as np

# Please use these constants in your code
TS_RATIO = .44
EFG_RATIO = .5

class NBA_Player():
    # This class should represent one player, or one line from the data.
    # Calculations for True Shooting and Effective Field Goal are:
    # TS = PTS / (2 * (FGA + (0.44 * FTA)))
    # EFG = (FGM + (0.5 * 3PM)) / FGA
    # Please use the constants above rather than the numbers directly in your code.
    #
    # There is a data dictionary on the terms, but you really shouldn't need it
    # https://www.basketball-reference.com/about/glossary.html 

    def __init__(self, gamesPlayed, name, team, pts, reb, ast, college, height, weight, birthdate, fga, threePA, threePM, fta, ftm, fgm):
        # This class should represent one player, or one line from the data. 
        # The only requirements here for attributes/methods are what you need to answer the questions, you can ignore others as needed. 
        self._name = name

        # You'll eventually need to calculate these, but they are not given in the data.
        # Change this code when you do the calculations.
        self._ts = -1
        self._efg = -1
        self._efg_ts_diff = -1
    
    # Please use these properties to access the attributes
    # You can add setters if needed. 
    @property
    def true_shooting(self):
        return self._ts
    @property
    def effective_field_goal(self):
        return self._efg
    @property
    def stat_diff(self):
        return self._efg_ts_diff
    @property
    def college(self):
        return self._college
    @property
    def name(self):
        return self._name
    
    def __lt__(self, other):
        # Calculate less than based on the difference between EFG and TS
        # I.e. calculate the difference between the two stats for each player, 
        # then compare those two differences here. 
        # (Player_1_EFG - Player_1_TS) < (Player_2_EFG - Player_2_TS)
        pass
    
    def collegeBase(self):
        # Remove the "extra" stuff from the college name, leaving only the "core" name
        # Remove the words "University", "College", "of", "at", "the", "College". 
        # For example, "University of North Carolina" should return "North Carolina"
        #
        # Note - there are several ways to do this, and there is some degree of error due to the fact that 
        # the simple list of words won't cover all cases. The things tested are not weird edge cases, they
        # work if you do it as directed. There may be other names that don't work perfectly, especialy internationally. 
        #
        # Double Note: after this gets marked, I'll look at some errors and see if there were 'mistakes' that I didn't
        # consider ahead of time in your code and were unfairly marked wrong, and if so, I'll adjust the marks to make it fair to you. 
        
        # Words to remove are called stopwords, this is the same in NLP.
        stopwords = ["University", "College", "of", "at", "the", "College"]
        
        pass
    def __str__(self):
        # Return a string with the player's name, team, and their True Shooting and Effective Field Goal percentages.
        # Details are up to you, as long as it is string like you're good. 
        pass
    
    @staticmethod
    def readCSV(filepath):
        # Create a static method to read the data from a CSV file at a given file path. 
        # Read each line of the CSV file, and create a new NBA_Player object for each line.
        # Return a list of all the NBA_Player objects.    
        pass
    
    @staticmethod
    def createDFfromPlayers(players):
        # Do this last, it isn't worth that much. 
        # Create a static method to create a pandas dataframe from a list of NBA_Player objects.
        # Note that the structure of the dataframe in terms of which columns isn't tested here - do something reasonable. 
        # All of the rows should be in the dataframe, add the columns that make sense to you - it isn't marked. 
        pass
    
    @staticmethod
    def contest(player1, player2, metric="TS", rounds=100, tests=1000, debug_print=False):
        # Create a static method that simulates a contest between two players.
        # This contest will simulate a number of rounds, in each round the two players will generate a score
        # based on the metric given - either True Shooting or Effective Field Goal. (If this was real basketball, each
        # of these is roughly a metric for how productive a player is, so we are having a fake contest to see who is better)
        # Note: please throw a ValueError if the metric of efg/ts is not correct.
        # The debug_print parameter is something I used to conditionally see some details as I made it, you can ignore it if you want. 

        # For each contest, there are a few steps involved:
        #   1. Depending on the metric selected, capture that score for each player. 
        #   2. The competition will be run a number of times:
        #       a. The number of rounds (param) is the number of times the players will compete in a single contest.
        #          i. In this context, this is the number of plays in a game between the players. 
        #       b. The number of tests (param) is the number of times the contest will be run.
        #          i. This is the number of games between the players.
        #       c. So, for the default params, the contest will be run 1000 times, with each contest having 100 rounds.
        #          i. The players contest each other over 100 plays in one game, in each play, the likelihood of scoring a point is based on their metric.
        #         ii. We determine the winner, then do another (by default) 999 rounds to see who wins the most games - this is what is reported. 
        #   3. In each round, use the slected metric to randomly generate a score for each player.
        #       a. This can be done by using a binomial distribution, https://numpy.org/doc/2.0/reference/random/generated/numpy.random.binomial.html
        #       b. The number of rounds is n, the size is the number of tests, and the probability is the player's metric.
        #       c. This is roughly similar to a game - the metric gives their percentage chance of scoring on each play, each round
        #          takes 100 plays and sees who scores more, and the contest is run 1000 times to see who wins the most overall. 
        #   4. The player with the higher score wins the round.
        #   5. Tabulate the results of the total number of wins for each player, and the number of ties.
        #   6. Return the number of wins for each player, and the number of ties.
        #       a. In each one of the tests, there are 100 rounds - each one won by the most number of points.
        #   7. If the option for TS/EFG gets an incorrect/invalid input, raise a ValueError.
        #
        # Note: the tests are not deterministic, so the results will vary a bit from trial to trial. 
        # The things that will be marked are not borderline, they should resolve one way or another. 
        # Like with the string processing, I'll look to see if there seemed to be anything unexpected that 
        # may impact you unfairly, and adjust the marks accordingly.
        p1wins = 0
        p2wins = 0
        ties = 0

        # Do some code stuff here....

        return p1wins, p2wins, ties
