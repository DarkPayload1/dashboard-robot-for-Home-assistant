"""UI setup and options for Dashboard Robot."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import entity_registry as er, device_registry as dr
from homeassistant.components.frontend import DATA_PANELS
from homeassistant.helpers.selector import AreaSelector, AreaSelectorConfig, EntitySelector, EntitySelectorConfig, TextSelector, SelectSelector, SelectSelectorConfig
from .const import DOMAIN

def paths(value):
    return [p.strip().strip('/') for p in (value.split(',') if isinstance(value,str) else value or []) if p.strip()]

def room_entities(hass, area_ids, domain):
    selected=set(area_ids or [])
    registry,devices=er.async_get(hass),dr.async_get(hass)
    result=[]
    for entity_id,entity in registry.entities.items():
        if entity.disabled_by or entity_id.split('.',1)[0]!=domain:
            continue
        device=devices.devices.get(entity.device_id) if entity.device_id else None
        area_id=entity.area_id or (device.area_id if device else None)
        if area_ids is None or area_id in selected or (domain=='media_player' and selected and not area_id):
            result.append(entity_id)
    return sorted(result)

def room_schema(defaults):
    return vol.Schema({
        vol.Required('name',default=defaults.get('name','Dashboard Robot')):TextSelector(),
        vol.Required('area_ids',default=defaults.get('area_ids',[])):AreaSelector(AreaSelectorConfig(multiple=True)),
    })

def schema(defaults, hass):
    selected=paths(defaults.get('dashboard_paths', []))
    available={domain:room_entities(hass,defaults.get('area_ids',[]),domain) for domain in ['light','media_player','camera']}
    available['media_player']=room_entities(hass,None,'media_player')
    available['camera']=room_entities(hass,None,'camera')
    defaults={**defaults, 'light_entities':[e for e in (defaults.get('light_entities') or []) if e in available['light']], 'media_entities':[e for e in (defaults.get('media_entities') or []) if e in available['media_player']], 'camera_entity':defaults.get('camera_entity') if defaults.get('camera_entity') in available['camera'] else None}
    panels=hass.data.get(DATA_PANELS,{})
    options={p:p for p in selected}
    for path,panel in panels.items():
        title=getattr(panel,'title',None)
        component=getattr(panel,'component_name',None)
        if component=='lovelace' or path=='lovelace':
            options[path]=title or path
    if not options:
        options={'lovelace':'Home'}
    fields={
        vol.Required('speech_voice', default=defaults.get('speech_voice', 'auto')): SelectSelector(SelectSelectorConfig(options=[{'value':'auto','label':'Automatic'},{'value':'local','label':'On-device voice'},{'value':'online','label':'Online voice'}])),
        vol.Required('speech_rate', default=str(defaults.get('speech_rate', '0.85'))): SelectSelector(SelectSelectorConfig(options=[{'value':'0.5','label':'50 %'},{'value':'0.7','label':'70 %'},{'value':'0.85','label':'85 %'},{'value':'1','label':'100 %'},{'value':'1.1','label':'110 %'},{'value':'1.3','label':'130 %'},{'value':'1.5','label':'150 %'}])),
        vol.Required('robot_name', default=defaults.get('robot_name', 'Huself Kræz')): TextSelector(),
        vol.Optional('view_paths', default=defaults.get('view_paths','')): TextSelector(),
        vol.Required('language', default=defaults.get('language', 'da')): SelectSelector(SelectSelectorConfig(options=[{'value':'da','label':'Dansk'},{'value':'en','label':'English'},{'value':'de','label':'Deutsch'}])),
        vol.Required('dashboard_paths', default=selected): SelectSelector(SelectSelectorConfig(options=[{'value':key,'label':value} for key,value in options.items()],multiple=True,custom_value=True)),
        vol.Optional('agent_id', description={'suggested_value': defaults.get('agent_id')}): EntitySelector(EntitySelectorConfig(domain='conversation')),
        vol.Optional('light_entities', default=defaults.get('light_entities', [])): EntitySelector(EntitySelectorConfig(domain='light', multiple=True, include_entities=available['light'])),
        vol.Optional('media_entities', default=defaults.get('media_entities', [])): EntitySelector(EntitySelectorConfig(domain='media_player', multiple=True, include_entities=available['media_player'])),
        vol.Optional('electricity_price_entity', description={'suggested_value': defaults.get('electricity_price_entity')}): EntitySelector(EntitySelectorConfig(domain='sensor')),
        vol.Optional('power_entity', description={'suggested_value': defaults.get('power_entity')}): EntitySelector(EntitySelectorConfig(domain='sensor')),
        vol.Optional('waste_entity', description={'suggested_value': defaults.get('waste_entity')}): EntitySelector(EntitySelectorConfig(domain='sensor')),
        vol.Optional('fuel_entity', description={'suggested_value': defaults.get('fuel_entity')}): EntitySelector(EntitySelectorConfig(domain='sensor')),
        vol.Optional('weather_entity', description={'suggested_value': defaults.get('weather_entity')}): EntitySelector(EntitySelectorConfig(domain='weather')),
        vol.Optional('package_entities', description={'suggested_value': defaults.get('package_entities')}): EntitySelector(EntitySelectorConfig(domain='sensor', multiple=True)),
        vol.Optional('camera_entities', default=[e for e in (defaults.get('camera_entities') or ([defaults['camera_entity']] if defaults.get('camera_entity') else [])) if e in available['camera']]): EntitySelector(EntitySelectorConfig(domain='camera', multiple=True, include_entities=available['camera'])),
    }
    # Empty include_entities may be treated as unrestricted by a client.
    for key,domain in [('light_entities','light'),('media_entities','media_player'),('camera_entities','camera')]:
        if not available[domain]:
            fields={marker:value for marker,value in fields.items() if marker.schema!=key}
    return vol.Schema(fields)

def filter_room_choices(hass,data):
    data=dict(data)
    for key,domain in [('light_entities','light'),('media_entities','media_player')]:
        allowed=room_entities(hass,None if domain=='media_player' else data.get('area_ids'),domain)
        data[key]=[e for e in (data.get(key) or []) if e in allowed]
    cameras=room_entities(hass,None,'camera')
    data['camera_entities']=[e for e in (data.get('camera_entities') or ([data['camera_entity']] if data.get('camera_entity') else [])) if e in cameras]
    data['camera_entity']=next(iter(data['camera_entities']),None)
    return data

def automatic_room_choices(hass,data):
    data=dict(data)
    data['light_entities']=room_entities(hass,data.get('area_ids'),'light')
    media=room_entities(hass,data.get('area_ids'),'media_player')
    all_media=room_entities(hass,None,'media_player')
    data['media_entities']=sorted(set(media)|{e for e in (data.get('media_entities') or []) if e in all_media})
    cameras=room_entities(hass,data.get('area_ids'),'camera')
    all_cameras=room_entities(hass,None,'camera')
    previous=data.get('camera_entities') or ([data['camera_entity']] if data.get('camera_entity') else [])
    data['camera_entities']=sorted(set(cameras)|{e for e in previous if e in all_cameras})
    data['camera_entity']=next(iter(data['camera_entities']),None)
    return filter_room_choices(hass,data)

def integration_entities(hass,entry_ids):
    selected=set(entry_ids or [])
    return sorted(entity_id for entity_id,entity in er.async_get(hass).entities.items()
                  if not entity.disabled_by and entity.config_entry_id in selected)

def integration_options(hass):
    counts={}
    for entity in er.async_get(hass).entities.values():
        if not entity.disabled_by and entity.config_entry_id:
            counts[entity.config_entry_id]=counts.get(entity.config_entry_id,0)+1
    return [{'value':entry.entry_id,'label':f'{entry.title} ({entry.domain}, {counts[entry.entry_id]})'}
            for entry in hass.config_entries.async_entries()
            if entry.domain!=DOMAIN and not entry.disabled_by and entry.entry_id in counts]

def source_candidates(hass,ids):
    result={key:[] for key in ['agent_id','weather_entity','power_entity','electricity_price_entity','fuel_entity','waste_entity','package_entities']}
    for entity_id in ids:
        state=hass.states.get(entity_id)
        if state is None:continue
        domain=entity_id.split('.',1)[0]
        attrs=state.attributes
        text=(entity_id+' '+str(attrs.get('friendly_name',''))).casefold()
        unit=str(attrs.get('unit_of_measurement','')).casefold()
        if domain=='conversation':result['agent_id'].append(entity_id)
        if domain=='weather':result['weather_entity'].append(entity_id)
        if domain!='sensor':continue
        if attrs.get('device_class')=='power':result['power_entity'].append(entity_id)
        if 'kwh' in unit and '/' in unit:result['electricity_price_entity'].append(entity_id)
        if any(word in text for word in ['benzin','diesel','petrol','fuel_price','kraftstoff']):result['fuel_entity'].append(entity_id)
        if any(word in text for word in ['affald','waste','garbage','abfall','next_collection']):result['waste_entity'].append(entity_id)
        if 'parcels' in attrs:result['package_entities'].append(entity_id)
    # Prefer an explicitly current price over spot prices, taxes and forecasts.
    prices=result['electricity_price_entity']
    current=[]
    for entity_id in prices:
        state=hass.states.get(entity_id)
        text=(entity_id+' '+str(state.attributes.get('friendly_name',''))).casefold()
        if any(word in text for word in ['current_price','current price','aktuel','aktueller','price_now','price now']):
            current.append(entity_id)
    if len(current)==1:
        result['electricity_price_entity']=current
    return result

def sources_schema(hass,defaults):
    ids=integration_entities(hass,defaults.get('integration_ids'))
    candidates=source_candidates(hass,ids)
    fields={}
    for key,found in candidates.items():
        if key=='agent_id':continue
        domain='conversation' if key=='agent_id' else 'weather' if key=='weather_entity' else 'sensor'
        allowed=[e for e in ids if e.startswith(domain+'.')]
        if not allowed:continue
        previous=defaults.get(key)
        if key=='package_entities':
            value=[e for e in (previous or found) if e in allowed]
            fields[vol.Optional(key,default=value)]=EntitySelector(EntitySelectorConfig(multiple=True,include_entities=allowed))
        else:
            value=previous if previous in allowed else found[0] if len(found)==1 else None
            marker=vol.Optional(key,default=value) if value is not None else vol.Optional(key)
            fields[marker]=EntitySelector(EntitySelectorConfig(include_entities=allowed))
    return vol.Schema(fields)

def apply_sources(hass,draft,user_input):
    data=dict(draft)
    allowed=set(integration_entities(hass,data.get('integration_ids')))
    for key in ['weather_entity','power_entity','electricity_price_entity','fuel_entity','waste_entity']:
        data[key]=user_input.get(key) if user_input.get(key) in allowed else None
    for key in ['package_entities']:
        data[key]=[e for e in (user_input.get(key) or []) if e in allowed]
    return data

def basic_schema(defaults,hass):
    return vol.Schema({marker:value for marker,value in schema(defaults,hass).schema.items()
                       if marker.schema in ['robot_name','speech_voice','speech_rate','language','dashboard_paths','agent_id']})

def integrations_schema(defaults,hass):
    options=integration_options(hass)
    fields={}
    if options:
        fields[vol.Optional('integration_ids',default=[e for e in defaults.get('integration_ids',[]) if e in {o['value'] for o in options}])]=SelectSelector(SelectSelectorConfig(options=options,multiple=True))
    fields[vol.Required('advanced',default=False)]=bool
    fields[vol.Required('extra_readings',default=False)]=bool
    return vol.Schema(fields)

def devices_schema(defaults,hass):
    return vol.Schema({marker:value for marker,value in schema(defaults,hass).schema.items()
                       if marker.schema in ['light_entities','media_entities','camera_entities','view_paths']})

def readings_schema(defaults,hass):
    ids=[entity_id for entity_id,entity in er.async_get(hass).entities.items()
         if not entity.disabled_by and entity_id.split('.',1)[0] in ['sensor','binary_sensor','calendar','weather']]
    if not ids:return vol.Schema({})
    return vol.Schema({vol.Optional('read_entities',default=[e for e in (defaults.get('read_entities') or []) if e in ids]):EntitySelector(EntitySelectorConfig(multiple=True,include_entities=sorted(ids)))})

def valid(data):
    selected=paths(data.get('dashboard_paths',[]))
    return bool(selected) and all('/' not in p and not any(c in p for c in '*?#:') for p in selected)

class RobotSteps:
    def _finish(self):
        data={key:value for key,value in self._draft.items() if not key.startswith('_')}
        return self.async_create_entry(title=data['name'],data=data)

    async def async_step_placement(self,user_input=None):
        errors={}
        if user_input is not None:
            data={**self._draft,**user_input}
            if valid(data):
                data['agent_id']=user_input.get('agent_id')
                self._draft=automatic_room_choices(self.hass,data)
                return await self.async_step_integrations()
            errors['base']='invalid_paths'
        return self.async_show_form(step_id='placement',data_schema=basic_schema({**self._draft,**(user_input or {})},self.hass),errors=errors)

    async def async_step_integrations(self,user_input=None):
        if user_input is not None:
            self._draft.update(integration_ids=user_input.get('integration_ids',[]),_advanced=user_input.get('advanced',False),_extra_readings=user_input.get('extra_readings',False))
            if self._draft['integration_ids']:
                return await self.async_step_sources()
            # No chosen source page: retain manually configured roles and AI.
            return await self._after_sources()
        return self.async_show_form(step_id='integrations',data_schema=integrations_schema(self._draft,self.hass))

    async def async_step_sources(self,user_input=None):
        if user_input is not None:
            self._draft=apply_sources(self.hass,self._draft,user_input)
            return await self._after_sources()
        return self.async_show_form(step_id='sources',data_schema=sources_schema(self.hass,self._draft))

    async def _after_sources(self):
        if self._draft.get('_advanced'):
            return await self.async_step_devices()
        return await self._after_devices()

    async def async_step_devices(self,user_input=None):
        if user_input is not None:
            self._draft.update(user_input)
            for key in ['light_entities','media_entities','camera_entities']:
                self._draft[key]=user_input.get(key,[])
            self._draft['camera_entity']=None
            self._draft=filter_room_choices(self.hass,self._draft)
            return await self._after_devices()
        return self.async_show_form(step_id='devices',data_schema=devices_schema(self._draft,self.hass))

    async def _after_devices(self):
        if self._draft.get('_extra_readings'):
            return await self.async_step_readings()
        return self._finish()

    async def async_step_readings(self,user_input=None):
        if user_input is not None:
            allowed={entity_id for entity_id,entity in er.async_get(self.hass).entities.items() if not entity.disabled_by and entity_id.split('.',1)[0] in ['sensor','binary_sensor','calendar','weather']}
            self._draft['read_entities']=[e for e in user_input.get('read_entities',[]) if e in allowed]
            return self._finish()
        return self.async_show_form(step_id='readings',data_schema=readings_schema(self._draft,self.hass))

class RobotConfigFlow(RobotSteps, config_entries.ConfigFlow, domain=DOMAIN):
    VERSION=1
    async def async_step_user(self,user_input=None):
        errors={}
        if user_input is not None:
            if user_input.get('area_ids'):
                self._draft=dict(user_input)
                return await self.async_step_placement()
            errors['base']='choose_rooms'
        return self.async_show_form(step_id='user',data_schema=room_schema(user_input or {}),errors=errors)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return RobotOptionsFlow()

class RobotOptionsFlow(RobotSteps,config_entries.OptionsFlow):
    async def async_step_init(self,user_input=None):
        defaults={**self.config_entry.data,**self.config_entry.options}
        errors={}
        if user_input is not None:
            if user_input.get('area_ids'):
                self._draft={**defaults,**user_input}
                return await self.async_step_placement()
            errors['base']='choose_rooms'
        return self.async_show_form(step_id='init',data_schema=room_schema(user_input or defaults),errors=errors)
