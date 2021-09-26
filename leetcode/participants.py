
from functools import reduce


participants_list = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
]

def is_participant_attended(original,to_test):
    result = []
    for person in to_test:
        if person in original:
            result.append(person)
    return result


def daily_participants(participants_list):
    """Returns the list of all participants who participated everyday
    for the sample input, the right answer is
    ['Desmond', 'Krish', 'Sam']
    expected return object is a list of strings
    """
    everyday = participants_list[0]
    for i in range(1,len(participants_list)):
        everyday = is_participant_attended(everyday,participants_list[i])
    return everyday


def red(participants_list):
    return list(reduce((lambda x,y:set(x).intersection(set(y))),participants_list))

def one_time_participants(participants_list):
    """Returns the list of all participants who participated only once
    for the sample input, the right answer is
    ['Kapil', 'Ron', 'Ginny', 'Ted', 'Sachin', 'John', 'Joan']
    expected return object is a list of strings
    """
    one_time = {i:1 for i in participants_list[0]}
    for i in range(1,len(participants_list)):
        for person in participants_list[i]:
            if one_time.get(person):
                one_time[person] += 1
            else:
                one_time[person] = 1
            # one_time[person] = one_time.get(person,0) + 1
    return [ k for k,v in one_time.items() if v == 1]


def first_day_only_participants(participants_list):
    """Returns the list of all participants who participated on the first day and never participated again.
    for the sample input, the right answer is
    ['John', 'Joan']
    expected return object is a list of strings
    """
    never_seen_twice = participants_list[0]
    for i in range(1,len(participants_list)):
        for person in participants_list[i]:
            if person in never_seen_twice:
                never_seen_twice.remove(person)
    return never_seen_twice

def main():
    print(daily_participants(participants_list))
    print(one_time_participants(participants_list))
    print(first_day_only_participants(participants_list))
    print("OKKKK")
    print(red(participants_list))
if __name__ == '__main__':
    main()
# Output
# ['Krish', 'Desmond', 'Sam']
# ['Joan', 'John', 'Ron', 'Ginny', 'Ted', 'Sachin', 'Kapil']
# ['Joan', 'John']