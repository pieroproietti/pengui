## **penGUI take cure of eggs!**
![icon](https://github.com/pieroproietti/pengui/blob/main/assets/pengui.png?raw=true)

**Notice:** pengui is not yet a finished software, it is still in embryo and is deciding how
 to grow, however is starting to be usefull to get configuration and produce. 

 You can run all the eggs commands menu, on the toolbar we have just the most used: Dad, Produce and kill.

You can simply install it with `dpkg -i pengui-0.1.x.deb` and start it with `sudo pengui` or from the desktop link. 

The icon is that of penguins-eggs, I hope some graphic designer will take the trouble to design another one, for those who would like to participate in the project entering currently is easy, the project has just started.

To check the progress of the project status refer to the [CHANGELOG](https://github.com/pieroproietti/pengui/blob/main/CHANGELOG.md).


## x-terminal-emulator
pengui calls x-terminal-emulator to open a terminal window, you can varial your configuration with the command:

`sudo update-alternatives --config x-terminal-emulator`

On my development machine, I normally use `xfce4-terminal`.

## dbus-x11
Since we are going to open a terminal as root, using sudo, we need to have the `dbus-x11` package installed. So, before using the program, install it:

`sudo apt-get install dbus-x11`
'sudo service dbus restart'

# pengui

pengui makes it easy for you to learn eggs commands, once you learn them you will probably use it less, but a GUI for penguins-eggs was needed and now there is.

I'm using python 3.11.2 and PySide6 to build the program.

## Install pengui
pengui is not yet included pm penguins-eggs-ppa, so dowload it from the [penguins-eggs page on sourceforge](https://sourceforge.net/projects/penguins-eggs/files/pengui/) andi install it with `sudo dpkg -i pengui-0.1.x-x.deb`

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
