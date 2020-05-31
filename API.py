import datetime

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.targetingsearch import TargetingSearch
from facebook_business.adobjects.targeting import Targeting
from facebook_business.adobjects.adimage import AdImage


access_token = 'EAAKc3n4wikYBAOewatZB4Knh85gZBQGN3f0qZCIdT36zJmADPT1nANHs9XmvZA19SqOyGQRYndwgYh9ec22AxxUXLzu5eZCN0TZCwSkIYW79eARGykD8nHQpZApHf8m4lgiywSTeyaTgJ4jTUUYiZBJjxcORqX5NZCeIBOchPGYYFgxe4S9ZA9PQUQ8JFiv2bc3HwZD'
app_secret = '1e10d16ea04132d8697bece15d3f58ee'
app_id = '735429367204422'
ad_account_id = 'act_213629878'
page_id = '102321268159896'



FacebookAdsApi.init(access_token=access_token)

params = { 
    'name': 'Campaign Test', 
    'objective': 'POST_ENGAGEMENT', 
    'status': 'PAUSED',
    'special_ad_categories' : ['None']
}


campaign_result = AdAccount(ad_account_id).create_campaign(params=params)
print(campaign_result)

today = datetime.date.today()
start_time = str(today)
end_time = str(today + datetime.timedelta(weeks=1))

adset = AdSet(parent_id=ad_account_id)
adset.update({    
    'name': 'ADSET Test',    
    'campaign_id': '6184277186301',    
    'daily_budget': 20978,    
    'billing_event': 'IMPRESSIONS',    
    'optimization_goal': 'REACH',    
    'bid_amount': 10,    
    'targeting': {'geo_locations': {'countries': 'TR'}},
    'publisher_platforms': 'facebook',    
    'start_time': start_time,    
    'end_time': end_time,
})

adset.remote_create(params={'status': 'ACTIVE'})

print(adset)

image = AdImage(parent_id=ad_account_id)
image[AdImage.Field.filename] = '/Users/geofe/Pictures/Wallpapers/Be_original.jpg'
image.remote_create() 

image_hash = image[AdImage.Field.hash]
print(image_hash)
fields = []
params = {  
    'name': 'Test Name',  
    'object_story_spec': {'page_id':page_id,'link_data':{'image_hash':image_hash,'link':'https://www.facebook.com/API-Chop-Shop-for-Botty-106905097700335/','message':'Test '}},}
adcreative = AdAccount(ad_account_id).create_ad_creative(fields=fields, params=params)


fields = []
params = {  
    'name': 'AD Test',  
    'adset_id': adset['id'],  
    'creative': {'creative_id': adcreative['creative_id']},
    'status': 'PAUSED'}


    
print(AdAccount(ad_account_id).create_ad(fields=fields, params=params))