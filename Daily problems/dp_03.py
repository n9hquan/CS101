"""
This program calculates the minimum time to wash n loads of clothes in the first task
and calculates the individual weights of three objects in the second task.

Author: Nguyen Chinh Quan
Time spent: 45 minutes
"""
def compute_laundry_time():
    Numberofloads = int(input("Enter the number of loads: "))
    Minimumtime = Numberofloads*60-(Numberofloads-1)*35
    """Where I got this formula: For example we have 2 loads. Normally it takes 2 hours to finish the laundry. But if we
    utilize the time, as mentioned in the task, soon as we’ve finished washing load 1 and started hanging the clothes to 
    dry, we can start washing load 2. This means that we have shorten the normal time by 35 minutes per 1 extra load.
    Therefore, if we have n loads, we can shorten 35 minutes times (n-1) loads.
    Other formula: Minimumtime = 60+(Numberofloads-1)*25 where it takes more 25 minutes per each extra load."""
    print("Total laundry time:",Minimumtime)

def weigh_three():
    "Assume that the weights of obejct 1,2,3 are labelled to the following: x,y,z"
    a=float(input("Enter the combined weights of objects 1 and 2: "))
    b=float(input("Enter the combined weights of objects 1 and 3: "))
    c=float(input("Enter the combined weights of objects 2 and 3: "))
    """
    x+y=a, x+z=b, y+z=c
    y=c-z, z=b-x => y=c-b+x => x+c-b+x=a => 2x=a+b-c => x=(a+b-c)/2
    Therefore: y=(c+a-b)/2, z=(b+c-a)/2"""
    x=float((a+b-c)/2)
    y=float((c+a-b)/2)
    z=float((b+c-a)/2)
    print("The weights of objects 1, 2, and 3 are:",x,y,z)
