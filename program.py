#!/usr/bin/env python3

#import modules
import os
import time
os.system("clear")

global poolKey
global farmerKey

if "POOL_KEY" in os.environ:
    poolKey = os.environ['POOL_KEY']

if "FARMER_KEY" in os.environ:
    farmerKey = os.environ['FARMER_KEY']

#Mount Drive 
def program1():
    os.system("lsblk")
    print("")
    drivePath = input("Please enter the drive path [eg /dev/sdb1]: ")
    while not(os.path.exists(drivePath)):
        if drivePath == "":
            res = input("Do you want to go back to main program? [y/N] ")
            if res == "y":
                return
        print(drivePath + " does not exist")
        drivePath = input("Please enter the drive path [eg /dev/sdb1]: ")

    mountPath = input("Where do you want to mount " + drivePath + "? [eg /media/temp] ")
    while not(os.path.exists(mountPath)):
        if mountPath == "":
            res = input("Do you want to go back to main program? [y/N] ")
            if res == "y":
                return
        else:
            res = input("Do you want to create "+mountPath+" ? [Y/n] ")
            if res == "" or res == "y":
                os.system("sudo mkdir "+mountPath)
                print(mountPath+" is created!")
        mountPath = input("Where do you want to mount " + drivePath + "? [eg /media/temp] ")
        
    os.system("sudo mount " + drivePath + " " + mountPath)
    print(drivePath+" is mounted at "+mountPath)

#Mount Ram Drive
def program2():
    mountPath = input("Where do you want to mount the ram drive? [eg /media/temp] ")
    while not(os.path.exists(mountPath)):
        if mountPath == "":
            res = input("Do you want to go back to main program? [y/n] ")
            if res == "y":
                return
        else:
            res = input("Do you want to create "+mountPath+" ? [Y/n] ")
            if res == "" or res == "y":
                os.system("sudo mkdir "+mountPath)
                print(mountPath+" is created!")
        mountPath = input("Where do you want to mount the ram drive? [eg /media/temp] ")
    
    os.system("sudo mount -t tmpfs -o size=110G tmpfs " + mountPath)
    print("ram disk is mounted at "+mountPath)


#Unmount Drive 
def program3():
    os.system("df -h")
    print("")
    drivePath = input("Please enter the drive path [eg /media/temp]: ")
    while not(os.path.exists(drivePath)):
        if drivePath == "":
            res = input("Do you want to go back to main program? [y/N] ")
            if res == "y":
                return
        print(drivePath + " does not exist")
        drivePath = input("Please enter the drive path [eg /media/temp]: ")
    
    unmount = input("Are you sure you want to unmount " + drivePath + "? [Y/n] ")
    if unmount == "" or unmount == "y":
        os.system("sudo umount " + drivePath)
        print(drivePath + " is unmounted!")

#Delete All File In Drive
def program4():
    os.system("df -h")
    print("")
    drivePath = input("Please enter the drive path [eg /media/temp]: ")
    while not(os.path.exists(drivePath)):
        if drivePath == "":
            res = input("Do you want to go back to main program? [y/N] ")
            if res == "y":
                return
        print(drivePath + " does not exist")
        drivePath = input("Please enter the drive path [eg /media/temp]: ")
    
    erase = input("Do you want to delete all files inside " + drivePath + "? [Y/n] ")
    if erase == "" or erase == "y":
        os.system("sudo rm " + drivePath + "/*")
        print("All files deleted in " + drivePath + " !")

#Turn Off System Swap
def program5():
    os.system("sudo swapoff -a")
    print("Swap is disabled!")

#Turn On High Performance
def program6():
    os.system('echo "performance" | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor')
    os.system("cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor")

#Open Screen Session
def program7():
    os.system("screen -ls")
    print("")
    sessionName = input("Enter a session name: ")
    if sessionName == "":
        res = input("Do you want to go back to main program? [y/N] ")
        if res == "y":
            return
    else:
        res = input("Do you want to create "+sessionName+"? [y/N] ")
        if res == "y":
            os.system("screen -dmS "+sessionName)
            print(sessionName+" is created!")
    
    res = input("Do you want to open "+sessionName+"? [Y/n] ")
    if res == "" or res == "y":
        os.system("screen -rd "+sessionName)

#List Disk Infomation 
def program8():
    watch = input("Do you want to watch in real time? [y/N] ")
    try:
        while watch == "y":
            os.system("clear")
            print("==> List Disk Infomation ")
            os.system("df -h")
            print("\nPress Ctrl+C to terminate watch in real time")
            time.sleep(2)

    except KeyboardInterrupt: #Ctrl+C
        print("Exiting")
        pass
    
    if watch == "n":
        os.system("df -h")

#Start MadMax Plotter
def program9():
    madmaxPath = str(input("Enter MadMax path: [ENTER for default] "))
    if madmaxPath == "":
        madmaxPath = "/home/lemling/chia/chia-plotter/build/chia_plot"
    
    nrOfCores = str(input("Enter number of cores: [Default=28] "))
    if nrOfCores == "":
        nrOfCores = "28"

    nrOfBuckets = str(input("Enter number of buckets: [Default=512] "))
    if nrOfBuckets == "":
        nrOfBuckets = "512"

    tempDirectory = str(input("Enter path to temp directory: [Default=/media/temp/] "))
    if tempDirectory == "":
        tempDirectory = "/media/temp/"

    ramdrive = input("Do you want to use a ram drive? [Y/n] ")
    if ramdrive == "" or ramdrive == "y":
        ramDirectory = input("Enter path to ram directory: [Default=/media/ramdisk/] ")
        if ramDirectory == "":
            ramDirectory = " -2 /media/ramdisk/"
        else:
            ramDirectory = " -2 "+ramDirectory
    else:
        ramDirectory = ""

    destinationDirectory = str(input("Enter path to output directory: [Default=/media/temp/] "))
    if destinationDirectory == "":
        destinationDirectory = "/media/temp/"

    log = input("Do you want to log the plotter output?: [Y/n] ")
    #fileName = ""
    #if log == "" or log == "y":
    #    tmp = input("Enter a file name: [Default=plotter]")
    #    if tmp == "":
    #        tmp = "plotter"

    #    fileName = " > "+tmp+".log"

    runInAnotherShell = input("Do you want to start the plotter in a detached shell? [Y/n] ")

    command = madmaxPath+" -n -1 -r "+nrOfCores+" -u "+nrOfBuckets+" -t "+tempDirectory+ramDirectory+" -d "+destinationDirectory+" -c "+poolKey+" -f "+farmerKey
    os.system("clear") 
    print("==> Start MadMax Plotter")
    
    print("PREVIEW: "+command)
    startPlot = input("Are you sure you want to run this command? [Y/n] ")
    if startPlot == "y":
        os.system("clear")
        if runInAnotherShell == "y":
            #os.system("screen -dmS plotter bash -c '"+command+fileName+"; exec bash'")
            os.system("screen -dmSL plotter bash -c '"+command+"; exec bash'")
            print("The plotter is successfully running in the background!")
        else:
            os.system(command)
            #os.system(command+fileName)

#Start Plot Mover
def program10():
    source = input("Enter plot source folder: [Default=/media/temp/] ")
    if source == "":
        source = "/media/temp/"
    
    destination = input("Enter plot destination folder: [Default=/media/output/] ")
    if destination == "":
        destination = "/media/output/"

    log = input("Do you want to log the plot mover output?: [Y/n] ")
    fileName = ""
    if log == "y":
        tmp = input("Enter a file name: ")
        fileName = " > "+tmp+".log"

    runInAnotherShell = input("Do you want to start the plot mover in a detached shell? [Y/n] ")

    command = "watch -n 10 mv "+source+"*.plot "+destination
    print("PREVIEW: "+command)
    startPlot = input("Are you sure you want to run this command? [Y/n] ")
    if startPlot == "" or startPlot == "y":
        os.system("clear")
        if runInAnotherShell == "y":
            os.system("screen -dmS mover bash -c '"+command+fileName+"; exec bash'")
            print("The plot mover is successfully running in the background!")
        else:
            os.system(command+fileName)

#View Move Processes
def program11():
    watch = input("Do you want to watch in real time? [y/N] ")
    try:
        #while watch == "y":
        if watch == "y":
            os.system("clear")
            print("==> View Move Processes")
            print("\nPress Ctrl+C to terminate watch in real time")
            time.sleep(3)
            os.system("watch progress -w")
            os.system("clear")
            print("==> View Move Processes")
            #print("\nPress Ctrl+C to terminate watch in real time")
            #time.sleep(10)

    except KeyboardInterrupt: #Ctrl+C
        print("Exiting")
        pass
    
    if watch == "n":
        os.system("progress -w")

# Check Environment Variables
def program12():
    global poolKey
    global farmerKey


    if "POOL_KEY" in os.environ:
        poolKey = os.environ['POOL_KEY']
    else:
        poolKey = input("POOL_KEY was not found. Paste you key here: ")
        command = 'sudo sh -c \'echo POOL_KEY=\\"'+poolKey+'\\" >> /etc/environment\''
        os.system(command)
        print("POOL_KEY successfully added! The key will be loaded when you restart your ssh session")

    if "FARMER_KEY" in os.environ:
        farmerKey = os.environ['FARMER_KEY']
    else:
        farmerKey = input("FARMER_KEY was not found. Paste you key here: ")
        command = 'sudo sh -c \'echo FARMER_KEY=\\"'+farmerKey+'\\" >> /etc/environment\''
        os.system(command)
        print("FARMER_KEY successfully added! The key will be loaded when you restart your ssh session")

    print("POOL_KEY: "+poolKey)
    print("FARMER_KEY: "+farmerKey)

welcome = ("""\
 --------------------------------------------
|                                            |
|   W E L C O M E  T O  M Y  P R O G R A M   |
|                                            |
|   Select one of the following options:     |
|                                            |
|   [ 1 ]   - Mount Drive                    |
|   [ 2 ]   - Mount Ram Drive                |
|   [ 3 ]   - Unmount Drive                  |
|   [ 4 ]   - Delete All File In Drive       |
|   [ 5 ]   - Turn Off System Swap           |
|   [ 6 ]   - Turn On High Performance       |
|   [ 7 ]   - Open Screen Session            |
|   [ 8 ]   - List Disk Infomation           |
|   [ 9 ]   - Start MadMax Plotter           |
|   [ 10 ]  - Start Plot Mover               |
|   [ 11 ]  - View Move Processes            |
|   [ 12 ]  - Check Environment Variables    |
|   [ q ]   - Quit Program                   |
|                                            |
 --------------------------------------------
""")

while True:
    os.system("clear")
    print(welcome)
    selection = input("Program Number: ")

    if selection == "q":
        print("Shutting Down Program. . .")
        exit()
    elif selection == "1":
        os.system("clear")
        print("==> Mount Drive")
        program1()
        input("\nPress ENTER to go back to main program")
    elif selection == "2":
        os.system("clear")
        print("==> Mount Ram Drive")
        program2()
        input("\nPress ENTER to go back to main program")
    elif selection == "3":
        os.system("clear")
        print("==> Unmount Drive ")
        program3()
        input("\nPress ENTER to go back to main program")
    elif selection == "4":
        os.system("clear")
        print("==> Delete All File In Drive")
        program4()
        input("\nPress ENTER to go back to main program")
    elif selection == "5":
        os.system("clear")
        print("==> Turn Off System Swap")
        program5()
        input("\nPress ENTER to go back to main program")
    elif selection == "6":
        os.system("clear")
        print("==> Turn On High Performance")
        program6()
        input("\nPress ENTER to go back to main program")
    elif selection == "7":
        os.system("clear")
        print("==> Open Screen Session")
        program7()
        input("\nPress ENTER to go back to main program")
    elif selection == "8":
        os.system("clear")
        print("==> List Disk Infomation")
        program8()
        input("\nPress ENTER to go back to main program")
    elif selection == "9":
        os.system("clear")
        print("==> Start MadMax Plotter")
        program9()
        input("\nPress ENTER to go back to main program")
    elif selection == "10":
        os.system("clear")
        print("==> Start Plot Mover")
        program10()
        input("\nPress ENTER to go back to main program")
    elif selection == "11":
        os.system("clear")
        print("==> View Move Processes")
        program11()
        input("\nPress ENTER to go back to main program")
    elif selection == "12":
        os.system("clear")
        print("==> Check Environment Variables")
        program12()
        input("\nPress ENTER to go back to main program")
    else:
        print("Wrong User Input")
