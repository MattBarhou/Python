print(r'''***********************************************
                _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-' 
***********************************************        
''')
print("Welcome to Treasure Island, your mission is to find the treasure.")
leftorright = input("Your at a cross road. Where do you want to go? Type 'left' or 'right' ").lower()

if leftorright != "left":
    print("You fell into a hole. Game Over.")
else: 
   swimorwait = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
   if swimorwait != "wait":
    print("You were attacked by trout. Game Over.")
   else: 
      color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n").lower()
      if color == "red":
        print("You were burned by fire. Game Over.")
      elif color == "blue":
        print("You were eaten by beasts. Game Over.")
      elif color == "yellow":
        print("You Win!")
      else:
          print("Game Over.")
   
