VENV=pengui
rm venv_* -rf
python3 -m venv venv_${VENV}
echo "insert:"
echo "source venv_${VENV}/bin/activate"
echo "pip install pyside6"
echo "NOTE: deactive to exit venv"
