import requests
import urllib
from bs4 import BeautifulSoup as bs
import time
from time  import sleep
import pytesseract
from pytesseract import image_to_string
from selenium import webdriver
from io  import BytesIO
import sys
import re
from PIL import Image
from selenium.common.exceptions import StaleElementReferenceException



def hasXpath(xpath):
    try:
        if(wd1.find_element_by_xpath(xpath)):
            return(True)

    except:
        return (False)


def hasXpath1(xpath):
    try:
        if(wd1.find_element_by_xpath(xpath)):
            return(True)

    except:
        return (False)

wd = webdriver.Chrome()
wd.get('https://www.social-searcher.com/google-social-search/')

abc=wd.find_elements_by_xpath('//*[@class="google-social-option"]')


for i in range(1, lenI(abc)):

    abc[i].click()


keyword="stock market fraud"

f=open(keyword+".txt",'wb')


key=(jls_extract_var).find_element_by_id('googlesearchinput')

key.send_keys(keyword) 

button=(jls_extract_var).find_element_by_class_name('main-search')

button.click()

get_social_media=(jls_extract_var).find_elements_by_xpath('//iframe[@class="cse-iframe"]')

links=[x.get_attribute("src") for x in get_social_media]


for i in links:
    (jls_extract_var).get(i)

    sleep(10)

    arr_post=[]


if "facebookcse" in i:

    j=1

    while(j<=10):
        posts=(jls_extract_var).find_elements_by_xpath('//div[@class="gsc-webResult gsc-result"]/div/div/div/a')

        links_for_post=[x.get_attribute("data-ctorig") for x in posts]

        wd1 = webdriver.Chrome()

        for each_link in links_for_post:

            wd1.get(each_link)

            sleep(3)

            if hasXpath('//div[@class="_5pbx userContent _3576"]'):
                content=wd1.find_element_by_xpath('//div[@class="_5pbx userContent _3576"]')
                post_of_user=content.text
                arr_post.append(post_of_user)

        wd1.close()

        j=j+1

        jls_extract_var = find_elements_by_xpath
        page_numbers=(jls_extract_var).jls_extract_var('//div[@class="gsc-cursor-page"]')

        for n in range(0,len(page_numbers)):

            if (page_numbers[n].text==str(j)):

                print(j)

                page_numbers[n].click()

                break

        sleep(3)

