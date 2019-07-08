import random
print("Hello reader")
name = input("What is your name? ")
print("Hello " + name)
gender = input("Are you a girl or a boy? ")

if gender == "girl":
    pronoun = "she"

elif gender == "boy":
    pronoun = "he"

else:
    pronoun = "they"

names = ["Scarlett","Chris","Sebastian","Robert","Paul","Tom","Zendaya"]
roles = ["Spy","Soldier","Assasin","Millionaire","Ex-con","Fanboy","Protester"]
actions = ["kill","hit","eat","count money","run","scream","cheer"]
places = ["Earth","Knowhere","Vormir","Zen-Whoberi","Titan","Nidavellir"]

actor_name = random.choice(names)
actor_role = random.choice(roles)
quest = random.choice(actions)
settings = random.choice(places)

story = "Once upon a time, there was a " + actor_role + "called" + actor_name
". Since this Narrator knows nothing about Avengers, this story's going to be inaccurate. Very inaccurate."
"Anyways" + actor name + 
