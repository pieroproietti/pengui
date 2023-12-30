# PyInstaller

`pyinstaller --windowed penGui.py`

look into your folder and you’ll notice you now have two new folders `dist` and `build`.

# fpm

`sudo apt install ruby`

`gem install fpm --user-install`

add in .bashrc
`~/.local/share/gem/ruby/3.1.0/bin/`

now fpm is ready:
`fpm --version`

# Create package
I chosen for now to install pengui under /opt.

## Create directory scructure
```
mkdir -p package/opt/pengui
mkdir -p package/usr/share/applications
mkdir -p package/usr/share/icons
mkdir -p package/usr/bin
cp asset/pengui.png package/usr/share/icons/
cp asset/pengui.desktop package/usr/share/applications
cp -r dist/pengui/* package/opt/pengui
find package/opt/pengui -type f -exec chmod 644 -- {} +
find package/opt/pengui -type d -exec chmod 755 -- {} +
find package/usr/share -type f -exec chmod 644 -- {} +
chmod +x package/opt/pengui/pengui
```
fpm -C package -s dir -t deb -n "pengui" -v 0.1.0 -p pengui.deb
