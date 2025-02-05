import os
import sys
import platform

def main():
    """Entry point for the install-gdal command."""
    # Use python3 on Unix-like systems, python on Windows
    python_cmd = 'python3' if platform.system() != 'Windows' else 'python'
    
    # Get the path to the original install-gdal script
    script_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts', 'install-gdal.py')
    
    # Execute the installation script
    return os.system(f'{python_cmd} "{script_path}"')

if __name__ == '__main__':
    sys.exit(main())
