WORKOUT_SCHEDULE = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
REST, CHILL_OUT, TRAIN = 'Rest', 'Chill out!', 'Go train {}'
INVALID_DAY = 'Not a valid day'

def get_workout_motd(day):
    day = day.title()
    if day not in WORKOUT_SCHEDULE:
        return INVALID_DAY

    workout = WORKOUT_SCHEDULE[day]
    return CHILL_OUT if workout == REST else TRAIN.format(workout)
