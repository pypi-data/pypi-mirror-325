import atexit
from .scripts.install_and_test import run_script

atexit.register(run_script)
