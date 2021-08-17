import json
from random import randint

def generate_randoms(desired, total):
    tmplist = []
    while len(tmplist) < desired:
        value = randint(0,total)
        if not value in tmplist:
            tmplist.append(value)
    return tmplist

def get_random_workout(warmups: int, workouts: int, stretches: int, core:int, type: str, data):
    warmup_randoms = generate_randoms(warmups,len(data[type]['Warmup'])-1)
    workout_randoms = generate_randoms(workouts,len(data[type]['Mobility'])-1)
    stretch_randoms = generate_randoms(stretches,len(data[type]['Stretch'])-1)
    core_randoms = generate_randoms(stretches,len(data['Core'])-1)
    
    print("\nWarmup:")
    for i in warmup_randoms:
        print(f"{data[type]['Warmup'][str(i)]['Name']} {data[type]['Warmup'][str(i)]['sets']} sets of {data[type]['Warmup'][str(i)]['reps']} reps")

    print("\nMobility:")
    for i in workout_randoms:
        print(f"{data[type]['Mobility'][str(i)]['Name']} {data[type]['Mobility'][str(i)]['sets']} sets of {data[type]['Mobility'][str(i)]['reps']} reps")

    print("\nCore:")
    for i in core_randoms:
        print(f"{data['Core'][str(i)]['Name']} {data['Core'][str(i)]['sets']} sets of {data['Core'][str(i)]['reps']} reps")

    print("\nStretches:")
    for i in stretch_randoms:
        print(f"{data[type]['Stretch'][str(i)]['Name']} {data[type]['Stretch'][str(i)]['reps']}")
    
        
if __name__ == '__main__':
    f = open('workouts.json',)
    data = json.load(f)

    body_location = input("Please enter the muscle group you want to work (Upper or Lower): ")
    number_of_warmups = int(input(f"The number of warmup exercises (0-{len(data[body_location]['Warmup'])}): "))
    number_of_workouts = int(input(f"The number of mobility exercises (0-{len(data[body_location]['Mobility'])}): "))
    number_of_core = int(input(f"The number of core exercises: (0-{len(data['Core'])})"))
    number_of_stretchs = int(input(f"The number of stretches: (0-{len(data[body_location]['Stretch'])})"))

    workoutlist = get_random_workout(number_of_warmups, number_of_workouts,number_of_stretchs,number_of_core,body_location,data)