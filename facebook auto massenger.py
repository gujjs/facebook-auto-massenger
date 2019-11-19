from selenium import webdriver
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
import random
import pandas as pd

##
#options = Options()

keyboard = KeyboardController()
mouse = MouseController()

browser = webdriver.Chrome('C:\\Users\Guja\Downloads\chromedriver')
#chrome_options = webdriver.ChromeOptions()
#prefs = {"profile.default_content_setting_values.notifications" : 2}
#chrome_options.add_experimental_option("prefs",prefs)
#browser = webdriver.Chrome(chrome_options=chrome_options)


browser.maximize_window()
browser.get('https://www.facebook.com/php')


email = 'guja1515@gmail.com'
password = ''

browser.find_element_by_id('email').send_keys(email)
browser.find_element_by_id('pass').send_keys(password)
browser.find_element_by_id('loginbutton').click()
mouse.position = (532, 955)

#x = 1
#while x == 1:
   #x = x + int(input())
random = random.randint

df = pd.read_excel("archive.xlsx", "Sheet1")
target_list = df['working column'].tolist()

z = 0
y = 0
#options.add_argument("--disable-notifications")

for x in target_list:
   if str(x) == 'nan':
       break
   z = z + 1
   target_url = 'https://www.facebook.com/messages/t/' + str(x)
   browser.get(target_url)
   #print(target_url)
   time.sleep(random(10,30))
   mouse.position = (532, 955)
   #print('mouse')
   time.sleep(random(10,30))
   mouse.click(Button.left, 1)
   keyboard.type('სალამი, მე ჯაფარას თანაშემწე ვარ, პასუხისმგებელი მისისალამი, მე ჯაფარას თანაშემწე ვარ, პასუხისმგებელი მისი საქმიანობისთვის ფინანსების მობილიზებაზე. თქვენთვის მოწერა გადავწყვიტე, რადგან ზურას ფეიჯზე აქტიურობდით. თუკი მოგწონთ მისი პოლიტიკური საქმიანობა და მნიშვნელოვანი მიგაჩნიათ თავისუფლების გავრცელება, მაშინ მინდა ზურას პოლიტიკური საქმიანობის დაფინანსება შემოგთავაზოთ. ალბათ გაიგებდით რომ გირჩმა პოლიტიკური პლატფორმა აამოქმედა, სადაც ნებისმიერ მსურველს აქვს საშუალება დარეგისტრირდეს და გირჩის პარტიულ სიაში მოხვდეს. ამასთან ერთად, გირჩი გადავიდა ფანდრეიზინგის ამერიკულ მოდელზე, რაც ნიშნავს რომ ყველა პოლიტიკოსი ინდივიდუალურადაა პასუხისმგებელი საკუთარ ბიუჯეტზე. ჯაფარა აქამდე საკუთარ პოლიტიკურ საქმიანობას ლექციების ჩატარებით აფინანსებდა, ხოლო იმისთვის რომ მან მისი სრული დრო პოლიტიკურ საქმიანობას დაუთმოს, მას დაფინანსება სჭირდება. დღეს ადამიანების უმეტესობა ფიქრობს რომ მხოლოდ სოლიდურ კონტრიბუციას აქვს მნიშვნელობა და რამდენიმე ლარი არაფერს არ წყვეტს, თუმცა სინამდვილეში ეს ასე არ არის. ნებისმიერი რეგულარულად შემოწირული დაფინანსება, თუნდაც 5 ლარი ყოველთვიურად, ძალიან მნიშვნელოვანია. მეტიც, ბევრი მცირე დამფინანსებლის ყოლა მეტ თავისუფლებას აძლევს პოლიტიკოსს, ასე ის დამოკიდებული არ ხდება ერთ ან რამდენიმე მსხვილ წყაროზე.
                 საქმიანობისთვის ფინანსების მობილიზებაზე. თქვენთვის მოწერა გადავწყვიტე, რადგან ზურას ფეიჯზე აქტიურობდით. თუკი მოგწონთ მისი პოლიტიკური საქმიანობა და მნიშვნელოვანი მიგაჩნიათ თავისუფლების გავრცელება, მაშინ მინდა ზურას პოლიტიკური საქმიანობის დაფინანსება შემოგთავაზოთ. ალბათ გაიგებდით რომ გირჩმა პოლიტიკური პლატფორმა აამოქმედა, სადაც ნებისმიერ მსურველს აქვს საშუალება დარეგისტრირდეს და გირჩის პარტიულ სიაში მოხვდეს. ამასთან ერთად, გირჩი გადავიდა ფანდრეიზინგის ამერიკულ მოდელზე, რაც ნიშნავს რომ ყველა პოლიტიკოსი ინდივიდუალურადაა პასუხისმგებელი საკუთარ ბიუჯეტზე. ჯაფარა აქამდე საკუთარ პოლიტიკურ საქმიანობას ლექციების ჩატარებით აფინანსებდა, ხოლო იმისთვის რომ მან მისი სრული დრო პოლიტიკურ საქმიანობას დაუთმოს, მას დაფინანსება სჭირდება. დღეს ადამიანების უმეტესობა ფიქრობს რომ მხოლოდ სოლიდურ კონტრიბუციას აქვს მნიშვნელობა და რამდენიმე ლარი არაფერს არ წყვეტს, თუმცა სინამდვილეში ეს ასე არ არის. ნებისმიერი რეგულარულად შემოწირული დაფინანსება, თუნდაც 5 ლარი ყოველთვიურად, ძალიან მნიშვნელოვანია. მეტიც, ბევრი მცირე დამფინანსებლის ყოლა მეტ თავისუფლებას აძლევს პოლიტიკოსს, ასე ის დამოკიდებული არ ხდება ერთ ან რამდენიმე მსხვილ წყაროზე.')
   #print('text')
   time.sleep(random(10,30))
   keyboard.press(Key.enter)
   print(target_url + '- sent')
   time.sleep(random(10,30))
   while z == 20:
      print(z)
      y = y + 1
      time.sleep(random(y*300,y*600))
      z = 0

browser.quit()
print('Session Ended')
