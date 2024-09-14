# player.py

import random

# Global variables
statcat = [" R", " 2B", " 3B", " HR", " RBI", " BB", " K"]
away = [0] * 11
home = [0] * 11

class Player:
    def __init__(self, pname, avgm, obpm, hitsm, dm, tm, hrm, bbm, hbpm, som, abm, pam):
        self.name = pname
        self.avg = avgm
        self.obp = obpm
        self.hits = hitsm
        self.d = dm
        self.t = tm
        self.hr = hrm
        self.bb = bbm
        self.hbp = hbpm
        self.so = som
        self.ab = abm
        self.pa = pam
        self.s = hitsm - hrm - dm - tm
        self.gamestats = [0] * 11
        self.atbats = []

    def run(self):
        self.gamestats[2] += 1

    def rbi(self):
        self.gamestats[6] += 1

    def sacfly(self):
        self.rbi()
        self.gamestats[1] -= 1

    def printstats(self):
        print(f"{self.name}: {self.gamestats[0]}-{self.gamestats[1]}", end="")
        for i in range(2, 11):
            if self.gamestats[i] > 0:
                print(f", {self.gamestats[i]}{statcat[i - 2]}", end="")
        print()

    def printabs(self):
        print(", ".join(self.atbats))

    def printboxstats(self):
        print(f"{self.name:<15}{self.gamestats[1]:>4}    {self.gamestats[2]:>4}    {self.gamestats[0]:>4}    {self.gamestats[6]:>4}    {self.gamestats[7]:>4}    {self.gamestats[8]:>4}")

    def returnname(self):
        return self.name

    def getoutcome(self, value):
        outcome = ""
        if value > self.obp:
            self.gamestats[1] += 1
            sor = (self.so * 1000.0) / self.pa
            thresh = 1000 - sor
            segment = (thresh - self.obp) / 5
            seg1 = thresh - segment
            seg2 = seg1 - segment
            seg3 = seg2 - segment
            seg4 = seg3 - segment
            if value > thresh:
                outcome = "Strike out"
                self.gamestats[8] += 1
            elif value > seg1:
                outcome = "Pop out"
            elif value > seg2:
                outcome = "Fly out"
            elif value > seg3:
                outcome = "Line out"
            elif value > seg4:
                outcome = "Ground out"
            else:
                outcome = "Reached on error"
        elif value > self.avg:
            bbrate = self.bb / (self.bb + self.hbp)
            thresh = ((self.obp - self.avg) * bbrate) + self.avg
            if value > thresh:
                outcome = "Hit by pitch"
            else:
                outcome = "Base on balls"
                self.gamestats[7] += 1
        else:
            self.gamestats[0] += 1
            self.gamestats[1] += 1
            num = (value * 100.0) / self.avg
            hrs = ((self.hits - self.hr) * 100.0) / self.hits
            ts = ((self.hits - self.hr - self.t) * 100.0) / self.hits
            ds = ((self.hits - self.hr - self.t - self.d) * 100.0) / self.hits
            if num > hrs:
                outcome = "Home run"
                self.gamestats[5] += 1
            elif num > ts:
                outcome = "Triple"
                self.gamestats[4] += 1
            elif num > ds:
                outcome = "Double"
                self.gamestats[3] += 1
            else:
                outcome = "Single"
        self.atbats.append(outcome)
        return outcome

class Team:
    def __init__(self, pname):
        self.name = pname
        self.lineup = [
            Player("Aaron Judge1", 333, 467, 156, 31, 1, 51, 110, 9, 138, 468, 590),
            Player("Aaron Judge2", 333, 467, 156, 31, 1, 51, 110, 9, 138, 468, 590),
            Player("Aaron Judge3", 333, 467, 156, 31, 1, 51, 110, 9, 138, 468, 590),
            Player("Aaron Judge4", 333, 467, 156, 31, 1, 51, 110, 9, 138, 468, 590),
            Player("Aaron Judge5", 333, 467, 156, 31, 1, 51, 110, 9, 138, 468, 590),
            Player("Aaron6", 333, 467, 156, 31, 1, 51, 110, 9, 138, 468, 590),
            Player("Aaron Judge7", 333, 467, 156, 31, 1, 51, 110, 9, 138, 468, 590),
            Player("Aaron Judge8", 333, 467, 156, 31, 1, 51, 110, 9, 138, 468, 590),
            Player("Aaron Judge9", 333, 467, 156, 31, 1, 51, 110, 9, 138, 468, 590),
        ]

def printbox(lineups):
    if len(lineups) < 9:
        return
    print("               AB   R    H   RBI   BB   K")
    for i in range(9):
        lineups[i].printboxstats()
    print()

def printscore(t1, t2):
    print("     ", end="")
    for i in range(3, len(away)):
        print(f"{i - 2:2}", end=" ")
    print("  R  H  E")
    print(f"{t1}  ", end="")
    for i in range(3, len(away)):
        print(f"{away[i]:2}", end=" ")
    print("  ", end="")
    for i in range(3):
        print(f"{away[i]:2}", end=" ")
    print()
    print(f"{t2}  ", end="")
    for i in range(3, len(home)):
        print(f"{home[i]:2}", end=" ")
    if len(home) < len(away):
        print("   ", end="")
    print("  ", end="")
    for i in range(3):
        print(f"{home[i]:2}", end=" ")
    print()
    print()

def playball():
    global away, home
    away = [0] * 11
    home = [0] * 11

def gameplay(count, n):
    if n:
        away[count + 2] += 1
        n = False
    else:
        home[count + 2] += 2
        n = True
        count += 1
    return count, n

def extras(n):
    if n:
        away.append(1)
        n = False
    else:
        home.append(1)
        n = True
    return n

def spamabs(outcomes):
    print("Choose player:")
    for i, player in enumerate(outcomes):
        print(f"{i + 1} {player.returnname()}")
    wplayer = int(input()) - 1
    nabs = int(input("How many at-bats? "))
    for _ in range(nabs):
        n = random.randint(0, 999)
        outcomes[wplayer].getoutcome(n)
    outcomes[wplayer].printabs()
    outcomes[wplayer].printstats()
