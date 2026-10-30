import ast,json,unittest
from pathlib import Path
from types import SimpleNamespace as NS
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'custom_components/dashboard_robot'

def load_function(file,name,scope=None):
    tree=ast.parse((BASE/file).read_text())
    node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==name)
    env={} if scope is None else scope
    exec(compile(ast.Module(body=[node],type_ignores=[]),str(file),'exec'),env)
    return env[name]

class PackageTests(unittest.TestCase):
    def test_python_and_json_parse(self):
        for p in BASE.rglob('*.py'):compile(p.read_text(),str(p),'exec')
        for p in BASE.rglob('*.json'):json.loads(p.read_text())
    def test_old_and_new_dashboard_paths(self):
        paths=load_function('config_flow.py','paths')
        valid=load_function('config_flow.py','valid',{'paths':paths})
        self.assertTrue(valid({'dashboard_paths':'home,tablet'}))
        self.assertTrue(valid({'dashboard_paths':['home','tablet']}))
        for value in [[], '', ['https://example.com'],['home/view'],['*']]:self.assertFalse(valid({'dashboard_paths':value}))
    def test_localized_forms_have_same_fields(self):
        reference=json.loads((BASE/'strings.json').read_text())
        for lang in ['da','en','de']:
            obj=json.loads((BASE/f'translations/{lang}.json').read_text())
            for branch,step in [('config','user'),('options','init'),('config','devices'),('options','devices'),('config','placement'),('options','placement'),('config','sources'),('options','sources'),('config','integrations'),('options','integrations'),('config','readings'),('options','readings')]:
                self.assertEqual(set(reference[branch]['step'][step]['data']),set(obj[branch]['step'][step]['data']))
    def test_selected_entities_and_area_resolution(self):
        registry=NS(entities={
            'light.one':NS(disabled_by=None,area_id='living',device_id=None),
            'light.other':NS(disabled_by=None,area_id='living',device_id=None),
            'media_player.one':NS(disabled_by=None,area_id=None,device_id='speaker'),
            'media_player.unassigned':NS(disabled_by=None,area_id=None,device_id=None),
        })
        areas=NS(async_get_area=lambda key:NS(name='Living room') if key=='living' else None)
        devices=NS(devices={'speaker':NS(area_id='living')})
        scope={'er':NS(async_get=lambda h:registry),'ar':NS(async_get=lambda h:areas),'dr':NS(async_get=lambda h:devices)}
        fn=load_function('__init__.py','_entry_config',scope)
        entry=NS(data={'light_entities':['light.one'],'media_entities':['media_player.one'],'language':'da'},options={'language':'de'},entry_id='fixture')
        cfg=fn(NS(states=NS(get=lambda entity:object())),entry)
        self.assertEqual(cfg['language'],'de')
        self.assertEqual(cfg['controls']['lights'],{'living room':['light.one']})
        self.assertEqual(cfg['controls']['speakers'],{'living room':['media_player.one']})
        self.assertEqual(cfg['profile_id'],'fixture')
        entry.options['media_entities']=['media_player.unassigned']
        cfg=fn(NS(states=NS(get=lambda entity:NS(attributes={'friendly_name':'Portable speaker'}))),entry)
        self.assertEqual(cfg['controls']['speakers'],{'portable speaker':['media_player.unassigned']})
    def test_no_personal_identifiers_or_credentials(self):
        forbidden=['nicolai','nakskov','maribovej','stromligning_current','watts_live_012','192.168.','duckdns.org']
        for p in BASE.rglob('*'):
            if not p.is_file() or p.suffix in ['.png','.pyc']:continue
            data=p.read_text().lower()
            for value in forbidden:self.assertNotIn(value,data,str(p))
    def test_room_choices_filter_and_clear_old_devices(self):
        registry=NS(entities={
            'light.one':NS(disabled_by=None,area_id='living',device_id=None),
            'light.other':NS(disabled_by=None,area_id='bath',device_id=None),
            'light.disabled':NS(disabled_by='user',area_id='living',device_id=None),
            'media_player.one':NS(disabled_by=None,area_id=None,device_id='speaker'),
            'camera.other':NS(disabled_by=None,area_id='bath',device_id=None),
            'camera.second':NS(disabled_by=None,area_id='bath',device_id=None),
            'camera.portable':NS(disabled_by=None,area_id=None,device_id=None),
            'media_player.portable':NS(disabled_by=None,area_id=None,device_id=None),
            'media_player.other_room':NS(disabled_by=None,area_id='bath',device_id=None),
        })
        scope={'er':NS(async_get=lambda h:registry),'dr':NS(async_get=lambda h:NS(devices={'speaker':NS(area_id='living')}))}
        rooms=load_function('config_flow.py','room_entities',scope)
        self.assertEqual(rooms(None,['living'],'light'),['light.one'])
        self.assertEqual(rooms(None,['living'],'media_player'),['media_player.one','media_player.portable'])
        self.assertEqual(rooms(None,None,'media_player'),['media_player.one','media_player.other_room','media_player.portable'])
        self.assertEqual(rooms(None,[],'light'),[])
        filter_choices=load_function('config_flow.py','filter_room_choices',{'room_entities':rooms})
        cfg=filter_choices(None,{'area_ids':['living'],'light_entities':['light.one','light.other'],'camera_entity':'camera.other','media_entities':None})
        self.assertEqual(cfg['light_entities'],['light.one'])
        self.assertEqual(cfg['media_entities'],[])
        self.assertEqual(cfg['camera_entity'],'camera.other')
        auto=load_function('config_flow.py','automatic_room_choices',{'room_entities':rooms,'filter_room_choices':filter_choices})
        cfg=auto(None,{'area_ids':['living'],'light_entities':[],'media_entities':[]})
        self.assertEqual(cfg['light_entities'],['light.one'])
        self.assertEqual(cfg['media_entities'],['media_player.one','media_player.portable'])
        cfg=auto(None,{'area_ids':['bath'],'light_entities':['light.one']})
        self.assertEqual(cfg['light_entities'],['light.other'])
        self.assertEqual(cfg['media_entities'],['media_player.other_room','media_player.portable'])
        self.assertEqual(cfg['camera_entity'],'camera.other')
        self.assertEqual(cfg['camera_entities'],['camera.other','camera.second'])
        manual=filter_choices(None,{'camera_entities':['camera.portable','camera.deleted']})
        self.assertEqual(manual['camera_entities'],['camera.portable'])
        cfg=auto(None,{'area_ids':['living'],'camera_entity':'camera.other'})
        self.assertEqual(cfg['camera_entity'],'camera.other')
        cfg=auto(None,{'area_ids':['bath'],'camera_entity':'camera.other'})
        self.assertEqual(cfg['camera_entity'],'camera.other')

    def test_brand_sizes(self):
        import struct
        for name,size in [('icon.png',256),('icon@2x.png',512)]:
            raw=(BASE/'brand'/name).read_bytes()
            self.assertEqual(raw[:8],b'\x89PNG\r\n\x1a\n')
            self.assertEqual(struct.unpack('>II',raw[16:24]),(size,size))

if __name__=='__main__':unittest.main()
