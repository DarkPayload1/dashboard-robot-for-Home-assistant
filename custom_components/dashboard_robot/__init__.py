"""Standalone floating dashboard companion."""
from pathlib import Path
import voluptuous as vol
from homeassistant.components import frontend, websocket_api
from homeassistant.components.http import StaticPathConfig
from homeassistant.helpers import area_registry as ar, device_registry as dr, entity_registry as er
from .const import DOMAIN, VERSION, FRONTEND_SCRIPT

async def async_setup(hass, config):
    if DOMAIN in hass.data:
        return True
    hass.data[DOMAIN] = {}
    await hass.http.async_register_static_paths([StaticPathConfig('/dashboard_robot_static', str(Path(__file__).parent / 'frontend'), cache_headers=True)])
    frontend.add_extra_js_url(hass, f'/dashboard_robot_static/{FRONTEND_SCRIPT}?v={VERSION}')
    websocket_api.async_register_command(hass, ws_config)
    return True

async def async_setup_entry(hass, entry):
    await async_setup(hass, {})
    entry.async_on_unload(entry.add_update_listener(_updated))
    return True

async def _updated(hass, entry):
    await hass.config_entries.async_reload(entry.entry_id)

async def async_unload_entry(hass, entry):
    return True

@websocket_api.websocket_command({vol.Required('type'): 'dashboard_robot/config'})
@websocket_api.async_response
async def ws_config(hass, connection, msg):
    entries = hass.config_entries.async_entries(DOMAIN)
    result=[]
    for entry in entries:
        if entry.state.value == 'loaded':
            result.append(_entry_config(hass,entry))
    connection.send_result(msg['id'], result)

def _entry_config(hass,entry):
    cfg = {**entry.data, **entry.options}
    entities, devices, areas = er.async_get(hass), dr.async_get(hass), ar.async_get(hass)
    lights, speakers = {}, {}
    camera_labels={}
    allowed_cameras=set(cfg.get('camera_entities') or ([cfg['camera_entity']] if cfg.get('camera_entity') else []))
    allowed_lights, allowed_media = set(cfg.get('light_entities', [])), set(cfg.get('media_entities', []))
    for entity_id, entity in entities.entities.items():
        if entity.disabled_by or hass.states.get(entity_id) is None:
            continue
        device = devices.devices.get(entity.device_id) if entity.device_id else None
        area_id = entity.area_id or (device.area_id if device else None)
        area = areas.async_get_area(area_id) if area_id else None
        if entity_id in allowed_cameras:
            state=hass.states.get(entity_id)
            name=getattr(state,'attributes',{}).get('friendly_name',entity_id)
            camera_labels[entity_id]=name+(' · '+area.name if area else '')
        if entity_id in allowed_media:
            state=hass.states.get(entity_id)
            name=getattr(state,'attributes',{}).get('friendly_name',entity_id.split('.',1)[-1].replace('_',' '))
            speaker_key=(area.name if area else name).casefold().strip()
            speaker_key={'gange':'gang'}.get(speaker_key,speaker_key)
            speakers.setdefault(speaker_key, []).append(entity_id)
        if cfg.get('area_ids') and area_id not in cfg['area_ids']:
            continue
        if not area:
            continue
        key = area.name.casefold().strip()
        key = {'gange':'gang'}.get(key, key)
        if entity_id in allowed_lights:
            lights.setdefault(key, []).append(entity_id)
    return {**cfg, 'camera_labels': camera_labels, 'profile_id': entry.entry_id, 'controls': {'lights': lights, 'speakers': speakers}}
