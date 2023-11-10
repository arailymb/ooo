#task_1_1
user_input = input("Enter a string with whitespaces: ")
user_input = user_input.lower()

char_list = []

for char in user_input:
    char_list.append(char)

print("Created list is:")
print(char_list)

#task_1_2
from collections import Counter

char_list = ['p', 'u', 'l', 'p', ' ', 'f', 'i', 'c', 't', 'i', 'o', 'n']

char_count = Counter(char_list)

char_frequency_list = list(char_count.items())

char_frequency_list.sort()

print(char_frequency_list)

#task_1_3
char_frequency_list = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]

list_vow = []
list_cons = []
list_symb = []

vowels = {'a', 'e', 'i', 'o', 'u'}

for char, count in char_frequency_list:
    if char in vowels:
        list_vow.append((char, count))
    elif char.isalpha():
        list_cons.append((char, count))
    else:
        list_symb.append((char, count))

print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_symb =", list_symb)

#task_1_4
list_A = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]

list_A.sort()

total_elements = len(list_A)
index_q1 = total_elements // 4
index_q2 = 2 * index_q1
index_q3 = 3 * index_q1

q1 = list_A[:index_q1]
q2 = list_A[index_q1:index_q2]
q3 = list_A[index_q2:index_q3]
q4 = list_A[index_q3:]

if total_elements % 4 != 0:
    q1 += [0] * (index_q1 - len(q1))

print("q1 =", q1)
print("q2 =", q2)
print("q3 =", q3)
print("q4 =", q4)

#task_2_1
student_name = "Adam"
assignment_scores = [82, 56, 44, 30]
lab_scores = [78.20, 77.20]
test_scores = [78, 77]

student = {
    'name': student_name,
    'assignment': assignment_scores,
    'test': test_scores,
    'lab': lab_scores
}

print(student)

#task_2_2
student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}

submission_check = {student['name']: 0}

if len(student['assignment']) == 4:
    submission_check[student['name']] += 4

if len(student['lab']) == 2:
    submission_check[student['name']] += 2

if len(student['test']) == 2:
    submission_check[student['name']] += 2

print(submission_check)

#task_2_3
student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}
submission_rate = {'Adam': 6}

if submission_rate.get(student['name'], 0) >= 4:
    assignment_average = sum(student['assignment']) / len(student['assignment'])
    lab_average = sum(student['lab']) / len(student['lab'])
    test_average = sum(student['test']) / len(student['test'])
    final_grade = 0.3 * assignment_average + 0.5 * lab_average + 0.2 * test_average
    student['final_grade'] = final_grade
else:
    student['final_grade'] = 0

print(student)

#task_2_4
student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2], 'final_grade': 70.25}
student2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2], 'final_grade': 0}

students = {student['name']: {key: value for key, value in student.items() if key != 'name'},
            student2['name']: {key: value for key, value in student2.items() if key != 'name'}}

print(students)

#task_3_1
transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]

stats = {}

for user, transaction in transactions:
    if str(user) not in stats:
        stats[str(user)] = {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None}

    stats[str(user)][transaction] += 1

for user, user_stats in stats.items():
    transactions_counts = user_stats.copy()
    transactions_counts.pop('mft', None)
    transactions_counts.pop('lft', None)

    max_count = max(transactions_counts.values(), default=None)
    min_count = min(transactions_counts.values(), default=None)

    most_frequent_transaction = next((t for t, count in transactions_counts.items() if count == max_count), None)
    least_frequent_transaction = next((t for t, count in transactions_counts.items() if count == min_count), None)

    user_stats['mft'] = most_frequent_transaction
    user_stats['lft'] = least_frequent_transaction

print("stats =", stats)
