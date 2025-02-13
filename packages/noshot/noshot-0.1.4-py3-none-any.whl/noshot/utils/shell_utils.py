import os
import shutil
import subprocess
import pathlib

def get_folder(folder_path = "ML TS XAI", loc = False):
    src = os.path.join(os.path.realpath(__file__)[:-20], "data", folder_path)
    try:
        dest = os.path.join(os.getcwd(), pathlib.Path(folder_path))
        shutil.copytree(src, dest, symlinks=False, copy_function = shutil.copy2,
                        ignore=shutil.ignore_patterns('.ipynb_checkpoints', '__init__.py', '__pycache__'),
                        ignore_dangling_symlinks=False, dirs_exist_ok=True)
    except:
        try:
            dest = os.path.join(os.path.expanduser('~'), "Downloads", pathlib.Path(folder_path))
            shutil.copytree(src, dest, symlinks=False, copy_function = shutil.copy2,
                            ignore=shutil.ignore_patterns('.ipynb_checkpoints', '__init__.py', '__pycache__'),
                            ignore_dangling_symlinks=False, dirs_exist_ok=True)
        except Exception as error:
            print(error)
            return
    finally:
        if loc:
            print("Path:",dest)

def get_file(file_path, loc = False, open = False):
    src = os.path.realpath(os.path.join("./src/noshot/data", file_path))
    try:
        dest = os.path.join(os.getcwd(), pathlib.Path(file_path).name)
        shutil.copy(src, dest)
        if open:
            subprocess.Popen(f"jupyter notebook {dest}")
    except:
        try:
            dest = os.path.join(os.path.expanduser('~'), "Downloads", pathlib.Path(file_path).name)
            shutil.copy(src, dest)
        except Exception as error:
            print(error)
    finally:
        if loc:
            print("Path:",dest)

def remove_folder(folder_path = "ML TS XAI"):
    try:
        shutil.rmtree(os.path.join(os.path.expanduser('~'), "Downloads", pathlib.Path(folder_path)),
                      ignore_errors = True)
        shutil.rmtree(os.path.join(os.getcwd(), pathlib.Path(folder_path)))
        print("Folder removed successfully")
        return True
    except WindowsError as error:
        print("Failed to delete!\nClose and reopen Jupyter Notebook and run this again")
        return False
    except Exception as error:
        print(error)