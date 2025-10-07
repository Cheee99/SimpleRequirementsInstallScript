# SimpleRequirementsInstallScript
Simple script that installs all requirements for main specified subfolder 

# 🐍 Python Requirements Updater

A lightweight Python utility script for automatically finding and updating all `requirements.txt` files across a project — including submodules and nested folders.  

Ideal for monorepos or modular Python projects where each library or app has its own `requirements.txt`. (ComfyUI)

---

## ✨ Features

-  **Recursive Search** — Scans the main folder and all subdirectories for `requirements.txt` files  
-  **Multi-Library Support** — Handles complex project structures with multiple dependency files  
-  **Automatic Path Detection** — Uses the script’s directory as the root if no path is provided  
- **Manual Mode** — Optionally define a custom folder path directly inside the script  
-  **Batch Updating** — Updates all detected requirements in one go  

---

## Usage

### 1️⃣ Place the Script
Put the script (e.g. `update_requirements.py`) anywhere in your project — ideally in the main directory.
Also you can edit main folder yourself. It will start search from specified folder.

### 2️⃣ Run It
```
python Install_requirments_subfolders.py
