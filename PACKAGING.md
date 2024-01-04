## **penGUI take cure of eggs!**
![icon](https://github.com/pieroproietti/pengui/blob/main/assets/pengui.svg?raw=true)

# PACKAGING

I'm just looking to package for Debian, for now.

on Debian for pyside6-deploy we ned to install:
`sudo apt install python3-dev`

## requirements.txt
I don't know if we need with pyside6-deploy
`pip freeze > requirements.txt`

## pyside6-deploy
will generate a single pengui.bin file on `dist`, just:
```
cd src
pyside6-deploy penguin.py
```

## fpm
First install ruby

`sudo apt install ruby`

then install fpm
`gem install fpm --user-install`

add path in .bashrc
`~/.local/share/gem/ruby/3.1.0/bin/`

now fpm is ready:
`fpm --version`

## Create package
I chosen to install pengui under /opt/pengui. and build a short script under `bin`. All the necessary complementes: a `pengui.desktop` file and a `pengui.png` icon are under `asset`.

To create the package just run `bin/create-package-pengui`

NOTE: create-package will remove the dirs package create during the buid, leaving just a simple `pengui.deb` on the root.
