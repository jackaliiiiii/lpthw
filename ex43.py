#!/usr/bin/env Python
#Test for Windows Git GUI

from sys import exit
from random import randint


saved_scene_name = 'initial value'
class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):
    """This class is used as the controller which can control tho whole game running"""

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        global saved_scene_name
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        #add end scene begin
        end_scene = self.scene_map.next_scene('ended')
        #add end scene end
        saved_scene_name = self.scene_map.scene_name = "central_corridor"
        #current_scene = last_scene
        print "\fWho are you?"
        c = ''
        c = raw_input('> ')
        if c == "felix":
            print "Yes my Majesty, you can do anthing you like:(Start from any scene directly)"
            current_scene = self.scene_map.select_scene()
        else:
            print "Welcom to the fancy world, %s!" %c
            raw_input('...')
        while current_scene != end_scene:
            next_scene_name = current_scene.enter()
            saved_scene_name = self.scene_map.scene_name#Save the game for selection
            if current_scene == last_scene:
                print '*' * 20
                print "Now you've completed the mission, would you like to play again?(yes or no)"
                choose = ''
                choose = raw_input('> ')
                if choose in 'Yyes':
                    current_scene = self.scene_map.select_scene()
                else:
                    print "You chose NO, so finished the game"
                    current_scene = self.scene_map.next_scene(next_scene_name)
            else:
                current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene(end scene)
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would b proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        global saved_scene_name
        print Death.quips[randint(0, len(self.quips)-1)]+'\n'
        print '*' * 40
        restart = raw_input("Do you want to restart the game?(yes or no)\n>")
        if restart in "yesY":
            print "OK, let's make it this time!\n"
            print '*' * 40
            return saved_scene_name
        else:
            print "You lost in the void of infinite universe."
            print "God bless you, hope we can find you. Bye."
            print '*' * 10 + "The End" + '*' * 10 + '\n'
            raw_input("...")
            return 'ended'


class CentralCorridor(Scene):

    def enter(self):
        print '\f'
        print '\n' + '\n'
        print '*' * 10 + "The Gothons of Planet Percal" + '*' * 10 + '\n'
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "you entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapon Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        raw_input('...')
        print "\n"
        print "Chapter 1 CentralCorridor", '*'*30
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."
        print '*' * 20
        print "What would you do? Shoot, Dodge or Do something funny?"
        action = raw_input("> ")
        print '*' * 20
        if action in "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim. Your laser hits his costume but misses him entirely. This"
            print " completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the face until"
            print "you are dead. Then he eats you."
            return 'death'

        elif action == "dodge":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "you wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "dance" or "fight":
            print "You just simplely start to dance like a joker and lose your weapon on the"
            print "floor by accident. The Gothon's watches your weapon droped and thinks you are"
            print "taunting them. Like an elephant stepping on an aunt you are just be crushed under"
            print "the huge body of the Gothon and grinded into surface. You're a died piece of paper"
            return 'death'

        elif action in "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfrm, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            raw_input("...")
            return 'laser_weapon_armory'

        else:
            print "DOES NOT MAKE ANY SENSE!"
            raw_input('...')
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print '\f'
        print "Chapter 2 Laser Weapon Armory", '*'*30
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet."
        print "You standup and run to the far side of the room and find the"
        print "neutron bomb in its container. There's a keypad lock on the box"
        print "and you need the code the get the bomb out. If you get the code"
        print "wrong 5 times and the lock closes forever and you can't"
        print "get the bomb. The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print '*' * 20
        print "What's the 3 digits number is?"
        guess = raw_input("[keypad]> ")
        print '*' * 20
        guesses = 0

        while guess != code and guesses < 5:
            if guesses < 2:
                print "BZZZZEDDD!"
            else:
                print "BZZZZZZEDDDDDDD!!!"
            guesses += 1
            if guesses >= 4:
                print "Whoa, here come a ligth shows some kind of tip:"
                print "The sum of the code is %d" %(int(code[0] + code[1] + code[2]))
            else:
                pass
            guess = raw_input("[keypad]> ")

            if guess == code:
                print "The container clicks open and the seal breaks letting gas out."
                print "You grab the neutron bomob and run as fast as you can to the"
                print "bridge where you must put it in the right spot."
                raw_input("...")
                return 'the_bridge'
            else:
                continue
        print "The lock buzzes one last time and then you hear a sickening"
        print "melting sound as the mechanism is fused together."
        print "You decide to sit here, and finally the Gothons blow up the"
        print "ship from their ship and you die."
        raw_input("...")
        return 'death'


class TheBridge(Scene):

    def enter(self):
        print '\f'
        print "Chapter 3 The Bridge", '*'*30
        print "You burst on to the bridge with the neutron destruct bomb"
        print "under your arm and surprises 5 Gothons who are trying to"
        print "take control of the ship. Each of them even has a uglier"
        print "clown costume than the last. They havn't put their"
        print "weapons out yet, as they say the active bomb under your"
        print "arm and don't want to set it off."

        print '*' * 20
        print "What would you do: throw the bomb or place the bomb?"
        action = raw_input("> ")
        print '*' * 20
        if action in "throw":
            print "In a panic you throw the bomb through a group of Gothons"
            print "and make a leap for the door. Right as you drop it a"
            print "Gothon shoots you right in the back and killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            raw_input("...")
            return 'death'

        elif action in "slowly place":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "put the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock and the Gothons can't get out."
            print "Now the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            raw_input("...")
            return 'escape_pod'

        else:
            print "DOES NOT MAKE ANY SENSE!"
            raw_input('...')
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print '\f'
        print "Chapter 4 The Escape Pod" ,'*' * 30
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes. It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escap pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you don't have time to look. There's 5 pods, which one"
        print "do you take?"
        good_pod = randint(1,5)
        print "*****" + "  " + "*****" + "  " + "*****" + "  " + "*****" + "  " + "*****"
        print "* 1 *" + "  " + "* 2 *" + "  " + "* 3 *" + "  " + "* 4 *" + "  " + "* 5 *"
        str = ['*'] * 5
        str [good_pod-1] = '#'
        str = ''.join(str) # list convert to string
        print str + "  " + str + "  " + str + "  " + str + "  " + str
        print '*' * 20
        guess = raw_input("[pod #]> ")
        print '*' * 20
        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            raw_input("...")
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." %guess
            print "The pod easily slides out into the space heading to"
            print "the planet below. As it flies into the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon's ship at the "
            print "same time. You won!"
            raw_input()
            return 'finished'

class Finished(Scene):

    def enter(self):
        print '\f'
        print '\n'
        print "The finished Chapter: Congratulations!", '*' * 30
        print "You won! Good job."
        print "Please dial 2742 8363 for a reward"
        #add end scene begin
        raw_input("...")
        #add end scene end
        return 'ended'

#Add end scene begin
class Ended(Scene):
    def enter(self):
        print '\f'
        print '\n'
        print '*' * 50
        print ' ' * 20 + "Game Over"
        print '*' * 50
        print '\n' * 10
        exit(1)
#Add end scene end

class Map(object):
    """This class is used as the scene(state) selection. It tells the game
        system that which scene now should be selected"""
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
        #Add end scene begin
        'ended': Ended(),
        #Add end scene end
    }
    #Add end scene begin
    scenes_list = ['central_corridor', 'laser_weapon_armory',
        'the_bridge', 'escape_pod', 'finished']


    def __init__(self, start_scene):
        self.scene_name = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        self.scene_name = scene_name
        return val

    def opening_scene(self):
        return self.next_scene(self.scene_name)

    #add end scene begin
    def select_scene(self):
        print '*' * 20
        print "Now you can choose one scene to start again!"
        select_name = 'no_selected'
        for i, select_name in enumerate(Map.scenes_list):
            print i+1, select_name
           # if i <= len(Map.scenes) - 2:# Don't show the end scene
            #    print (i+1), '. ', Map.scenes.keys()[i]

        number = ''
        while not number.isdigit() or int(number) > len(Map.scenes_list):
            print "Choose your scene by input the number front:"
            number = raw_input('> ')
        select_name = Map.scenes_list[int(number) - 1]
        print "You've chosen the scene: ", select_name
        return self.next_scene(select_name)

    #add end scene end

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
