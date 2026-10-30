const fs=require('fs'),vm=require('vm'),assert=require('assert');let C;
vm.runInNewContext(fs.readFileSync('custom_components/dashboard_robot/frontend/robot.js','utf8').split('// Dashboard-scoped singleton.')[0],{HTMLElement:class{},customElements:{get(){},define(n,c){C=c}},window:{}});
const r=Object.create(C.prototype);Object.assign(r,{_stage:{classList:{toggle(){}},querySelector(){return null}},_hass:{states:{}},_model(){return {parcels:Array(8).fill({kind:'incoming'}),title:'Der er 8 pakker på vej til dig.'}},_visible:true,_parcelBubble:{}});
r._refreshExpression();assert.equal(r._parcelBubble.textContent,'Tryk på mig for at tale eller skrive');r._listening=true;r._refreshExpression();assert.equal(r._parcelBubble.textContent,'Jeg lytter …');
assert.ok(!fs.readFileSync('custom_components/dashboard_robot/frontend/robot.js','utf8').includes("`Se pakker${"));
console.log('Passed: eight parcels never replace the neutral welcome; listening feedback remains.');
