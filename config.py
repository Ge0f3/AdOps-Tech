import os 
import json 

class RequriedCredentials(object):
    
    ACCESS_TOKEN =  os.getenv('access_token','EAAMKqQl6f7IBAKUf6ND4Ng4OZAulkZCmwEZBiDbKHZAxGohRgoa2vhi6jdm5716iFZBDgYJdWqg79eHwXTouYODOhVZB9yW743EbA2Ob1zSX2UYllfj7TSnE7hZC0G7uCdggJJmGMYG0dMYTRe9EJXBrsZB1DtZBVJrrZBIaywr8QuD2JlAnk6r8NDJZBOuMxi2GlYZD')
    APP_SECRET = os.getenv('app_secret','cecf581c1e3916cb73d3ff0a2de74c53')
    APP_ID = os.getenv('app_id','856146054905778')
    AD_ACCOUNT_ID = os.getenv('ad_account_id','act_553598345584321')
    PAGE_ID = os.getenv('page_id','106905097700335')