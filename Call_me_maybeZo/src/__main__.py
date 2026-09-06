from important import main
from sys import exit

if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print("\033[031m", e, "\033[0m")
        exit(1)
