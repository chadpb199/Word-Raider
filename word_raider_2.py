import customtkinter as ctk
import random as rand

title_font_family = "Informal Roman"
main_font_family = "Palatino Linotype"
letters = ("Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M")

# possible color pallette for later:
# palette = {"gunmetal": "#2C363F", "azure": "#3A86FF", "eggshell": "#FAF3DD", "tea green": "#C8D5B9", "cambridge blue": "#8FC0A9"}

class App(ctk.CTk):
    """Main Menu Window of Word Raider II Game
    """
    
    def __init__(self):
        super().__init__()
        # basic window config
        self.title("Word Raider II")
        self.geometry("400x300")
        self.resizable(False, False)
        
        # create fonts
        self.title_font = ctk.CTkFont(family=title_font_family, size=48, weight="bold")
        self.main_font = ctk.CTkFont(family=main_font_family, size=24)
        
        # generate custom widgets for main menu window
        self.create_title().pack(expand = True, fill = "both")
        self.create_title_btns().pack(expand = False, fill = "both")
        
        self.mainloop()
        
    def create_title(self):
        """Custom Main Menu Title widget

        Returns:
            CtkFrame: Custom frame widget with label inside.
        """
        frm = ctk.CTkFrame(self)
        ctk.CTkLabel(frm, text = "WORD RAIDER II ", font=self.title_font).pack(expand = True, fill = "both")
        return frm
        
    def create_title_btns(self):
        """Custom main menu buttons widget

        Returns:
            CTkFrame: Custom frame widget with two buttons inside.
        """
        frm = ctk.CTkFrame(self)
        play_btn = ctk.CTkButton(frm, text = "PLAY", font = self.main_font, command = self.play_btn_press)
        quit_btn = ctk.CTkButton(frm, text = "QUIT", font = self.main_font, command = lambda: self.quit())
        
        quit_btn.pack(side = "bottom", pady = 30)
        play_btn.pack(side = "bottom")
        
        return frm
    
    def play_btn_press(self):
        """Open gameplay window and hide root window.
        """
        self.withdraw()
        self.gameplay_window = GameWindow()

class GameWindow(ctk.CTkToplevel):
    """Gameplay window for Word Raider II
    """
    guessed_word = []
    guesses = {}
    letter_btns = {}
    
    def __init__(self):
        super().__init__()
        # basic window config
        self.title("Word Raider II")
        self.resizable(False,False)
        
        title_font = ctk.CTkFont(family=title_font_family, size=36, weight="bold")

        # create title label, pack at top of window
        title_lbl = ctk.CTkLabel(self, text = "WORD RAIDER II ", font=title_font)
        title_lbl.pack(pady=5)
        
        # create frame for guess boxes, pack below title
        guess_frm = ctk.CTkFrame(self, fg_color="transparent")
        guess_frm.pack(pady=5)
        
        # create actual guess boxes and place inside frame
        for i in range (0,6):
            self.guesses[i] = GuessFrames(guess_frm)
        
        # create and place keyboard buttons below guess boxes
        self.keyboard = self.create_keyboard(self)
        self.keyboard.pack(pady=5)
        
        # variable to keep track of which guess user is on
        self.active_guess = 1
        
    def destroy(self):
        super().destroy()
        # closing gameplay window should also quit app.
        App.quit(self)
    
    def create_keyboard(self, parent):
        """Generate custom QWERTY keyboard widget with submit and backspace buttons.

        Args:
            parent (Any): Master for main frame widget.

        Returns:
            CTkFrame: Custom frame widget with buttons inside.
        """
        keyboard_font = ctk.CTkFont(family=main_font_family, size=18)
          
        def keyboard_letter_btn(letter):
            """Generate single letter button for the custom keyboard widget.

            Args:
                letter (str): Letter on face of keyboard button.

            Returns:
                CTkButton: Letter button for keyboard.
            """
            btn = ctk.CTkButton(keyboard_frm, text=letter, font=keyboard_font, command = lambda: self.choose_letter(letter), width=50, height=50)
            return btn
        
        # create main keyboard frame widget to be returned from func
        # also configure grid geometry
        keyboard_frm = ctk.CTkFrame(parent, fg_color="transparent")
        keyboard_frm.rowconfigure((0,1,2), weight = 1, uniform="a")
        keyboard_frm.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20), weight = 1, uniform="b")
        
        # loop to generate letter buttons as dict values
        for letter in letters:
            self.letter_btns[letter] = keyboard_letter_btn(letter)
        
        # generate submit and backspace buttons
        submit_btn = ctk.CTkButton(keyboard_frm, text="\u2713", font=keyboard_font, command = self.submit_guess, width=50, height=50)
        backspace_btn = ctk.CTkButton(keyboard_frm, text="\u232B", font=keyboard_font, command = self.backspace, width=50, height=50)
        
        # place buttons in keyboard grid
        self.letter_btns["Q"].grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["W"].grid(row=0, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["E"].grid(row=0, column=4, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["R"].grid(row=0, column=6, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["T"].grid(row=0, column=8, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["Y"].grid(row=0, column=10, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["U"].grid(row=0, column=12, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["I"].grid(row=0, column=14, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["O"].grid(row=0, column=16, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["P"].grid(row=0, column=18, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["A"].grid(row=1, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["S"].grid(row=1, column=3, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["D"].grid(row=1, column=5, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["F"].grid(row=1, column=7, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["G"].grid(row=1, column=9, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["H"].grid(row=1, column=11, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["J"].grid(row=1, column=13, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["K"].grid(row=1, column=15, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["L"].grid(row=1, column=17, columnspan=2, sticky="nsew", padx=5, pady=5)
        submit_btn.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
        self.letter_btns["Z"].grid(row=2, column=3, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["X"].grid(row=2, column=5, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["C"].grid(row=2, column=7, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["V"].grid(row=2, column=9, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["B"].grid(row=2, column=11, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["N"].grid(row=2, column=13, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.letter_btns["M"].grid(row=2, column=15, columnspan=2, sticky="nsew", padx=5, pady=5)
        backspace_btn.grid(row=2, column=17, columnspan=3, sticky="nsew", padx=5, pady=5)
        
        return keyboard_frm
        
    def choose_letter(self, letter):
        """Method executed when a keyboard letter button is pressed.

        Args:
            letter (str): Which letter button was pressed.
        """
        self.guessed_word.append(letter)
        
        print(f"The {letter} key was pressed.")
        print(self.guessed_word)
    
    def backspace(self):
        """Method executed when backspace keyboard button is pressed.
        """
        # not yet implemented
        print("The Backspace key was pressed.")
    
    def submit_guess(self):
        """Method executed when submit keyboard button is pressed.
        """
        # not yet implemented
        print("The Submit key was pressed.")
        
class GuessFrames(ctk.CTkFrame):
    """Custom widget containing 5 labels in 5 frames. Used for the guessed word. Labels will be filled when user presses the keyboard buttons.
    """
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.pack()
        
        # generate custom letter box widgets
        self.guess_letter_box1 = self.guess_letter_box()
        self.guess_letter_box2 = self.guess_letter_box()
        self.guess_letter_box3 = self.guess_letter_box()
        self.guess_letter_box4 = self.guess_letter_box()
        self.guess_letter_box5 = self.guess_letter_box()
        
    def guess_letter_box(self):
        """Generate custom frame widget containing a label for a single letter.

        Returns:
            CTkFrame: Custom widget.
        """
        guess_font = ctk.CTkFont(family=main_font_family, size=24)
        
        # generate frame and label, pack label inside frame, and pack frame from left inside larger frame
        letter_box_frm = ctk.CTkFrame(self, border_width=5, width=50, height=50)
        letter_box_lbl = ctk.CTkLabel(letter_box_frm, text="X", font=guess_font, width=50, height=50)
        letter_box_frm.pack(side="left", padx=5, pady=10)
        letter_box_lbl.pack()
        
        return letter_box_frm
        
App()