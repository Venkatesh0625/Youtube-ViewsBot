from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import sys, os, logging

def load_proxies(que, length):
    #Get different number of proxy when  you run this at each time
    req_proxy = RequestProxy() 
    
    #Create proxy list 
    proxies = req_proxy.get_proxy_list() 
    
    length  += len(proxies)
    for proxy in proxies[::-1]:
        que.put(proxy)
        
    return length
    
def generate_proxies(que, req_length):
    length = 0
    
    #Load proxies from requestProxy
    while(length < req_length):
        load_proxies(que, length)
    

