from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from time import sleep
import queue 

from youtubeApi import get_duration

def run_video(video_id, frequency, proxies_que, view_time):
    #looping in frequency to be played
    for _ in range(frequency):
        
        try:
            try:
                proxy_ip = proxies_que.get_nowait()
                PROXY = proxy_ip.get_address()
                print(PROXY)
            
                #Setting up a new proxy 
                webdriver.DesiredCapabilities.CHROME['proxy']= {
                    "httpProxy":PROXY,
                    "ftpProxy":PROXY,
                    "sslProxy":PROXY,
                    
                    "proxyType":"MANUAL",
                }
            except queue.Empty:
                #We dont need to use proxy then
                pass
            
            #Initializing the driver 
            driver = webdriver.Chrome()
            
            wait = WebDriverWait(driver, 3)
            visible = EC.visibility_of_element_located
            
            #Loading the link
            driver.get('https://www.youtube.com/watch?v=cSLAO7zxS2M' + video_id)
            
            #waiting to load fully and click the play 
            wait.until(visible((By.ID, "video-title")))
            driver.find_element_by_id("video-title").click()
            
            #wait for the video to run video time then close the driver
            sleep(view_time)
            driver.close()
        except:
            pass



