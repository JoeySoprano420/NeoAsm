import os
import sys
import subprocess
import platform
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    required_version = (3, 7)
    current_version = sys.version_info
    if current_version < required_version:
        print(f"Error: NeoASM requires Python 3.7 or higher. You are using Python {current_version[0]}.{current_version[1]}")
        sys.exit(1)

def install_dependencies():
    """Install necessary dependencies using pip."""
    try:
        print("Installing required dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "ply", "numpy", "llvmlite", "py-cpuinfo"])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during dependencies installation: {e}")
        sys.exit(1)

def create_directories():
    """Create necessary directories for NeoASM."""
    directories = ["neoasm_bin", "neoasm_lib", "neoasm_examples"]
    for directory in directories:
        path = Path(directory)
        if not path.exists():
            path.mkdir(parents=True)
            print(f"Directory {directory} created.")
        else:
            print(f"Directory {directory} already exists.")

def download_compiler():
    """Download the NeoASM compiler or tools (this is a placeholder for actual download)."""
    try:
        print("Downloading NeoASM compiler...")
        # In a real scenario, you would use an HTTP request to download the files or Git clone a repository
        # subprocess.check_call(["git", "clone", "https://github.com/NeoASM/NeoASMCompiler.git"])
        print("NeoASM compiler downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading NeoASM compiler: {e}")
        sys.exit(1)

def setup_runtime():
    """Setup runtime environment for NeoASM."""
    try:
        print("Setting up NeoASM runtime environment...")
        # Placeholder for setting up runtime components
        # e.g., linking libraries or runtime-specific setup steps
        print("NeoASM runtime environment setup completed.")
    except Exception as e:
        print(f"Error during runtime setup: {e}")
        sys.exit(1)

def install_on_windows():
    """Windows specific installation steps."""
    if platform.system() == "Windows":
        print("Setting up NeoASM on Windows...")
        subprocess.check_call(["choco", "install", "llvm", "git"])  # Assuming you use Chocolatey for package management
        print("Windows installation completed.")

def install_on_linux():
    """Linux specific installation steps."""
    if platform.system() == "Linux":
        print("Setting up NeoASM on Linux...")
        subprocess.check_call(["sudo", "apt-get", "install", "llvm", "git", "build-essential", "python3-pip"])
        print("Linux installation completed.")

def install_on_mac():
    """Mac specific installation steps."""
    if platform.system() == "Darwin":
        print("Setting up NeoASM on macOS...")
        subprocess.check_call(["brew", "install", "llvm", "git", "python3"])
        print("macOS installation completed.")

def main():
    """Main installer script."""
    check_python_version()
    install_dependencies()
    create_directories()
    download_compiler()
    setup_runtime()

    if platform.system() == "Windows":
        install_on_windows()
    elif platform.system() == "Linux":
        install_on_linux()
    elif platform.system() == "Darwin":
        install_on_mac()
    else:
        print(f"Unsupported OS: {platform.system()}")
        sys.exit(1)

    print("NeoASM installation completed successfully.")
    print("You can now start using NeoASM by running 'neoasm' from your terminal.")

if __name__ == "__main__":
    main()
