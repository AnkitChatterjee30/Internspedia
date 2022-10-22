print("\t\tWelcome to the Adventure Game")
print("It is a treasure hunt game where you need to choose the correct path to get the reward.")
one=input("You have two ways.Choose one between left and right :")
if one.lower()=='left':
    two=input("You now reached a river. Will you swim or use a boat :")
    if two.lower()=='swim':
        print('Unfortunately, you were eaten up by crocodiles.')
    elif two.lower()=='boat':
        print("You reached a man.He gives you 4 pills-red,yellow,blue,green.")
        three=input("You are asked to eat one of the pills, you choose :")
        if three.lower()=='red':
            print('You died of poison.')
        elif three.lower()=='green':
            print('You gain a lot of energy and become powerful.')
            four=input("You keep moving and find a forest.\nThere are 4 weapons in the forest-sword,gun,bomb,knife. Choose one of them: ")
            if four.lower()=='sword':
                print("You chop your own arm unfortunately and die.")
            elif four.lower()=='gun':
                print("You take the gun and keep moving. A dragon approaches you.\nYou have only one bullet in your gun.")
                five=input("Will you hit the dragon on-head, neck,chest,arms: ")
                if five.lower()=='head':
                    print("Dragon was wearing a helmet, it blows fire at you and you die.")
                elif five.lower()=='neck':
                    print("The dragon dies. You keep moving. You are thirsty, you find a man offering water.")
                    six=input("He has a bottle, a mug , a bucket and a glass. Choose any one :")
                    if six.lower()=='bottle':
                        print("The water in the bottle was very poisonous and you die.")
                    elif six.lower()=='mug':
                        print("The water in the mug was muddy, your throat gets chocked and you die.")
                    elif six.lower()=='glass':
                        print("The glass was broken, you cut your fingers and start bleeding and you die.")
                    elif six.lower()=='bucket':
                        print("You have quenched your thirst successfully and you keep moving.")
                        seven=input("You finally find a key and 4 treasure boxes.Choose between 1,2,3,4 :")
                        if seven.lower()=='1':
                            print("The key doesn't work, you become frustrated and commit suicide.")
                        elif seven.lower()=='2':
                            print("The key successfully opens the box, but there was a corpse.You get scared and die.")
                        elif seven.lower()=='3':
                            print("The key successfully opens the treasure box.")
                            print("Congratulations! you have finally won the entire game and get a reward of $10000000.")
                        elif seven.lower()=='4':
                            print("The treasure box doesn't open, so you fire at it and the bullet strikes back at your head and you die.")
                        else:
                            print('Not a valid option. You lost.')  
                elif five.lower()=='chest':
                    print("The dragon was wearing a bullet-proof jacket,  it blows fire at you and you die.")
                elif five.lower()=='arms':
                    print("The dragon had extra arms,  it blows fire at you and you die.")
                else:
                    print('Not a valid option. You lost.')    
            elif four.lower()=='bomb':
                print("The bomb blasts and you're brutally killed.")
            elif four.lower()=='knife':
                print("You chop off your fingers unfortunately.")
        elif three.lower()=='yellow':
            print("You lose all your energy in a moment and die.")
        elif three.lower()=='blue':
            print("You become unconscious.")
        else:
            print('Not a valid option. You lost.')
    else:
        print('Not a valid option. You lost.')
elif one.lower()=='right':
    print("You walked for 2 miles, didn't find anything and died.")
else:
    print('Not a valid option. You lost.')