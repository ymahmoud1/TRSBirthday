import streamlit as st

def welcomemessage() -> str:
    message  = " Hi 7bbti. Happy 18th birthday my lovely, sweet, intelligent, charming, beautiful, young woman.\n " \
               "I debated long and hard on what to do for your special 18th birthday and I've come to the consensus of\n " \
               "sending you multiple gifts because I love you and I can't only send one gift to the person I love the most in my life which is you.\n " \
               "So, for one of your gifts, I've decided to make you your special own website with many different features that\n " \
               "I hope you will enjoy exploring. Here is a brief of summary of all the different features on this website: ...\n " \
               "That's all for now baby, I wish I could be with you on your special day, celebrating you, but trust me I will only\n " \
               "be thinking of how grateful I am of you for the whole duration of my journey back to the USA and for all the motnhs\n " \
               "I will be spending there until I can be blessed by being near your presence again in the summer. I love you, appreciate you,\n " \
               "and I am proud of all that you have achieved in the 18 years you've lived so far my little bug my little bug, happy birthday :)\n"
    return message

def pickacategorymessage() -> str:
    message = "Pick a category!\n1. Messages from loved ones\n2.Love Languages\n3.Attention Button"

    return print(message)
def lovelanguagesmessage() -> str:
    message = "Which type of love would you like to recieve today?\n1.Act of Service\n2.Quality Time" \
              "\n3.Gifts\n4.Physical Touch\n5.Words of Affirmation"
    return print(message)

def picklovelanguage(X:str):
    if X == "Act of Service":
        return "Act of Service picked!"
    elif X== "Quality Time":
        return "Quality Time picked!"
    elif X== "Gifts":
        return "Gifts picked!"
    elif X=="Physical Touch":
        return "Physical Touch picked!"
    else:
        return "Words of Affirmation picked!"

def category(X: int):
    if X == 1:
        return print("Love letter")

    elif X == 2:
        lovelanguagesmessage()
        A = int(input())

        return picklovelanguage(A)

    else:
        return print("Work in Progress")


if __name__ == "__main__":
    # app setup
    st.set_page_config(layout="wide")
    st.sidebar.title("My Baby's 18th Birthday <3")
    navigation = st.sidebar.selectbox("Navigate",
                                      ("Home", "Love Letters", "Love Languages",
                                       "Attention Button"))
    st.sidebar.markdown("Daily Reminder: I LOVE YOU ❤️❤️❤️️")

    #Home page
    if navigation == "Home":
        st.title("Happy 18th Birthday My Little Bug")
        st.markdown(welcomemessage())

    #Love Letters
    elif navigation == "Love Letters":
        st.title("Letters From Your Loved Ones")

    #LoveLanguages
    elif navigation == "Love Languages":
        st.title("What Type of Love Do you Want Right Now?")
        language = st.selectbox("Pick whichever you want and I will provide :)",
                     ["Act of Service","Quality Time","Gifts","Physical Touch","Words of Affirmation"])
        st.markdown(picklovelanguage(language))

