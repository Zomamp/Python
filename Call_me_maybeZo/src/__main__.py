"""main of the program."""
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
        print(
            "\033[039m  _____          _      _          "
            "__  __ ______      __  __      __     ______  ______ \n"
            " / ____|   /\\   | |    | |        "
            "|  \\/  |  ____|    |  \\/  |   /\\\\ \\   / /  _ \\|  ____|\n"
            "| |       /  \\  | |    | |"
            "  ______| \\  / | |__ ______| \\  / |  "
            "/  \\\\ \\_/ /| |_) | |__   \n"
            "| |      / /\\ \\ | |    | | |______| "
            "|\\/| |  __|______| |\\/| | / /\\ \\\\   "
            "/ |  _ <|  __|  \n"
            "| |____ / ____ \\| |____| |____    "
            "| |  | | |____     | |  | |/ ____ \\| |  | |_) | |____ \n"
            " \\_____/_/    \\_\\______|______|   "
            "|_|  |_|______|    |_|  |_/_/    \\_\\_|  |____/|______|\n"
            "                                  "
            "                                "
            "                       \n"
            "                                         "
            "                                                \n")
        print("\033[038mInitialisation ...\033[0m")
        begin = time.time()
        main()
        end = time.time()
        result = int(end - begin)
        minutes = int(result // 60)
        secondes = int(result % 60)
        if minutes >= 5:
            print("\nOh no ! the program take a lot of time 😕 "
                  f"=> \033[031m{minutes} m {secondes} s\033[0m")
        else:
            print("\n🙌🎉 Congratulation "
                  f"=> \033[032m{minutes} m {secondes} s\033[0m")

    except FileNotFoundError as e:
        print("\033[031m", e, "\033[0m")
        exit(1)
