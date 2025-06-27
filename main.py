import subprocess, os, time, numpy
from subprocess import CREATE_NEW_CONSOLE

def mainProgram(inputs):
    element1 = "ah79b.txt"      #taken from airfoiltools.com
    element2 = "e423.txt"       #taken from airfoiltools.com
    #element3 = "e423.txt"       #taken from airfoiltools.com
    
    newInputs = numpy.round(inputs, 3)
    #print("These are the new inputs:", newInputs)
    
    e1Scale = newInputs[0]
    e1Angle = newInputs[1]
    
    e2Scale = newInputs[2]
    e2Angle = newInputs[3]
    e2X = newInputs[4]
    e2Y = newInputs[5]
    
    #e3Scale = newInputs[6]
    #e3Angle = newInputs[7]
    #e3X = newInputs[8]
    #e3Y = newInputs[9]
    
    print("New E1 Scale:", e1Scale)
    print("New E1 Angle:", e1Angle)
    print("New E2 Scale:", e2Scale)
    print("New E2 Angle:", e2Angle)
    print("New E2 X-Position:", e2X)
    print("New E2 Y-Position:", e2Y)
    #print("New E3 Scale:", e3Scale)
    #print("New E3 Angle:", e3Angle)
    #print("New E3 X-Position:", e3X)
    #print("New E3 Y-Position:", e3Y)
    
    #airset
    program1 = "airset.exe" 
    text1 = ("Adde\n" + element1 + "\nS\n" + str(e1Scale) + "\nA\n" + str(e1Angle) + "\n\n"
             + element2 + "\nS\n" + str(e2Scale) + "\nA\n" + str(e2Angle) + "\nM\n" + str(e2X) + "\n" + str(e2Y) + "\n\n"
             #+ element3 + "\nS\n" + str(e3Scale) + "\nA\n" + str(e3Angle) + "\nM\n" + str(e3X) + "\n" + str(e3Y)
             + "\n\n\nSave\nblade\nY\n")

    subprocess.run(program1, input=text1, creationflags=CREATE_NEW_CONSOLE, text=True)

    #mset
    program2 = "mset.exe"
    #NEED TO CHANGE NUMBER OF \N FOR EVERY ELEMENT ADDED
    text2 = "1\n0\n2\n\n\n3\n4\n14\n"
    #str(e2Angle/2)
    
    subprocess.run(program2, input=text2, creationflags=CREATE_NEW_CONSOLE, text=True)

    #makespecfile
    program3 = "makespecfile.exe"
    #text3 = "\n5\n0\n" + str(newAngle) + "\n0.5\n"
    text3 = "\n5\n0\n0\n0.5\n"

    subprocess.run(program3, input=text3, creationflags=CREATE_NEW_CONSOLE, text=True)

    #change REYNIN to 4.000E+05
    with open("mses", "r") as file1:
        filedata1 = file1.read()
    filedata1 = filedata1.replace("0.000E+00", "5.000E+05")
    #filedata1 = filedata1.replace("0.05000", "0.00000")
    with open("mses", "w") as file1:
        file1.write(filedata1)
    file1.close()

    #mses
    program4 = "mses.exe"
    text4 = "50\n\n"

    subprocess.run(program4, input=text4, creationflags=CREATE_NEW_CONSOLE, text=True)
    
    #msis
    #programTest = "msis.exe"
    #textTest = "150\n\n"

    #subprocess.run(programTest, input=textTest, creationflags=CREATE_NEW_CONSOLE, text=True)

    #mpolar
    program5 = "mpolar.exe"

    subprocess.run(program5, creationflags=CREATE_NEW_CONSOLE)

    #get Cl value from polar
    with open("polar", "r") as file2:
        solution = file2.readlines()
    file2.close()

    solutionValues = solution[-1]
    solutionValues = solutionValues.replace("   ", " ")
    solutionValues = solutionValues.replace("  ", " ")
    solutionValues = solutionValues.split(" ")
    solutionValues.pop(0)
    solutionValues = list(solutionValues)
    #print("These are the solutionValues:", solutionValues)

    solutionValuesFloats = []
    for i in solutionValues:
        if solutionValues[0] == "------":
            #time delays and file deletion for stability purposes
            os.remove("blade")
            time.sleep(1)
            os.remove("mdat")
            time.sleep(1)
            os.remove("mses")
            time.sleep(1)
            os.remove("polar")
            time.sleep(1)
            os.remove("polarx")
            time.sleep(1)
            os.remove("spec")
            time.sleep(2)
            return 0
        floatValue = float(i)
        solutionValuesFloats.append(floatValue)
    
    liftCoefficient = solutionValuesFloats[1]
    print("Current Lift Coefficient:", liftCoefficient)
    
    #time delays and file deletion for stability purposes
    os.remove("blade")
    time.sleep(1)
    os.remove("mdat")
    time.sleep(1)
    os.remove("mses")
    time.sleep(1)
    os.remove("polar")
    time.sleep(1)
    os.remove("polarx")
    time.sleep(1)
    os.remove("spec")
    time.sleep(2)

    return liftCoefficient

#mainProgram([1.0, 0.0, 0.5, 10.0, 0.85, -0.15])