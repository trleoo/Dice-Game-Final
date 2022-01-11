import random
import sys
import time

dice = ["Empty", "\n     " + "\n  o  " + "\n     ", "\no    " + "\n     " + "\n    o", "\n    o" + "\n  o  " + "\no    ", "\no   o" + "\n     " + "\no   o", "\no   o" + "\n  o  " + "\no   o", "\no   o" + "\no   o" + "\no   o"]

score = [0,1,2,3,4,5,6]
playerscore=0
AIscore=0

#Text effect
def printy(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

printy("Welcome to the dice game.")
time.sleep(0.5)
printy("Would you like to roll?")
time.sleep(0.5)
answer = input("Yes(y) or No(n): ")

while answer == "y":
 
  #Player score

  printy("\n[Your roll]")
  time.sleep(0.5)

  randomnumber1 = random.randint(1,6)

  print("_____")
  print(dice[randomnumber1])
  print("_____")
  print(score[randomnumber1])

  printy("\n[Your roll]")
  time.sleep(0.5)

  randomnumber2 = random.randint(1,6)

  print("_____")
  print(dice[randomnumber2])
  print("_____")
  print(score[randomnumber2])

  printy("\n[Your total]")
  time.sleep(0.5)
  
  playerscore += (int(randomnumber1) + int(randomnumber2))
  print(playerscore)


  if (int(randomnumber1) + int(randomnumber2)) == 2:
    print("\n(SNAKEEYES)")
    playerscore=0

  if (int(randomnumber1) == int(randomnumber2)):
    print("\n(DOUBLE)")
    playerscore += (int(randomnumber1) + int(randomnumber2))

  #Computer score
  
  printy("\n[AI roll]")
  time.sleep(0.5)
  
  randomnumber3 = random.randint(1,6)

  print("_____")
  print(dice[randomnumber3])
  print("_____")
  print(score[randomnumber3])

  printy("\n[AI roll]")
  time.sleep(0.5)

  randomnumber4 = random.randint(1,6)

  print("_____")
  print(dice[randomnumber4])
  print("_____")
  print(score[randomnumber4])

  printy("\n[AI total]")
  time.sleep(0.5)

  AIscore += (int(randomnumber3) + int(randomnumber4))
  print(AIscore)

  if (int(randomnumber3) + int(randomnumber4)) == 2:
    print("\n(SNAKEEYES)")
    AIscore=0

  if (int(randomnumber3) == int(randomnumber4)):
    print("\n(DOUBLE)")
    AIscore += (int(randomnumber3) + int(randomnumber4))


  printy("Would you like to roll again?")
  time.sleep(0.5)
  answer = input("Yes(y) or No(n): ")

#if game ends

if answer == "n":
  printy("\n[Your final score is " + str(playerscore) + "]")
  time.sleep(0.5)
  printy("[AI final score is " + str(AIscore) + "]")
  time.sleep(0.5)

  #declares winner

  if playerscore > AIscore:
    print("\n{YOU WIN}")

  if playerscore < AIscore:
    print("\n{YOU LOSE}")

  if playerscore == AIscore:
    print("\n{TIED}")

  if answer == "n":
    printy("\nGame finished.")


