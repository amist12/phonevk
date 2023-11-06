#by @rebik канал @DDoS_Adepts
import requests
print("by @rebik канал @DDoS_Adepts") 
def search_vk_by_phone(phone_number):
    response = requests.get(f"https://find.vk.com/phone/{phone_number}")
    if response.status_code == 200:
        return response.text
    else:
        return None
#by @rebik канал @DDoS_Adepts
phone = "НОМЕР"
result = search_vk_by_phone(phone)
if result is not None:
    print(result)
else:
    print("Пользователь с таким номером телефона не найден. By @DDoS_Adepts By @rebik")
#by @rebik канал @DDoS_Adepts
