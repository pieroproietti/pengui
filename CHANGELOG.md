## **penGUI take cure of eggs!**
![icon](https://github.com/pieroproietti/pengui/blob/main/assets/pengui.png?raw=true)

# CHANGELOG
This project started near the end of the 2023, due my necessity to improve my ability with python and learn about GUI.

I tried - same time ago - to use electron, but at last eventually I decided to try it again in python, and I am seeing good results in terms of lightness and practicality of development.

# Versions

## pengui-0.2.2
* added calamares --install, calamares --remove, status and cuckoo (disabled);
* fixed icon, finally!!!

## pengui-0.1.9
* penGUI now is used always with normal user, no root:
* before to open a Terminal, penGUI will show a message box, to accept or nome.

I chose to configure pengui for exclusive use as a normal user, because it gives me problems with the terminal call and wardrobe commands.

## pengui-0.1.8
* check presence of eggs at start and suggest installation of it;
* added some advices on status bar:
* a lot of tempts with terminal, unproductive for now.

## pengui-0.1.7
* replaced names with isons in toolbar:
* replaced comboBox with checkBox to select filters;

## pengui-0.1.6
* changed main icon;
* added dialog config tools;

## pengui-0.1.5
* improved dialogs, added help

## pengui-0.1.4
* dialogs open now in the center of the mainwindow;
* a lot of temps to see for terminal but improductive.

## pengui-0.1.3
* a bit dirthy work, but now dialogs act as dialogs.
* fixed problems using root without wardrobe

## pengui-0.1.2
* added working skeleton toolbar and statusbar;

## pengui-0.1.1
* I started to release the package as Debian package, building as pengui.bin using `pyside6-deploy`, then adding a fakeroot and icon, pengui.desktop and a symbolic link, finally creating Debian package with `fpm`;
* Dialogs produce and eggs_configuration are working now.
* starting to count versions of pengui.

**Note**: I was not able to open terminal until I changed  x-terminal-emulator configuration. pengui calls `x-terminal-emulator` to open a terminal window. You can change your configuration with the command:

`sudo update-alternatives --config x-terminal-emulator`

On my development machine, I normally use `xfce4-terminal`.

## pengui.bin
At the moment just the dialog produce is implemented and connected to the pengui, I have another two widget: eggs_configuration, already working and terminal to invent again.

With produce, just select File ->Produce, you can compose the command in a GUI, then copy and paste the result in a terminal.

For now, 30 december 2023 is enought!
