#!/usr/bin/env python
# coding: utf-8

# In[12]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# In[13]:


import os
import wget


# In[ ]:




# In[ ]:





# In[ ]:





# In[5]:


driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")


# In[6]:


driver.get("https://www.instagram.com/")


# In[14]:


username = WebDriverWait(driver , 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name = 'username']")))


# In[15]:


password = WebDriverWait(driver , 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name = 'password']")))
username.clear()
password.clear()
username.send_keys("arjxzz")
password.send_keys("Arjun1234")


# In[ ]:


log_in =  WebDriverWait(driver , 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type= 'submit']"))).click()


# In[27]:


not_now = WebDriverWait(driver , 10).until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()
not_now2 = WebDriverWait(driver , 10).until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()


# In[43]:

scearchbox = WebDriverWait(driver , 10).until(ec.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
scearchbox.clear()
keyword = "#superman"
scearchbox.send_keys(keyword)


# In[44]:


scearchbox.send_keys(Keys.ENTER)


# In[45]:


driver.execute_script("window.scrollTo(0,9000);")


# In[46]:


images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images


# In[48]:


path = "D:\picz"
path = os.path.join(path , keyword[1:])
os.mkdir(path)
path


# In[49]:


counter = 0
for image in images:
    save_as = os.path.join(path,keyword[1:] + str(counter) + '.jpg')
    wget.download(image,save_as)
    counter += 1


# In[ ]:




