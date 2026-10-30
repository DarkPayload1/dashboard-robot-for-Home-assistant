import unittest
from types import SimpleNamespace as NS
from test_package import load_function

class DiscoveryTests(unittest.TestCase):
    def fixtures(self):
        entities={
            'sensor.petrol':NS(config_entry_id='fuel',disabled_by=None),
            'sensor.petrol_two':NS(config_entry_id='fuel',disabled_by=None),
            'sensor.disabled':NS(config_entry_id='fuel',disabled_by='user'),
            'sensor.secret':NS(config_entry_id='other',disabled_by=None),
        }
        entries=[NS(entry_id='fuel',domain='different_provider',title='Fuel prices',disabled_by=None),NS(entry_id='other',domain='other',title='Other',disabled_by=None)]
        states={'sensor.petrol':NS(attributes={'friendly_name':'Petrol station','unit_of_measurement':'DKK/L'}),'sensor.petrol_two':NS(attributes={'friendly_name':'Diesel','unit_of_measurement':'DKK/L'})}
        hass=NS(config_entries=NS(async_entries=lambda:entries),states=NS(get=states.get))
        scope={'er':NS(async_get=lambda h:NS(entities=entities)),'DOMAIN':'dashboard_robot'}
        return hass,scope
    def test_provider_independent_selection_and_disabled_filter(self):
        hass,scope=self.fixtures()
        entities=load_function('config_flow.py','integration_entities',scope)
        self.assertEqual(entities(hass,['fuel']),['sensor.petrol','sensor.petrol_two'])
        self.assertEqual(entities(hass,[]),[])
        options=load_function('config_flow.py','integration_options',scope)(hass)
        self.assertEqual(options[0]['value'],'fuel')
        self.assertIn('Fuel prices',options[0]['label'])
    def test_multiple_candidates_not_arbitrarily_chosen(self):
        hass,scope=self.fixtures()
        candidates=load_function('config_flow.py','source_candidates')(hass,['sensor.petrol','sensor.petrol_two'])
        self.assertEqual(candidates['fuel_entity'],['sensor.petrol','sensor.petrol_two'])
        self.assertEqual(candidates['electricity_price_entity'],[])
    def test_save_rejects_entities_from_unselected_provider_and_clears_fields(self):
        hass,scope=self.fixtures()
        entities=load_function('config_flow.py','integration_entities',scope)
        save=load_function('config_flow.py','apply_sources',{'integration_entities':entities})
        result=save(hass,{'integration_ids':['fuel'],'waste_entity':'sensor.secret','read_entities':['sensor.petrol_two']}, {'fuel_entity':'sensor.petrol','read_entities':['sensor.petrol_two','sensor.secret']})
        self.assertEqual(result['fuel_entity'],'sensor.petrol')
        self.assertEqual(result['read_entities'],['sensor.petrol_two'])
        self.assertIsNone(result['waste_entity'])

    def test_current_electricity_price_wins_over_components(self):
        states={
            'sensor.provider_current_price':NS(attributes={'friendly_name':'Aktuel inkl. moms','unit_of_measurement':'kr/kWh'}),
            'sensor.provider_spot':NS(attributes={'friendly_name':'Spotpris','unit_of_measurement':'kr/kWh'}),
            'sensor.provider_today_min':NS(attributes={'friendly_name':'Laveste pris','unit_of_measurement':'kr/kWh'}),
            'sensor.provider_tax':NS(attributes={'friendly_name':'Afgift','unit_of_measurement':'kr/kWh'}),
        }
        fn=load_function('config_flow.py','source_candidates')
        result=fn(NS(states=NS(get=states.get)),list(states))
        self.assertEqual(result['electricity_price_entity'],['sensor.provider_current_price'])
        states['sensor.second_current_price']=NS(attributes={'unit_of_measurement':'kr/kWh'})
        result=fn(NS(states=NS(get=states.get)),list(states))
        self.assertEqual(len(result['electricity_price_entity']),5)

    def test_independent_ai_choice_survives_source_review_and_reopen(self):
        hass,scope=self.fixtures()
        entities=load_function('config_flow.py','integration_entities',scope)
        save=load_function('config_flow.py','apply_sources',{'integration_entities':entities})
        data={'integration_ids':['fuel'],'agent_id':'conversation.google_ai'}
        for _ in range(3):
            data=save(hass,data,{'fuel_entity':'sensor.petrol'})
            self.assertEqual(data['agent_id'],'conversation.google_ai')
        # AI is now owned exclusively by the Robot page, never Sources.
        scope['er'].async_get(hass).entities['conversation.agent']=NS(config_entry_id='fuel',disabled_by=None)
        cleared=save(hass,data,{})
        self.assertEqual(cleared['agent_id'],'conversation.google_ai')
