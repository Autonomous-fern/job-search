import os
import creds
from pyairtable import Table

# !! AIRTABLE API IS LIMITED TO 5 requests/sec !!

api_key = creds.AIRTABLE_API_KEY
base_id = creds.BASE_ID
table_id = creds.TABLE_ID

table = Table(api_key, base_id, table_id)
