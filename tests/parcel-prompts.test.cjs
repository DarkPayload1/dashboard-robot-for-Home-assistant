const fs=require('fs'),vm=require('vm'),assert=require('assert');let C;
vm.runInNewContext(fs.readFileSync('custom_components/dashboard_robot/frontend/robot.js','utf8').split('// Dashboard-scoped singleton.')[0],{HTMLElement:class{},customElements:{get(){},define(n,c){C=c}},window:{}});
const r=Object.create(C.prototype);r._hass={states:{},services:{gls:{track_parcel:{}},postnord:{track_parcel:{}},dhl:{track_parcel:{}}}};
r._config={language:'da',sources:['GLS','PostNord','DHL'].map(carrier=>({carrier}))};
for(const carrier of ['GLS','PostNord','DHL']){
 for(const [lang,q,expected] of [['da','Kan du tilføje en '+carrier+' pakke',/pakkenummeret/],['en','Can you add '+carrier+' parcel',/tracking number/],['de',carrier+'-Paket hinzufügen',/Sendungsnummer/]]){
  r._config.language=lang;const reply=r._parseParcelCommand(q);assert.match(reply.error,expected);assert.ok(reply.error.includes(carrier));
 }
}
for(const carrier of ['DAO','Bring']){
 for(const [lang,q,expected] of [['da','Kan du tilføje en '+carrier+' pakke',/automatisk/],['en','Can you add '+carrier+' parcel',/automatically/],['de',carrier+'-Paket hinzufügen',/automatisch/]]){
  r._config.language=lang;const reply=r._parseParcelCommand(q);assert.match(reply.error,expected);assert.ok(reply.error.includes(carrier));assert.ok(!reply.error.includes('GLS'));assert.ok(!reply.domain);
 }
}
r._config.language='da';r._config.sources=[{carrier:'DHL'}];const missing=r._parseParcelCommand('Tilføj en pakke').error;assert.match(missing,/DHL/);assert.ok(!missing.includes('GLS'));assert.match(r._parseParcelCommand('Fjern en DAO pakke').error,/automatisk/);
r._config.sources=[{entity:'sensor.dao',carrier:'DAO',kind:'incoming',can_untrack:false}];r._config.package_entities=['sensor.dao'];r._hass.states['sensor.dao']={state:'1',attributes:{parcels:[{barcode:'DAO12345678',sender:'DAO shop',status:'in_transit'}]}};assert.match(r._answerQuestion('Har jeg nogen DAO pakker?'),/DAO shop/);assert.equal(r._model(r._hass.states).parcels[0].can_untrack,false);
