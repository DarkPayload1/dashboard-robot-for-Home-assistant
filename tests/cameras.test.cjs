const fs=require('fs'),vm=require('vm'),path=require('path'),assert=require('assert');let C;
const box={hidden:true,buttons:[],replaceChildren(){this.buttons=[]},append(b){this.buttons.push(b)}};let opened=[];
vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../custom_components/dashboard_robot/frontend/robot.js'),'utf8').split('// Dashboard-scoped singleton.')[0],{HTMLElement:class{},customElements:{get(){},define(n,c){C=c}},window:{},document:{createElement:()=>({addEventListener(n,fn){this.click=fn}})}});
const r=Object.create(C.prototype);r._config={language:'da',camera_entities:['camera.a','camera.b','camera.off'],camera_labels:{'camera.a':'Kamera · Stue','camera.b':'Kamera · Køkken','camera.off':'Offline'}};r._hass={states:{'camera.a':{state:'idle'},'camera.b':{state:'idle'},'camera.off':{state:'unavailable'}}};r.shadowRoot={querySelector:()=>box};r._update=()=>{};r._openCamera=id=>opened.push(id);
r._showCameras('Vis kamera');assert.equal(opened.length,0);assert.equal(box.buttons.length,3);assert.equal(box.buttons[2].disabled,true);box.buttons[1].click();assert.equal(opened.pop(),'camera.b');
r._showCameras('Vis kamera i stue');assert.equal(opened.pop(),'camera.a');
r._config={language:'en',camera_entity:'camera.a'};r._showCameras('Show camera');assert.equal(opened.pop(),'camera.a');
r._config={language:'de',camera_entities:[]};r._showCameras('Kamera');assert.equal(box.hidden,true);assert.equal(opened.length,0);
console.log('Passed: all cameras, room selection, disabled unavailable, legacy single camera, no automatic choice with multiple cameras.');
