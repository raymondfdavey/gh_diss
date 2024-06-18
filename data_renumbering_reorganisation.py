import os



def rename_files(directory, pref, suff=None):
    # Define common complex extensions
    complex_extensions = ['.nii.gz']

    # Get the list of files in the directory
    files = os.listdir(directory)

    # Sort the files alphabetically
    files.sort()

    # Iterate over the files and rename them
    for index, file in enumerate(files, start=1):
        old_name = os.path.join(directory, file)
        
        # Check for complex extensions first
        if any(file.endswith(ext) for ext in complex_extensions):
            # Find the appropriate complex extension and slice it off
            extension = next(ext for ext in complex_extensions if file.endswith(ext))
        else:
            # If no complex extension, use simple splitext
            _, extension = os.path.splitext(file)
        
        # Determine the new name based on whether a suffix is provided
        if suff is not None:
            new_name = os.path.join(directory, f"{pref}{index}_{suff}{extension}")
        else:
            new_name = os.path.join(directory, f"{pref}{index}{extension}")
        
        # Rename the file
        os.rename(old_name, new_name)

    print(f"Renamed {len(files)} files in the directory.")

# Example usage
# /Users/rfd/Desktop/RAW_DATA/
# paths = [
#     # (r'C:\Users\rd81\OneDrive - University of Sussex\Desktop\diss_git\RAW_DATA\SORTED_DATA\renumbered\Brats21\seg', ['Brats', 'seg']),
#     # (r'C:\Users\rd81\OneDrive - University of Sussex\Desktop\diss_git\RAW_DATA\SORTED_DATA\renumbered\Brats21\t2', ['Brats']),
#     (r'C:\Users\rd81\OneDrive - University of Sussex\Desktop\diss_git\RAW_DATA\SORTED_DATA\renumbered\IXI\t2', ['IXI']),
#     (r'C:\Users\rd81\OneDrive - University of Sussex\Desktop\diss_git\RAW_DATA\SORTED_DATA\renumbered\MSLUB\seg', ['MSLUB', 'seg']),
#     (r'C:\Users\rd81\OneDrive - University of Sussex\Desktop\diss_git\RAW_DATA\SORTED_DATA\renumbered\MSLUB\t2', ['MSLUB'])
# ]
paths = [
    ('/Users/rfd/Desktop/RAW_DATA/Brats21/seg', ['Brats', 'seg']),
    ('/Users/rfd/Desktop/RAW_DATA/Brats21/t2', ['Brats']),
    ('/Users/rfd/Desktop/RAW_DATA/IXI/t2', ['IXI']),
    ('/Users/rfd/Desktop/RAW_DATA/MSLUB/seg', ['MSLUB', 'seg']),
    ('/Users/rfd/Desktop/RAW_DATA/MSLUB/t2', ['MSLUB'])
]
for path, fixes in paths:
    if len(fixes) != 1:
        prefix, suffix = fixes
    else: 
        prefix = fixes[0]
        suffix = None
    
    rename_files(path, prefix, suffix)