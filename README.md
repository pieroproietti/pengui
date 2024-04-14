## **penGUI take cure of eggs!**
![icon](https://github.com/pieroproietti/pengui/blob/main/assets/pengui.png?raw=true)

**Notice:** starting from 0.7.x series penGUI, is again a little wild but is usable and I recommend it, expecially for new users.

**Notice:** penGUI is not yet a finished software, it is still in embryo and is deciding how to grow. However, it is already useful for both experts and novices to set up eggs and also to get-at a glance-a complete picture. You can find and run all the eggs commands from the menu; on the toolbar we have just the most used commands: `dad`, `produce` and `kill`.

**Notice:** In case penGUI does not start, you can try installing `libxcb-cursor`. eg:

```
sudo apt-get install libxcb-cursor
```

I tried pengui on Debian and Arch, on arch I used the .bin version, there is not a PKGBUILD for now.

On Debian and Arch is working, start and - on Debian can produce ISOs - on Arch I don't know why refuse.

# Download

You can download [penGUI](https://sourceforge.net/projects/penguins-eggs/files/DEBS/) and install it with `dpkg -i pengui-0.7.x.deb` and start from the terminal giving: `pengui` as normal user or from the the usual desktop link. There is not yet a package for Arch, Manjaro and derivatives but you can directly use the [pengui-0-7-x.bin](https://sourceforge.net/projects/penguins-eggs/files/DEBS/) which is an executable.

The icon is changed now, I still a penguin from [wikipedia](https://en.wikipedia.org/wiki/File:Penguin_icon.svg#filelinks), the icon was created from user FormalDude: thanks a lot! I like it very much, and I think can adopt this nice penguin, we need same others icons too and I home some graphic designer will take the trouble to design a custom icon, I'm not able.

To check the progress of the project status refer to the [CHANGELOG](https://github.com/pieroproietti/pengui/blob/main/CHANGELOG.md), however things are changing rapidly and penGUI can already be considered usable.

## x-terminal-emulator
penGUI uses `x-terminal-emulator` to open a terminal window and launch eggs commands; which terminal will be opened depends on your configuration, but you can change it with the command:

`sudo update-alternatives --config x-terminal-emulator`

On my development machine, I feelme confortable with `xfce4-terminal`.


## Arch
On Arch I just created a link:

`sudo ln -sf /usr/bin/xfce4-terminal /usr/bin/x-terminal-emulator`



# penGUI
penGUI makes it easier to learn Eggs commands; once you learn them, you will probably use it less, but a GUI for penguins-eggs was needed and is now there.

![icon](https://github.com/pieroproietti/pengui/blob/main/assets/penGUI.png?raw=true)

## Development prerequisites
For penGUI development I am using python 3.11.2 and PySide6 on a common Debian bookworm, in my case the classic [colibri](https://sourceforge.net/projects/penguins-eggs/files/ISOS/debian/bookworm/amd64/). 

I added only the following packages:

`sudo apt install build-essential`

`sudo apt install python3-full python-is-python3`

For pyside6 to work properly, I also installed:

`sudo apt install libxcb-cursor0 libpython3.11` 

# sources
This is the repository of pengui, to get this sources just: 

`git clone https://github.com/pieroproietti/pengui`

It is recommended, however to create yourself a [fork](https://github.com/pieroproietti/pengui/fork) of the repository, so that you can manage the project yourself and possibly create some [Pull Requests](https://github.com/pieroproietti/pengui/pulls).

# start to develop
You need to install `sudo apt install python3-pip python3-venv` 

Just run `bin/create_venv` from the root of the project and and follow the instructions. Under `bin`, there are usefull scripts to `run`, `create-bin`, `create-deb`, etc. They must always be run from the root of the project and have a self-explanatory name.

# nuitka
We are using nuitka 2.1.4 on python 3.11. 

`sudo apt install ccache patchelf`

# fpm
To create debian packages we use fpm. 

First install ruby `sudo apt install ruby`, them with gem install fpm.

