"""Є вiдкритий API NASA який дозволяє за певними
параметрами отримати данi у виглядi JSON про фото зробленi
ровером “Curiosity” на Марсi. Серед цих даних є посилання на
фото якi потрiбно розпарсити i потiм за допомогою додаткових
запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg ,
mars_photo2.jpg . Завдання потрiбно зробити використовуючи модуль requests"""

# Account Email: poltavskalugova@gmail.com
# Account ID: f08f216c-f24b-48d1-a21f-c67b2aedfa50
import requests
# https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
# API_KEY = 'uXd5IQYvohZvRFnksz6eB68l49fAIUnMl1E0pLNG'


params = {
    'sol': 10,
    'api_key': 'uXd5IQYvohZvRFnksz6eB68l49fAIUnMl1E0pLNG'
}

response_photos = requests.get(
    "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos",
    params=params
)

print('status_code', response_photos.status_code)
# print('url', response_photos.url)
# print('headers', response_photos.headers)
print('text', response_photos.text)


if response_photos.status_code == 200:
    list_of_photos = response_photos.json()
    photos = list_of_photos.get("photos", [])

    if not photos:
        print("Фото не знайдено.")
    else:
        for i, photo in enumerate(photos[:2], start=1):
            img_url = photo['img_src']
            img_data = requests.get(img_url).content

            file_name = f"mars_photo{i}.jpg"
            with open(file_name, 'wb') as f:
                f.write(img_data)

            print(f"Фото {i} збережено: {file_name}")
else:
    print("Помилка запиту:", response_photos.text)