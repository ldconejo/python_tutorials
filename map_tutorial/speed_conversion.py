speed_per_hour = [3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5]

def calculate_miles_per_minute(speed):
    pace_minutes = int(60 / speed)
    pace_seconds = str(int(round((60 / speed - pace_minutes) * 60, 0))).zfill(2)
    overall_pace = f"{pace_minutes}:{pace_seconds}"
    return speed, overall_pace

if __name__ == "__main__":
    results = list(map(calculate_miles_per_minute, speed_per_hour))
    print("Speed(MPH)\tPace(min/mile)")
    for mph, min_per_mile in results:
        print(f"{mph}\t\t{min_per_mile}")