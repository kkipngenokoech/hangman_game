
from random import choice#selects a random item from the list
#from Ipython.display import clear_output#it clears the loop once we alreaddy used it so as to avvoid it piling on top of each other
words=["tree","basket","chair","paper","pythons","yes"]
word=choice(words)#randomly chooses a word in the list
guessed,game_lives,game_over=[],7,False
guesses=["_"]*len(word)
"""while not game_over:
    ans=input("\ntype quit or guess letter: ").lower()
    if ans=="quit":
        print("\nthanks for playing")
        game_over=True
"""
while not game_over:
    hidden_word="".join(guesses)
    print("word to guess:{}".format(hidden_word))
    print("LIVES:{}".format(game_lives))
    ans = input("\ntype quit or guess a letter: ").lower()
 #   clear_output()
    if ans == "quit":
        print("\nthanks for playing")
        game_over = True
    elif ans in word:
        print("you guessed correctly!")
        for index in range(len(word)):
            if word[index]==ans:
                guesses=ans
    else:
        game_lives-=1
        print("incorrect !you lost a life")
        if game_lives<=0:
            print("you lost all lives ,GAME OVER")
            game_over=True
        elif word==" ".join(guesses):
            print("congratulations ,you guessed correctly")
            game_over=True
