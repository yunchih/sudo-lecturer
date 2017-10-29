import random
import subprocess

class CowLecturer:
    cows = [
        "bong","default","dragon","elephant","eyes","kitty","moose","small",
        "stegosaurus","three-eyes","turkey","turtle","udder","www"
    ]

    msgs = [
        "KID!!!  Don't you know `sudo` will blow the earth?",
        "Man! holy `sudo` is untouchable!",
        "Don't even attempt to stain `sudo` with your dirty fingers.",
        "Doraemon couldn't `sudo`, either, even in 21th century. QQ",
        "Boy! The `sudo` command will be given to you as a Christmas present.",
        "How about `sudo rm -fr --no-preserve-root`?",
        "I bet you copy-and-paste this silly command from the Internet ....",
        "`sudo` on CSIE workstation?  You should have taken Prof. Hsin-Mu Tsai's NASA course ..."
    ]

    tail_msg = "\t\t\t\t\tBy ta217"

    def generate(self):
        random.shuffle(self.cows)
        random.shuffle(self.msgs)

        res, err = "", "None"
        while err:
            cow, msg = self.cows[0], self.msgs[0]
            process = subprocess.Popen(['cowsay', '-W', '50', '-f', cow],
                                       stdout=subprocess.PIPE,
                                       stdin=subprocess.PIPE,
                                       universal_newlines=True)
            res, err = process.communicate(input=msg)
            res += "\n%s\n\n" % self.tail_msg

        return res

    def deliver(self, path):
        lecture = self.generate()
        with open(path, "w") as f:
            f.write(lecture)
