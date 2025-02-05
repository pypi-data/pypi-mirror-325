import atexit
from .post_install import run_script

atexit.register(run_script)
