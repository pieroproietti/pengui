## **penGUI take cure of eggs!**
![icon](https://github.com/pieroproietti/pengui/blob/main/assets/pengui.png?raw=true)

**Notice:** penGUI is not yet a finished software, it is still in embryo and is deciding how to grow. However, it is already useful for both experts and novices to set up eggs and also to get-at a glance-a complete picture. You can find and run all the eggs commands from the menu; on the toolbar we have just the most used commands: `dad`, `produce` and `kill`.

You can download [penGUI](https://sourceforge.net/projects/penguins-eggs/files/penGUI/) and install it with `dpkg -i pengui-0.2.x.deb` and start from the terminal giving: `pengui` as normal user or from the the usual desktop link. 

The icon is changed now, I still a penguin from [wikipedia](https://en.wikipedia.org/wiki/File:Penguin_icon.svg#filelinks), the icon was created from user FormalDude: thanks a lot! I like it very much, and I think can adopt this nice penguin, we need same others icons too and I home some graphic designer will take the trouble to design a custom icon, I'm not able.

To check the progress of the project status refer to the [CHANGELOG](https://github.com/pieroproietti/pengui/blob/main/CHANGELOG.md), things are changing speedly actually, and penGUI can be considered usable.


## x-terminal-emulator
pengui calls x-terminal-emulator to open a terminal window, you can varial your configuration with the command:

`sudo update-alternatives --config x-terminal-emulator`

On my development machine, I normally use `xfce4-terminal`.

## dbus-x11
Since we are going to open a terminal as root, using sudo, we need to have the `dbus-x11` package installed. So, before using the program, install it:

`sudo apt-get install dbus-x11`
'sudo service dbus restart'

# penGUI

penGUI makes it easy for you to learn eggs commands, once you learn them you will probably use it less, but a GUI for penguins-eggs was needed and now there is.

I'm using python 3.11.2 and PySide6 to build the program.

## Install penGUI
penGUI is not yet included pm penguins-eggs-ppa, so download it from the [penguins-eggs page on sourceforge](https://sourceforge.net/projects/penguins-eggs/files/pengui/) andi install it with `sudo dpkg -i pengui-0.2.x.deb`

## Development prerequisites

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
