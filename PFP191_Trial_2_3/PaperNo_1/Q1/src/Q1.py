class Main:
    
    #====================f1====================
    def f1(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        move = inputString.split(", ")
        for m in move:
            print(m)
        # end def


    #====================f2====================
    def f2(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        x,y =0,0
        movement = inputString.split(", ")
        for move in movement:
            part = move.split(" ")
            direction = part[0]
            step = int(part[1])
            if direction == "UP":
                y += step
            if direction ==  "DOWN":
                y -= step
            if direction == "LEFT":
                x -= step
            if direction == "RIGHT":
                x += step
        dis =(x ** 2 + y ** 2) ** 0.5
        print(round(dis))
     
#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (2 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        inputString = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(inputString)
        elif choice == 2:
            self.f2(inputString)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
