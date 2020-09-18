import requests
import isodate 
API_key = 'AIzaSyBLwL_28p6j5yThMPgPQyvoqqNLChgi-_Y'

def get_duration(video_id, key = API_key):
    URL = 'https://www.googleapis.com/youtube/v3/videos?id=' + video_id + '&part=contentDetails&key=' + key
    
    r = dict(requests.get(url=URL).json())
    
    result = r['items'][0]['contentDetails']['duration']
    
    duration = isodate.parse_duration(result)
    return duration.seconds

def get_details(video_id, key = API_key):
    URL = 'https://www.googleapis.com/youtube/v3/videos?id=' + video_id + '&part=contentDetails&key=' + key
    
    r = requests.get(url=URL)
    
    return dict(r.json())


