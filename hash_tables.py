# This is a simple hash table code to check of users have voted in an election

voted = {}
def check_voter(name):
      if voted.get(name):
            print(f"Kick {name} out!")
      else:
            voted[name] = True
            print(f"Let {name} vote!")

check_voter("Tom")
check_voter("Greg")
check_voter("Greg")