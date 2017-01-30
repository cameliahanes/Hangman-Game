class Console:
    def __init__(self, controller):
        self.__controller = controller

    def run(self):
        print('{: ^30}\n{:^29}\n{: ^32}'.\
              format('=Hangman=','        add <sentence>\n            play\n', ''))
        while True:
            try:
                inp = input()
                arg = self.argumented(inp)
                if arg:
                    if arg['command'] == 'add':
                        self.__controller.add_sentence(" ".join(arg['args']))
                    elif arg['command'] == 'play':
                        self.game_menu()
            except Exception as e:
                print(e)


    def argumented(self, inp):
        argd = inp.strip().split(" ")
        if len(argd) == 0:
            return False
        if argd[0] == "":
            return False
        argd = [a.strip() for a in argd]
        #the spaces are removed
        cmd = argd.pop(0).lower()
        return {
            'command':cmd,
            'args':argd
        }

    def game_menu(self):
        game = self.__controller.start_new_game()
        print("".join(game.get_sentence()))
        while True:
            ip = input("letter: ")
            if len(ip) > 1:
                print("Enter only a letter!")
                continue
            result = game.play(ip)
            print("\n".join(hangmans[result.trials]))
            print("".join(result.sentence))
            if result.state == -1:
                print("Game failed!")
                return
            if result.state == 2:
                print("Congratulations, you won the game!")
                return

hangmans = [["__________","|         |","|         0","|        /|\\","|        / \\","|","|", "hangman"],
            ["__________","|         |","|         0","|        /|\\","|        / ","|","|","hangma"],
            ["__________","|         |","|         0","|        /|\\","|        ","|","|","hangm"],
            ["__________","|         |","|         0","|        /|","|        ","|","|","hang"],
            ["__________","|         |","|         0","|        /","|        ","|","|","han"],
            ["__________","|         |","|         0","|        ","|        ","|","|","ha"],
            ["__________","|         |","|         ","|        ","|        ","|","|","h"],
            ["__________","|         ","|         ","|        ","|        ","|","|"]
            ]

