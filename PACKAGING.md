# Packaging 

I'm just looking to package for Debian. 

## requirements.txt
`pip freeze > requirements.txt`

## PyInstaller

`pyinstaller --windowed pengui.py`

will buil inside your folder two new folders `dist` and `build`.

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
I chosen to install pengui under /opt/pengui. and build a short script under `bin`. All the necessary complementes, a pengui.desktop file and a pengui.png ico are under `asset`

To create the package just run `bin/create-package-pengui`

NOTE: create-package will remove the dirs build, dist and package create during the buid, leaving jis a simple `pengui.deb` file.
