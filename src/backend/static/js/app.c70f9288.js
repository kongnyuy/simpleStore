(function(e){function t(t){for(var a,s,i=t[0],l=t[1],c=t[2],v=0,p=[];v<i.length;v++)s=i[v],Object.prototype.hasOwnProperty.call(r,s)&&r[s]&&p.push(r[s][0]),r[s]=0;for(a in l)Object.prototype.hasOwnProperty.call(l,a)&&(e[a]=l[a]);u&&u(t);while(p.length)p.shift()();return o.push.apply(o,c||[]),n()}function n(){for(var e,t=0;t<o.length;t++){for(var n=o[t],a=!0,i=1;i<n.length;i++){var l=n[i];0!==r[l]&&(a=!1)}a&&(o.splice(t--,1),e=s(s.s=n[0]))}return e}var a={},r={app:0},o=[];function s(t){if(a[t])return a[t].exports;var n=a[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.m=e,s.c=a,s.d=function(e,t,n){s.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},s.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.t=function(e,t){if(1&t&&(e=s(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var a in e)s.d(n,a,function(t){return e[t]}.bind(null,a));return n},s.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return s.d(t,"a",t),t},s.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},s.p="/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],l=i.push.bind(i);i.push=t,i=i.slice();for(var c=0;c<i.length;c++)t(i[c]);var u=l;o.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"034f":function(e,t,n){"use strict";var a=n("85ec"),r=n.n(a);r.a},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var a=n("2b0e"),r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("div",{staticClass:"app-app center grid"},[n("vs-row",[n("vs-col",{attrs:{"vs-type":"flex","vs-justify":"center","vs-align":"center",w:"12"}},[n("Home")],1)],1)],1)])},o=[],s=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"app-home"},[n("div",{},[n("Header",{attrs:{tabs:e.tabs,showAdminPanel:"false"}}),n("router-link",{attrs:{to:"/bar"}},[e._v("Go to Bar")]),n("div",{staticClass:"app-rv"},[n("router-view")],1),n("vs-button",{on:{click:function(t){e.active=!e.active}}},[e._v(" Open Dialog ")]),n("vs-dialog",{scopedSlots:e._u([{key:"header",fn:function(){return[n("h4",{staticClass:"not-margin"},[e._v(" Welcome to "),n("b",[e._v("Vuesax")])])]},proxy:!0},{key:"footer",fn:function(){return[n("div",{staticClass:"footer-dialog"},[n("vs-button",{attrs:{block:""}},[e._v(" Sign In ")]),n("div",{staticClass:"new"},[e._v(" New Here? "),n("a",{attrs:{href:"#"}},[e._v("Create New Account")])])],1)]},proxy:!0}]),model:{value:e.active,callback:function(t){e.active=t},expression:"active"}},[n("div",{staticClass:"con-form"},[n("vs-input",{attrs:{placeholder:"Email"},scopedSlots:e._u([{key:"icon",fn:function(){return[e._v(" @ ")]},proxy:!0}]),model:{value:e.email,callback:function(t){e.email=t},expression:"email"}}),n("vs-input",{attrs:{type:"password",placeholder:"Password"},scopedSlots:e._u([{key:"icon",fn:function(){return[n("i",{staticClass:"bx bxs-lock"})]},proxy:!0}]),model:{value:e.password,callback:function(t){e.password=t},expression:"password"}}),n("div",{staticClass:"flex"},[n("vs-checkbox",{model:{value:e.remember,callback:function(t){e.remember=t},expression:"remember"}},[e._v("Remember me")]),n("a",{attrs:{href:"#"}},[e._v("Forgot Password?")])],1)],1)])],1)])},i=[],l=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("vs-navbar",{attrs:{"center-collapsed":""},scopedSlots:e._u([{key:"left",fn:function(){return[n("img",{attrs:{src:"/logo2.png",alt:""}})]},proxy:!0},{key:"right",fn:function(){return[n("div",{directives:[{name:"show",rawName:"v-show",value:"false"==e.showAdminPanel,expression:"showAdminPanel == 'false'"}]},[n("vs-button",{attrs:{flat:""}},[e._v("Login")]),n("vs-button",[e._v("Get Started")])],1)]},proxy:!0}]),model:{value:e.active,callback:function(t){e.active=t},expression:"active"}},[n("vs-navbar-item",{attrs:{active:"guide"==e.active,id:"guide"}},[e._v("Guide")]),n("vs-navbar-item",{attrs:{active:"docs"==e.active,id:"docs"}},[e._v("Documents")]),n("vs-navbar-item",{attrs:{active:"components"==e.active,id:"components"}},[e._v("Components")]),n("vs-navbar-item",{attrs:{active:"license"==e.active,id:"license"}},[e._v("license")]),e._l(e.tabs,(function(t){return n("vs-navbar-item",{key:t.label,attrs:{active:e.active==t.label,id:"tab.label"}},[n("router-link",{attrs:{to:"/foo"}},[e._v(e._s(t.label))])],1)}))],2)},c=[],u={name:"Header",props:["tabs","showAdminPanel"],data:function(){return{active:"home"}}},v=u,p=n("2877"),f=Object(p["a"])(v,l,c,!1,null,null,null),d=f.exports,b={name:"Home",components:{Header:d},props:{},data:function(){return{tabs:[{label:"label",url:"/destination_link"},{label:"Articles",url:"/articles"},{label:"Inventory",url:"/store/inventory"}],active:!1,email:"",password:"",remember:!1}}},m=b,h=(n("6acf"),Object(p["a"])(m,s,i,!1,null,null,null)),_=h.exports,y={name:"App",components:{Home:_}},w=y,g=(n("034f"),Object(p["a"])(w,r,o,!1,null,null,null)),x=g.exports,k=n("2f62"),O=n("8c4f"),j=n("574d"),P=n.n(j),C=(n("04f2"),{template:"<div>foo</div>"}),S={template:"<div>bar</div>"},A=[{path:"/foo",component:C},{path:"/bar",component:S}],H=new O["a"]({routes:A}),E=H;a["default"].config.productionTip=!1,a["default"].use(k["a"]),a["default"].use(O["a"]),a["default"].use(P.a,{}),new a["default"]({render:function(e){return e(x)},router:E}).$mount("#app")},"6acf":function(e,t,n){"use strict";var a=n("940d"),r=n.n(a);r.a},"85ec":function(e,t,n){},"940d":function(e,t,n){}});
//# sourceMappingURL=app.c70f9288.js.map