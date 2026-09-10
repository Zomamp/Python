import sys
try:
    from .important import main
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
        if result >= 300:
            print("\nOh no ! the program take a lot of time 😕 "
                  f"=> \033[031m{result}\033[0m")
        else:
            print("\n🙌🎉 Congratulation "
                  f"=> \033[032m{result}\033[0m")

    except FileNotFoundError as e:
        print("\033[031m", e, "\033[0m")
        exit(1)
