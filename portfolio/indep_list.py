from random import *

###level 1 - name generator
#word_list = ["Yorsalem", "Allyson", "Dana", "Daisy", "Nyah", "Raphi", "Luolan", "Sophie", "Lisa", "Carly", "Sinead", "Anna", "Theodora", "Seyla", "Zayba", "Isabella", "Sohini", "Hui", "Mariana"]
#answer = int(input("How many names do you want? (1-19)"))
#
#for i in range(0,answer):
#    x = randint(0, len(word_list)-1)
#    print (word_list[x])

###level 2 - menu generator
#main = ["pasta", "rice", "noodles", "pancakes", "fish and chips", "pizza"]
#side = ["french fries", "mashed potatoes", "corn", "onion rings"]
#drink = ["iced tea", "coffee", "smoothie", "frappe", "milkshake"]
#dessert = ["cake", "gum", "ice-cream", "cheesecake", "pie"]

#x = randint(0, len(main)-1)
#y = randint(0, len(side)-1)
#z = randint(0, len(drink)-1)
#a = randint(0, len(dessert)-1)

#print ("Your meal today will be: "+main[x]+", "+side[y]+", "+drink[z]+", and "+dessert[a]+". ")


###level 3 - haiku generator


fiveSyl = ["A day will be as", "Are you okay now", "I think you are cool", "'Yolo' said the man", "I love computers", "All and are as but"]
sevenSyl = ["I like my tea iced, don't you?", "KARD's debut was so good, right?", "We had some good food today", "Honesty or honest tea?"]
fiveSyl1 = ["I gotta finish this", "I'm hurrying now", "Can't count syllables", "Wow wow wow wow wow", "I do not even know"]

x = randint(0, len(fiveSyl)-1)
y = randint(0, len(sevenSyl)-1)
z = randint(0, len(fiveSyl1)-1)

print(fiveSyl[x])
print(sevenSyl[y])
print(fiveSyl1[z])
