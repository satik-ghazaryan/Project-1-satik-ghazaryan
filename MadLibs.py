
choice = input("Type 1, 2, or 3: ")

# --- Story 1 ---
if choice == "1":
    number = input("Enter a number: ")
    time_measure = input("Enter a measure of time: ")
    transport = input("Enter a mode of transportation: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    color = input("Enter a color: ")
    body_part1 = input("Enter a part of the body: ")
    verb1 = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter another noun: ")
    part_body2 = input("Enter another part of the body: ")
    verb2 = input("Enter another verb: ")
    noun4 = input("Enter another noun: ")
    adjective3 = input("Enter another adjective: ")
    silly_word = input("Enter a silly word: ")

    text1 = f"""
It was about {number} {time_measure} ago when I arrived at the hospital in a {transport}.
The hospital is a/an {adjective1} place, there are a lot of {adjective2} {noun1} here.
There are nurses here who have {color} {body_part1}.
If someone wants to come into my room, I told them that they have to {verb1} first.
I've decorated my room with {noun2}.
Today I talked to a doctor and they were wearing a {noun3} on their {part_body2}.
I heard that all doctors {verb2} {noun4} every day for breakfast.
The most {adjective3} thing about being in the hospital is the {silly_word} {noun1}!
"""
    print(text1)

# --- Story 2 ---
elif choice == "2":
    person = input("Person’s name: ")
    noun = input("Noun: ")
    adjective1 = input("Adjective (feeling): ")
    verb = input("Verb: ")
    adjective2 = input("Adjective (feeling 2): ")
    animal = input("Animal: ")
    verb2 = input("Verb2: ")
    color = input("Color: ")
    verb_ing = input("Verb ending in -ing: ")
    adverb = input("Adverb ending in -ly: ")
    number = input("Number: ")
    time_measure = input("Measure of time: ")
    silly_word = input("Silly word: ")
    noun2 = input("Noun2: ")

    text2 = f"""
This weekend I am going camping with {person}.
I packed my lantern, sleeping bag, and {noun}.
I am so {adjective1} to {verb} in a tent.
I am {adjective2} we might see a(n) {animal}, I hear they’re kind of dangerous.
While we’re camping, we are going to hike, fish, and {verb2}.
I have heard that the {color} lake is great for {verb_ing}.
Then we will {adverb} hike through the forest for {number} {time_measure}.
If I see a {color} {animal} while hiking, I am going to bring it home as a pet!
At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!!
"""
    print(text2)

# --- Story 3 ---
elif choice == "3":
    person = input("Person’s name: ")
    adjective1 = input("Adjective: ")
    color = input("Color: ")
    animal = input("Animal: ")
    place = input("Place: ")
    adjective2 = input("Adjective2: ")
    magical1 = input("Magical creature (plural): ")
    adjective3 = input("Adjective3: ")
    magical2 = input("Another magical creature (plural): ")
    room = input("Room in a house: ")
    noun = input("Noun: ")
    noun2 = input("Another noun: ")
    noun3 = input("Noun (plural): ")
    adjective4 = input("Adjective4: ")
    noun4 = input("Another noun (plural): ")
    number = input("Number: ")
    time_measure = input("Measure of time: ")
    verb_ing = input("Verb ending in -ing: ")
    adjective5 = input("Adjective5: ")
    noun5 = input("Noun5: ")

    text3 = f"""
Dear {person},
I am writing to you from a {adjective1} castle in an enchanted forest.
I found myself here one day after going for a ride on a {color} {animal} in {place}.
There are {adjective2} {magical1} and {adjective3} {magical2} here!
In the {room} there is a pool full of {noun}.
I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}.
It feels as though I have lived here for {number} {time_measure}.
I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun5}!!
"""
    print(text3)

else:
    print("Invalid choice. Please type 1, 2, or 3.")
