import os
import re


while True:
    print('Welcome to the bloat photo deletion tool!\n')

    # Get file prefix
    while True:
        prefix = input('Enter the file prefix for the photos: ')
        response = input(f'Is {prefix} the correct prefix? Y/N: ')
                         
        if response == 'Y':
            break

    # Get edited file folder path
    while True:
        edited_path = input('\nEnter the path name for the edited photos folder: ').replace('"', '')
        response = input(f'Is {edited_path} the correct path? Y/N: ')
        
        if response == 'Y':
            break

    # Retrieve files in edited folder path and get file numbers for keeping
    edited_dir_list = [f for f in os.listdir(edited_path) if os.path.isfile(os.path.join(edited_path, f))]
    r = re.compile(f"{prefix}(\d+).*")
    keep_photo_list = [r.search(filename).group(1) if r.search(filename) is not None else None for filename in edited_dir_list if r.search(filename) is not None]

    # Get parent directory
    parent_dir = edited_path.replace('\\edited', '')
    # List files in parent directory
    parent_dir_list = [f for f in os.listdir(parent_dir) if os.path.isfile(os.path.join(parent_dir, f))]
    # Get tuples of filename and cleaned file number in parent director
    parent_dir_file_nums = [(filename, r.search(filename).group(1)) if r.search(filename) is not None else (filename, None) for filename in parent_dir_list]
    # Get file numbers in parent directory that aren't in edited directory (except files I couldn't find a match for)
    parent_dir_rm_files = [t[0] for t in parent_dir_file_nums if t[1] not in keep_photo_list + [None]]

    proceed = input(f'\nProceed with deleting {len(parent_dir_rm_files)} files? Y/N: ')

    if proceed == 'Y':
        for file in parent_dir_rm_files:
            os.remove(os.path.join(parent_dir, file))
        
        print(f'\nSuccessfully deleted {len(parent_dir_rm_files)} files from {parent_dir}!')
    else:
        print('\nOperation aborted!')
        break

    run_again = input('\nWould you like to run the program again? Y/N: ')

    if run_again == 'Y':
        print('\n')
        continue
    else:
        break