"""
This program calculates and prints out the minimum number of quizzes that are needed
for your average grade to be at least 9.5, assuming you receive a 10 on all future quizzes.

Author: Nguyen Chinh Quan
Time spent: 20 minutes
"""
def compute_quizzes_needed():
    Sum_of_scores = 0
    list_Quizz_Scores = input("Enter quiz scores received so far: ")
    list_Quizz_Scores = eval(list_Quizz_Scores)
    if list_Quizz_Scores == []:
        print("You need 1 more quiz")
    else:
        for i in range(len(list_Quizz_Scores)):
            Sum_of_scores += list_Quizz_Scores[i]
        average = Sum_of_scores/len(list_Quizz_Scores)
        if average>=9.5:
            print("You need 0 more quizzes")
        elif len(list_Quizz_Scores)%2!=0:
            print("You need 1 more quiz")
        else:
            temp=0
            while average<9.5:
                Sum_of_scores += 10
                temp += 1
                average = Sum_of_scores / (len(list_Quizz_Scores) + temp)
                if average == 9.5:
                    break
            print("You need",temp,"more quizzes")
#compute_quizzes_needed()
