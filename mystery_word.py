import random
import string
# from string import maketrans   # Required to call maketrans function.


def greeting():
  print("Hello! Welcome to the Mystery Word Game! Hit any key to continue.")
  input()

# You must guess the mystery word within 8 turns or the computer wins :(

# Choose a level of difficulty:
# Easy mode only has words of 4-6 characters;
# Normal mode only has words of 6-8 characters;
# Hard mode only has words of 8+ characters.

def choose_random_word():
  # random_number = random.randint(1,235886)
  # print(random_number)
  with open("words.txt") as file:
    word_list = file.read()
    words = word_list.split()
    # print (words)
    random_word = random.choice(words)
    # random_word = file.read(random_number)
    print("random" , random_word)
    # print(type(random_word))
    # word_length = len(random_word)
    # print ("len" , word_length)
    return random_word

def print_current_word_status(random_word, letters):
  print("Your mystery word is ", len(random_word)," characters long.")
  blank_word = ("_" * len(letters))
  print ("blank_word" , blank_word)
  # print("type blank", type(blank_word))
  # print("type random", type(random_word))
  letters_string = "".join(letters)
  print ("Letter string" , letters_string)
  current_word_status = str.maketrans(str(letters_string), blank_word)
  print(current_word_status)
  print(random_word.translate(current_word_status))

  
  # intab = "aeiou"
  # outtab = "12345"
  # trantab = maketrans(intab, outtab)
  
  # str = "this is string example....wow!!!"
  # print (str.translate(trantab))



def print_current_guesses(guesses):
  print ("Current number of guesses left is :" , 8 - guesses)

def get_input():
  print("Please select a letter.")
  guess = input().lower()
  print(f"letter {guess.lower()}")
  return guess

def check_guess(guess, letters, random_word):

  # letters = list (random_word)
  if len(guess) == 1 :
    while guess in letters:
    # if guess.lower in random_word:
      # letters_left = letters.remove(guess)
      # print("yay", letters_left)
      letters.remove(guess)


    print(guess , letters, len(letters))
    # if guess in letters:
    # elif (len(guess) = len (random_word))
      


def game():
  greeting()
  random_word = choose_random_word()
  print("Your mystery word is ", len(random_word)," characters long.")
  print("")
  print("___ " * len(random_word))
  letters = list (random_word)
  guesses = 0
  while guesses < 8:
    print_current_word_status(random_word, letters)
    print_current_guesses(guesses)
    guess = get_input()
    guesses += 1
    check_guess(guess, letters, random_word)
    if len(letters) == 0:
      print("you won!")
      break
  
  if len(letters) > 0:
    print("You ran out of guesses.  Better luck next time")

# check_win()
# print_loss()


game()