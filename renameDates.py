#! python3
# renameDates.py - Rename filenames with American MM-DD-YYY date format to EU DD-MM-YYYY

import shutil, os, re

#Create a regex that matches files with the American date format.

datePattern = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)

#  Loop over the files in the working directory.
for muricaFilename in os.listdir('.'):
    mo = datePattern.search(muricaFilename)

# Skip files without a date.
    if mo == None:
        continue
# Get the different parts of the filename.
    beforePart = mo.groups(1)
    monthPart = mo.groups(2)
    dayPart = mo.groups(4)
    yearPart = mo.groups(6)
    afterPart = mo.groups(8)

    euFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    muricaFilename = os.path.join(absWorkingDir, muricaFilename)
    euFilename = os.path.join(absWorkingDir, euFilename)

# Rename the files.
    print('Renaming "%s" to "%s"...' % (muricaFilename, euFilename))
    # shutil.move(amerFilename, euroFilename)   # uncomment after testing if files are renamed correctly
