# Bu kod Requests kütüphanesi ve ücretsiz bir api aracılığıyla get işlemi yapar
import os
import requests

# icon api adresi
api_url = "https://img.icons8.com/2266EE/"

# aranacak icon ismini kullanıcan al
api_url += input("icon aramasi (search, button vb.) : ")

# cevap içeriğini img dosyasına yaz
img = requests.get(api_url).content

# icon.jpg dosyasını wb modunda (yoksa oluşturur) aç ve img'yi dosyaya yaz
with open('icon.jpg', 'wb') as icon:
    icon.write(img)

# icon.jpg dosyasını aç
os.system("icon.jpg")
