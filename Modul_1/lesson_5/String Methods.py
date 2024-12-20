
############################################# capitalize() ######################################################

# word = "hello, welcome to my world!"
# print(word.capitalize())
#
# word = "i am AMIRSAID"
# print(word.capitalize())

############################################# casefold() ######################################################

# word = "HELLO, AND WELCOME TO MY WORLD!"
# print(word.casefold())

############################################# center() ######################################################

# word = "banana"
# print(word.center(20, '_'))


############################################# count() ######################################################
# word = "I love my apples, apples are the best"
# print(word.count("apples"))

# word = "I love my apples, apples are the best, apples are amazing"
# print(word.count("apples", 10, len(word)))

############################################# encode() ######################################################

# word = "My name is фыв"
# print(word.encode(encoding = "ascii" , errors='namereplace'))
#
# txt = "My name is Ståle"
#
# print(txt.encode(encoding="ascii",errors="backslashreplace"))
# print(txt.encode(encoding="ascii",errors="ignore"))
# print(txt.encode(encoding="ascii",errors="namereplace"))
# print(txt.encode(encoding="ascii",errors="replace"))
# print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

############################################# endswith() ######################################################

# word = "My name is Amirsaid"
# print(word.endswith("Amirsaid", 5, len(word)))

############################################# expandtabs() ######################################################

# txt = "H\te\tl\tl\to"
#
# print(txt)
# print(txt.expandtabs())
# print(txt.expandtabs(2))
# print(txt.expandtabs(4))
# print(txt.expandtabs(10))

############################################# find() ######################################################

# word = "Hello, welcome to my world"
# print(word.find("world", 5, len(word)))

############################################# format() ######################################################
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)
#
# print(txt1)
# print(txt2)
# print(txt3)

############################################# format_map() ######################################################

# data = {'name': 'Alice', 'age': 30}
#
# sentence = "My name is {name} and I am {age} years old."
#
# formatted_sentence = sentence.format_map(data)
#
# print(formatted_sentence)

############################################# index() ######################################################

# word = "Welcome to my fantasy world"
#
# print(word.index("fantasy"))

############################################# isalnum() ######################################################

# word = "Company1201"
# print(word.isalnum())

############################################# isascii() ######################################################

# word = "Company1201&& 1*"
# print(word.isascii())

############################################# isidentifier() ######################################################

# a = "MyFolder"
# b = "Demo002"
# c = "2bring"
# d = "my demo"
#
# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())

############################################# isprintable() ######################################################

# txt = "Hello! Are you #1?"
#
# x = txt.isprintable()
#
# print(x)

# txt = "Hello!\nAre you #1?"
#
# x = txt.isprintable()
#
# print(x)

############################################# istitle() ######################################################
# txt = "Hello, And Welcome To My World!"
#
# x = txt.istitle()
#
# print(x)

# a = "HELLO, AND WELCOME TO MY WORLD"
# b = "Hello"
# c = "22 Names"
# d = "This Is %'!?"
#
# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

############################################# join() ######################################################

# myTuple = ("John", "Peter", "Vicky")
#
# x = "#".join(myTuple)
#
# print(x)

# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"
#
# x = myDict.join(myDict)
#
# print(x)

# words = ["H", "e", "l", "l", "o"]
#
# joined_string = "".join(words)
#
# print(joined_string)

############################################# ljust() ######################################################

# txt = "banana"
#
# x = txt.ljust(20)
#
# print(x, "is my favorite fruit.")
#
# txt = "banana"
#
# x = txt.ljust(20, "O")
#
# print(x)

############################################# lstrip() ######################################################

# txt = "     banana     "
#
# x = txt.rstrip()
# y = txt.lstrip()
# print("of all fruits", x, "is my favorite")
# print("of all fruits", y, "is my favorite")


# txt = ",,,,,ssaaww.....banana"
#
# x = txt.lstrip(",.asw")
#
# print(x)

# word = "aaaaAmirbbbbSaid"
# print(word.lstrip("a"))

############################################# maketrans() ######################################################

# txt = "Hello Sam!"
# mytable = str.maketrans("S", "P")
# print(txt.translate(mytable))

# txt = "Hi Sam!"
# x = "mSa"
# y = "eJo"
# mytable = str.maketrans(x, y)
# print(txt.translate(mytable))

# txt = "Good night Sam!"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# print(str.maketrans(x, y, z))


# trans_table = str.maketrans("abc", "123")
# txt = "abcde"
# translated_txt = txt.translate(trans_table)
# print(translated_txt)


############################################# partition() ######################################################

# txt = "I could eat bananas all day"
#
# x = txt.partition("bananas")
#
# print(x)

############################################# replace() ######################################################

# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)

# txt = "one one was a race horse, two two was one too."
# x = txt.replace("one", "three", 1)
# print(x)


############################################# split() ######################################################

# txt = "welcome to the jungle"
# x = txt.split()
# print(x)

# txt = "hello, my name is Peter, I am 26 years old"
# x = txt.split(", ")
# print(x)

# txt = "apple#banana#cherry#orange"
# x = txt.split("#", 1)
# print(x)


############################################# splitlines() ######################################################
# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines()
# print(x)

# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines(True)
# print(x)

############################################# strip() ######################################################

# txt = "     banana     "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")

# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)

############################################# zfill() ######################################################
# txt = "50"
# x = txt.zfill(2)
# print(x)

# a = "hello"
# b = "welcome to the jungle"
# c = "10.000"
#
# print(a.zfill(10))
# print(b.zfill(10))
# print(c.zfill(10))



