(window.webpackJsonp=window.webpackJsonp||[]).push([[17,34,47,103,104,105],{1134:function(e,t,n){var content=n(1226);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,n(10).default)("be8ff50e",content,!0,{sourceMap:!1})},1135:function(e,t,n){var content=n(1228);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,n(10).default)("c0ed8164",content,!0,{sourceMap:!1})},1225:function(e,t,n){"use strict";n(1134)},1226:function(e,t,n){var c=n(9)(!1);c.push([e.i,".agency-card[data-v-79ce11b0]{display:grid;grid-gap:20px;width:100%;border-bottom:1px solid #e4e4e4}@media screen and (min-width:1024px){.agency-card[data-v-79ce11b0]{grid-template-columns:auto 1.5fr auto}}@media screen and (max-width:1024px)and (min-width:600px){.agency-card[data-v-79ce11b0]{grid-template-columns:auto 1.5fr}}@media screen and (max-width:600px){.agency-card[data-v-79ce11b0]{grid-template-rows:auto 1.5fr}}.agency-card-logo[data-v-79ce11b0]{margin-left:auto;margin-right:auto}.agency-card-logo--not[data-v-79ce11b0]{width:120px;height:60px}.agency-card-title[data-v-79ce11b0]{font-size:18px;font-weight:700}.agency-card-info[data-v-79ce11b0]{display:inline-flex;align-items:center;margin-top:8px}.agency-card-info-email[data-v-79ce11b0]{color:#1299dd}.agency-card-info svg[data-v-79ce11b0]{margin-right:8px}.agency-card-offers[data-v-79ce11b0]{display:block}@media screen and (max-width:1024px){.agency-card-offers[data-v-79ce11b0]{display:none}}.agency-card-offer[data-v-79ce11b0]{display:flex;justify-content:space-between;margin-bottom:8px}.agency-card-link[data-v-79ce11b0]{margin-top:10px;font-weight:600;color:#1299dd}.agency-card-link[data-v-79ce11b0]:hover{color:#41ade4}.agency-card-button-show-offers[data-v-79ce11b0]{font-size:14px;font-weight:600;line-height:19px;padding:10px 24px}@media screen and (min-width:1024px){.agency-card-button-show-offers[data-v-79ce11b0]{display:none}}@media screen and (max-width:1024px){.agency-card-button-show-offers[data-v-79ce11b0]{display:block}}.truncate-text[data-v-79ce11b0]{width:245px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-right:25px}",""]),e.exports=c},1227:function(e,t,n){"use strict";n(1135)},1228:function(e,t,n){var c=n(9)(!1);c.push([e.i,".banner-biz[data-v-d7badd1c]{width:708px;margin-bottom:50px;border:1px solid #e9e9e9;border-radius:3px;padding:0 30px 20px;display:flex}@media screen and (max-width:800px){.banner-biz[data-v-d7badd1c]{width:100%;flex-direction:column-reverse;align-items:center}}.banner-biz-content[data-v-d7badd1c]{max-width:344px;margin-top:30px}@media screen and (max-width:800px){.banner-biz-content[data-v-d7badd1c]{text-align:center}}.banner-biz-content div[data-v-d7badd1c]{font-size:16px;font-weight:400;line-height:24px;margin-bottom:20px}.banner-biz-button[data-v-d7badd1c]{font-size:14px;font-weight:700;line-height:16px;padding:8px 16px;width:200px}@media screen and (max-width:800px){.banner-biz-button[data-v-d7badd1c]{width:100%}}.banner-biz-image[data-v-d7badd1c]{margin-left:44px}@media screen and (max-width:800px){.banner-biz-image[data-v-d7badd1c]{margin-left:0}}",""]),e.exports=c},1286:function(e,t,n){"use strict";n.r(t);n(18);var c={name:"AgencyRow",props:{agency:{type:Object,default:function(){return{}}}}},r=(n(1225),n(1)),component=Object(r.a)(c,(function(){var e=this,t=e._self._c;return t("div",{staticClass:"agency-card"},[t("NuxtLink",{staticClass:"agency-card-logo",attrs:{to:"/agency/".concat(e.agency.id)}},[e.agency.logo?t("img",{attrs:{src:e.agency.logo,title:e.agency.name,width:"120px",height:"60px",alt:"Логотип",loading:"lazy"}}):t("div",{staticClass:"agency-card-logo--not bg-light-grey border-radius flex x-center y-center"},[t("svg",{attrs:{width:"45px",height:"50px"}},[t("use",{attrs:{"xlink:href":"/assets/sprites/agents.svg#agency"}})])])]),e._v(" "),t("div",[t("NuxtLink",{staticClass:"agency-card-title",attrs:{to:"/agency/".concat(e.agency.id)}},[t("h2",[e._v("\n        "+e._s(e.agency.name)+"\n      ")])]),e._v(" "),e.agency.site?t("div",[t("span",{staticClass:"agency-card-info"},[t("svg",{attrs:{height:"16px",width:"16px"}},[t("use",{attrs:{"xlink:href":"/assets/sprites/agents.svg#world"}})]),e._v(" "),t("a",{staticClass:"agency-card-info-website",attrs:{href:e.agency.url}},[e._v("\n          "+e._s(e.agency.site)+"\n        ")])]),e._v(" "),t("br")]):e._e(),e._v(" "),e.agency.email?t("div",[t("span",{staticClass:"agency-card-info"},[t("svg",{attrs:{height:"16px",width:"16px",stroke:"#000"}},[t("use",{attrs:{"xlink:href":"/assets/sprites/layout.svg#mail"}})]),e._v(" "),t("a",{staticClass:"agency-card-info-email",attrs:{href:"mailto:".concat(e.agency.email)}},[e._v("\n          "+e._s(e.agency.email)+"\n        ")])]),e._v(" "),t("br")]):e._e(),e._v(" "),e.agency.address?t("div",[t("span",{staticClass:"agency-card-info"},[t("svg",{attrs:{height:"16px",width:"16px"}},[t("use",{attrs:{"xlink:href":"/assets/sprites/layout.svg#location"}})]),e._v("\n        "+e._s(e.agency.address)+"\n      ")]),e._v(" "),t("br")]):e._e()],1),e._v(" "),t("div",{staticClass:"agency-card-offers"},[e._l(e.agency.offers,(function(n){return t("NuxtLink",{key:n.id,attrs:{to:n.path}},[t("div",{staticClass:"agency-card-offer"},[t("span",{staticClass:"truncate-text"},[e._v("\n          "+e._s(n.title)+"\n        ")]),e._v(" "),t("span",[e._v("\n          "+e._s(n.price.toLocaleString("ru-RU"))+" руб.\n        ")])])])})),e._v(" "),e.agency.offersCount>3?t("NuxtLink",{staticClass:"agency-card-link",attrs:{to:"/agency/".concat(e.agency.id)}},[e._v("\n      Еще "+e._s(e.agency.offersCount-3)+" объявлений\n    ")]):e._e()],2),e._v(" "),t("NuxtLink",{staticClass:"agency-card-button-show-offers btn-outline",attrs:{to:"/agency/".concat(e.agency.id)}},[e._v("\n    Показать "+e._s(e.agency.offersCount)+" объявлений\n  ")])],1)}),[],!1,null,"79ce11b0",null);t.default=component.exports},1297:function(e,t,n){var content=n(1360);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,n(10).default)("77c09526",content,!0,{sourceMap:!1})},1331:function(e,t,n){"use strict";n.r(t);var c={name:"BannerBiz"},r=(n(1227),n(1)),component=Object(r.a)(c,(function(){var e=this,t=e._self._c;return t("div",{staticClass:"banner-biz"},[e._m(0),e._v(" "),t("div",{staticClass:"banner-biz-image"},[t("figure",[t("svg",{attrs:{width:"305",height:"157"}},[t("use",{attrs:{"xlink:href":"/assets/sprites/agents.svg#banner"}})])])])])}),[function(){var e=this,t=e._self._c;return t("div",{staticClass:"banner-biz-content"},[t("div",[e._v("\n      Все агентства недвижимости сахалина в каталоге Сахалин.Бизнес\n    ")]),e._v(" "),t("a",{staticClass:"block banner-biz-button btn-fill",attrs:{href:"https://sakhalin.biz/dir/198/93"}},[e._v("\n      Посмотреть\n    ")])])}],!1,null,"d7badd1c",null);t.default=component.exports},1359:function(e,t,n){"use strict";n(1297)},1360:function(e,t,n){var c=n(9)(!1);c.push([e.i,".agencies-sort-icon[data-v-9f7996ac]{margin-right:5px}.agencies-more[data-v-9f7996ac]{margin-bottom:40px;font-size:14px;font-weight:600;line-height:19px;padding:8px 13px}@media screen and (max-width:600px){.agencies-more[data-v-9f7996ac]{width:100%}}.flex[data-v-9f7996ac]{display:flex}.flex-x-center[data-v-9f7996ac]{justify-items:center}.header[data-v-9f7996ac]{font-size:24px;font-weight:600;margin-top:40px;margin-bottom:22px}.agencies-list[data-v-9f7996ac]{display:flex;flex-wrap:wrap;flex:1 1 auto}.sort-method[data-v-9f7996ac]{font-weight:600;color:#1299dd;margin-bottom:30px}.dropdown-menu[data-v-9f7996ac]{padding-top:0;padding-bottom:0}.dropdown-item[data-v-9f7996ac]{cursor:pointer;padding:12px 25px}.agency[data-v-9f7996ac]{padding-bottom:25px;margin-bottom:25px}.agency[data-v-9f7996ac]:last-child{border-bottom:none}@media screen and (max-width:600px){.banner-biz[data-v-9f7996ac]{display:none}}@media screen and (max-width:1280px){.agencies[data-v-9f7996ac]{padding-left:20px;padding-right:20px}}.agencies-margin[data-v-9f7996ac]{margin-bottom:20px}",""]),e.exports=c},1419:function(e,t,n){"use strict";n.r(t);n(452),n(51),n(18);var c=n(71),r=n(746),o=n(1286),d=n(1331),l={name:"AgenciesPage",components:{AgencyRow:o.default,BannerBiz:d.default,Select:r.default,Sprite:c.a},props:{response:{type:Array,required:!0}},data:function(){return{agencies:this.response.slice(0),sortBy:"По умолчанию",limit:20}},computed:{sortMethods:function(){return["По умолчанию","По алфавиту","По количеству объявлений"]}},methods:{sort:function(e){switch(this.sortBy=e.item,e.item){case"По умолчанию":this.agencies=this.response.slice(0);break;case"По алфавиту":this.agencies=this.agencies.sort((function(a,b){var e=a.name.toUpperCase(),t=b.name.toUpperCase();return e<t?-1:e>t?1:0}));break;case"По количеству объявлений":this.agencies=this.agencies.sort((function(a,b){return b.offersCount-a.offersCount}))}},loadMore:function(){this.limit+=20,this.limit>this.agencies.length&&(this.limit=this.agencies.length)}}},f=(n(1359),n(1)),component=Object(f.a)(l,(function(){var e=this,t=e._self._c;return t("main",{staticClass:"content agencies"},[t("h1",{staticClass:"header"},[e._v("\n    Агентства недвижимости\n  ")]),e._v(" "),t("div",{staticClass:"dropdown"},[t("Select",{staticClass:"agencies-margin",attrs:{list:e.sortMethods},on:{change:e.sort}},[t("span",{staticClass:"sort-method",attrs:{href:"#",role:"button","data-bs-toggle":"dropdown","aria-expanded":"false"}},[t("button",{staticClass:"agencies-sort text-light-blue transition-colors duration-3 hover-text-blue flex y-center"},[t("Sprite",{staticClass:"agencies-sort-icon",attrs:{id:"sort-arrows",height:"24px",width:"24px","file-name":"agents"}}),e._v("\n          "+e._s(e.sortBy)+"\n        ")],1)])])],1),e._v(" "),0===e.agencies.length?t("div"):t("div",{staticStyle:{width:"90%"}},[t("div",{staticClass:"agencies-list"},e._l(e.agencies.slice(0,e.limit),(function(e){return t("AgencyRow",{key:e.id,staticClass:"agency",attrs:{agency:e}})})),1),e._v(" "),e.limit!=e.agencies.length?t("button",{staticClass:"agencies-more btn-section",on:{click:e.loadMore}},[e._v("\n      Загрузить еще\n    ")]):e._e(),e._v(" "),t("BannerBiz",{staticClass:"banner-biz"})],1)])}),[],!1,null,"9f7996ac",null);t.default=component.exports;installComponents(component,{AgencyRow:n(1286).default})},690:function(e,t,n){var content=n(707);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,n(10).default)("3c3db17c",content,!0,{sourceMap:!1})},693:function(e,t,n){var content=n(717);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,n(10).default)("6f5e8e2b",content,!0,{sourceMap:!1})},700:function(e,t,n){"use strict";n.r(t);n(60);var c={name:"SelectItem",props:{item:{type:String,required:!0},index:{type:[Number,String],required:!0},active:{type:Boolean}},methods:{change:function(){this.$emit("change",{item:this.item,index:this.index})}}},r=(n(706),n(1)),component=Object(r.a)(c,(function(){var e=this;return(0,e._self._c)("li",{staticClass:"select-item select-font",class:{"select-item-active ":e.active},on:{click:e.change}},[e._v("\n  "+e._s(e.item)+"\n")])}),[],!1,null,"e86fddca",null);t.default=component.exports},701:function(e,t,n){var content=n(742);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,n(10).default)("324f528b",content,!0,{sourceMap:!1})},703:function(e,t,n){"use strict";n.r(t);var c={name:"SelectMenu",components:{SelectItem:n(700).default},props:{list:{type:Array,default:function(){return[]}}},data:function(){return{canClose:!1}},mounted:function(){document.addEventListener("click",this.close)},beforeDestroy:function(){document.removeEventListener("click",this.close)},methods:{change:function(e){this.$emit("change",e)},close:function(){this.canClose&&this.$emit("close"),this.canClose=!this.canClose}}},r=(n(716),n(1)),component=Object(r.a)(c,(function(){var e=this,t=e._self._c;return t("ul",{staticClass:"select-ul"},e._l(e.list,(function(n,c){return t("SelectItem",{key:c,attrs:{item:n,index:c},on:{change:e.change}})})),1)}),[],!1,null,"895d3234",null);t.default=component.exports},706:function(e,t,n){"use strict";n(690)},707:function(e,t,n){var c=n(9)(!1);c.push([e.i,".select-font[data-v-e86fddca]{font-weight:400;font-size:14px;color:#000;line-height:19px}.select-item[data-v-e86fddca]{display:block;width:100%;cursor:pointer;padding:9px 30px 5px 20px;font-weight:400;color:#212529;z-index:3;border:0;-webkit-user-select:none;-moz-user-select:none;user-select:none;transition:background-color .2s ease-in-out}@media screen and (min-width:500px){.select-item[data-v-e86fddca]{white-space:nowrap}}.select-item-active[data-v-e86fddca],.select-item[data-v-e86fddca]:hover{background:#e7f4fb}",""]),e.exports=c},716:function(e,t,n){"use strict";n(693)},717:function(e,t,n){var c=n(9)(!1);c.push([e.i,".select-ul[data-v-895d3234]{max-height:400px;overflow-y:auto}",""]),e.exports=c},741:function(e,t,n){"use strict";n(701)},742:function(e,t,n){var c=n(9)(!1);c.push([e.i,".baseSelect[data-v-0db5cae4]{cursor:pointer}.baseSelect-menu[data-v-0db5cae4]{display:block;position:absolute;margin-top:5px;z-index:11;padding:3px 0;list-style:none;background:#fff;box-shadow:0 2px 7px rgba(0,0,0,.25);border-radius:3px}.baseSelect-fade-enter-active[data-v-0db5cae4],.baseSelect-fade-leave-active[data-v-0db5cae4]{transition:all .2s ease-in-out}.baseSelect-fade-enter[data-v-0db5cae4],.baseSelect-fade-leave-to[data-v-0db5cae4]{opacity:0;transform:translateY(-12px)}",""]),e.exports=c},746:function(e,t,n){"use strict";n.r(t);var c={name:"BaseSelect",components:{SelectMenu:n(703).default},props:{list:{type:Array,required:!0},classMenu:{type:String,default:function(){return""}},isHidden:{type:Boolean,default:function(){return!0}}},data:function(){return{hidden:this.isHidden}},watch:{isHidden:function(e){this.hidden=e}},methods:{change:function(e){this.$emit("change",e)},showOrHide:function(){this.hidden=!this.hidden,this.$emit("hidden",this.hidden)}}},r=(n(741),n(1)),component=Object(r.a)(c,(function(){var e=this,t=e._self._c;return t("div",{staticClass:"baseSelect"},[t("div",{staticClass:"baseSelect-option",on:{click:e.showOrHide}},[e._t("default")],2),e._v(" "),t("transition",{attrs:{name:"baseSelect-fade"}},[e.hidden?e._e():t("SelectMenu",{staticClass:"baseSelect-menu",class:e.classMenu,attrs:{list:e.list},on:{change:e.change,close:e.showOrHide}})],1)],1)}),[],!1,null,"0db5cae4",null);t.default=component.exports}}]);