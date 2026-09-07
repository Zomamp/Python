import sys
try:
    from important import main
    from sys import exit
    import time
except Exception as e:
    print(e)
    sys.exit(1)

if __name__ == "__main__":
    try:
        begin = time.time()
        main()
        end = time.time()
        result = end - begin
        if result >= 200:
            print(f"\nOh no ! the program take a lot of time 😕 => \033[031m{result}\033[0m")
        elif result <= 50:
            print(f"\n😄 Felicitation the program is over at => \033[033m{result}\033[0m")
        elif result <= 30:
            print(f"\n🙌🎉 Congratulation => \033[032m{result}\033[0m")

    except FileNotFoundError as e:
        print("\033[031m", e, "\033[0m")
        exit(1)
