import unittest
from types import SimpleNamespace as NS
from test_package import load_function

class ParcelSourceTests(unittest.TestCase):
    def test_registry_roles_and_selected_sources(self):
        def entity(entry,role,disabled=None):
            return NS(config_entry_id=entry,translation_key=role,disabled_by=disabled,area_id=None,device_id=None)
        registry=NS(entities={
            'sensor.renamed_one':entity('dhl-account','incoming_parcels'),
            'sensor.renamed_two':entity('bring-account','awaiting_pickup'),
            'sensor.outgoing':entity('dhl-account','outgoing_delivered_parcels'),
            'sensor.disabled':entity('dhl-account','delivered_parcels','user'),
            'sensor.not_selected':entity('dhl-account','delivered_parcels'),
        })
        entries={'dhl-account':NS(domain='dhl'),'bring-account':NS(domain='posten_bring')}
        hass=NS(states=NS(get=lambda key:NS(attributes={'parcels':[]})),config_entries=NS(async_get_entry=entries.get),services=NS(has_service=lambda domain,service:domain=='dhl'))
        scope={'er':NS(async_get=lambda h:registry),'ar':NS(async_get=lambda h:NS(async_get_area=lambda key:None)),'dr':NS(async_get=lambda h:NS(devices={}))}
        fn=load_function('__init__.py','_entry_config',scope)
        entry=NS(data={'package_entities':['sensor.renamed_one','sensor.renamed_two','sensor.outgoing','sensor.disabled']},options={},entry_id='profile')
        sources=fn(hass,entry)['parcel_sources']
        self.assertEqual([s['entity'] for s in sources],['sensor.renamed_two','sensor.renamed_one'])
        self.assertEqual(sources[0]['carrier'],'Bring')
        self.assertFalse(sources[0]['can_track'])
        self.assertEqual(sources[1]['config_entry_id'],'dhl-account')
        self.assertTrue(sources[1]['can_track'])
