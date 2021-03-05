from dataclasses import dataclass, field
from typing import List

@dataclass
class Game:
  names: List[str] = field(default_factory=list)
  scores: List[int] = field(default_factory=list)

def load_scores():
  ret=[]
  f=open("Agricola_scores", "r")
  line=f.readline()
  while line:
    ret.append(int(line))
    line=f.readline()
  f.close()
  return ret

def save_scores(new_scores):
  f=open("Agricola_scores", "w")
  for score in new_scores:
    f.write("%d\n" % score)
  f.close()

#scores =load_scores()
scores=[]
print("Hello welcome to the Agricola score keeper")

while True:
  print("push 1 to look at old games push 2 to  add a new game")
  choice =input('')
  if choice=="1":
    if len(scores)==0:
      print("no games yet")
    else:
      # for score in scores:
      #  print(score)
      print("%r"%scores)
  elif choice=="2":
    g=Game()
    print("Who are the players?")
    print("push enter to stop")
    name=input("")
    while name !="":
         g.names.append(name)
         name=input("")
    # score=input("what is your score ")
    #  score=int(score)
    #  scores.append(score)
    # save_scores(scores)
    print("What are your scores")
    print("push enter to stop")
    number=input("")
    while number !="":
      g.scores.append(int(number))
      number=input("")
    scores.append(g) 
  else:

    print("What human are you stupid?!?")
