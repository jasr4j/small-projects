#! /usr/bin/env python3

import os


def init():
    i = input(
        "Where should the project directory be created (complete file path, i.e. /home/username/Desktop/directory)? "
    )
    j = input("What should the project directory be named? ")

    os.system(f"cd {i} && mkdir {j} && cd {j}")
    print("Created project directory")
    return i, j


def bash_init():

    i, j = init()
    os.system(
        f"cd {i} && cd {j} && mkdir src && cd src && touch app.sh && chmod +x app.sh"
    )
    print("Created src folder and created app.sh file")

    k = int(input("README.txt = 0; README.md = 1: "))
    if k == 1:
        os.system(f"cd {i} && cd {j} && touch README.md")
    else:
        os.system(f"cd {i} && cd {j} && touch README.txt")
    print("README created")

    l = int(input("Temporary Test Dir. called tmp (Yes = 1; No = 0): "))
    if l == 1:
        os.system(
            f"cd {i} && cd {j} && mkdir tmp && cd tmp && touch test01.sh && chmod +x test01.sh"
        )
        print("Created tmp folder and added test01.sh")
        os.system("cd ..")

    print(
        "Remember to add the shebang line #!/usr/bin/env bash to the beginning of the .sh files to make them executable in the terminal.\nRun the files by running the command ./app.sh or ./test01.sh"
    )


def py_init():
    i, j = init()
    j = j.strip()
    i = i.strip()

    print("Only 1 module file will be created in the project folder")

    os.system(
        f"cd {i} && cd {j} && touch main.py && chmod +x main.py && mkdir project && cd project && touch module.py && chmod +x module.py && touch __init__.py && chmod +x __init__.py"
    )
    print(
        "Created project folder and created module.py, __init__.py, and main.py files"
    )

    k = int(input("README.txt = 0; README.md = 1: "))
    if k == 1:
        os.system(f"cd {i} && cd {j} && touch README.md")
    else:
        os.system(f"cd {i} && cd {j} && touch README.txt")
    print("README created")

    l = int(input("Temporary Test Dir. called tmp (Yes = 1; No = 0): "))
    if l == 1:
        os.system(
            f"cd {i} && cd {j} && mkdir tmp && cd tmp && touch test01.py && chmod +x test01.py"
        )
        print("Created tmp folder and added test01.py")
        os.system("cd ..")

    print(
        "Remember to add the shebang line #!/usr/bin/env python3 to the beginning of the .py module files to make them executable in the terminal.\nRun the files by running the command ./app.py or ./test01.py"
    )


def node_init():
    i, j = init()

    k = int(
        input(
            "Is npm (node package manager) installed? \nIf it's installed, enter 1. If it's not installed, for zsh, enter 2, and for bash, enter 0. \n"
        )
    )
    if k != 1:
        os.system(
            "wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash"
        )
        if k == 0:
            print("Add the following text to the file ~/.bash_profile")
            print("Text: ")
            str1 = r'export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"'
            str2 = r'[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"'
            print(f"{str1}\n{str2}")
            print(
                "Open a new terminal window using Ctrl+Alt+T and then type nano ~/.bash_profile.\nAdd the text above the file and then do Ctrl+S and Ctrl+X to save and exit"
            )
            os.system("source ~/.bashrc")
        elif k == 2:
            print("Add the following text to the file ~/.zshrc")
            print("Text: ")
            str1 = r'export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"'
            str2 = r'[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"'
            print(f"{str1}\n{str2}")
            print(
                "Open a new terminal window using Ctrl+Alt+T and then type nano ~/.zshrc.\nAdd the text above the file and then do Ctrl+S and Ctrl+X to save and exit"
            )
            os.system("source ~/.bashrc")
        print("Updating node.js to the latest version...")
        os.system("nvm install latest")

    os.system(f"cd {i}/{j} && npm init -y")
    os.system(f"cd {i}/{j} && touch index.js && chmod +x index.js")
    print(
        "Remember to add the shebang line #!/usr/bin/env node to the beginning of the index.js file to make it executable in the terminal. \nRun the files by running the command ./index.js or node . in the project directory"
    )
    print(
        r'For command line tools, in the package.json file, under "main": index.js, add "type": "module",'
    )
    print("Then save the file and begin working. ")


def main():
    lang = int(input("Command-Line Tool Language\nPython = 1; Node.js = 2; Bash = 3: "))
    match lang:
        case 1:
            py_init()
        case 2:
            node_init()
        case 3:
            bash_init()
        case _:
            print(
                "If you made an error in the input, please rerun the tool and try again"
            )
            quit()
    x = {
        1: "Python",
        2: "Node.js",
        3: "Bash",
    }

    y = x[lang]

    print(f"Your {y} project has been initialized")


main()
