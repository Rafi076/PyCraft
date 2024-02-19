# The following are some of the most commonly used function in shutil module:
# Shutil.copy(src,dst) --> this function copies the file location at src to new location specified by dst.
# #
import shutil
shutil.copy("main.py","duplicateFile.py") # let a file name name 'main.py' outside of any folder. by this we can copy the content of 'main.py' into 'duplicateFile.py'
shutil.copytree("folder.py","duplicateFolder") # let a foldr name name 'folder.py'. by this we can copy the content of 'folder.py' into 'duplicateFolder.py'
shutil.move("MianFolder/introduction.file","introduction.file") # let a MianFolder inside this a file name "introduction.file".to move this file outside the Mainfolder 
