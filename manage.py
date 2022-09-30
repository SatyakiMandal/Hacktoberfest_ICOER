"""
Script for managing the Contributors.md file.
What this script does?
- Remove trailing whitespaces before '####'
- Replace every heading with '####'
- Sort the list of Contributors

Running the script -
python3 manage.py

PS: DO NOT USE PYTHON 2
"""
import re

def format_Contributor(contrib):
    """
    Helper function to format the details properly.
    """
    name_str = 'Name: ['
    contrib = contrib.replace('：', ':')
    contrib = contrib.replace('htpps', 'https')
    contrib = contrib.replace('Name:[', name_str)
    contrib = contrib.replace('Name : [', name_str)
    contrib = contrib.replace('Name :[', name_str)
    contrib = contrib.replace('Name: [ ', name_str)
    contrib= '#### ' + contrib+ '\n\n'
    return contrib


# Remove trailing whitespaces
# Make the file ready for sorting
with open('Contributors.md', 'r+') as file:
    new_file_data = []
    for line in file.readlines():
        line = re.sub('^#{1,3} ', '#### ', line)
        if(line.startswith(' ##')):
            new_file_data.append(line.lstrip())
        else:
            new_file_data.append(line)
    file.seek(0)
    file.truncate()
    file.writelines(new_file_data)


# Sorts the list of Contributors and saves to file
# The real thing happens here.
with open('Contributors.md', 'r+') as file:
    Contributors = [Contributor.strip() for Contributor in file.read().split('####')
                                if Contributor]
    Contributors = [format_Contributor(contrib) for contrib in Contributors]
    Contributors = sorted(Contributors)
    file.seek(0)
    file.truncate()
    file.writelines(Contributors)
