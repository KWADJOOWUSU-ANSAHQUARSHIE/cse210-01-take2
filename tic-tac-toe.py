'''Tic-Tac-Toe
By Kwadjo Owusu-Ansah Quarshie
'''


def main():
    player = next_player("")
    system = create_system()
    while not (has_winner(system) or is_a_draw(system)):
        display_system(system)
        make_move(player, system)
        player = next_player(player)
    display_system(system)
    print("\n Hope you had fun. Wow!") 

def create_system():
   system = []
   for square in range(9):
        system.append(square + 1)
   return system

def display_system(system):
    print()
    print(f"{system[0]}|{system[1]}|{system[2]}")
    print('-+-+-')
    print(f"{system[3]}|{system[4]}|{system[5]}")
    print('-+-+-')
    print(f"{system[6]}|{system[7]}|{system[8]}")
    print()
    
def is_a_draw(system):
    for square in range(9):
        if system[square] != "x" and system[square] != "o":
            return False
    return True 
    
def has_winner(system):
    return (system[0] == system[1] == system[2] or
            system[3] == system[4] == system[5] or
            system[6] == system[7] == system[8] or
            system[0] == system[3] == system[6] or
            system[1] == system[4] == system[7] or
            system[2] == system[5] == system[8] or
            system[0] == system[4] == system[8] or
            system[2] == system[4] == system[6])

def make_move(player, system):
    square = int(input(f"\n {player}'s make options from (1-9): "))
    system[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()