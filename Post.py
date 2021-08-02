import requests
def ct_get_posts(count=None, start_date= None, end_date= None, include_history= None,listIds = None,language = None,
                 sort_by="date", types=None, search_term=None,searchTerm = None, 
                 min_interactions = 0, offset = None, api_token=None):
    """Retrieve a set of posts for the given parameters get post from crowdtangle 
    Args:
        count (int, optional): The number of posts to return. Defaults to 10. options [1-100]
        start_date (str, optional): The earliest date at which a post could be posted. Time zone is UTC. 
                                    Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” 
                                    (defaults to time 00:00:00).
        end_date (str, optional): The latest date at which a post could be posted.
                                  Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss”
                                  or “yyyy-mm-dd” (defaults to time 00:00:00).
                                  defaults to "now".
        include_history (str, optional): Includes timestep data for growth of each post returned.
                                         Defaults to null (not included). options: 'true'
        sort_by (str, optional): The method by which to filter and order posts.
                                options: 'date', 'interaction_rate', 'overperforming',
                                'total_interactions', 'underperforming'.
                                defaults 'overperforming'
        min_interactions (int, optional): If set, will exclude posts with total interactions 
                                          below this threshold. options int > 0, default 0
        offset (int, optional): The number of posts to offset (generally used for pagination). 
                                Pagination links will also be provided in the response.                                                          
        types (str, optional):  The types of post to include. These can be separated by commas 
                                to include multiple types. If you want all live videos 
                                (whether currently or formerly live), be sure to include both 
                                live_video and live_video_complete. The "video" type does not 
                                mean all videos, it refers to videos that aren't native_video,
                                youtube or vine (e.g. a video on Vimeo).   
                                options: "episode", "extra_clip", "link", "live_video", 
                                "live_video_complete", "live_video_scheduled", "native_video",
                                "photo", "status", "trailer","video", "vine", "youtube"  
                                default all
        search_term (str, optional): Returns only posts that match this search term. 
                                     Terms AND automatically. Separate with commas for OR, 
                                     use quotes for phrases. E.g. CrowdTangle API -> AND. 
                                     CrowdTangle, API -> OR. "CrowdTangle API" -> AND in that
                                     exact order. You can also use traditional Boolean search
                                     with this parameter. default null                                                                                                                         
        api_token (str, optional): you can locate your API token via your crowdtangle dashboard
                                   under Settings > API Access.
    Returns:
        [dict]: The Response contains both a status code and a result. The status will always
                be 200 if there is no error. The result contains an array of post objects and
                a pagination object with URLs for both the next and previous page, if they exist
    Example:
        ct_get_posts(include_history = 'true', api_token="AKJHXDFYTGEBKRJ6535")                    
    """
    
    # api-endpoint
    URL_BASE = "https://api.crowdtangle.com/posts"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'count': count, 'sortBy':sort_by, 'token': api_token, 
              'minInteractions': min_interactions, 'offset': offset}

    # add params parameters
    if offset:
        PARAMS['offset'] = offset
    if searchTerm:
        PARAMS['searchTerm'] = searchTerm
    if language:
        PARAMS['language'] = language
    if listIds:
        PARAMS['listIds'] = listIds
    if start_date:
        PARAMS['startDate'] = start_date
    if end_date:
        PARAMS['endDate'] = end_date
    if include_history == 'true':
        PARAMS['includeHistory'] = include_history
    if types:
        PARAMS['types'] =  types
    if search_term:
        PARAMS['searchTerm'] =  search_term 

    # sending get request and saving the response as response object
    r = requests.get(url=URL_BASE, params=PARAMS)
    if r.status_code != 200:
        out = r.json()
        print(f"status: {out['status']}")
        print(f"Code error: {out['code']}")
        print(f"Message: {out['message']}")
    return r.json()
def ct_get_lists(api_token=""):
    """Retrieve the lists, saved searches and saved post lists of the dashboard associated with the token sent in
    Args:
        api_token (str, optional): you can locate your API token via your crowdtangle dashboard
                                   under Settings > API Access.
    Returns:
        [dict]: The Response contains both a status code and a result. The status will always
                be 200 if there is no error. The result contains an array of a lists objects
    Example:
        ct_get_lists(api_token="AKJHXDFYTGEBKRJ6535")                    
    """
    
    # api-endpoint
    URL_BASE = "https://api.crowdtangle.com/lists"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'token': api_token}

    # sending get request and saving the response as response object
    r = requests.get(url=URL_BASE, params=PARAMS)
    if r.status_code != 200:
        out = r.json()
        print(f"status: {out['status']}")
        print(f"Code error: {out['code']}")
        print(f"Message: {out['message']}")
    return r.json()
token = "1TYSrPnhowtxTAY5izMHtkPyqtbAzPQI890ohIM0"

def ct_search(count=None, start_date= None, end_date= None, include_history= None,inListIds = None,language = None,
                 sort_by="date", types=None, search_term=None,searchTerm = None, an=None,no=None,
                 min_interactions = 0, offset = None, api_token=None):
    """Retrieve a set of posts for the given parameters get post from crowdtangle 
    Args:
        accounts (null (any account in the List or Dashboard)): The account handles or platform ids to search. These can be separated by commas to include multiple accounts.
        count (int, optional): The number of posts to return. Defaults to 10. options [1-100]
        start_date (str, optional): The earliest date at which a post could be posted. Time zone is UTC. 
                                    Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” 
                                    (defaults to time 00:00:00).
        end_date (str, optional): The latest date at which a post could be posted.
                                  Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss”
                                  or “yyyy-mm-dd” (defaults to time 00:00:00).
                                  defaults to "now".
        include_history (str, optional): Includes timestep data for growth of each post returned.
                                         Defaults to null (not included). options: 'true'
        sort_by (str, optional): The method by which to filter and order posts.
                                options: 'date', 'interaction_rate', 'overperforming',
                                'total_interactions', 'underperforming'.
                                defaults 'overperforming'
        min_interactions (int, optional): If set, will exclude posts with total interactions 
                                          below this threshold. options int > 0, default 0
        offset (int, optional): The number of posts to offset (generally used for pagination). 
                                Pagination links will also be provided in the response.                                                          
        types (str, optional):  The types of post to include. These can be separated by commas 
                                to include multiple types. If you want all live videos 
                                (whether currently or formerly live), be sure to include both 
                                live_video and live_video_complete. The "video" type does not 
                                mean all videos, it refers to videos that aren't native_video,
                                youtube or vine (e.g. a video on Vimeo).   
                                options: "episode", "extra_clip", "link", "live_video", 
                                "live_video_complete", "live_video_scheduled", "native_video",
                                "photo", "status", "trailer","video", "vine", "youtube"  
                                default all
        search_term (str, optional): Returns only posts that match this search term. 
                                     Terms AND automatically. Separate with commas for OR, 
                                     use quotes for phrases. E.g. CrowdTangle API -> AND. 
                                     CrowdTangle, API -> OR. "CrowdTangle API" -> AND in that
                                     exact order. You can also use traditional Boolean search
                                     with this parameter. default null                                                                                                                         
        api_token (str, optional): you can locate your API token via your crowdtangle dashboard
                                   under Settings > API Access.
        searchTerm (str): 
    Returns:
        [dict]: The Response contains both a status code and a result. The status will always
                be 200 if there is no error. The result contains an array of post objects and
                a pagination object with URLs for both the next and previous page, if they exist
    Example:
        ct_get_posts(include_history = 'true', api_token="AKJHXDFYTGEBKRJ6535")                    
    """
    
    # api-endpoint
    URL_BASE = "https://api.crowdtangle.com/posts/search"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'count': count, 'sortBy':sort_by, 'token': api_token, 
              'minInteractions': min_interactions, 'offset': offset, }

    # add params parameters
    if offset:
        PARAMS['offset'] = offset
    if searchTerm:
        PARAMS['searchTerm'] = searchTerm
    if language:
        PARAMS['language'] = language
    if inListIds:
        PARAMS['inListIds'] = inListIds
    if start_date:
        PARAMS['startDate'] = start_date
    if end_date:
        PARAMS['endDate'] = end_date
    if include_history == 'true':
        PARAMS['includeHistory'] = include_history
    if types:
        PARAMS['types'] =  types
    if searchTerm:
        PARAMS['searchTerm'] = searchTerm
    if an:
        PARAMS['and'] = an
    if no:
        PARAMS['not'] = no



    # sending get request and saving the response as response object
    r = requests.get(url=URL_BASE, params=PARAMS)
    if r.status_code != 200:
        out = r.json()
        print(f"status: {out['status']}")
        print(f"Code error: {out['code']}")
        print(f"Message: {out['message']}")
    return r.json()


def ct_link(count=None, start_Date= None, end_Date= None, include_History= None, link= None, include_Summary= None,
                 sortBy="date", searchField= None, offset = None, api_token=None,platforms=None):

    # api-endpoint
    URL_BASE = "https://api.crowdtangle.com/links"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'count': count, 'sortBy':"date", 'token': api_token, 'offset': offset}

    # add params parameters
    if offset:
        PARAMS['offset'] = offset
    if start_Date:
        PARAMS['startDate'] = start_Date
    if end_Date:
        PARAMS['endDate'] = end_Date
    if include_History == 'true':
        PARAMS['includeHistory'] = include_History
    if link:
        PARAMS['link'] =  link
    if platforms:
        PARAMS['platforms'] =  'facebook'
    if include_Summary == 'true':
        PARAMS['include_Summary'] =  include_Summary
    if searchField:
        PARAMS['searchField'] =  Include_query_strings
        
    


    # sending get request and saving the response as response object
    r = requests.get(url=URL_BASE, params=PARAMS)
    if r.status_code != 200:
        out = r.json()
        print(f"status: {out['status']}")
        print(f"Code error: {out['code']}")
        print(f"Message: {out['message']}")
    return r.json()
