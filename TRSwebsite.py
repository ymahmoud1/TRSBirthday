import random

import streamlit as st
from PIL import Image
import base64
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
        st.markdown("**Acts of Service picked!**")
        st.markdown("Acts of service along with physical touch are probably the two hardest love languages to show through long distance, but ones that I enjoy giving you the most of.  \n"
                    "I want to do anything possible to make your life easier, whether it is to put your socks on, tie your shoe laces for you, give you a massage for your neck, right shoulder and back after sa long day, etc.  \n"
                    "I wish I could be there to provide you any sort of service to alleviate your stress, make you feel more at home, and just reset you back to factory settings of comfort.  \n"
                    "However, I have brainstormed a few ways that I will be making sure that I am doing the utmost I can in helping you out/removing things from your plate galbi.  \nHere are a few:  \n"
                    "1. Help you out with any math related, statistical related, or logical related problem you might have and are looking for solutions to.  \n"
                    "2. Instead of providing solutions to problems, if you just want me to listen, I can do that instead too  \n"
                    "3. Helping you stick to a schedule, remind you of things you have going on, deadlines, and more.  \n"
                    "4. Surprise you with some of your favorite foods/snacks after a long day (I know where you live, not in a creepy way).  \n"
                    "5. Bi-Weekly spotify playlist of a compilation of songs that remind me of you and my love for you.  \n"
                    "6. Hour long monologue about how special you are, and how much of an amazing person and girlfriend you are, and how grateful I am for you (Hour is not enough).  \n"
                    "7. More that I won't tell you and instead surprise you with.")
        st.markdown("I've listed these things, so that you have some quick ideas if you are craving or feeling an acts of service love language day.")
        return ""
    elif X== "Quality Time":
        st.markdown("**Quality Time picked!**")
        st.markdown("For Quality Time, I thought its about time we make a shared calendar!"
                    " This should hopefully help ease the time complexities of being in a 9 hour time difference long distance relationship.\n"
                    "My class times, work schedule, and other responsibilities are all already on there, so please go ahead and add your class times, counseling appointments, therapy, etc.\n"
                    "This calendar is also for you to request stricter tala times, days in advance, so that I make sure to have no obligations in that time slot.\n"
                    "For example, if you want us to watch a certain movie or a show soon, just add an event and I'll be notified of it!\n"
                    "I would also recommend downloading the Google Calendar App on your phone to always have our schedule on you.\n "
                    "Anyways, that's enough talking from me, I hope you enjoy!")
        col1, col2 = st.columns([1,1])
        with col1:
            st.subheader("Steps to make an event:")
            st.markdown(" 1. Click on the button labelled 'Our Calendar'.  \n2. Log-in with your google account, and then click on the 'Create' tab and then on event.")
            image1 = Image.open('./Images/step2.jpg')
            st.image(image1)
            st.markdown("3. Add a title for the event. Then pick a time and date.  \nIf you want the event to be a daily/weekly/bi-weekly thing, then click on the time slot and make it repeatable!")
            st.markdown("4. Add a description if you wanna be cute.")
            image2 = Image.open('./Images/step3.jpg')
            st.image(image2)
            st.markdown("5. Make sure it says 'Our Calendar' and not any other calendar at the bottom! If it does just click on it and switch it.")
            image3 = Image.open("./Images/step4.jpg")
            st.image(image3)
            st.markdown("6. Click save and boom event created!")
        with col2:
            st.markdown("**Click on the button below to redirect you to our calendar:**")
            st.link_button("Our Calendar", "https://calendar.google.com/calendar/u/1?cid=NmMzZDc1OGExMWZjODVhZjVmN2QyMDlkNzdhODBlYWRlMmM1YTkzMzA4NzdiYmFkMTVhY2NhYzQ0OTU0YWU1ZEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t")
        return ""
    elif X== "Gifts":
        st.markdown("**Gifts Picked!**")
        file_ = open("./Images/catgift.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="">',
            unsafe_allow_html=True,
        )
        st.markdown("^this you hehe")
        st.markdown("**Click on the link below to redirect you to a special page**")
        st.link_button("Gift Giving", "https://forms.gle/4iHQvV8KqS5Nyoj17")
        return ""
    elif X=="Physical Touch":
        st.markdown("**Physical Touch picked!**")
        st.markdown("Physical touch is near impossible to work out through long distance.  \n "
                    "So, if you ever feel like receiving it, here are some pictures of us engaging in this beautiful love language.")
        newcol1, newcol2, newcol3 = st.columns([1,1,1])
        with newcol1:
            image4 = Image.open("./Images/Tpic1.jpg")
            image4 = image4.rotate(180)
            st.image(image4)
            image5 = Image.open("./Images/Tpic2.JPG")
            st.image(image5)
            image6 = Image.open("./Images/Tpic3.jpg")
            image6=image6.rotate(180)
            st.image(image6)
            file_ = open("./Images/Tgif2.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="">',
                unsafe_allow_html=True,
            )
        with newcol2:
            image8 = Image.open("./Images/Tpic5.jpg")
            image8=image8.rotate(180)
            st.image(image8)
            image9 = Image.open("./Images/Tpic6.JPG")
            st.image(image9)
            image10 = Image.open("./Images/Tpic7.JPG")
            st.image(image10)
            image11 = Image.open("./Images/Tpic8.JPG")
            st.image(image11)
        with newcol3:
            image7 = Image.open("./Images/Tpic4.jpg")
            image7rotate = image7.rotate(180)
            st.image(image7rotate)
            image13 = Image.open("./Images/Tpic10.JPG")
            st.image(image13)
            file_ = open("./Images/Tgif1.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="">',
                unsafe_allow_html=True,
            )
            image12 = Image.open("./Images/Tpic9.JPG")
            st.image(image12)
        return ""
    else:
        st.markdown("**Words of Affirmation picked!**")
        st.markdown("You deserve to know how special you are. Sometimes, as people do, we can get in our head, or get caught up in life, and forget who we are.  \nSo, I dedicate this page to remind you of the lovely person you are Talaa Raed Sater.")
        lcol, mcol, rcol = st.columns([1,1,1])
        with lcol:
            st.markdown("If you're stressed and work is causing you migraines, use this button:")
            support_button = st.button("Click Me!")
            if support_button:
                list_of_support = ["My baby you're doing amazing.", "Keep it up 7ub!", "7bbti there is no other like you.",
                                   "You're such a hard worker my love.", "You're doing great 7ayati.", "I believe in you my baby.",
                                   "Your hard work, determination and passion will always be seen and valued by me qalbi.",
                                   "My smart little nerd, you've got this.", "My **FOUR** A stars girlfriend.", "You're the most intelligent girl I know.",
                                   "My baby is the brightest little bug.", "I'm so proud of everything that you've accomplished so far.",
                                   "All your accomplishments are seen by me.", "I can't wait to spend the rest of my life celebrating your accomplishments with you.",
                                   "Dont forget that you are the reason for your successes and no one else.", "My future surgeon wife.",
                                   "All the work you're putting in will go to our kids telling the other kids that their mum is a doctor inshallah.",
                                   "I'm always here for you if you need to rest and recharge.", "Here is a **BIIIIG** hug for all the hard work you've put in."]
                statement = random.choice(list_of_support)
                st.write(statement + " <3")
        with mcol:
            st.markdown("If you're feeling yourself or wanna be hyped, use this button:")
            sexy_button = st.button("Touch me ;)")
            if sexy_button:
                list_sexywords = ["Fuck me you're gorgeous.", "You're smoking hot GOD DAMN.", "You're beautiful brown eyes, wheres the nearest tree?",
                                  "The sexiest woman in planet fucking Earth.", "I will die for your curves", "That hourglass figure of yours fuck me.",
                                  "Your smile enchants me every single time", "Perfect face, perfect body, i can't wait to ruin them.",
                                  "Goddess, you're a literal goddess, body and face, my god.", "Skin is glowing, always so clean, so smooth.",
                                  "The things I want to do to you, I'm going to hell for these thoughts.", "Slim thick, thats my baby.",
                                  "Look at that itty bitty waist AND thick thighs OH MY GOD.", "How did i get so lucky to end up with a goddess?",
                                  "Are you Aphrodite's daughter and I just haven't found out yet?", "My sexy Arabian princess.",
                                  "I cant wait to bruise that beautiful skin of yours.", "Your ass is to die for, I'm not kididng.",
                                  "You've got the most beautiful complexion I've ever laid my eyes on.", "That ass so fiiiiiiineee.",
                                  "Your ass deserves some spanking for looking that good.", "You've got the most beautiful set of tits.",
                                  "My darling your eyes sparkle at night.", "I will ruin your perfect mouth and beautiful lips.", "My baby is so beautiful I cant.",
                                  "The prettiest girl ever, and shes mine."]
                statement = random.choice(list_sexywords)
                st.write(statement +" <3")
                file_ = open("./Images/catgif.gif", "rb")
                contents = file_.read()
                data_url = base64.b64encode(contents).decode("utf-8")
                file_.close()
                st.markdown(
                    f'<img src="data:image/gif;base64,{data_url}" alt="">',
                    unsafe_allow_html=True,
                )
        with rcol:
            st.markdown("If you need a reminder of who you really are and what you mean to me, use this button:")
            talas_button = st.button("TRS")
            if talas_button:
                list_oftala = ["I love you so much Tala Sater.", "I cannot wait to put a ring on that finge.r",
                               "Through thick and thin, I'll always be there to love you.", "Our bond is so deep, I've never felt this with anyone else."
                               "I'm so comfortable around you my darling", "You're no black cat, your the most golden of golden retrievers",
                               "You're the most genuine person I know", "You are so clean and pure, I love it and you should too",
                               "My girl is on her deen, she's perfect balance of deen and dunya", "My thoughtful little bug, little ms romance."
                               "You're the girliest of girls and I love it.", "The most beautiful sole on planet Earth.", "Your heart is like no other, with its care, courage, and love."
                               "You are the most perfect girlfriend ever., I love you", "I love you endlessly.", "I will never stop loving you.", "My gym goer, yoga teacher girlfriend.",
                               "I cant wait to travel the world with you.", "I cant wait to build a future with you.",
                               "My darling you've got the most beautiful hair, eyes, nose, lips, ears, everything.", "Pink is your color, don't you forget it.",
                               "My little sexy librarian, ope wrong button sorry.", "My intelligent young woman.", "You mean the world to me.", "You are my whole world, and universe."
                               "You are my strong baby, strongest woman out there", "My funny bitch", "Who knew someone so amazing could be packed in a tiny 5'2 Woman.",
                               "Mako A7la minitch bil 7aya", "You're crazy, and I love crazy.", "My princess with a disorder.", "There is no soul kinder than yours.",
                               "My favorite girl.", "My sweet, lovely girlfriend.", "You're the love of my life.", "You are mine forever.", "My little squish."]
                statement = random.choice(list_oftala)
                st.write(statement + " <3")

        return ""

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
        letter = st.selectbox("**Whose love/birthday letter would you like to read?**", ["Yazan", "Zeina", "Haya", "Yasemine"])

    #Love Languages
    elif navigation == "Love Languages":
        st.title("What Type of Love Do You Want Right Now?")
        language = st.selectbox("**Pick whichever you want and I will provide :)**",
                     ["Act of Service","Quality Time","Gifts","Physical Touch","Words of Affirmation"])
        st.markdown(picklovelanguage(language))


