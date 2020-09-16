"""Author: Elijah Morishita
   elmorishita@dmacc.edu
   9/16/2020
   The Average Scores Test Validation Program
   """

def names():
    """ gathers frist/last name as a string and returns a string """
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter you last name: ")

    full_name = last_name + "," + first_name + " age:"
    return full_name

def age():
    """ gathers age and returns an int"""
    age = int(input("Please enter your age: "))
    return age

try:
    def average(score1, score2, score3):
        """ Calculates an average, and returns an float"""
        sum = score1 + score2 + score3
        average_scores = sum / 3

        return average_scores
except:
    print("An exception occurred")

if __name__ == '__main__':
    name = names()
    age = age()

    score1 = float(input("Enter your first test score: "))
    score2 = float(input("Enter your second test score: "))
    score3 = float(input("Enter your third test score: "))

    print(name, age, "average grade:", average(score1, score2, score3))


# the input works well unless you enter a char when gathering
# the score input, it will however accept floats and ints