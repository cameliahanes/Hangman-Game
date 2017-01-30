from src.Console.Console import Console
from src.Controller.Controller import *
from src.Repository.Repository import Repository

if __name__ == '__main__':
    repository = Repository( True)
    controller = HangmanController(repository)
    console = Console(controller)
    console.run()