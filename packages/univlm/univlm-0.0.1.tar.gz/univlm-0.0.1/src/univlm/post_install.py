import os
import subprocess
import sys

def run_script():
    script_path = os.path.join(os.path.dirname(__file__), "install_and_test.sh")
    if os.path.exists(script_path):
        print(f"🚀 Running post-install script: {script_path}")
        subprocess.run(["bash", script_path], check=True)
    else:
        print("⚠️ Post-install script not found!", file=sys.stderr)
