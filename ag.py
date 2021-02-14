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

scores =load_scores()
print("Hello welcome to the Agricola score keeper")

while True:
  print("push 1 to look at old games push 2 to  add a new game")
  choice =input('')
  if choice=="1":
    if len(scores)==0:
      print("no games yet")
    else:
      print("%r" % scores)
  elif choice=="2":
    score=input("what is your score ")
    score=int(score)
    scores.append(score)
    save_scores(scores)
  else:
    print("What human are you stupid?!?")

