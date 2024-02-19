# Write a program to clear the clutter inside a folder on you computer.
# you should use os moduke to rename all the png image from 1.png all the 
# way till n.png where n is the number of png file in that folder.
# do the same for other formate.#
import os
files = os.listdir("clutterFolder")
 
i=1
for file in files:
    if file.endswith(".png"):
        os.rename(f"clutterfolder/{file}",f"clutterFolder/{i}.png")
        i += 1  # all the screenshort of clutterFolder renamed.
