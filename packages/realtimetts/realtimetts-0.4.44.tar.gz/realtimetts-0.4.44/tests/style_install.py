import subprocess
import sys

# Enable ANSI color support on Windows if possible.
try:
    import colorama
    colorama.init()
except ImportError:
    pass

# ANSI escape sequences for colors.
CYAN = "\033[96m"    # Bright cyan for installation progress.
GREEN = "\033[92m"   # Bright green for success messages.
RED = "\033[91m"     # Bright red for error messages.
GRAY = "\033[90m"    # Dim gray for pip output.
RESET = "\033[0m"

def install_package(package_name):
    """Install a Python package using pip with colored log output."""
    print(f"{CYAN}📦 Installing {package_name}...{RESET}")
    process = subprocess.Popen(
        [sys.executable, "-m", "pip", "install", package_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )
    
    # Read pip output line by line and print it in gray.
    while True:
        line = process.stdout.readline()
        if line == '' and process.poll() is not None:
            break
        if line:
            print(f"{GRAY}{line.rstrip()}{RESET}")
    
    retcode = process.poll()
    if retcode == 0:
        print(f"{GREEN}🎉 {package_name} installed successfully.{RESET}")
        print()
    else:
        print(f"{RED}🚫 Error installing {package_name}.{RESET}")
        print()

def main():
    packages = [
        "librosa",
        "munch",
        "einops",
        "einops_exts",
        "git+https://github.com/resemble-ai/monotonic_align.git",
        "matplotlib"
    ]
    for package in packages:
        install_package(package)

if __name__ == "__main__":
    main()
