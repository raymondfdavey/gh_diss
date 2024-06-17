import os

def rename_files(directory, pref, suff=None):
    # Get the list of files in the directory
    files = os.listdir(directory)

    # Sort the files alphabetically
    files.sort()

    # Iterate over the files and rename them
    for index, file in enumerate(files, start=1):
        old_name = os.path.join(directory, file)
        _, extension = os.path.splitext(file)  # Get the file extension
        if suff != None:
            new_name = os.path.join(directory, f"{pref}{index}_{suff}{extension}")
        else:
            new_name = os.path.join(directory, f"{pref}{index}{extension}")
        os.rename(old_name, new_name)

    print(f"Renamed {len(files)} files in the directory.")

# Example usage

paths = [
# (r'C:\Users\rd81\OneDrive - University of Sussex\Desktop\diss_git\RAW_DATA\SORTED_DATA\renumbered\Brats21\seg', ['Brats', 'seg'])
# ,(r'C:\Users\rd81\OneDrive - University of Sussex\Desktop\diss_git\RAW_DATA\SORTED_DATA\renumbered\Brats21\t2', ['Brats'] )
(r'C:\Users\rd81\OneDrive - University of Sussex\Desktop\diss_git\RAW_DATA\SORTED_DATA\renumbered\IXI\t2', ['IXI'])
,(r'C:\Users\rd81\OneDrive - University of Sussex\Desktop\diss_git\RAW_DATA\SORTED_DATA\renumbered\MSLUB\seg', ['MSLUB', 'seg'])
,(r'C:\Users\rd81\OneDrive - University of Sussex\Desktop\diss_git\RAW_DATA\SORTED_DATA\renumbered\MSLUB\t2', ['MSLUB'])
]

for path, fixes in paths:
    if len(fixes) != 1:
        prefix, suffix = fixes
    else: 
        prefix = fixes[0]
        suffix = None
    
    rename_files(path, prefix, suffix)