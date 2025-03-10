import os
import sys
import subprocess


class main:
    def __init__(self):
        file = os.path.join(os.path.dirname(__file__), ".system/index.py")
        if not os.path.exists(file):
            print("Failed to launch package!")
            sys.exit()

        index = file.replace("\\", "/")
        command = f'clight execute "{index}"'
        subprocess.run(command, shell=True, check=True)
        pass


if __name__ == "__main__":
    app = main()
