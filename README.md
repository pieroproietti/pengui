# penGUI


## **penGUI take cure of eggs!**
![](https://github.com/pieroproietti/penguins-eggs/blob/master/assets/eggs.png)


penGUI makes it easy for you to learn eggs commands, once you learn them you will probably use it less, but a GUI for penguins-eggs was needed and now there is.

I'm using python 3.11.2 and PySide6 to build the program.

## Prerequisites

I'm using Debian bookworm, just installed this packages to my [colibri](https://sourceforge.net/projects/penguins-eggs/files/ISOS/debian/bookworm/arm64/):

`sudo apt install build-essential`

`sudo apt install python3-full python-is-python3`

It seem we need for QT following packages too: 
`sudo apt install libxcb-cursor0 libpython3.11` 

# sources
This is the repository of pengui, to get this sources just: 

`git clone https://github.com/pieroproietti/pengui`

Perhaps will be better to [fork](https://github.com/pieroproietti/pengui/fork) the repository before of that, so you will be able to create [Pull Request](https://github.com/pieroproietti/pengui/pulls) and follow the project.

# venv
Just run `./bin/create_venv and` and follow the instructions.

# future plan

## poetry
I will like to manage the package with `poetry`, perhaps simply for love of poetry!

* `sudo apt install pipx`
* `pipx ensurepath`
* `pipx install poetry`
* `poetry completions bash >> ~/.bash_completion`

## pydantic
I come from typescript and love to declare variables and get help from editors. Probably pydantic will offer something.
