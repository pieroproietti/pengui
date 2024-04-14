# penGUI take cure of eggs!
penGUI makes it easier to learn eggs commands: once you learn them, you will probably use it less, but a GUI for penguins-eggs was needed and is now there is.

![icon](https://github.com/pieroproietti/pengui/raw/main/assets/pengui.png?raw=true)

**Status:** starting from **0.7.x** series penGUI, is again a little wild, but usable and I recommend it, expecially for new users.

**Notice:** In case penGUI does not start, you can try installing `libxcb-cursor`. eg:

```
sudo apt-get install libxcb-cursor
```

I tried penGUI on Debian and Arch. There is not yet a package for Arch, Manjaro and derivatives but you can directly use the [pengui-0-7-x.bin](https://sourceforge.net/projects/penguins-eggs/files/DEBS/) which is an executable.

# Download

You can download [penGUI](https://sourceforge.net/projects/penguins-eggs/files/DEBS/) and install it with `dpkg -i pengui-0.7.x.deb` and start from the terminal giving: `pengui` as normal user or from the the usual desktop link. 

The icon is changed now, I still a penguin from [wikipedia](https://en.wikipedia.org/wiki/File:Penguin_icon.svg#filelinks), the icon was created from user FormalDude: thanks a lot! I like it very much, and I think can adopt this nice penguin, we need same others icons too and I home some graphic designer will take the trouble to design a custom icon, I'm not able.

## x-terminal-emulator
penGUI uses `x-terminal-emulator` to open a terminal window and launch eggs commands; which terminal will be opened depends on your configuration, but you can change it with the command:

`sudo update-alternatives --config x-terminal-emulator`

On my development machine, I feelme confortable with `xfce4-terminal`.

## Arch
On Arch I just created a link:

`sudo ln -sf /usr/bin/xfce4-terminal /usr/bin/x-terminal-emulator`


# Development prerequisites
For penGUI development I am using python 3.11.2 and PySide6 on a common Debian bookworm, in my case the classic [colibri](https://sourceforge.net/projects/penguins-eggs/files/ISOS/debian/bookworm/amd64/). 

I added only the following packages:

`sudo apt install build-essential`

`sudo apt install python3-pip python3-venv`

For pyside6 to work properly, I also installed:

`sudo apt install libxcb-cursor0` 

# sources
This is the repository of pengui, to get this sources just: 

`git clone https://github.com/pieroproietti/pengui`

It is recommended, however to create yourself a [fork](https://github.com/pieroproietti/pengui/fork) of the repository, so that you can manage the project yourself and possibly create some [Pull Requests](https://github.com/pieroproietti/pengui/pulls).

# start to develop
Just run `bin/create_venv` from the root of the project and and follow the instructions. Under `bin`, there are usefull scripts to `run`, `create-bin`, `create-deb`, etc. They must always be run from the root of the project and have a self-explanatory name.

## nuitka
We are using **nuitka 2.1.5** on **python 3.11.2**. To create bin, we need to install:

`sudo apt install ccache patchelf`

## fpm
To create Debian packages we need to install fpm. 

First install ruby `sudo apt install ruby`, then with gem, install fpm.

