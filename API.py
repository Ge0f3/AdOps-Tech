import datetime

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.targetingsearch import TargetingSearch
from facebook_business.adobjects.targeting import Targeting
from facebook_business.adobjects.adimage import AdImage

from config import RequriedCredentials as RC
import pandas as pd 
from logging import warning as warn

# ...

def _precision_warn(p1, p2, extra=""):
    t = (
        "Lossy conversion from {} to {}. {} Convert image to {} prior to "
        "saving to suppress this warning."
    )
    warn(t.format(p1, p2, extra, p2))

FacebookAdsApi.init( RC.APP_ID, RC.APP_SECRET, RC.ACCESS_TOKEN)
my_account = AdAccount(RC.AD_ACCOUNT_ID)
campaigns = my_account.get_campaigns()
# print(campaigns)

campaign_created = dict()
ad_set_created= set()

bulksheet = pd.read_csv('bulksheet.csv')


def create_campaigns(campaign_name):

    params = { 
    'name': campaign_name, 
    'objective': 'POST_ENGAGEMENT', 
    'status': 'PAUSED',
    'special_ad_categories' : ['None']
    }

    campaign_result = AdAccount(RC.AD_ACCOUNT_ID).create_campaign(params=params)
    campaign_created[campaign_name]=campaign_result['id']
    print(campaign_created)
    
    if campaign_name in campaign_created:
        return campaign_created[campaign_name]
    else:
        return campaign_result['id']


def create_adset(adset_name,publisher_platform,ad_name,camp_id):
    today = datetime.date.today()
    start_time = str(today)
    end_time = str(today + datetime.timedelta(weeks=1))

    adset = AdSet(parent_id=RC.AD_ACCOUNT_ID)
    adset.update({    
        'name': adset_name,    
        'campaign_id': camp_id,    
        'daily_budget': 20978,    
        'billing_event': 'IMPRESSIONS',    
        'optimization_goal': 'REACH',    
        'bid_amount': 10,    
        'targeting': {'geo_locations': {'countries': 'TR'}},
        'publisher_platforms': publisher_platform,    
        'start_time': start_time,    
        'end_time': end_time,
    })

    adset.remote_create(params={'status': 'PAUSED'})

    image = AdImage(parent_id=RC.AD_ACCOUNT_ID)
    image[AdImage.Field.filename] = '/Users/geofe/Pictures/Wallpapers/Be_original.jpg'
    image.remote_create() 

    image_hash = image[AdImage.Field.hash]
    print(image_hash)
    fields = []
    params = {  
        'name': 'Test image',  
        'object_story_spec': {'page_id':RC.PAGE_ID,'link_data':{'image_hash':image_hash,'link':'https://www.facebook.com/API-Chop-Shop-for-Botty-106905097700335/','message':'Test '}},}
    adcreative = AdAccount(RC.AD_ACCOUNT_ID).create_ad_creative(fields=fields, params=params)

    print(adcreative)
    fields = []
    params = {  
        'name': ad_name,  
        'adset_id': adset['id'],  
        'creative': {'creative_id': adcreative['id']},
        'status': 'PAUSED'}
        
    print(AdAccount(RC.AD_ACCOUNT_ID).create_ad(fields=fields, params=params))
    print("---------------------------------------AdSet-{} created Successfull !---------------------------------------".format(adset['id']))


    

for index,row in bulksheet.iterrows():
    camp_id = create_campaigns(row['Campaign Name'])
    print("---------------------------------------Campaign - {} created Successfull !---------------------------------------".format(camp_id))
    if(row['Ad Set Name'] in ad_set_created):
        print("---------------------------------------Ad Set Name is already in Ads Manager ! ---------------------------------------".format(camp_id))
    else:
        create_adset(row['Ad Set Name'],row['Publisher Platforms'],row['Ad Name'],camp_id)
        ad_set_created.add(row['Ad Set Name'])
    


    
    

'''


params = { 
    'name': 'Creative Test Campaign pre-demo !!', 
    'objective': 'POST_ENGAGEMENT', 
    'status': 'PAUSED',
    'special_ad_categories':['None']
    
}


campaign_result = AdAccount(RC.AD_ACCOUNT_ID).create_campaign(params=params)
print(campaign_result['id'])


params = { 
    'name': 'Creative Test Campaign pre-demo !!', 
    'objective': 'POST_ENGAGEMENT', 
    'status': 'PAUSED',
    'special_ad_categories' : ['None']
}


campaign_result = AdAccount(RC.AD_ACCOUNT_ID).create_campaign(params=params)
campaigns = my_account.get_campaigns()
print(campaigns)

today = datetime.date.today()
start_time = str(today)
end_time = str(today + datetime.timedelta(weeks=1))

adset = AdSet(parent_id=RC.AD_ACCOUNT_ID)
adset.update({    
    'name': 'ADSET Test',    
    'campaign_id': '23845218716530559',    
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

image = AdImage(parent_id=RC.AD_ACCOUNT_ID)
image[AdImage.Field.filename] = '/Users/geofe/Pictures/Wallpapers/Be_original.jpg'
image.remote_create() 

image_hash = image[AdImage.Field.hash]
print(image_hash)
fields = []
params = {  
    'name': 'Test Name',  
    'object_story_spec': {'page_id':RC.PAGE_ID,'link_data':{'image_hash':image_hash,'link':'https://www.facebook.com/API-Chop-Shop-for-Botty-106905097700335/','message':'Test '}},}
adcreative = AdAccount(RC.AD_ACCOUNT_ID).create_ad_creative(fields=fields, params=params)


fields = []
params = {  
    'name': 'AD Test',  
    'adset_id': adset['id'],  
    'creative': {'creative_id': adcreative['creative_id']},
    'status': 'PAUSED'}


    
print(AdAccount(RC.AD_ACCOUNT_ID).create_ad(fields=fields, params=params))
'''