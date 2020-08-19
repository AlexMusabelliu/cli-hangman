import os, time, random
import numpy as np
import framebank as fb

class Screen():
    def __init__(self, dtype=[], word="bird"):
        # if type(dtype) == str:
            # dtype = list(dtype)
        self.LIGHTNING_CHAR = "x"
        self.mem = dtype
        self.word = word
        self.spacer_func = (lambda x: " " * ((102 - len(x)) // 2) + x + " " * ((101 - len(x)) // 2))
        self.right = (lambda x: x[:-1])("▃ " * len(word))
        self.word_block = self.spacer_func(self.right)
        self.right = len(self.word) * "▃"
        self.check = 0

    def disp(self, dtype=None):
        if dtype:
            self.mem = dtype
        print(self)

    def process2(self, g, wrong=0):
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
        def get_indexes(d, k):
            r = []
            for i in range(len(d)):
                if d[i] == k:
                    r.append(i)
            return r
        
        g = g.lower()
        
        if g not in self.word:
            return False

        to_replace = get_indexes(self.word, g)
        for i in to_replace:
            self.right = self.right[:i] + g + self.right[i + 1:]

        self.word_block = self.spacer_func("".join([x + " " for x in self.right])[:-1])

        return (True, wrong) if self.word_block.count("▃") == 0 else (False, wrong)

    def die(self):
        def lightning(d):
            pic = ""
            for i in range(25):
                row = d[0 + i * 102:102 + i * 102]

                r = random.randint(0, len(row) - 1)
                while row[r] != "1":
                    r = random.randint(0, len(row) - 1)

                pic += row[:r] + "x" + row[r + 1:]
            return pic

        def flash(default=fb.clear, repeat=0):
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
        self.disp(fb.win_frame)

    def __str__(self):
        os.system("cls")
        os.system("mode con: cols=101 lines=29")
        return "".join(["\n"] + ["█" if x == "1" else " " if x == "-" else x for x in self.mem]) + "\n" * 2 + self.word_block

    def __repr__(self):
        return self.__str__()

def main():
    s = Screen([], "epicasdsd")
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

        if wrong == len(frames) - 1:
            s.die()
            break
        
        WON, wrong = s.process(guess, wrong)
        

    if WON:
        s.win()

    time.sleep(3)


if __name__ == "__main__":
    main()