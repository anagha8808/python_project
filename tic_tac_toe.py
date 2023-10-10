import random
box=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
computer='O'
user='X'

# Display the game layout

def display_box(box):  
    print(f'{box[1]} | {box[2]} | {box[3]}')
    print('..........')
    print(f'{box[4]} | {box[5]} | {box[6]}')
    print('..........')
    print(f'{box[7]} | {box[8]} | {box[9]}')
    print('           ')
display_box(box)                                      
    

# Check if there is a win conditions in the game

def check_win():
    if box[1]==box[2]==box[3] and box[1]!=' ':
        return True
    elif box[4]==box[5]==box[6] and box[4]!=' ':
        return True
    elif box[7]==box[8]==box[9] and box[7]!=' ':
        return True
    elif box[1]==box[4]==box[7] and box[1]!=' ':
        return True
    elif box[2]==box[5]==box[8] and box[2]!=' ':
        return True
    elif box[3]==box[6]==box[9] and box[3]!=' ':
        return True
    else:
        return False
    
# Check if the game board is full

def box_blank():
    if box.count(' ') < 1:
        return True
    else:
        return False

# Check if a given position on the game board is available

def avialable_position(position):
    if box[position]==' ':
        return True
    else:
        False

# Insert a letter X or O into a specified position

def insert(letter,position):
    if avialable_position(position):
        box[position] = letter
        display_box(box)
        if check_win():
            if letter=='O':
                print("computer wins")
                exit()
            else:
                print("congrats to you! you're the winner")
                exit()
        if box_blank():
            print('Draw')
            exit()
    else:
        if letter == 'X':
            position = int(input("not free! please re-enter your position"))
        else:
            position = random.randint(1,9)
            insert(letter,position)

        
            
# Allow the user to make a move

def user_moves(letter):
    position = int(input("Please Enter the position to insert!"))
    insert(letter,position)

# Allow the computer to make a move (randomly)

def computer_moves(letter):
    position = random.randint(1,9)
    insert(letter,position)


#main loop
while not check_win():
    user_moves(user)
    computer_moves(computer)
    