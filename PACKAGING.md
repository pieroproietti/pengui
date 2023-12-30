# requirements.txt
`pip freeze > requirements.txt`

# PyInstaller

`pyinstaller --windowed pengui.py`

will buil inside your folder two new folders `dist` and `build`.

# fpm
First install ruby

`sudo apt install ruby`

then install fpm
`gem install fpm --user-install`

add path in .bashrc
`~/.local/share/gem/ruby/3.1.0/bin/`

now fpm is ready:
`fpm --version`

# Create package
I chosen for now to install pengui under /opt.

## Create directory scructure and package
I made a simple script `create-package-pengui` under bin.

