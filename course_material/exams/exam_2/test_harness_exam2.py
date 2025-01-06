import START_exam_2
import pandas as pd
import numpy as np

fpath = "NBA.csv"
df = pd.read_csv("NBA.csv")
all_players = START_exam_2.NBA_Player.readCSV(fpath)
p1 = START_exam_2.NBA_Player(name="Lebron James", team="LAL", pts=2779, reb=456, ast=353, college="No College", 
        height="6-9", weight=250, birthdate="12/30/1984", fga=1500, threePA=500, 
        threePM=245, fta=340, ftm=274, fgm=1235, gamesPlayed=82)
p2 = START_exam_2.NBA_Player(name="Kevin Durant", team="GSW", pts=2020, reb=300, ast=200, college="Texas",
            height="6-11", weight=240, birthdate="09/29/1988", fga=1000, threePA=300,
            threePM=145, fta=240, ftm=200, fgm=800, gamesPlayed=70)
p3 = START_exam_2.NBA_Player(name="Michael Jordan", team="CHI", pts=3000, reb=500, ast=400, college="University of North Carolina",
            height="6-6", weight=220, birthdate="02/17/1963", fga=2000, threePA=100,
            threePM=45, fta=400, ftm=300, fgm=1500, gamesPlayed=82)
p4 = START_exam_2.NBA_Player(name="Kobe Bryant", team="LAL", pts=2500, reb=400, ast=300, college="Lower Merion High School",
            height="6-6", weight=220, birthdate="08/23/1978", fga=1800, threePA=500,
            threePM=245, fta=340, ftm=274, fgm=1235, gamesPlayed=82)
all_players = START_exam_2.NBA_Player.readCSV(fpath)

def test_readCSV():
    correct_ans = 490
    submission = len( START_exam_2.NBA_Player.readCSV(fpath) )
    assert np.isclose(correct_ans, submission, 1)

def test_createPlayer():
    p1_str = p1.__str__()
    assert len(p1_str) > 10

def test_TS_1():
    correct = .84232
    submission = p1.true_shooting
    assert np.isclose(correct, submission, .01)

def test_EFG_1():
    correct = .905
    submission = p1.effective_field_goal
    assert np.isclose(correct, submission, .01)

def test_diff_1():
    correct = .0626745
    submission = float(p1.stat_diff)
    assert np.isclose(correct, submission, .01)
'''def test_diff_2():
    correct = -.041
    submission = float(p2.stat_diff)
    print(submission, correct)

    assert np.isclose(correct, submission, .01)
'''
def test_ComparePlayers():
    assert p1 > p2

def test_CollegeName_1():

    correct = "North Carolina"
    submission = str(p3.collegeBase()).strip()
    assert correct == submission
def test_CollegeName_2():
    correct = "Texas"
    submission = str(p2.collegeBase()).strip()
    assert correct == submission
def test_CollegeName_3():
    correct = "Lower Merion High School"
    submission = str(p4.collegeBase()).strip()
    assert correct == submission

def test_contest_1():
    all_players = START_exam_2.NBA_Player.readCSV(fpath)
    p1c = [x for x in all_players if x.name == "James Harden"][0]
    p2c = [x for x in all_players if x.name == "LeBron James"][0]

    p1wins, p2wins, ties = START_exam_2.NBA_Player.contest(p1c, p2c, metric="TS", rounds=1000)
    print(p1wins, p2wins, ties)
    assert p1wins > p2wins

def test_contest_2():
    p1c = [x for x in all_players if x.name == "Chris Paul"][0]
    p2c = [x for x in all_players if x.name == "Damian Lillard"][0]

    p1wins, p2wins, ties = START_exam_2.NBA_Player.contest(p1c, p2c, metric="EFG", rounds=1000)
    print(p1wins, p2wins, ties)
    assert p1wins > p2wins
def test_contest_3():
    p1c = [x for x in all_players if x.name == "Kevin Durant"][0]
    p2c = [x for x in all_players if x.name == "Kobe Bryant"][0]
    try:
        p1wins, p2wins, ties = START_exam_2.NBA_Player.contest(p1c, p2c, metric="TMP", rounds=1000)
    except ValueError as e:
        assert True
    else:
        assert False

def test_asDataframe():
    samp_df = START_exam_2.NBA_Player.createDFfromPlayers(all_players)
    assert np.isclose(samp_df.shape[0], len(all_players), .01)