import sys


class TheCommandLiner():
    def __init__(self):
        passed_arguments = len(sys.argv)
        if passed_arguments != 2:
            print(f"[-] ERROR : Incorrect Number of Parameters passed to this aching application ... sigh ...")
            sys.exit(1)

    def path_finder(self):
        file_path = sys.argv[1]

        return file_path
