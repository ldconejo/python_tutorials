# Python _map()_

The _map()_ function in Python allows you to pass the values in one or more iterables to a function with a single line of code.

In the example below, we want to take a list of speeds expressed in miles per hour and convert each value into pace (expressed in minutes per mile.)
This is something that would be useful for a runner training on a treadmill.

```python
speed_per_hour = [3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5]

def calculate_miles_per_minute(speed: float):
    '''
    Receives a speed value and returns the received
    value and the conversion to pace.
    '''
    pace_minutes: int = int(60 / speed)
    pace_seconds: str = str(int(round((60 / speed - pace_minutes) * 60, 0))).zfill(2)
    overall_pace: str = f"{pace_minutes}:{pace_seconds}"
    return speed, overall_pace

if __name__ == "__main__":
    results = list(map(calculate_miles_per_minute, speed_per_hour))
    print("Speed(MPH)\tPace(min/mile)")
    for mph, min_per_mile in results:
        print(f"{mph}\t\t{min_per_mile}")
```

The first value passed to _map()_ is the function that your values will be "mapped" to.
The second value is an iterable (a list). As you can see, each of the values in _speed_per_hour
is processed with _calculate\_miles\_per\_minute()_ and returned as part of _results_.

Also important to note is that the object return is of "map" type, which is why we are converting
it into a list for ease of use.

```
Speed(MPH)      Pace(min/mile)
3.5             17:09
4.0             15:00
4.5             13:20
5.0             12:00
5.5             10:55
6.0             10:00
6.5             9:14
7.0             8:34
7.5             8:00
8.0             7:30
8.5             7:04
```

Now, if the function you want to map takes multiple arguments, you will need to pass as many iterables as the number of arguments required.

In this second example, and average grade is calculated based on three lists: _student\_names_, _first\_semester_ and _second\_semester_.

```python
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
```
Note that _second\_semester_ only has two elements. Since _map()_ will combine the
elements in all three iterables in parallel, it will only use the first two elements
from each list (the smallest iterable becomes the limiter).

```
Student         Average grade
Luis Conejo     87.5
Jane Doe        92.5
```
