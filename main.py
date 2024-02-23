


# This is the main file for the Password Keeper Program.

# Import main modules
import sys

sys.path.insert(0, 'res')
sys.path.insert(0, 'bin')

# Import app modules
import f


#Log the startup
f.LogStartUp()

# Check if the modules work or not.
print("Application started.")


if(not f.checkFileExists("bin/gp.txt")):
    f.Log("This is the first launch.","mainFile")
    import s
    s.showWindow()
else:
    f.Log("Data found","mainFile")
    import m
    m.showWindow()
