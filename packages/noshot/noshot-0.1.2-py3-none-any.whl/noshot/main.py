import os
import shutil
import subprocess


available = {'-1  ' : "AIDS CN NLP(Folder)"}

def get(name = None, open = False):
    try:
        if name is not None:
            name = str(name)
        if name in ['-1']     :   get_folder(loc = True)
        else:
            for k, v in available.items():
                sep = " : " if v else ""
                print(k,v,sep = sep)
    except:
        pass

def get_folder(loc = False, i = 0, j = 0):
    src = os.path.join(os.path.realpath(__file__)[:-7], "data", "AIDS CN NLP")
    try:
        dest =  os.path.join(os.getcwd(), ("AIDS CN NLP" + (f" ({i})" if i != 0 else "")))
        shutil.copytree(src, dest, symlinks=False,
                        copy_function = shutil.copy2,
                        ignore=shutil.ignore_patterns('.ipynb_checkpoints', '__init__.py', '__pycache__'),
                        ignore_dangling_symlinks=False, 
                        dirs_exist_ok=False)
        if loc:
            print("Path:",dest)
    except FileExistsError:
        get_folder(loc, i + 1, j)
    except:
        try:
            dest = os.path.join(os.path.expanduser('~'), "Downloads", ("AIDS CN NLP" + (f" ({i})" if i != 0 else "")))
            shutil.copytree(src, dest, symlinks=False,
                            copy_function = shutil.copy2,
                            ignore=shutil.ignore_patterns('.ipynb_checkpoints', '__init__.py', '__pycache__'),
                            ignore_dangling_symlinks=False, 
                            dirs_exist_ok=False)
            if loc:
                print("Path:",dest)
        except FileExistsError:
            get_folder(loc, i, j + 1)
        except:
            pass