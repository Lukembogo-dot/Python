class secretstash:
    def __init__(self):
        self.__choclates = 10
    def get_chocolates(self):
        if self.__choclates > 0:
            self.__choclates -= 1
            print("Chocolate taken!")
        else:
            print("No chocolates left!")

stash = secretstash()
stash.get_chocolates()