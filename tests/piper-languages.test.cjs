const fs=require('fs'),vm=require('vm'),assert=require('assert');let C;
vm.runInNewContext(fs.readFileSync('custom_components/dashboard_robot/frontend/robot.js','utf8').split('// Dashboard-scoped singleton.')[0],{HTMLElement:class{},customElements:{get(){},define(n,c){C=c}},window:{}});
const r=Object.create(C.prototype);r._hass={states:{'tts.piper':{attributes:{friendly_name:'Piper'}}}};
for(const [language,voice] of [['da','da_DK-talesyntese-medium'],['en','en_GB-cori-medium'],['de','de_DE-thorsten-medium']]){r._config={language};assert.equal(r._localSpeechOptions('tts.piper').voice,voice);}
assert.equal(Object.keys(r._localSpeechOptions('tts.other')).length,0);
console.log('Passed: Danish, English and German Piper voice selection; custom engine options preserved.');
