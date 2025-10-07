import os
import subprocess
import sys
from pathlib import Path

main_folder = ''

def install_requirements():
    """Find and install all requirements.txt files in subdirectories."""
    current_dir = Path.cwd()
    # Get the directory
    if os.path.exists(main_folder):
        current_dir = Path(main_folder)
    else:
        current_dir = os.getcwd()
    
    print(f"Searching for requirements.txt files in: {current_dir}")
    
    # Find all requirements.txt files
    requirements_files = list(current_dir.rglob("requirements.txt"))
    
    if not requirements_files:
        print("No requirements.txt files found.")
        return
    
    print(f"Found {len(requirements_files)} requirements.txt files:")
    
    # Install requirements from each file
    for req_file in requirements_files:
        print(f"\n{'='*60}")
        print(f"Installing from: {req_file}")
        print(f"{'='*60}")
        
        try:
            # Read the file
            with open(req_file, 'r', encoding='utf-8') as f:
                requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            if not requirements:
                print("  No requirements found in this file.")
                continue
            
            print(f"  Packages to install: {len(requirements)}")
            for req in requirements:
                print(f"    - {req}")
            
            # Install each
            for requirement in requirements:
                try:
                    print(f"  Installing: {requirement}")
                    result = subprocess.run(
                        [sys.executable, "-m", "pip", "install", requirement],
                        check=True,
                        capture_output=True,
                        text=True,
                        timeout=300  # 5 minute timeout per package
                    )
                    print(f"    ✓ Successfully installed {requirement}")
                    
                except subprocess.CalledProcessError as e:
                    print(f"    ✗ Failed to install {requirement}")
                    print(f"      Error: {e.stderr}")
                    
                except subprocess.TimeoutExpired:
                    print(f"    ⚠ Timeout installing {requirement}")
                    
        except Exception as e:
            print(f"  Error processing {req_file}: {e}")
    
    print(f"\n{'='*60}")
    print("Installation process completed!")
    print("Note: Some packages might have failed due to compatibility issues.")

def install_with_retry(package, max_retries=2):
    """Install a package with retry mechanism."""
    for attempt in range(max_retries + 1):
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", package],
                check=True,
                capture_output=True,
                text=True,
                timeout=300
            )
            return True, f"Successfully installed {package}"
        except subprocess.CalledProcessError as e:
            if attempt == max_retries:
                return False, f"Failed after {max_retries + 1} attempts: {e.stderr}"
            print(f"  Retrying {package} (attempt {attempt + 1})...")
        except subprocess.TimeoutExpired:
            return False, f"Timeout installing {package}"
    
    return False, "Unknown error"

if __name__ == "__main__":
    print("Installer Script by Cheee99")
    print("This script will install all packages from requirements.txt files found in subdirectories.")
    
    # Ask for confirmation
    response = input("Do you want to continue? (y/n): ").lower().strip()
    if response not in ['y', 'yes']:
        print("Installation cancelled.")
        sys.exit(0)
    
    install_requirements()