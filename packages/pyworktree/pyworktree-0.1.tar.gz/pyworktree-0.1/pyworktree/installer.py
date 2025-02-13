import subprocess
import sys

def install_library(library_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])
        print(f"'{library_name}' has been installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install '{library_name}'. Please check the package name and try again. Error: {e}")
    except PermissionError:
        print(f"Permission denied: You do not have the required permissions to install '{library_name}'. Try running as an administrator.")
    except OSError as e:
        if "No space left on device" in str(e):
            print(f"Disk Space Error: Not enough space to install '{library_name}'. Free up space and try again.")
        else:
            print(f"OS Error: {e}")
    except subprocess.TimeoutExpired:
        print(f"Network Error: Connection timed out while installing '{library_name}'. Check your internet connection and try again.")
    except ModuleNotFoundError:
        print(f"Missing System Dependency: Required system tools for '{library_name}' are missing. Install necessary dependencies and retry.")
    except ImportError:
        print(f"Dependency Resolution Error: Conflicts between package versions detected while installing '{library_name}'. Try updating dependencies.")
    except ValueError:
        print(f"Syntax Error: Incorrect package name or formatting in the requirements file for '{library_name}'.")
    except RuntimeError as e:
        if "not supported on this platform" in str(e):
            print(f"Platform-Specific Issue: '{library_name}' is not compatible with your OS or architecture.")
        elif "Python version" in str(e):
            print(f"Python Version Incompatibility: '{library_name}' does not support Python {sys.version.split()[0]}. Consider upgrading or using a compatible version.")
    except Exception as e:
        print(f"An unexpected error occurred while installing '{library_name}': {e}")

# Example usage
if __name__ == "__main__":
    lib_name = input("Enter the library name to install: ")
    install_library(lib_name)
