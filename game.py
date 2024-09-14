import random
import time

# Assuming you have player.py with the necessary classes and functions
from player import Player, Team, printbox, printscore, playball, gameplay, extras, spamabs

def main():
    random.seed(time.time())
    
    away_team = Team("NYY")
    home_team = Team("NYM")
    
    option = input("A) Simulate game  OR  B) Simulate player at-bats\n").strip().upper()
    
    if option == 'A':
        playball()
        inning = 1
        top = True
        
        for _ in range(8):
            gameplay(inning, top)
            gameplay(inning, top)
        
        gameplay(inning, top)
        top = False
        
        if home[0] <= away[0]:
            extras(top)
        
        for _ in range(5):
            extras(top)
            extras(top)
        
        home[0] = 10
        home[1] = 10
        home[2] = 10
        
        printscore("NYY", "NYM")
        
        # Update stats for demonstration
        home_team.lineup[0].rbi()
        home_team.lineup[0].run()
        home_team.lineup[0].sacfly()
        
        for _ in range(4):
            for i in range(9):
                away_team.lineup[i].getoutcome(200)
                home_team.lineup[i].getoutcome(random.randint(0, 999))
        
        printbox(away_team.lineup)
        printbox(home_team.lineup)
        
        home_team.lineup[0].printabs()
        home_team.lineup[0].printstats()
    
    elif option == 'B':
        wteam = input("A) Home team  OR  B) Away team\n").strip().upper()
        
        if wteam == 'A':
            spamabs(home_team.lineup)
        elif wteam == 'B':
            spamabs(away_team.lineup)
        else:
            print("Invalid option. Exiting.")
            return

if __name__ == "__main__":
    main()
