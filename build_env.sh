echo "Tinkerforge Environment: Building START"

echo "Tinkerforge Environment: Creating virtualenv..."
virtualenv venv2

echo "Tinkerforge Environment: Activating virtualenv..."
. venv2/bin/activate

echo "Tinkerforge Environment: Installing python bindings for tinkerforge"
pip install tinkerforge

deactivate

echo "Tinkerforge Environment: Building DONE"

echo "Tinkerforge Environment: Activate environment via '. venv2/bin/activate'"
