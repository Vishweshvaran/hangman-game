import random

print("H A N G M A N")
n=1
while n>0:
    enter_word = input('Type "play" to play the game, "exit" to quit: ')
    print()
    
    if enter_word == "play": 
        list = ['python', 'java', 'kotlin', 'javascript']
        word = random.choice(list)
        word1 = word.replace(str(word), '-'*len(word))
        print(word1)

        x=[]
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        i=8


        while i>0 : 
            if word1 == word:
                print("You guessed the word!")
                print("You survived!\n")
                break
            else:
                guess = input("Input a letter: ")
                

                if len(guess) == 1:
                    if guess in letters:
                        if guess not in x:
                            if guess in word:
                                b = word.count(guess)
                                a = word.find(guess)
                                c = word.rfind(guess)
                                word1 = word1[:a] + guess + word1[a+1:]
                                word1 = word1[:c] + guess + word1[c+1:]
                                print(f"\n{word1}")
                            else:
                                if i == 1:
                                    print("No such letter in the word")
                                else:
                                    print("No such letter in the word\n")
                                    print(word1)
                                i-=1
                        else:
                            print("You already typed this letter\n")
                            print(word1)
                    else:
                        print("It is not an ASCII lowercase letter\n")
                        print(word1)
                else:
                    print("You should input a single letter\n")
                    print(word1)
                    
                x.append(guess) 
        if word1 != word:
            print("You are hanged!\n")   
                  
    else:
        break 
    
        



