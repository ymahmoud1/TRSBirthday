def welcomemessage() -> str:
    message  = "Hi 7bbti. Happy 18th birthday my lovely, sweet, intelligent, charming, beautiful, young woman. " \
               "I debated long and hard on what to do for your special 18th birthday and I've come to the consensus of " \
               "sending you multiple gifts because I love you and I can't only send one gift to the person I love the most in my life which is you. " \
               "So, for one of your gifts, I've decided to make you your special own website with many different features that " \
               "I hope you will enjoy exploring. Here is a brief of summary of all the different features on this website: ... " \
               "That's all for now baby, I wish I could be with you on your special day, celebrating you, but trust me I will only " \
               "be thinking of how grateful I am of you for the whole duration of my journey back to the USA and for all the motnhs " \
               "I will be spending there until I can be blessed by being near your presence again in the summer. I love you, appreciate you, " \
               "and I am proud of all that you have achieved in the 18 years you've lived so far my little bug my little bug, happy birthday :)"
    return message

def pickacategorymessage() -> str:
    message = "Pick a category!\n1. Messages from loved ones\n2.Love Languages\n3.Attention Button"

    return message
def lovelanguagesmessage() -> str:
    message = "Which type of love would you like to recieve today?\n1.Act of Service\n2.Quality Time" \
              "\n3.Gifts\n4.Physical Touch\n5.Words of Affirmation"
    return message

def picklovelanguage(X:int):
    if X == 1:

    elif X==2:

    elif X==3:

    elif X==4:

    else:

def category(X: int):
    if X == 1:
        print("Love letter")

    elif X == 2:
        lovelanguagesmessage()



    else:






if __name__ == "__main__":