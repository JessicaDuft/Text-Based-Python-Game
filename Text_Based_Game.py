
def intro():  #gets users name and allows user to choose to print background info and/or game directions 
        def get_name(): #gets users name
            print ("Hello, what is your name?")
            name=input()
            print ("Hello, ", name, "Welcome to the game! Enjoy!\n")
            
        def background_info(): #allows user to choose to print background information
            print ("Type Y to read game background information. Type N to skip")
            user_background_input=input().upper() #makes input uppercase to match condition
            
            if user_background_input=="Y": #if user selects 'y' print background info
                
                print(
                    'You are stuck inside of a museuem with a group of vicious robbers.\n'
                    'The robbers are after an extremely valuable gemstone that has belonged to your family for centuries.\n'
                    'You must stop the robbers by leaving the office to collect items that you need to trigger the panic button that is located in the storage room (Where the robbers are!). \n '
                    'You must get the following items before making your way to the robbers and pushing the panic button:\n'
                    '*A map of the museum that is located in the training room,\n '
                    '*A sword (to protect yourself with)from the Samurai room,\n'
                    '*A key that is hidden in the mummy exhibit room, \n'
                    '*An energy bar from the break room(to gain enough energy to complete the mission),\n'
                    '*A pen and a piece of paper from the lobby which you will use to write down important information about the criminals,\n'
                    '*and a password that will grant you access to the panic button. \n'
                    'The robbers are hiding out in the storage room putting final touches on their heist.\n'
                    '\nBe sure not to run into them before collecting all 6 items!'
                    '\nAfter collecting all of the items you will make your way to the storage room, unlock the door, enter the password you collected on your way and finally push the panic button to alert police and stop the robbers. ')
                print('------------------------------------------------------------------')
        def game_directions(): #allows user to choose to print game directions
            print("Type Y to read game directions. Type N to skip")
            user_input_directions=input().upper() #makes input uppercase to make condition
            if user_input_directions.upper()=='Y':#if user chooses 'y' print directions
                print("HOW TO PLAY: \n")
                print("*You can navigate the musuem using the following prompts:")
                print("*Go north to travel north")
                print("*Go south to travel south")
                print("*Go east to travel east")
                print("*Go west to travel west")
                print("*NOTE: You  must type Go in front of your direction you can not just type north,south,east or west")
                print("*If you see an item in a room you can retrieve that item by typing get 'item name'")
                print('*You must collect all 6 items and make your way to the storage room to win the game')
                print ("TYPE EXIT TO EXIT GAME AT ANY TIME!")
                
        get_name() #executes get name function
        background_info()#executes background_info function
        game_directions() #executes game_directions function

def main():
    room = 'Office' #current room or start room is 'office'
    inventory = [] #holds items collected in game
    inventory_length = len(inventory) #length of inventory list
    
    rooms = { #dictionary that links rooms and items
        'Office': {'south': 'lobby'},
        'lobby': {'west': 'training room', 'item': 'pen and paper'},
        'training room': {'east': 'lobby', 'south': 'break room', 'west': 'storage room', 'north': 'samurai exhibit',
                          'item': 'map'},
        'break room': {'north': 'training room', 'east': 'viking exhibit', 'item': 'energy bar'},
        'viking exhibit': {'west': 'break room', 'item': 'password(118SBD)'},
        'storage room': {'east': 'training room', 'item': 'robbers'},
        'samurai exhibit': {'south': 'training room', 'east': 'mummy exhibit', 'item': 'sword'},
        'mummy exhibit': {'west': 'samurai exhibit', 'item': 'key'}
    }
    
    print ('----------------------------------------') #for visual aspect
    print ("LETS GET STARTED! GOOD LUCK!")
    print("You are in the office!")
    print("Inventory: empty", ) #inventory starts off empty
    print("What's your next move?") #prompts user input
    print('------------------------')
    move = input().lower() #user inputs command
    print("-------------------------")
    
    while room != 'storage room': #while not in storage room or 'end' room execute gameloop
        
        if (move.lower()=='exit'): #if user types 'exit', game ends and loop breaks
            print ("EXITING GAME NOW! COME BACK SOON!") #prints exit message
            break
        while move=='show stats': #if user enters 'show stats', current room and inventory is printed
            print("You are  in the", room, "!") #prints current room
            print("Current Inventory: ", inventory) #prints current inventory
            print("What's your next move?") #prompts user input
            print("----------------------") #prints visual break
            move=input().lower() #gets user input
            
        while room=='Office'and (move.split(' ')[0].lower()=='get'): #if user trys to get inventory item from start room "no items available" prints
            print ("No items available yet!") #prints no available items
            print("You are  in the", room, "!") #prints current room
            print("Current Inventory: ", inventory) #prints inventory list
            print("What's your next move?") #prompts user input
            print("----------------------") #prints visual break 
            move=input().lower() #gets user input



            
        while len(move.split(" "))<2 or move.split(' ')[0]!='get' and move.split(' ')[0]!='go' and move.split(' ')[0]!='exit': #if user input does not start with 'go', 'get'or 'exit' or is only one word long (ex:north instead of go north) error message prints
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") #prints visual break
            print ("ERROR! Please check your prompt and retry using:\n""Go south, Go east, Go north, Go west or get 'item name'") #prints valid commands
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") #prints visual break
            print("You are  in the", room, "!") #prints current room
            print("Current Inventory: ", inventory)#prints current inventory
            print("What's your next move?") #prompts user input
            print("----------------------") #prints visual break
            move=input().lower() #gets user input
            
            

            
            
            
        while not move.split(" ")[1] in rooms[room] and move.split(" ")[0] == 'go': #if user enters an invalid direction the game prints a prompt to enter a new direction
            if (room!= 'Office'):
                print("Can't go that direction!") #prints error message
                print("You are  in the", room, "!") #prints current room
                print("You see a ", items) #prints items in room
                print("Current Inventory: ", inventory) #prints current inventory
                print("What's your next move?") #prompts user input
                print("----------------------") #prints visual break
                move = input().lower() #gets user input
                print("-------------------------")#prints visual break
            if (room=='Office'):
                print("Can't go that direction!") #prints error message
                print("You are  in the", room, "!") #prints current room
                print("What's your next move?") #prompts user input
                print("----------------------") #prints visual break
                move = input().lower() #gets user input
                print("-------------------------")#prints visual break
    
        while move.split(" ")[1] in rooms[room] and move.split(" ")[0] == 'go' : #if user enters a valid direction loop executes
            new_room = rooms[room][move.split(" ")[1]] #variable to hold new room
            items = rooms[new_room]['item'] #variable to hold items in room
            room = new_room #assigns current room with new room 
      	       
            if (new_room == 'storage room') and inventory_length != 6:#if user enters storage room before collecting all 6 items game ends and loop breaks
                print("YOU HAVE BEEN CAUGHT BY THE ROBBERS! GAME OVER!") #prints game over message
                break #ends game, breaks loop
            
            if (new_room == 'storage room') and inventory_length == 6: #If user has all 6 items and enters storage room loop executes
                print("YOU HAVE MADE IT INTO THE STORAGE ROOM! YOU HAVE ALL ITEMS YOU NEED!") #prints game status message
                print("Inventory: ", inventory) #prints current inventory
                print ("Would you like to use the key to unlock the storage room? YES OR NO?") #prompts user to decide to unlock door with a key
                use_key=input().upper() #gets user input 
                
                if use_key=='NO': #if user chooses not to unlock storage room door with key, user is prompted to quickly enter the password they found in the game.
                    print ("THE ROBBERS HAVE OPENED THE DOOR! YOU MUST STAY HIDDEN AND ACT QUICKLY") #prints game status message
                    print("ENTER THE PASSWORD YOU COLLECTED IN THE VIKING EXHIBIT!") #prompts user to enter password found in game. password can be seen on inventory list
                    password=input().upper() #gets user input
                    password_hardcopy='118SBD' #variable to hold value of password
                    
                    if password==password_hardcopy: #if user enters the correct password game prompts user to choose to push panic button or not
                        print ("WOULD YOU LIKE TO PUSH THE PANIC BUTTON? YES OR NO") #prompts user to decide to push panic button or not
                        panic_button=input().upper() #gets user input
                        
                        if panic_button=="YES": #if user selects 'yes', panic button is triggered and game is won and loop breaks
                            print("YOU DEFEATED THE ROBBERS! CONGRATULATIONS! YOU WIN!!") #prints winning message
                            break #ends game, breaks loop
                    if password!=password_hardcopy: #if user enters the wrong password, game ends and loop breaks
                        print ("PASSWORD INCORRECT!!") #prints incorrect password message
                        print ("YOU HAVE BEEN CAUGHT BY THE ROBBERS! GAME OVER!") #prints game over message
                        break #ends game, breaks loop
                if use_key=='YES': #if user chooses to use key to unlock door game prints prompt to enter password found in the game
                    print("YOU UNLOCKED THE DOOR!") #prints game status message
                    print("ENTER THE PASSWORD YOU COLLECTED IN THE VIKING EXHIBIT!") #prompts user to enter password found in game
                    password=input().upper() #gets user input
                    password_hardcopy='118SBD' #variable to hold value of password found in game
                    
                    if password==password_hardcopy: #if user enters the correct password they are prompted to coose to push the panic button
                        print ("WOULD YOU LIKE TO PUSH THE PANIC BUTTON? YES OR NO") #prompts user to choose to push panic button
                        panic_button=input().upper() #gets user input
                        
                        if panic_button=="YES": #if user chooses to push panic button game prints winning message and loop breaks
                            print("YOU DEFEATED THE ROBBERS! CONGRATULATIONS! YOU WIN!!") #winning message
                            break #ends game, breaks loop
                        
                    if password!=password_hardcopy: #if password is not correct game ends and loop breaks
                        print("OH NO! WRONG PASSWORD!") #prints wrong password
                        print ("YOU HAVE BEEN CAUGHT BY THE ROBBERS! GAME OVER!") #prints game over message
                        break #ends game, breaks loop
                    
            #if user is not in the storage room and all entries are valid current stats are printed:    
            print("You are now in the", new_room, "!") #prints current room
            print("You see a ", items) #prints items in room
            print("Current Inventory: ", inventory) #prints current inventory
            print("What's your next move?") #prompts user input
            print("-------------------------") #prints visual break
            move = input().lower()#gets user input
            print("-------------------------") #prints visual break
    
            while not move.split(" ")[1] in items and move.split(' ')[0] == 'get': #if user input does not exist as item in room, game prints error message and prompts new input until input is valid
                print("Can't", move) #prints error message
                print("You are  in the", new_room, "!") #prints current room
                print("You see a ", items) #prints items in room
                print("Current Inventory: ", inventory) #prints current inventory
                print("What's your next move?")#prompts user input
                print("-------------------------") #prints visual break
                move = input().lower() #gets user input
                print("-------------------------") #prints visual break
    
            while move.split(" ")[1] in items and move.split(' ')[0] == 'get': #if user input exist as an item in the room ; item is either stored in inventory or an error message prints for a duplicate item. 
               
                if items in inventory: #if item in room already is in inventory error message prints
                    print("Item already exist in inventory!") #prints error message
                    print("You are  in the", new_room, "!") #prints current room
                    print("You see a ", items) #prints items in room
                    print("Current Inventory: ", inventory) #prints current inventory
                    print("What's your next move? ") #prompts user input
                    print("-------------------------") #prints visual break
                    move = input().lower() #gets user input
                    print("-------------------------") #prints visual break
                    
                if not items in inventory: #if item does not already exist in inventory
                    inventory.append(items) #add item to inventory
                    print("New item added to inventory!") #prints game status
                    print("You are  in the", new_room, "!") #prints current room
                    print("You see a ", items) #prints item in room
                    print("New Inventory: ", inventory) #prints new inventory list
                    inventory_length += 1 #adds 1 to inventory length each time a new item is added
                    print("What's your next move? ") #prompts user input
                    print("-------------------------") #prints visual break
                    move = input().lower() #gets user input
                    print("-------------------------") #prints visual break
                    
                while not move.split(" ")[1] in items and move.split(' ')[0] == 'get': #if user input first matched an item in the room and then user input was invalid; game prints error message and prompts new input
                    print("Can't", move) #prints error message
                    print("You are in the", new_room, "!") #prints current room
                    print("Inventory: ", inventory) #prints current inventory
                    print("What's your next move?") #prompts user input
                    print("-------------------------") #prints visual break
                    move = input().lower() #gets user input
                    print("-------------------------") #prints visual break


intro()
main()
