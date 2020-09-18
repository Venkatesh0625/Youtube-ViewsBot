import math
import queue
import sys
from threading import Thread 

from proxy import load_proxies, generate_proxies
from youtubeApi import get_duration, get_details
from video import run_video

#Getting inputs
n_thread = int(input('Number threads (from 1 to 10) : '))
views = int(input('Number of views: '))
view_time = int(input('View time(seconds) : '))
video_id = input('Enter youtube video id : ')
proxy_flag = input('Want to add proxy ip\'s(you need fast internet) [y/n] : ')

if(n_thread < 0  or n_thread > 10):
    print('Thread should be from 1 to 10')
    sys.exit()
    
#Getting info about the video
r = get_details(video_id)
try:
    r['items'][0]
except:
    print('Video id invalid')
    sys.exit()    

duration = get_duration(video_id)
view_time = duration if duration < view_time else view_time

link = 'https://www.youtube.com/watch?v=' + video_id

proxies_que = queue.Queue()

#if proxy flah is 'n' then proxies_que will be empty which will be handled in video modules
if(proxy_flag == 'y'):
    #load initial proxies to start with 
    l = load_proxies(proxies_que, 0)

    #If we want more view than the loaded proxies then loading more 
    if(views > l):
        proxy_thread = Thread(target=generate_proxies, args = (proxies_que, views - l,))
        proxy_thread.start()

#Calculating frequency per thread
freq_per_thread = math.ceil(views / n_thread)

video_threads  = []
#Appedning Thread instance
for i in range(n_thread - 1):
    video_threads.append(Thread(target=run_video, args = (video_id, freq_per_thread, proxies_que, view_time)))

#Calculating frequency of last thread
freq_last_thread = freq_per_thread if views % n_thread == 0 else views % n_thread 
video_threads.append(Thread(target=run_video, args = (video_id,freq_last_thread , proxies_que, view_time)))

for thrd in video_threads:
    thrd.start()
for thrd in video_threads:
    thrd.join()