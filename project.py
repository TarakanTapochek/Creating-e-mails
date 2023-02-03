"""
1. Парсинг данных из файла с добавление уникального номер каждому сотруднику
employees = {
  0: {
    NAME: 'Name'
    LAST_NAME: 'Last_name'
    TEL: '1111111'
    CITY: 'City'
    EMAIL: ''
  }
}
2. Выбор валидных данных для генерации почты
3. Генерация почты
4. Добавление почты в данные файла
5. Запись файла
"""

all_empoyees = {}
valid_data = []
ID = []
user_id = 0

with open(r'/content/drive/MyDrive/Python/task_file.txt', 'r', encoding='utf-8') as file:
  file.readline() #пропускаем строку с заголовками
  for line in file:
    line = line.replace(' ', '')
    line = line.replace('\n', '')
    data = line[1:].split(',') #['Ivan', 'Abramov', '7776514', 'Moscow']

    #dividing data
    name = data[0]
    last_name = data[1]
    tel = data[2]
    city = data[3]

    employee = {
        'NAME': name,
        'LAST_NAME': last_name,
        'TEL': tel,
        'CITY': city,
        'EMAIL': ''
        }

    all_empoyees[user_id] = employee

    # data validation
    if name and last_name and len(tel) == 7 and tel.isdigit() and city:
      ID.append(user_id)
      valid_data.append([name, last_name])
    user_id += 1

# emails generating
def email_gen(list_of_names):
  """Function generates e-mails out of given name and surname

    Example:
    print(email_gen(['Ivan', 'Petrov'], ['Ivan', 'Petrov'], ['Ivan', 'Petrov']))
    ['Petrov.I@company.io', 'Petrov.Iv@company.io', 'Petrov.Iva@company.io']

    Args:
    list of lists with names and surnames

    Returns:
    List of emails
  """ 
  emails = []
  for i in valid_data:
    letter = 1
    while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
      letter+=1
    emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
  return emails

emails = email_gen(valid_data)

# adding emails to data
for i in range(len(ID)):
  all_empoyees[ID[i]] ['EMAIL'] = emails[i]

# saving data
with open(r'/content/drive/MyDrive/Python/project/result_file.txt', 'w', encoding='utf-8') as final:
  final.write('EMAIL, NAME, LAST_NAME, TEL, CITY\n')
  for ID in all_empoyees.keys():
    line = f"{all_empoyees[ID]['EMAIL']}, {all_empoyees[ID]['NAME']}, {all_empoyees[ID]['LAST_NAME']}, {all_empoyees[ID]['TEL']}, {all_empoyees[ID]['CITY']}\n"
    final.write(line)