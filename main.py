from play import Game, HUMAN, ALPHABETA,PLAYER1, PLAYER2

print("choose Difficulity :\n1-EASY\n2-AMATURE\n3-WORLDCLASS\n")
Difficulity = int(input())

print("choose desired mode: \n1-with stealing\n2-without stealing")
mode=int(input())

if(mode == 1):
   mode = True
else:
   mode = False

print("which player to start ? \n")
print("1-Human\n2-Computer\n")
player = int(input())

game = Game()

if(player==1):
   player = PLAYER1
   game.start(HUMAN, ALPHABETA,player,Difficulity,mode)

if(player==2):
   player = PLAYER2
   game.start(ALPHABETA,HUMAN,player,Difficulity,mode)