# This is a breadth-first search algorithm to find the nearest developer.
from collections import deque
graph = {}
graph['you'] = ["alice", "bob", "claire"]
graph['bob'] = ["anjul", "peggy"]
graph['claire'] = ["thom", "jonny"]
graph['alice'] = ["peggy"]
graph["anjul"]=[]
graph["peggy"]=[]
graph["thom"]=[]
graph["jonny"]=[]

def search_dev(name):
      search_queue = deque()
      search_queue += graph[name]
      searched = []
      while search_queue:
            person = search_queue.popleft()
            if not person in search_queue:
                  if person_is_dev(person):
                        print(f"{person} is a developer!")
                        return True
                  else:
                        search_queue += graph[person]
                        searched.append(person)
      return False

search_dev("you")

def person_is_dev(person):
      pass