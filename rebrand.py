import os
import shutil

# The absolute truth of our rebrand
TEXT_MAP = {
    "dexa": "shellens",         # Code imports, CLI commands, package names
    "Dexa": "Shell Lens",       # UI Banners, README headers
    "DEXA": "SHELLENS",         # Environment variables (if any)
    ".dexa": ".shellens",       # Hidden system folders
    "Dexa.spec": "Shellens.spec" # PyInstaller build file
}

def antigravity_replace():
    print("🚀 Initiating Antigravity Rebrand Protocol...")
    
    # Exclude virtual environments and git histories from the sweep
    excludes = {'.venv', 'venv', 'shell', '.git', '__pycache__', 'dist', 'build'}

    # Phase 1: Deep Content Sweep (Find & Replace in files)
    for root, dirs, files in os.walk('.', topdown=True):
        dirs[:] = [d for d in dirs if d not in excludes]
        
        for file in files:
            if file == "rebrand.py" or file.endswith(('.pyc', '.parquet', '.png', '.exe')):
                continue
                
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for old, new in TEXT_MAP.items():
                    new_content = new_content.replace(old, new)
                    
                if content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"  [TEXT] Rewrote: {file_path}")
            except Exception as e:
                pass

    # Phase 2: Structural Sweep (Rename Folders and Files from the bottom up)
    for root, dirs, files in os.walk('.', topdown=False):
        # Rename files
        for file in files:
            if file == "Dexa.spec":
                os.rename(os.path.join(root, file), os.path.join(root, "Shellens.spec"))
                print(f"  [FILE] Renamed: {file} -> Shellens.spec")
        
        # Rename directories
        for d in dirs:
            if d in excludes: continue
            if d == "dexa":
                os.rename(os.path.join(root, d), os.path.join(root, "shellens"))
                print(f"  [DIR]  Renamed: {d}/ -> shellens/")
            elif d == ".dexa":
                os.rename(os.path.join(root, d), os.path.join(root, ".shellens"))
                print(f"  [DIR]  Renamed: {d}/ -> .shellens/")

    print("✅ Antigravity Protocol Complete. The system is now Shell Lens.")

if __name__ == "__main__":
    antigravity_replace()