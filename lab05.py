########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed

import random

def play_again():
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    replay = input('Do you want to play again? Enter Y for yes or N for no. : ')
    # if lowercased input is not y, yes, n, or no, prompt user to input a valid response.
    while replay.lower() != 'y' and replay.lower() != 'yes' and replay.lower() != 'n' and replay.lower() != 'no':
        print("Invalid input! Try again.")
        replay = input('Do you want to play again? Enter Y for yes or N for no. : ')
    # return True or False in respect to the input given.
    if replay.lower() == 'y' or replay.lower() == 'yes':
        return True
    elif replay.lower() == 'n' or replay.lower() == 'no':
        return False
     
def get_wager(bank):
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    chip_wager = int(input('Enter the amount of chips you want to wager. : '))
    # Make sure user does not bet negative or 0 chips, or more than they have currently in their bank.
    while chip_wager <= 0 or chip_wager > bank:
        print('Input out of range!')
        chip_wager = int(input('Enter the amount of chips you want to wager. : '))
    return chip_wager            

def get_slot_results():
    ''' Returns the result of the slot pull '''
    # Generates a random number between 1 and 10 (inclusive) for each reels.
    slot_one = random.randint(1,10)
    slot_two = random.randint(1,10)
    slot_three = random.randint(1,10)
    return slot_one, slot_two, slot_three

def get_matches(reela, reelb, reelc):
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    # slot_result combines 3 reels into 1 string.
    # For example: reela = 1, reelb = 2, reelc = 3 would set slot_result as '123'.
    slot_result = str(reela) + str(reelb) + str(reelc)
    largest = 0
    # Goes through numbers 1 through 10 to find the number of matches. Largest number of match is stored to the
    # value 'largest'. After going through all the numbers, the 'largest' value is returned.
    for i in range(1,10):
        if slot_result.count(str(i)) > largest:
            largest = slot_result.count(str(i))
    # if the largest match is 1, return 0, since there were no matches.
    if largest == 1:
        return 0
    return largest

def get_bank():
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    bank_input = int(input('How many chips do you want to play with? Enter an amount between 0 and 101(non-inclusive) : '))
    # Keep asking the user to input a number between 101 and 0, non-inclusive.
    while bank_input > 101 or bank_input < 0:
        bank_input = int(input('Invalid input. Try again!\nHow many chips do you want to play with? Enter an amount between 0 and 101(non-inclusive) : '))
    return bank_input

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    # Return correct amount of wages return to the user according to the amount of matches given.
    if matches == 3:
        return wager * 9
    elif matches == 2:
        return wager * 2
    elif matches == 0:
        return wager * -1     
    


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        # Resets most_chip to value of bank and spin to zero.
        most_chip = bank
        spin = 0
        
        while bank > 0:
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

            spin += 1
            # if most_chip is now less than the current bank, set most_chip equal to bank.
            if most_chip < bank:
                most_chip = bank
            
        print("You lost all", wager, "in", spin, "spins")
        print("The most chips you had was", most_chip)
        playing = play_again()
