import os
import subprocess
    
# Get the current working directory
current_path = os.getcwd()
print("Current Path:", current_path)
from distutils.core import setup
from Cython.Build import cythonize

# Walk through all subdirectories
for root, dirs, files in os.walk(current_path):
    if root == current_path or root == current_path+"\\Models" or root == current_path+"\\Tests":  
        continue  # Skip the current directory
    result = subprocess.run(["python", "-m", "compileall", str(root), "-b"], capture_output=True, text=True)
    print(result.stdout)  # Print standard output
    print(result.stderr)  # Print error messages (if any)
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            #setup(ext_modules = cythonize([file_path]))
            os.remove(file_path)
            print(f"Removed: {file_path}")




# for root, dirs, files in os.walk(current_path):
#     if root == current_path or root == current_path+"\\Models" or root == current_path+"\\Tests":  
#         continue  # Skip the current directory       
#     for file in files:
#         if file.endswith(".pyc"):
#             file_path = os.path.join(root, file)
#             new_file_path = file_path[:-1]  # Remove the 'c' from '.pyc'
#             os.rename(file_path, new_file_path)
#             print(f"Renamed: {file_path} -> {new_file_path}")