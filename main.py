import time
from Bot import Bot
import requests

def main():
    b = Bot("BooBoo", True, 4)
    botList = []
    for i in range(500):
        botList[i] = Bot("change this please", True, 4)


if __name__ == "__main__":
    main()