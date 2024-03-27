#!/bin/bash 
source bin/program
cd ~/${PROGRAM}

# Pulizia
rm ${PROGRAM}-0* -rf

# build
python -m nuitka \
        --enable-plugins=pyside6 \
        --include-qt-plugins=sensible \
        --include-qt-plugins=sqldrivers \
        --onefile \
        --standalone \
        src/${PROGRAM}.py 

# pulizia
rm ${PROGRAM}.build -rf
rm ${PROGRAM}.dist -rf
rm ${PROGRAM}.onefile-build -rf
