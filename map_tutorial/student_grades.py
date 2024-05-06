'''
ldconejo - 05/05/2024
Displays an example of using Python's map() function for integrating
three sets of data. 
In this case, three iterables are passed as arguments to the function.
Note that 'second semester' only has two values, so it will become
the limiter to the map() function.
'''
student_names = ["Luis Conejo", "Jane Doe", "John Doe"]
first_semester = [85, 95, 73]
second_semester = [90, 90]

def grade_average(student_name, grade_first_semester, grade_second_semester):
    '''
    Takes three arguments and returns the name of the student and their
    average grade.
    '''
    average_grade = round((grade_first_semester + grade_second_semester)/2, 2)
    return student_name, average_grade

if __name__ == "__main__":
    results = map(grade_average, student_names, first_semester, second_semester)
    print("Student\t\tAverage grade")
    for name, grade in results:
        print(f"{name}\t{grade}")
