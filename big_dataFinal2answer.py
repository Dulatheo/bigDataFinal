from selenium import webdriver as w
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
from xlwt import Workbook
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import nltk
nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize



path_to_chromedriver = '/Users/dulat/Desktop/chromedriver' 
d = w.Chrome(executable_path = path_to_chromedriver)
d.get('https://vesti.kz/')



d.execute_script("window.scrollTo(0, 500)");
time.sleep(3)

element = WebDriverWait(d,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-top-news"]/div[@class="jspContainer"]/div[@class="jspPane"]/div[@class="single-item"]')))
k=1
try:
	print "found"

except selenium.common.exceptions.WebDriverException:
	print "not found"

cl = NaiveBayesClassifier("path to the data that will have key words for categories")


link = d.find_elements_by_xpath('//*[@id="main-top-news"]/div[@class="jspContainer"]/div[@class="jspPane"]/div[@class="single-item"]/a')
links=[]
for a in link:
    print(a.get_attribute('href'))
    links.append(a.get_attribute('href'))

wb = Workbook()
sheet1 = wb.add_sheet('sheet1')




for i in range(0,len(links)):	
	d.get(links[i])
	d.execute_script("window.scrollTo(0, 700)");
	time.sleep(5)
	text_article = d.find_elements_by_xpath('//*[@id="resize_font"]')
	texts=[]
	for a in text_article:
		texts.append(a.text)
	for i in range(0,len(texts)):
		print texts[i]
	
print(cl.classify(texts[i]))  

# Classify a TextBlob
blob = TextBlob(classifier=cl)
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))

# Show 5 most informative features
cl.show_informative_features(5)
