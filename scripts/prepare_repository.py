"""Set links to the actual publication repository, without creating/publishing it."""
import json,re,sys
from pathlib import Path
if len(sys.argv)!=2 or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',sys.argv[1]):
    raise SystemExit('Usage: python scripts/prepare_repository.py OWNER/REPOSITORY')
root=Path(__file__).resolve().parents[1]
p=root/'custom_components/dashboard_robot/manifest.json'
data=json.loads(p.read_text());url='https://github.com/'+sys.argv[1]
data.update(documentation=url+'#readme',issue_tracker=url+'/issues',codeowners=['@'+sys.argv[1].split('/')[0]])
p.write_text(json.dumps(data,indent=2)+'\n')
print('Manifest links prepared. No repository was created or published.')
