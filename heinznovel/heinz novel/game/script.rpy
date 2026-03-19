define h = Character('???', color="#245353")
define h1 = Character('Heinz', color="#174de1")
define m = Character('You', color="#20a2de")
define b = Character('Unnamed Bully', color="#ca2727")
define b1 = Character('Lesser Bully', color="#cc5b5b")

define gui.text_color = "#402000"

define gui.text_font = "ari-w9500-bold.ttf"
define gui.name_text_font = "ari-w9500-bold.ttf"

define gui.name_ypos = 20


label start:

    h "Hey..."

    h "You awake? Hellooo..."

    m "What?"

    "Your head throbs like you've just slammed straight into concrete."

    "Maybe you did. Dumbass."

    h "I can't let a fellow Darter just lie there like that! Come here."

    m "Huh?"

    "You suddenly find yourself being helped up by a strange old man."

    scene bg apopka front
    show heinz regular at right
    with fade

    h "Ooh... That fall really did hurt you."

    m "W-What? I'm at school?!"

    "Just a moment ago you were just sleeping. Summer really did go by that fast."

    h "Yeah! Welcome to your first day at Apopka High School!"

    "You then hear some kids sneering at you."

    show bully at left

    b "First day? Do I smell a freshie on MY campus?"

    "A group of bullies appear behind you, with their leader looking suspiciously like the man who helped you up."

    b "The rumor really is true. You freshmen always get tinier every year! Is your little sister a mouse?"

    b "Hahahaha!"

    b1 "Uhh.. Isn't that the principal?"

    b1 "Yeah- I think we should get outta here."

    b "H-Huh?"

    hide bully
    with moveoutleft

    "You then see a dean sprint over and shoo them away, waving a pink slip of paper in their hand and a Starbucks coffee in the other."

    h "Man.. These kids never change."

    m "You're... The principal?"

    h1 "Yup. Pincipal Heinz for you. Welcome to Apopka High School."

    h1 "Sorry if those kids soured this place for you. First impressions and all."

    h1 "Anyways, let's get to class. Do you have your Skyward on you?"

    hide bg apopka front
    hide heinz regular
    with fade

    "> Got to School Ending"

    "67 67 67"

    return



