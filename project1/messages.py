import csv

def request(counter, answer):
    result = 0
    setLogin = []
    getLogin = []
    with open('friends.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
                setLogin.append(row[0])
                getLogin.append(row[1])

    for i in range(len(setLogin)):
        if setLogin[i] == counter and getLogin[i] == answer or setLogin[i] == answer and getLogin[i] == counter:
            result = result + 1
        else:
            result = result
    return result

def friend_list(counter):

    list = []
    with open('friends.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            if row[0] == counter:
                list.append(row[1])
            elif row[1] == counter:
                list.append(row[0])
            else:
                list = list

    list = [i for i in list]
    return list

def friend_message(counter, answer, message):
    with open('messages.csv', 'a', newline = '') as file:
        csv_writer = csv.writer(file, delimiter = ',')
        csv_writer.writerow([str(counter), str(answer), str(message)])
    with open('new_messages.csv', 'a', newline = '') as file:
        csv_writer = csv.writer(file, delimiter = ',')
        csv_writer.writerow([str(counter), str(answer), str(message)])

def friend_delete(counter, answer):
    string = []
    with open('friends.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            string.append(row)

    with open('friends.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            if row[0] == counter and row[1] == answer or row[1] == counter and row[0] == answer:
                string.remove(row)

    with open('friends.csv', 'w', newline = '') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(string)

