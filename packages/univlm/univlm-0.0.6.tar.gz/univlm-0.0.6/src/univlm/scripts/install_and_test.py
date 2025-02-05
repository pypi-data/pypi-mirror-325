import os
import subprocess

def run_script():
    """Runs the install_and_test.sh script"""
    script_path = os.path.join(os.path.dirname(__file__), "install_and_test.sh")
    
    if os.path.exists(script_path):
        print("🚀 Running post-install script...")
        subprocess.run(["bash", script_path], check=True)
    else:
        print("⚠️ install_and_test.sh not found!")

if __name__ == "__main__":
    run_script()
