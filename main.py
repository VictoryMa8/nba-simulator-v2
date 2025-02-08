import sys

class State:
    def __init__(self, screen_num = 0):
        self.screen_num = screen_num
    
    def get_screen_num(self):
        return self.screen_num
    
    def update(self, user_input):
        # convert user input to int if possible
        try:
            choice = int(user_input)
        except ValueError:
            choice = -1
        
        if self.screen_num == 0:
            # move to next screen
            self.screen_num = 1
        
        elif self.screen_num == 1:
            if choice == 1:
                self.screen_num = 2
            else:
                self.screen_num = 3
        
        elif self.screen_num == 2:
            if choice == 1:
                print("Selected team A.")
            elif choice == 2:
                print("Selected team B.")
            self.screen_num = 4
        
        elif self.screen_num == 3:
            if choice == 1:
                print("Going back to screen 1.")
                self.screen_num = 1
        
        if self.screen_num > 4:  
            sys.exit(0)

def display_text(state):
    screen = state.get_screen_num()
    
    if screen == 1:
        print("[Screen 1] Press '1' to go to screen 2, anything else takes you to screen 3.")
    elif screen == 2:
        print("[Screen 2] Choose a team: 1) Team A, 2) Team B")
    elif screen == 3:
        print("[Screen 3] Press '1' to go back to screen 1.")
    elif screen == 4:
        print("[Screen 4] End of flow. Enter anything to exit.")
    else:
        print("[Screen 0] Initial screen. Enter anything to proceed.")

def main():
    state = State(screen_num = 0)
    while True:
        display_text(state)
        inp = input("> ")
        state.update(inp)

if __name__ == "__main__":
    main()