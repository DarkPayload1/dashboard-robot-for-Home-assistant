const fs=require('fs'),vm=require('vm'),assert=require('assert');let C;
vm.runInNewContext(fs.readFileSync('custom_components/dashboard_robot/frontend/robot.js','utf8').split('// Dashboard-scoped singleton.')[0],{HTMLElement:class{},customElements:{get(){},define(n,c){C=c}},window:{}});
(async()=>{
for(const agent of [null,'conversation.google']){
 for(const spoken of [true,false]){
  const r=Object.create(C.prototype);let speeches=0;
  Object.assign(r,{_config:{agent_id:agent},_visible:true,isConnected:true,_dialog:{open:true},shadowRoot:{querySelector(){return null}},_update(){},_isCameraCommand(){return false},_parseHomeCommand(){return null},_parseParcelCommand(){return null},_answerQuestion(){return 'Blyfri 95: 16,89 DKK/L'},_speak(){speeches++}});
  await r._ask('Hvad koster benzinen',spoken);
  assert.equal(speeches,spoken?1:0);assert.equal(r._busy,false);assert.equal(r._aiAnswer,'Blyfri 95: 16,89 DKK/L');
  r._dialog.open=false;await r._ask('Hvad koster benzinen',true);assert.equal(speeches,spoken?1:0);
 }
}
})().catch(e=>{console.error(e);process.exitCode=1});
