const fs=require('fs'),vm=require('vm'),assert=require('assert');let C;
vm.runInNewContext(fs.readFileSync('custom_components/dashboard_robot/frontend/robot.js','utf8').split('// Dashboard-scoped singleton.')[0],{HTMLElement:class{},customElements:{get(){},define(n,c){C=c}},window:{}});
const r=Object.create(C.prototype),sources=[{entity:'sensor.renamed_dhl',carrier:'DHL',kind:'incoming',config_entry_id:'dhl-selected',can_track:true,can_untrack:true},{entity:'sensor.renamed_bring',carrier:'Bring',kind:'incoming',can_track:false,can_untrack:false}];
r._config={language:'da',sources,package_entities:sources.map(s=>s.entity)};let calls=[];r._hass={services:{dhl:{track_parcel:{},untrack_parcel:{}}},states:{'sensor.renamed_dhl':{state:'1',attributes:{parcels:[{tracking_code:'00123456789',sender:'DHL sender',status:'in_transit'}]}},'sensor.renamed_bring':{state:'1',attributes:{parcels:[{tracking_code:'BR123456789',sender:'Bring sender',status:'at_pickup_point'}]}}},callService:async(...args)=>calls.push(JSON.parse(JSON.stringify(args)))};r._update=()=>{};
(async()=>{
for(const [lang,dhl,bring,add] of [['da','Har jeg DHL pakker?','Har jeg Bring pakker?','Tilføj DHL pakke 00123456789'],['en','Any DHL parcels?','Any Bring parcels?','Add DHL parcel 00123456789'],['de','Habe ich DHL Pakete?','Habe ich Bring Pakete?','DHL-Paket 00123456789 hinzufügen']]){
 r._config.language=lang;assert.match(r._answerQuestion(dhl),/DHL sender/);assert.ok(!r._answerQuestion(dhl).includes('Bring sender'));assert.match(r._answerQuestion(bring),/Bring sender/);assert.ok(!r._answerQuestion(bring).includes('DHL sender'));
 const command=r._parseParcelCommand(add);assert.equal(command.domain,'dhl');await r._handleParcelCommand(command);assert.deepStrictEqual(calls.pop(),['dhl','track_parcel',{tracking_code:'00123456789',config_entry_id:'dhl-selected'}]);
}
r._config.language='da';assert.match(r._parseParcelCommand('Tilføj Bring pakke BR123456789').error,/manuelt/);assert.equal(calls.length,0);
await r._handleParcelCommand(r._parseParcelCommand('Fjern DHL pakke 00123456789'));assert.equal(calls.length,0);await r._confirmParcel();assert.equal(calls.pop()[1],'untrack_parcel');await r._confirmParcel();assert.equal(calls.length,0);
r._hass.states['sensor.renamed_bring'].state='unavailable';assert.match(r._answerQuestion('Bring pakker'),/utilgængelige|ikke se/);assert.ok(!r._answerQuestion('Bring pakker').includes('DHL sender'));
r._config.sources=[sources[0]];assert.match(r._answerQuestion('Bring pakker'),/Vælg pakkesensorer/);
r._config.sources.push({...sources[0],entity:'sensor.other',config_entry_id:'second'});assert.match(r._parseParcelCommand('Tilføj DHL pakke 00123456789').error,/kun én/);
r._config.sources=[sources[0]];delete r._hass.services.dhl.track_parcel;assert.ok(r._parseParcelCommand('Tilføj DHL pakke 00123456789').error);
})().catch(e=>{console.error(e);process.exitCode=1});
