class Main:

    #====================GuessNumber function====================
    def GuessNumber(self, number):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        import random
        
        low = 1
        high = int(number)
        feedback = ''
        
        while feedback != 'c':
            if low > high:
                break
            guess = random.randint(low,high)
            feedback = input(f"Is {guess} too high(h), too low(l), or correct(c): ").lower()
            
            if feedback == 'h':
                high = guess - 1  
            elif feedback == 'l':
                low = guess + 1   
            elif feedback == 'c':
                print(f"Welldone! The computer guessed your number {guess} correctly!")
            else:
                print("Invalid input. Please enter 'h', 'l', or 'c'.")
        # end def

#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        number = input("Enter a range for guessed number: ")
        print("OUTPUT")
        self.GuessNumber(number)
        print("FINISH")
main = Main()
main.main()
