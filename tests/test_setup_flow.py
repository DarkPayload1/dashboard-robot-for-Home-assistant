import ast,asyncio,json,unittest
from types import SimpleNamespace as NS
from test_package import BASE,load_function

class SetupFlowTests(unittest.TestCase):
    def flow(self):
        tree=ast.parse((BASE/'config_flow.py').read_text())
        node=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='RobotSteps')
        env={
            'automatic_room_choices':lambda h,d:dict(d),
            'valid':lambda d:bool(d.get('dashboard_paths')),
            'basic_schema':lambda d,h:'robot',
            'integrations_schema':lambda d,h:'integrations',
            'sources_schema':lambda h,d:'sources',
            'devices_schema':lambda d,h:'devices',
            'readings_schema':lambda d,h:'readings',
            'filter_room_choices':lambda h,d:dict(d),
            'apply_sources':lambda h,d,u:{**d,**u},
            'er':NS(async_get=lambda h:NS(entities={'sensor.extra':NS(disabled_by=None)})),
        }
        exec(compile(ast.Module(body=[node],type_ignores=[]),'flow','exec'),env)
        flow=env['RobotSteps']();flow.hass=None
        flow._draft={'name':'Robot','area_ids':['living'],'agent_id':'conversation.google','read_entities':['sensor.extra'],'camera_entities':['camera.a']}
        flow.async_show_form=lambda **kw:kw
        flow.async_create_entry=lambda **kw:{'saved':kw['data']}
        return flow
    def test_short_flow_and_preserved_choices(self):
        async def run():
            flow=self.flow()
            result=await flow.async_step_placement({'language':'da','dashboard_paths':['home'],'agent_id':'conversation.google'})
            self.assertEqual(result['step_id'],'integrations')
            result=await flow.async_step_integrations({'integration_ids':['provider'],'advanced':False,'extra_readings':False})
            self.assertEqual(result['step_id'],'sources')
            result=await flow.async_step_sources({'electricity_price_entity':'sensor.price'})
            self.assertEqual(result['saved']['agent_id'],'conversation.google')
            self.assertEqual(result['saved']['read_entities'],['sensor.extra'])
            self.assertFalse(any(k.startswith('_') for k in result['saved']))
        asyncio.run(run())
    def test_optional_device_and_readings_pages(self):
        async def run():
            flow=self.flow()
            result=await flow.async_step_integrations({'integration_ids':[],'advanced':True,'extra_readings':True})
            self.assertEqual(result['step_id'],'devices')
            result=await flow.async_step_devices({'light_entities':[],'media_entities':['media_player.one'],'camera_entities':['camera.a'],'view_paths':'oversigt'})
            self.assertEqual(result['step_id'],'readings')
            result=await flow.async_step_readings({'read_entities':[]})
            self.assertEqual(result['saved']['read_entities'],[])
            self.assertEqual(result['saved']['agent_id'],'conversation.google')
        asyncio.run(run())
    def test_no_duplicated_visible_fields(self):
        obj=json.loads((BASE/'translations/da.json').read_text())
        for branch in ['config','options']:
            seen=set()
            for step in ['placement','integrations','sources','devices','readings']:
                keys=set(obj[branch]['step'][step]['data'])
                self.assertFalse(keys&seen,(step,keys&seen))
                seen|=keys
