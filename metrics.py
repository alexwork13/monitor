import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "cpu":
            print("You see cpu monitor")
        elif sys.argv[1] == "mem":
            print("You see mem yest")
        else:
            print("Please, enter parametr")
    else:
        print("Please, enter parametr")