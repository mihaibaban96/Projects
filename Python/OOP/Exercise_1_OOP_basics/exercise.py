######################################### OOP IN PYTHON##############################
################################# ENCAPSULATION AND INHERITENCE######################
####################################################################################

class Player:
    '''
    Parent class.
    It has only one method: log_in()
    Every player needs to be logged in, in order for him to be able to 
    choose a character.
    '''

    def log_in(self):
        print('You have been logged in!')
        print('\n')


class Archer(Player):
    def __init__(self, name, age, life_points, attack_power, number_of_arrows):
        self.name = name
        self.age = age
        self.life_points = life_points
        self.attack_power = attack_power
        self.number_of_arrows = number_of_arrows

    def attack(self):
        print(f'''
                                                        
                                                         \.
                                                         /|.
                                                       /  `|.
                                                     /     |.
                                                   /       |.
                                                 /         `|.
                                               /            |.
                                             /              |.
                                           /                |.
      __                                 /                  `|.
       -\                              /                     |.
         ||                          /                       |.
           |\                      /                         |.
            \|                   /                           |
              \#####\          /                             ||
          ==###########>     /                               ||
           \##==      \    /                                 ||
      ______ =       =|__/___                                ||
  ,--' ,----`-,__ ___/'  --,-`-==============================##==========>
 \               '        ##_______ ______   ______,--,____,=##,__
  `,    __==    ___,-,__,--'#'  ==='      `-'              | ##,-/
    `-,____,---'       \####\              |        ____,--\_##,/
        #_              |##   \  _____,---==,__,---'         ##
         #              ]===--==\                            ||
         #,             ]         \                          ||
          #_            |           \                        ||
           ##_       __/'             \                      ||
            ####='     |                \                    |/
             ###       |                  \                  |.
             ##       _'                    \                |.
            ###=======]                       \              |.
           ///        |                         \           ,|.
           //         |                           \         |.
                                                    \      ,|.
                                                      \    |.
                                                        \  |.
                                                          \|.
                                                          /.
                                                         |



        You've been attacked with the mighty arrows of the archer!
        attack power: {self.attack_power}
        Arrows lost:3''')
        self.number_of_arrows -= 3
        print("\n")

    def recharge(self):
        print("Recharge Activated! \n  Recharged with: 3 Arrows")
        self.number_of_arrows += 3
        print(f"Remaining arrows: {self.number_of_arrows}")


class Wizard(Player):
    def __init__(self, name, age, life_points, attack_power, magic_spell_name, number_of_magic_bottles):
        self.name = name
        self.age = age
        self.life_points = life_points
        self.attack_power = attack_power
        self.magic_spell_name = magic_spell_name
        self.number_of_magic_bottles = number_of_magic_bottles

    def attack(self):
        print(f'''
   
  .||,       /_ _| |    
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \    ,-'|"/,'`.   
   ||     ,'   `,,. `.  
   ,|____,' , ,;' \| |  
  (3|\    _/|/'   _| |  
   ||/,-''  | >-'' _,||  
   ||'      ==\ ,-'  ,' 
   ||       |  V \ ,|   
   ||       |    |` |   
   ||       |    |   \  
   ||       |    \    \ 
   ||       |     |    |
   ||       |      \_,-'
   ||       |___,,--")_|
   ||         |_|   ccc/
   ||        ccc/       
   ||                


    You've been attacked !
    Wizard {self.name} used magic spell {self.magic_spell_name} with the attack power of {self.attack_power} points!
    

    ''')
        self.number_of_magic_bottles -= 1
        print(
            f' One magic bottle lost. Number of active magic bottles: {self.number_of_magic_bottles}')
        print('\n')

    def recharge(self):
        self.number_of_magic_bottles += 1
        print(
            f'Magic bottles recharged by 1. \n Number of active magic bottles: {self.number_of_magic_bottles}')


class Knight(Player):
    def __init__(self, name, age, life_points, attack_power, number_of_swords):
        self.name = name
        self.age = age
        self.life_points = life_points
        self.attack_power = attack_power
        self.number_of_swords = number_of_swords

    def attack(self):
        print(f'''
  | |
  |.|
  |.|
  |:|      __
,_|:|_,   /  )
  (Oo    / _I_
   +\ \  || __|
      \ \||___|
        \ /.:.\-|
         |.:. /-----|
         |___|::oOo::|
         /   |:<_T_>:|
        |_____\ ::: /
         | |  \ \:/
         | |   | |
         \ /   | \___
         / |   \_____|
         `-'
        ''')

        print(
            f"You've been attacked  with the sword by the knight! Attack power: {self.attack_power} \n")
        self.number_of_swords -= 1
        print(
            f"Swords lost: 1. Current number of swords {self.number_of_swords}")
        print('\n')

    def recharge(self):
        self.number_of_swords += 2
        print(
            f"You have recharged by +2 swords. \n Current number of swords: {self.number_of_swords}")


archer1 = Archer('Robin', 300, 1000, 500, 100)
wizard1 = Wizard('Merlin', 18, 500, 300, 'Arthurian magic spell', 10)
knight1 = Knight('Arthur',  23, 800, 300, 10)
archer1.log_in()
wizard1.log_in()
knight1.log_in()
archer1.attack()
archer1.recharge()
wizard1.attack()
wizard1.recharge()
knight1.attack()
knight1.recharge()
