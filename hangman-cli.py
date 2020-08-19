import os, time, random
import numpy as np
# framebank is just where the frames for the hangman game are stored as they take up quite some space.
import framebank as fb

class Screen():
    '''
    A simple class meant to host the hangman game. Contains methods to update the screen and process input. To get the screen to show, print the object or call the disp() function.
    Args:
        dtype (def=[]) :: an iterable; the default screen to display, like the ones in framebank.py
        word (def="bird") :: a str; the word used in the hangman game 
    '''
    def __init__(self, dtype=[], word="bird"):
        # if type(dtype) == str:
            # dtype = list(dtype)
        word = word.lower()
        self.LIGHTNING_CHAR = "x"
        self.mem = dtype
        self.word = word
        self.spacer_func = (lambda x: " " * ((102 - len(x)) // 2) + x + " " * ((101 - len(x)) // 2))
        self.right = (lambda x: x[:-1])("▃ " * len(word))
        self.word_block = self.spacer_func(self.right)
        self.right = len(self.word) * "▃"
        self.check = 0

    def disp(self, dtype=[]):
        '''
        Displays a picture.
        Args:
            dtype (def=self.mem) :: an iterable of characters to be displayed. "-" characters are turned into whitespace. "1"'s are turned into full-blocks ("█") 
        '''
        if dtype != self.mem:
            self.mem = dtype
        print(self)

    def process2(self, g, wrong=0):
        '''
        A secondary, unused process method. Takes in a guess for the word. Correct guesses are those that are in order, starting with the first character.
        Args:
            g :: a str; the guess to be processed
            wrong (def=0) :: the number of wrong guesses accumulated thus far
        Returns:
            (won, wrong) :: a tuple; won is a boolean, whether or not the player has won and wrong is the number of wrong guesses thus far, either increased or the same

        Example:
            The word is "bird"

            Display:
                _ _ _ _
            Guess:
                "g" -> incorrect
                "i" -> incorrect
                "d" -> incorrect
                "b" -> correct
                "bir" -> correct
                "bi" -> correct
                "bird" -> correct

            Second display:
                b i _ _
            Seoncd guess:
                "rd" -> correct
                "r" -> correct
                "d", etc -> incorrect
        '''
        g = g.lower()
        spacer = 0
        for i in range(len(g)):
            if len(g) <= len(self.word) - self.word_block.count("▃"):
                spacer = len(self.word) - self.word_block.count("▃")
            # print(g[i], self.word[i + spacer], spacer, self.word_block.count("▃"), len(self.word), len(g))
            if g[i] != self.word[i + spacer]:
                self.disp(fb.wrong)
                time.sleep(1)
                return False, wrong + 1
        
        for i in range(len(g)):
            l = self.word_block.find("▃")
            # print(self.word_block.count("▃"))
            self.word_block = self.word_block[:l] + self.word[i + spacer] + self.word_block[l + 1:]
        
        return (True, wrong) if self.word_block.count("▃") == 0 else (False, wrong)

    def process(self, g, wrong=0):
        '''
        Proccesses input based on hangman rules: guesses can be in any order; the guess must be one character long; the guess, to be correct, must be in the word.
        Args:
            g :: a str; the guess to be processed
            wrong :: the number of wrong guesses thus far, cumulative
        Returns:
            (won, wrong) :: a tuple; won is a boolean, whether or not the player has won and wrong is the number of wrong guesses thus far, either increased or the same

        Example:
            1.
            The word is "bird"

            Display:
                _ _ _ _
            Guess:
                "i" -> correct; display is now: _ i _ _
                "d" -> correct; display is now: _ _ _ d
                "e" -> incorrect
                "g" -> incorrect

            2.
            The word is "nonogram"

            Display:
                _ _ _ _ _ _ _ _
            Guess:
                "n" -> correct; display is now: n _ n _ _ _ _ _
                "m" -> correct; display is now: _ _ _ _ _ _ _ m
                anything but the characters in "nonogram" -> incorrect
        '''
        def get_indexes(d, k):
            r = []
            for i in range(len(d)):
                if d[i] == k:
                    r.append(i)
            return r
        
        g = g.lower()
        
        if g not in self.word:
            return False, wrong + 1

        to_replace = get_indexes(self.word, g)
        for i in to_replace:
            self.right = self.right[:i] + g + self.right[i + 1:]

        self.word_block = self.spacer_func("".join([x + " " for x in self.right])[:-1])

        return (True, wrong) if self.word_block.count("▃") == 0 else (False, wrong)

    def die(self):
        '''
        The player died! Plays the death animation of our little hangman ;^(
        This hangman does not hang, though - he is electrocuted! This is the 21st century, after all: there are more efficient (and humane?) ways to do things!
        Args:
            N/A
        Returns:
            N/A
        '''
        def lightning(d):
            '''
            Adds "x"'s to represent lightning to a picture, randomly, one x per line.
            Args:
                d :: an iterable; the data to add lightning to
            '''
            pic = ""
            for i in range(25):
                row = d[0 + i * 103:102 + i * 103]

                r = random.randint(0, len(row) - 1)
                while row[r] != "1":
                    r = random.randint(0, len(row) - 1)

                pic += row[:r] + "x" + row[r + 1:]
            return pic

        def flash(default=fb.clear, repeat=0):
            '''
            Displays flashes of bright white light. Ough, my eyes!
            Args:
                default (def=fb.clear) :: an iterable; the default screen to return to post-flash
                repeat (def=0) :: the number of times to repeat the flashing
            '''
            for i in range(repeat + 1):
                self.disp(fb.flash)
                time.sleep(0.3)
                self.disp(default() if callable(default) else default)
                time.sleep(0.3)

        for i in range(len(self.word)):
            l = self.word_block.find("▃")
            self.word_block = self.word_block[:l] + self.word[i] + self.word_block[l + 1:]

        time.sleep(1)
        flash((lambda: lightning(fb.full)), 3)
        time.sleep(0.7)
        self.disp(fb.dead)
        time.sleep(2)
        self.disp(fb.lose)
    
    def win(self):
        '''
        The player won! Displays the win frame.
        Args:
            N/A
        Returns:
            N/A
        '''
        self.disp(fb.win_frame)

    def __str__(self):
        '''
        Allows printing of the object to display the internal picture in the cmd. "mode con:..." is made for Windows CMD.
        '''
        os.system("cls")
        # os.system("mode con: cols=101 lines=29")
        return "".join(["\n"] + ["█" if x == "1" else " " if x == "-" else x for x in self.mem]) + "\n" * 2 + self.word_block

    def __repr__(self):
        return self.__str__()

def main():
    WORD = "Nice"

    s = Screen([], WORD)
    frames = [fb.clear, fb.head, fb.head_w_eyes, fb.head_full, fb.body, fb.one_arm, fb.arms, fb.one_leg, fb.full]
    wrong = 0
    WON = False

    while not WON:
        s.disp(frames[wrong])
        time.sleep(0.3)
        guess = input("Give a guess!    ")

        if len(guess) > 1:
            print("Do it again: one character only!")
            time.sleep(1)
            continue

        if wrong == len(frames):
            s.die()
            break
        
        WON, wrong = s.process(guess, wrong)
        

    if WON:
        s.win()

    time.sleep(3)


if __name__ == "__main__":
    main()