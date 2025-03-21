import car_number
import country
import city

# Викликаємо функції з відповідних файлів
car_num = car_number.get_car_number()
car_country = country.get_car_country()
car_city = city.get_car_city()

# Виводимо результати
print("Номер авто:", car_num)
print("Країна:", car_country)
print("Місто де було зареєстровано:", car_city)