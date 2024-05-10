from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

author: dict = scholarly.search_author_id('GsURDp0AAAAJ')
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

shieldio_data_mtl = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['publications']['GsURDp0AAAAJ:zYLM7Y9cAGgC']['num_citations']}",
}
with open(f'results/gs_data_shieldsio_mtl.json', 'w') as outfile:
    json.dump(shieldio_data_mtl, outfile, ensure_ascii=False)
    
shieldio_data_mnemonics = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['publications']['GsURDp0AAAAJ:IjCSPb-OGe4C']['num_citations']}",
}
with open(f'results/gs_data_shieldsio_mnemonics.json', 'w') as outfile:
    json.dump(shieldio_data_mnemonics, outfile, ensure_ascii=False)
    
shieldio_data_aanets = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['publications']['GsURDp0AAAAJ:2osOgNQ5qMEC']['num_citations']}",
}
with open(f'results/gs_data_shieldsio_aanets.json', 'w') as outfile:
    json.dump(shieldio_data_aanets, outfile, ensure_ascii=False)
    
shieldio_data_e3bm = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['publications']['GsURDp0AAAAJ:d1gkVwhDpl0C']['num_citations']}",
}
with open(f'results/gs_data_shieldsio_e3bm.json', 'w') as outfile:
    json.dump(shieldio_data_e3bm, outfile, ensure_ascii=False)
   
shieldio_data_lst = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['publications']['GsURDp0AAAAJ:u5HHmVD_uO8C']['num_citations']}",
}
with open(f'results/gs_data_shieldsio_lst.json', 'w') as outfile:
    json.dump(shieldio_data_lst, outfile, ensure_ascii=False)

shieldio_data_robio = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['publications']['GsURDp0AAAAJ:u-x6o8ySG0sC']['num_citations']}",
}
with open(f'results/gs_data_shieldsio_lst.json', 'w') as outfile:
    json.dump(shieldio_data_robio, outfile, ensure_ascii=False)