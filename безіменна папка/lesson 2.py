#guests = {"Андрій", "Марія", "Оля", "Ігор"}
#other_guests = {"Сергій" ,"Влад" , "Оля" }
#all_guests = guests.union(other_guests)
#common_guests = guests.intersection(other_guests)\
#unique_guests = guests.difference(other_guests)
##print(unique_guests)

#team_red = {"Макс", "Оля", "Іван", "Настя"}
#eam_blue = {"Настя", "Сергій", "Іван", "Марія"}
#both_teams = team_red.intersection(team_blue)
#print(both_teams)


#team_red = {"Макс", "Оля", "Іван", "Настя"}
#team_blue = {"Настя", "Сергій", "Іван", "Марія"}
#all_players = team_red.union(team_blue)
#print("Оля" in all_players)

#a = set('Hello')
#print(a)

#a = {'098', '076' , '097'}
#print(a)

#items = {'cherry' , 'apple' , 'banana'}
#items.add('chocolate')
#items.discard('beer')
#print(items)

#a = set('hello')
#b = set('hi there!')
#print(a ^ b)

#names = ["Анна", "Олег", "Марія", "Анна", "Іван", "Марія", "Олег"]

#unique_names = set(names) 

#for name in unique_names:
#    print(name)

#friend1 = {"математика", "фізика", "історія", "література"}
#friend2 = {"біологія", "фізика", "історія", "географія"}
#print(friend1&friend2)

#votes = ["Анна", "Олег", "Анна", "Марія", "Іван", "Анна", "Марія", "Олег"]
#vote_count = {}
#for name in votes:
#    vote_count[name] = vote_count.get(name, 0) + 1
#for name, count in vote_count.items():
#    print(f"{name}: {count}")

#invited = {"Олег", "Анна", "Іван", "Марія", "Настя"}
#arrived = {"Анна", "Іван"}
#missed = invited.difference(arrived)
#print('не прийшли: ')
#for name in missed:
#    print(name)

#set1 = {1, 2, 3, 4, 5}
#set2 = {3, 4, 5, 6, 7}
#set3 = {5, 6, 7, 8, 9}
#num = set1.intersection(set2 , set3)
#print("спільні числа:")
#for num1 in num:
#    print(num1)

#spilni = (set1&set2&set3)
#print("спільні : ", spilni)

#text1 = "Програмування це творчість і логіка"
#text2 = "Творчість допомагає розвивати мислення"
#words1 = set(text1 .lower().split())
#words2 = set(text2 .lower().split())
#unique_words = words1.difference(words2)
#print('унікальні слова яких нема в 1: ')
#for wrd in unique_words:
#     print(wrd)








#import random
#
#password = int(input("Придумайте пароль із 2 цифр (від 10 до 99): "))
#while True:
#    guess = random.randint(10, 99)  # Генеруємо випадкове число від 10 до 99
#    print(f"Спроба: {guess}")  # Показуємо згенероване число
#    if guess == password:  # Порівнюємо безпосередньо числа
#        print("Пароль вгадано!")
#        break


#import random
#import string

# Введення пароля
#password = input("Придумайте пароль із 8 символів: ")

# Перевірка на довжину (на випадок, якщо користувач введе некоректний пароль)
#while len(password) != 8:
#    print("Пароль має бути рівно 8 символів.")
 #   password = input("Придумайте пароль із 8 символів: ")

# Набір символів для генерації
#characters = string.ascii_letters + string.digits + string.punctuation

# Лічильник спроб
#attempt = 1

#while True:
#    # Генерація випадкової комбінації довжиною 8 символів
#   guess = ''.join(random.choice(characters) for _ in range(8))
#   print(f"Спроба {attempt}: {guess}")
#  
  #  # Перевірка, чи пароль вгадано
 #   if guess == password:
 #       print(f"Пароль вгадано за {attempt} спроб(у)!")
#        print(f"Ваш пароль: {password}")
 #       break
 #   
 #   attempt += 1


import random

# Введення пароля
password = input("Придумайте пароль із 8 цифр: ")

# Перевірка, щоб пароль складався лише з цифр і мав довжину 8 символів
while not (password.isdigit() and len(password) == 8):
    print("Пароль має бути довжиною 8 символів і складатися лише з цифр.")
    password = input("Придумайте пароль із 8 цифр: ")

# Лічильник спроб
attempt = 1

while True:
    # Генерація випадкового числа довжиною 8 цифр
    guess = ''.join(random.choice('0123456789') for _ in range(8))
    print(f"Спроба {attempt}: {guess}")
    
    # Перевірка, чи пароль вгадано
    if guess == password:
        print(f"Пароль вгадано за {attempt} спроб(у)!")
        print(f"Ваш пароль: {password}")
        break
    
    attempt += 1