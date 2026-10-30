const fs=require('fs'),vm=require('vm'),assert=require('assert');let C;
vm.runInNewContext(fs.readFileSync('custom_components/dashboard_robot/frontend/robot.js','utf8').split('// Dashboard-scoped singleton.')[0],{HTMLElement:class{},customElements:{get(){},define(n,c){C=c}},window:{}});
(async()=>{
for(const [carrier,domain,supportsEntry] of [['PostNord','postnord',false],['GLS','gls',false],['DHL','dhl',true]]){
 const r=Object.create(C.prototype),calls=[];r._config={language:'da',sources:[{carrier,config_entry_id:'selected-account',can_track:true,can_untrack:true}]};r._update=()=>{};
 const fields={tracking_code:{},...(supportsEntry?{config_entry_id:{}}:{})};
 r._hass={services:{[domain]:{track_parcel:{fields},untrack_parcel:{fields}}},callService:async(d,a,p)=>{for(const key of Object.keys(p))assert.ok(key in fields,'unsupported '+key);calls.push([d,a,p]);}};
 for(const action of ['track_parcel','untrack_parcel']){
 const command={carrier,action,code:'00123456789'};await r._handleParcelCommand(command);
 if(action==='untrack_parcel'){assert.equal(calls.length,1);await r._confirmParcel();}
 const call=calls.at(-1);assert.equal(call[0],domain);assert.equal(call[1],action);assert.equal(call[2].tracking_code,'00123456789');assert.equal(call[2].config_entry_id,supportsEntry?'selected-account':undefined);
 }
 r._config.sources.push({...r._config.sources[0],config_entry_id:'second-account'});assert.ok(r._parcelTarget(carrier,'untrack_parcel').error);
}
console.log('Passed: strict PostNord/GLS payloads, scoped DHL payloads, confirmed removal, multiple-account guard.');
})().catch(e=>{console.error(e);process.exitCode=1});
