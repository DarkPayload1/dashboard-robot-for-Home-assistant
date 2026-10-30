const fs=require('fs'),vm=require('vm'),path=require('path'),assert=require('assert');let C;
vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../custom_components/dashboard_robot/frontend/robot.js'),'utf8').split('// Dashboard-scoped singleton.')[0],{HTMLElement:class{},customElements:{get(){},define(n,c){C=c}},window:{}});
const r=Object.create(C.prototype);r._config={language:'da',sources:[],read_entities:['sensor.custom']};
r._hass={states:new Proxy({'sensor.custom':{state:'72',attributes:{friendly_name:'Luftfugtighed atelier',unit_of_measurement:'%',private_token:'never-share'}}},{get(t,k){if(k==='sensor.secret')throw Error('Unselected read');return t[k]}})};
r._model=()=>({parcels:[],music:null});
assert.match(r._answerQuestion('Luftfugtighed atelier'),/72 %/);
assert.match(r._answerQuestion('Vis oplysninger'),/Luftfugtighed atelier/);
assert.ok(!JSON.stringify(r._currentFacts()).includes('never-share'));
r._config.read_entities=[];assert.equal(r._currentFacts().selected_readings.length,0);
console.log('Passed: selected provider readings work by name without private attributes.');
r._config={language:'da',sources:[],electricity_price_entity:'sensor.price',read_entities:['sensor.price','sensor.tax','sensor.future']};
r._hass={states:{'sensor.price':{state:'2.590688',attributes:{friendly_name:'Strømligning Aktuel inkl. moms',unit_of_measurement:'kr/kWh'}},'sensor.tax':{state:'0.14417',attributes:{friendly_name:'Strømligning Transporttarif',unit_of_measurement:'kr/kWh'}},'sensor.future':{state:'unknown',attributes:{friendly_name:'Strømligning i morgen',unit_of_measurement:'kr/kWh'}}}};
for(const question of ['Hvad er prisen for strøm','Hvad koster strømmen','Hvad koster strømmen nu?']){
 const answer=r._answerQuestion(question);assert.equal(answer,'Strømprisen lige nu er 2,59 kr/kWh');assert.ok(answer.length<80);assert.ok(!answer.includes('Transporttarif'));
}
r._config.language='en';assert.match(r._answerQuestion('What is the electricity price?'),/2\.59 kr\/kWh/);
r._config.language='de';assert.match(r._answerQuestion('Was kostet Strom?'),/2,59 kr\/kWh/);
r._config.electricity_price_entity=null;assert.ok(!r._answerQuestion('Strom').includes('0.14417'));
