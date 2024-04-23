import datetime
import json

def addExercise():
    exercises = {}
    date = datetime.datetime.now()
    while True:
        name = input("What exercise would you like to add?")
        if name == "exit":
            break
        if name:
            exercises['Exercise Name'] = f'{name}'
        numOfSets = int(input("How many sets?"))
        for x in range(numOfSets):
            setWeights=[]
            numOfReps= int(input(f"How many reps for set{x+1}?"+" "))
            repWeight=float(input(f"How much weight for set{x+1}"+" "))
            exercises[f'Set {x+1} Reps'] = numOfReps
            exercises[f'Set {x+1} Weight'] = repWeight
            setVol = numOfReps*repWeight
            setWeights.append(setVol)
            exercises[f'Set {x+1} Volume']= setVol
        totalVol= sum(setWeights)
        exercises['Total Volume']= totalVol
        exercises['Date of Exercise']= f"{date.month}/{date.day}/{date.year}"
        with open("exercises.json", "r") as e:
            exerciseList=json.load(e)
        exerciseList.append(exercises)
        with open("exercises.json", "w") as e:
            json.dump(exerciseList, e, indent=4)

addExercise()

