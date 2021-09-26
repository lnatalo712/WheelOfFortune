import random

playerBank = [0, 0, 0]
totalBank = [0, 0, 0]
playerTurn = 1

wheel = ["Bankrupt", "Lose a turn", "100", "150", "200", "250", "300", "350", "400", "450", "500", "550", "600", "650", "700", "750", "800", "850", "900", "950", "1000", "1500", "2000", "3000"]
words = ["tomorrow", "yesterday", "complete", "fight"]
vowels = ["a", "e", "i", "o", "u"]
answer = []
answer_s = ""
answer_s3 = ""
alreadyGuessed = []
rnd = 1
game = True

def wordSelection():
    rand = random.randrange(len(words))
    word = words[rand]
    words.remove(word)
    return word

def spinWheel():
    rand = random.randrange(len(wheel))
    spin = wheel[rand]
    return spin

def guessWord(word):
    decision = input("Would you like to guess the word?\n").lower()
    cont = False

    while cont == False:
        if decision == "yes":
            guess = input("Guess the word: ").lower()
            if guess == word:
                    print("You got it!")
                    return 1
            else:
                    print("That's incorrect, your turn is over.")
                    return  0
            cont = True
        elif decision == "no":
            cont = True
            return 2
        else:
            decision = input("Please respond with either yes or no.\n").lower()

def takeTurn(player, word):
    cont = False
    
    print("It is player " + str(player) + "'s turn.")
    correct = guessWord(word)
    if correct == 0:
        return 0
    elif correct == 1:
        return 1
    
    spin = spinWheel()
    print("The wheel landed on " + spin)
    if spin == "Bankrupt":
        print("Oh no you've gone bankrupt!")
        return 3
    elif spin == "Lose a turn":
        print("Oh no you've lost your turn!")
        return 0
    
    right = consonantCheck(word)
    
    if right > 0:
        playerBank[player-1] += (int(spin)*right)
        print("You have " + str(playerBank[player - 1]) + " dollars in this round.")

        while cont == False:
            if playerBank[player-1] >= 250:
                check = vowelCheck(player, word)
            
            if check == 0:
                return 0

            correct = guessWord(word)
            if correct == 0:
                return 0
            elif correct == 1:
                return 1
            
            spin = spinWheel()
            print("The wheel landed on " + spin)
            if spin == "Bankrupt":
                print("Oh no you've gone bankrupt!")
                return 3
            elif spin == "Lose a turn":
                print("Oh no you've lost your turn!")
                return 0

            right = consonantCheck(word)
            if right < 0:
                return 1            
            elif right > 0:
                playerBank[player-1] += (int(spin)*right)
                print("You have " + str(playerBank[player - 1]) + " dollars in this round.")
            else:
                return 0
    else:
        return 0
    
def consonantCheck(word):
    right = 0
    cont = False

    guess = input("Please guess a consonant: ").lower()
    while cont == False:
        if guess.isalpha() == False:
            guess = input("Please guess a consonant: ").lower()
            cont = False
        elif guess in vowels:
            print("You cannot buy a vowel until you have successfully guessed a consonant.")
            guess = input("Please guess a consonant: ").lower()
            cont = False
        else:
            cont = True
    
    if guess in alreadyGuessed:
        print("The letter " + guess + " has already been guessed. Your turn is over.")
        return right
    elif guess in word:
        alreadyGuessed.append(guess)
        print("The letter " + guess + " is correct!")
        for i in range(len(word)):
            if guess == word[i]:
                answer[i] = guess
                right += 1
        answer_s = "".join(answer)
        if answer_s == word:    
                print("You got it! The word was " + word + ".")
                return -1
        print("Here is what the word currently looks like: " + answer_s)
        return right
    else:
        print("The letter " + guess + " is incorrect. Your turn is over.")
        return right

def vowelCheck(player, word):
    right = 0
    cont = False

    choice = input("Would you like to buy a vowel? Each vowel costs 250 dollars.\n").lower()
    while cont == False:
        if choice == "yes":
            guess = input("Please guess a vowel: ").lower()
            playerBank[player - 1] -= 250
            cont = True
        elif choice == "no":
            cont = True
            return 2
        else:
            choice = input("Please respond with either yes or no.\n").lower()
    
    if guess in alreadyGuessed:
        print("The letter " + guess + " has already been guessed. Your turn is over.")
        return right
    elif guess not in vowels:
        print("You did not guess a vowel so your turn is over.")
        return right
    elif guess in word:
        alreadyGuessed.append(guess)
        print("The letter " + guess + " is correct!")
        for i in range(len(word)):
            if guess == word[i]:
                answer[i] = guess
                right += 1
        answer_s = "".join(answer)
        if answer_s == word:    
                print("You got it! The word was " + word + ".")
                return 1
        print("Here is what the word currently looks like: " + answer_s)
        return right
    else:
        print("The letter " + guess + " is incorrect. Your turn is over.")
        return right

def rnd3Setup(letter, w3):
    for i in range(len(w3)):
        if letter == w3[i]:
            answer3[i] = letter
    answer_s3 = "".join(answer3)
    if letter == "e":    
        print("The final word will be displayed with the letters R-S-T-L-N-E revealed.")
        print("Here is what the final word looks like: " + answer_s3)

def rnd3GuessWord(word):
    guess = input("Guess the word: ").lower()
    if guess == word:
        print("Congratulations you got it! You won $123,456,789!")
    else:
        print("That's incorrect, the correct word was " + word + " . Better luck next time!")
            

while rnd < 3:
    w = wordSelection()
    answer = list("_" * len(w))
    print("The word to guess has " + str(len(answer)) + " letters.")
    game = True

    while game == True:
        go = takeTurn(playerTurn, w)

        if go == 0:
            if playerTurn == 3:
                playerTurn = 1
            else:
                playerTurn += 1
        elif go == 1:
            rnd += 1
            totalBank[0] += playerBank[0]
            totalBank[1] += playerBank[1]
            totalBank[2] += playerBank[2]
            playerBank[0] = 0
            playerBank[1] = 0
            playerBank[2] = 0
            alreadyGuessed = []
            game = False
        elif go == 3:
            playerBank[playerTurn - 1] = 0
            if playerTurn == 3:
                playerTurn = 1
            else:
                playerTurn += 1

topPlayer = totalBank.index(max(totalBank))
print("Player " + str(topPlayer + 1) + " has the most money with $" + str(totalBank[topPlayer]) + ", and gets to play the final round!")
playerTurn = topPlayer + 1

w3 = wordSelection()
answer3 = list("_" * len(w3))
rnd3Setup("r", w3)
rnd3Setup("s", w3)
rnd3Setup("t", w3)
rnd3Setup("l", w3)
rnd3Setup("n", w3)
rnd3Setup("e", w3)

print("You will only have ONE try to guess the correct word. Good luck!")
rnd3GuessWord(w3)