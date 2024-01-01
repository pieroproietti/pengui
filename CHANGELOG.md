## **penGUI take cure of eggs!**
![icon](https://github.com/pieroproietti/pengui/blob/main/assets/pengui.png?raw=true)

## State
This project started near the end of the 2023, due my necessity to improve my ability with python and learn about GUI.

I tried - same time ago - to use electron, but at last eventually, partly for work reasons, I decided to try it again in python, and I am seeing good results in terms of lightness and practicality of development.

# Versions

## pengui-0.1.1

2024 January, 1

## pengui-0.1.0-1
* I started to release the package as Debian package, building as pengui.bin using `pysoide6-deploy`, then adding a fakeroot and icon, pengui.desktop and link, finally creating Debian package with `fpm``;
* Dialogs produce and eggs_configuration are working, but I'm not yet able to get working the terminal once installed in a clean system. Note: from the source or installed on the development machine it is working;
* starting to count versions of pengui.

2023, Decembre 31

## pengui.bin
At the moment just the dialog produce is implemented and connected to the penGUI, I have another two widget: eggs_configuration, already working and terminal to invent again.

With produce, just select File ->Produce, you can compose the command in a GUI, then copy and paste the result in a terminal.

For now, 30 december 2023 is enought!
