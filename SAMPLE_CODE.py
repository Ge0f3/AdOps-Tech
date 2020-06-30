# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebookads.adobjects.business import Business
from facebookads.adobjects.productcatalog import ProductCatalog
from facebookads.adobjects.productfeed import ProductFeed
from facebookads.adobjects.productset import ProductSet
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adpreview import AdPreview
from facebookads.api import FacebookAdsApi

access_token = 'EAAMKqQl6f7IBAP8puZCc6oBYRA8pnw0Nump8rZBeaUgUzjVdubVZBRu6tV8w0KkO8ITIFzelgYBWt60ZCyGFjBMjvVvZBq35jgKUQOhW1VN2CI2Ist9hacjQzLRVGWXzwQ0qBjbjG9gJt5MMygOUStYR2pv1rpzVtMRDn2383SivS0c93PZAnNQlEhVGSfZAYnmQh3dkbzXaQZDZD'
app_secret = 'cecf581c1e3916cb73d3ff0a2de74c53'
ad_account_id = '3069537593134411'
business_id = '699539507564745'
page_id = '113744243668266'
pixel_id = '266546624542113'
app_id = '856146054905778'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
    'name': 'Test Catalog',
}
product_catalog = Business(business_id).create_owned_product_catalog(
    fields=fields,
    params=params,
)
print 'product_catalog', product_catalog

product_catalog_id = product_catalog.get_id()
print 'product_catalog_id:', product_catalog_id, '\n'

fields = [
]
params = {
    'name': 'Test Feed',
    'schedule': {'interval':'DAILY','url':'https://developers.facebook.com/resources/dpa_product_catalog_sample_feed.csv','hour':'22'},
}
ProductCatalog(product_catalog_id).create_product_feed(
    fields=fields,
    params=params,
)


fields = [
]
params = {
    'name': 'All Product',
}
product_set = ProductCatalog(product_catalog_id).create_product_set(
    fields=fields,
    params=params,
)
print 'product_set', product_set

product_set_id = product_set.get_id()
print 'product_set_id:', product_set_id, '\n'

fields = [
]
params = {
    'external_event_sources': [pixel_id],
}
print ProductCatalog(product_catalog_id).create_external_event_source(
    fields=fields,
    params=params,
)


fields = [
]
params = {
    'name': 'My Campaign',
    'objective': 'PRODUCT_CATALOG_SALES',
    'promoted_object': {'product_catalog_id':product_catalog_id},
    'status': 'PAUSED',
}
campaign = AdAccount(ad_account_id).create_campaign(
    fields=fields,
    params=params,
)
print 'campaign', campaign

campaign_id = campaign.get_id()
print 'campaign_id:', campaign_id, '\n'

fields = [
]
params = {
    'name': 'My AdSet',
    'optimization_goal': 'OFFSITE_CONVERSIONS',
    'billing_event': 'IMPRESSIONS',
    'bid_amount': '20',
    'promoted_object': {'product_set_id': product_set_id},
    'daily_budget': '1000',
    'campaign_id': campaign_id,
    'targeting': {'geo_locations':{'countries':['US']}},
    'status': 'PAUSED',
}
ad_set = AdAccount(ad_account_id).create_ad_set(
    fields=fields,
    params=params,
)
print 'ad_set', ad_set

ad_set_id = ad_set.get_id()
print 'ad_set_id:', ad_set_id, '\n'

fields = [
]
params = {
    'name': 'My Creative',
    'object_story_spec': {'page_id': page_id, 'template_data': {'call_to_action': {'type': 'SHOP_NOW'}, 'link': 'www.example.com', 'name': '{{product.name}} - {{product.price}}', 'description': '{{product.description}}', 'message': '{{product.name | titleize}}'}},
    'applink_treatment': 'web_only',
    'product_set_id': product_set_id,
    'url_tags': 'utm_source=facebook',
}
creative = AdAccount(ad_account_id).create_ad_creative(
    fields=fields,
    params=params,
)
print 'creative', creative

creative_id = creative.get_id()
print 'creative_id:', creative_id, '\n'

fields = [
]
params = {
    'name': 'My Ad',
    'adset_id': ad_set_id,
    'creative': {'creative_id':creative_id},
    'tracking_specs': [ {'action_type': ['offsite_conversion'], 'fb_pixel': [pixel_id]} ],
    'status': 'PAUSED',
}
ad = AdAccount(ad_account_id).create_ad(
    fields=fields,
    params=params,
)
print 'ad', ad

ad_id = ad.get_id()
print 'ad_id:', ad_id, '\n'

fields = [
]
params = {
    'ad_format': 'DESKTOP_FEED_STANDARD',
}
print Ad(ad_id).get_previews(
    fields=fields,
    params=params,
)


