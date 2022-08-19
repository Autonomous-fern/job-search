import os
import creds
from pyairtable import Table

# !! AIRTABLE API IS LIMITED TO 5 requests/sec !!

api_key = creds.AIRTABLE_API_KEY
base_id = creds.BASE_ID
table_id = creds.TABLE_ID

table = Table(api_key, base_id, table_id)

# BASIC stuff_________________________________________________________
# first_test5_record = table.first(formula="({Name}='test5')")
# test5_records = table.all(formula="({Name}='test5')")
# record_ids_to_delete = [records["id"] for records in test5_records]
# table.batch_delete(record_ids_to_delete)
