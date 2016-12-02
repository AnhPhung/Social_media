
# coding: utf-8

# In[ ]:

# function with default to return a complete list video ids
# argument 'youtube' from function build with api_service_name, api_version, developer_key

def search_video_all(key):
    nextpage = None
    videoID_list = []
    while (nextpage != 'lastpage'):
        search_result = search_video(keyword = key, page = nextpage)
        videoID_list = videoID_list + search_result[0]
        nextpage = search_result[1]
        
    return videoID_list


# In[ ]:

def search_video(keyword, n = 50, result_type = 'video', info = 'id', page=None, sortby='relevance'):    
 
    videoID_list = []
    search_response = youtube.search().list(
        part= info,
        q= keyword,
        maxResults = n,
        type = result_type,
        pageToken = page,
        order = sortby
    ).execute()
    
    for i in  range(len(search_response['items'])):
        videoID_list.append(search_response['items'][i]['id']['videoId'])
    
    try:
        nextpage = search_response['nextPageToken']
    except:
        nextpage = 'lastpage'
        
    return (videoID_list, nextpage)


# In[ ]:

def get_property(video_id):
    
    return youtube.videos().list(
        part = 'id, snippet, statistics, recordingDetails',
        id = video_id
    ).execute()


# In[ ]:

def get_channel(channel_id):
    
    return youtube.channels().list(
        part='snippet, statistics, contentDetails',
        id = channel_id
    ).execute()


# In[ ]:

def get_comment_thread(channel_id, page=None):
    
    search_commentthread = youtube.comment

