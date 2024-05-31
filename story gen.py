
import random as ran
YorN = input("Do you want it to ask multiple times?(Enter Y or N):")
if YorN.lower() == "n":
    repeat = 1
elif YorN.lower() == "y":
    repeat = int(input("How many times?:"))
who = []
when = []
where = []
what = []
for i in range(repeat):
    when2 = str(input("Enter a time:"))
    who2 = str(input("Enter a name:"))
    where2 = str(input("Enter a place:"))
    what2 = str(input("Enter what they did:"))
    who.append(who2)
    when.append(when2)
    where.append(where2)
    what.append(what2)
print(ran.choice(when)+", a person named "+ran.choice(who)+", was in  "+ran.choice(where)+",and "+ran.choice(what))

# import random
#
# when = ['Yesterday', 'In the future', 'In a parallel universe', 'Last summer', 'On New Year\'s Eve']
# who = ['a space explorer', 'a wizard', 'a robot', 'a mermaid', 'a superhero']
# name = ['Zara', 'Orion', 'Quasar', 'Nixie', 'Blaze']
# residence = ['Mars', 'Atlantis', 'Cyber City', 'Enchanted Forest', 'Sky Haven']
# went = ['space station', 'magic academy', 'digital realm', 'enchanted garden', 'celestial observatory']
# happened = ['discovered a new galaxy', 'cast a spell on a dragon', 'solved a digital puzzle', 'found a hidden treasure', 'saved the universe']
#
# print(random.choice(when) + ', ' + random.choice(who) + ' named ' + random.choice(name) + ' that lived in ' +
#       random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
