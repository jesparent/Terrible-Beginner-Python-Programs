#Jesse Parent
#8baller


import time
import math
import random 


def hi():   # intro function 

    print "Welcome to Ualbany Magic 8Ball 9000!" #welcoming
    print "Let us begin: your task is to...."
    print ".... focus your mind on a question - one of the answer Yes or No"
    print ''
    print ''
    nu = raw_input("When you are ready: press enter  ") #setting raw in put and int -- although im not sure if should not be classed as an INT now in terms of try /except

    print ''
    print "Let us wait while the wisdom of the UALB Magic 8ball 9000 unfolds..."
    print "... ..... ...." 
    time.sleep(5)
    print "... .... ..... ....... "
    print " "
hi()


def baller():


    shake = random.randint(1,10)  # simulates rolling a six-sided die
  

    if  shake == 1: #start of decision tree; start positve response
        print "The pristine and ultimate wisdom of the Ualbany Magic 8ball 9000 reveals to you this answer: "
        print "--There Can Be No Other End! " #positive - source Skyrim - dremora lord summon; positive bc of the certainty and affirmation - and bc its what the summons says upon victory
        

    elif shake == 2:
        print "The pristine and ultimate wisdom of the Ualbany Magic 8ball 9000 reveals to you this answer: "
        print " -- Your destiny is burdened with this being so - yes" #positive - slight rip off of Loki / avengers

    elif shake == 3:
        print "The pristine and ultimate wisdom of the Ualbany Magic 8ball 9000 reveals to you this answer: "
        print " -- The scouter says Over 9000% chance it will be so - enjoy." #positive VEGETA etc


    elif shake == 4:
        print "The pristine and ultimate wisdom of the Ualbany Magic 8ball 9000 reveals to you this answer: "
        print " -- Only the ones who believe, ever see what they dream, ever dream what comes true" #positive; Color of Roses


    elif shake == 5:
        print "The pristine and ultimate wisdom of the Ualbany Magic 8ball 9000 reveals to you this answer: "
        print " --I'm going to ask you a bunch of questions, and I want to have them answered immediately. First, I would like to just get to know you: Who is your daddy, and what does he do?!?!"
                # Arnold Swarzenegger Prank Call Soundboard/ Kindergarten Cop
                #massively indeterminante response

    elif shake == 6:
        print "The pristine and ultimate wisdom of the Ualbany Magic 8ball 9000 reveals to you this answer: "
        print " --You will receive More Than A Raven Can Hunt For In The Night..."
                #Supremely indeterminante. From "Metal Gear Awesome"
                #You should watch it, here: https://youtu.be/JhXd1dzFxl8?t=4m5s (language warning)


    elif shake == 7:
        print "The pristine and ultimate wisdom of the Ualbany Magic 8ball 9000 reveals to you this answer: "
        print " --This is best responded to by an old Texas saying that goes something like this: Fool me once, shame on .... shame on you.... f-... .well, ... point is you can't get foold again.."
                #indeterminate. Thanks to GWB 


    elif shake == 8:
        print "The pristine and ultimate wisdom of the Ualbany Magic 8ball 9000 reveals to you this answer: "
        print " --That you ask means you are a path of unalterable suffering."
        print "....sorry...."
        time.sleep(3) 
        print "yeah that really sucks man, here is #SadViolin for you:"
        print " https://www.youtube.com/watch?v=_R9gVc9ggZg " 
                #negative response is negative, plus minor level trolling

    elif shake == 9:
        print "The pristine and ultimate wisdom of the Ualbany Magic 8ball 9000 reveals to you this answer: "
        print " --Hwy sometimes you just need to give up."
                #real wisdom negative


    elif shake == 10:
        print "The pristine and ultimate wisdom of the Ualbany Magic 8ball 9000 reveals to you this answer: "
        print " -- Evil is not born, deary, it is made - reconsider this or you will regret it."
                #negative - a la Mr Gold from Once Upon a Time

    else:

        print "Fate has been forever changed by your question. Try again another time."
                #cryptic alternate reality warning 




        

baller()
