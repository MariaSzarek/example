"""
MOJ WLASNY PIERWSZY W CAŁOSCI PROGRAM 
"""
import random
import art
print(art.logo)


#star = input("Do you want to playa game of Blackjack? Type 'y' on 'n': ")

def result(your_cards, your_score, comp_cards):
    print(f'\nYour cards: {your_cards}, current score: {your_score}')
    print(f"Computer's first card: {comp_cards[0]}")

def fullresult(your_cards, your_score, comp_cards, comp_score):
    print(f'\nYour cards: {your_cards}, current score: {your_score}')
    print(f"Computer's first card: {comp_cards}, comp score: {comp_score}")

def play_cards():
        
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_cards = [random.choice(cards)]
    comp_cards = [random.choice(cards), random.choice(cards)]
    #your_cards = [6]
    #comp_cards = [11, 10]

    end = 'n'    
    next_card = 'y'
    while next_card == 'y':
        your_cards.append(random.choice(cards))
        #your_cards.append(6)
        #your_cards = [6, 6]
        your_score = sum(your_cards)
        comp_score = sum(comp_cards)
        
#----------------------------------------------------------------------    
    #to sprawdza w pierwszym rozdaniu czy jest blackjack
        if set(your_cards) == {11, 10}:
            print('>>> GAME OVER --- YOU WIN <<<')
            break
        elif set(comp_cards) == {11, 10}:
            print(comp_cards)
            print('>>> BLACKJACK --- YOU LOSE <<<')
            break
        elif len(your_cards) == 2:
            print('NO BLACKJACK ON TABLE')
#----------------------------------------------------------------------      
        #ace in total over 21 is for 1 point
        if your_score > 21:
            if 11 in your_cards and your_score - 10 < 21:
                idx = your_cards.index(11)
                your_cards[idx] = 1
                your_score = sum(your_cards)
                result(your_cards, your_score, comp_cards)
                next_card = input("Type 'y' to get another card, type 'n' to pass: ") 
            else:
                fullresult(your_cards, your_score, comp_cards, comp_score)
                print('>>> You lose')
                end = 'y'
                break
        elif your_score < 21:
            result(your_cards, your_score, comp_cards)
            next_card = input("Type 'y' to get another card, type 'n' to pass: ")
        elif your_score == 21:
            fullresult(your_cards, your_score, comp_cards, comp_score)
            print('>>> You win')
            end = 'y'
            break
#----------------------------------------------------------------------   
    # i to powinno sie juz nie wykonywac po tym jak ja 'you lose'
    while end == 'n' and comp_score < 17:
        comp_cards.append(random.choice(cards))
        comp_score = sum(comp_cards)

#----------------------------------------------------------------------   
    
    if end == 'n':
        fullresult(your_cards, your_score, comp_cards, comp_score)
        
        if comp_score> 21: 
            print(">> You win")
        elif comp_score > your_score:
            print('>>> You lost')
        elif comp_score < your_score:
            print('>>> You win')
        elif comp_score == your_score:
            print('>>> Draw')
        
    again = input('Type "y" to play again, type "n" to quit game: ')
    if again == 'y':
        print("""
    
              >>> NEW GAME <<<
    
              """)
        play_cards()
    elif again == 'n':
        print('Goodbye')
            
play_cards()

