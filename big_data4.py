from selenium import webdriver as w
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
from xlwt import Workbook



path_to_chromedriver = '/Users/dulat/Desktop/chromedriver' 
d = w.Chrome(executable_path = path_to_chromedriver)

d.get('https://tengrinews.kz/kazakhstan_news/nazarbaev-rasskazal-iz-kazahstantsev-rasschityivat-301846/')

time.sleep(3)
d.execute_script("window.scrollTo(0, document.body.scrollHeight)");

element = WebDriverWait(d,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jsBtn"]')))
try:
	element.click()
	print "clicked"

except selenium.common.exceptions.WebDriverException:
	print "element is not clickable"

wb = Workbook()
sheet1 = wb.add_sheet('sheet1')
sheet1.write(0,0,"User")
sheet1.write(0,1,"Rating")
sheet1.write(0,2,"Date")
sheet1.write(0,3,"Comments")

sheet1.col(0).width = 7000
sheet1.col(1).width = 7000
sheet1.col(2).width = 7000
sheet1.col(3).width = 15000



comments_user = d.find_elements_by_xpath('//*[@id="comments_tree"]/div[@class="comment"]/div[@class="user"]/span')
comments_text = d.find_elements_by_xpath('//*[@id="comments_tree"]/div[@class="comment"]/div[@class="comment_text"]/span[@class="substr"]')
comments_rating = d.find_elements_by_xpath('//*[@id="comments_tree"]/div[@class="comment"]/div[@class="rating"]/span[1]')
comments_date = d.find_elements_by_xpath('//*[@id="comments_tree"]/div[@class="comment"]/div[@class="date"]')


comment_text=[]
comment_user=[]
comment_rating=[]
comment_date=[]
for i in comments_text:
	comment_text.append(i.text)
for i in range(0,len(comment_text)):
		#print comment_text[i]
		sheet1.write(i+1,3,comment_text[i])
for i in comments_user:
	comment_user.append(i.text)
for i in range(0,len(comment_user)):
		#print comment_user[i]
		sheet1.write(i+1,0,comment_user[i])
for i in comments_date:
	comment_date.append(i.text)
for i in range(0,len(comment_date)):
		#print comment_date[i]
		sheet1.write(i+1,2,comment_date[i])
for i in comments_rating:
	comment_rating.append(i.text)		
for i in range(0,len(comment_rating)):
		#print comment_rating[i]
		sheet1.write(i+1,1,comment_rating[i])
wb.save('example.xls')

