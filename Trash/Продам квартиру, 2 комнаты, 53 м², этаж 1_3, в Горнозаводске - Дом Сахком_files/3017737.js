(window.webpackJsonp=window.webpackJsonp||[]).push([[229],{1436:function(t,e,r){"use strict";r.r(e);var n=r(29),o=(r(61),r(791)),c=r(271),h=r(448),l={name:"My",components:{MyOffers:r(1334).default},mixins:[o.a],middleware:[h.default],asyncData:function(t){return Object(n.a)(regeneratorRuntime.mark((function e(){var r,n,data;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return r=t.query,n=t.store,e.next=3,n.dispatch("offer/fetchMyList",Object(c.a)(r));case 3:return data=e.sent,e.abrupt("return",{meta:data.meta,state:"total",category:{title:data.title,list:data.list,hash:data.hash,limit:data.limit,totalCount:data.totalCount}});case 5:case"end":return e.stop()}}),e)})))()},watch:{category:function(t){this.$store.commit("offer/changeCategory",t)}},watchQuery:["page"],created:function(){this.$store.commit("offer/resetOffer"),this.$store.commit("offer/changeCategory",this.category)}},d=r(1),component=Object(d.a)(l,(function(){return(0,this._self._c)("MyOffers",{attrs:{state:this.state}})}),[],!1,null,null,null);e.default=component.exports},791:function(t,e,r){"use strict";r.d(e,"a",(function(){return n}));r(51),r(23),r(72);var n={head:function(){var title=this.meta.title?"".concat(this.meta.title," - Дом Сахком"):"Дом Сахком",t="https://domsakhcom.ru/".slice(0,-1)+this.$route.fullPath;return{title:title,meta:[{hid:"description",name:"description",content:this.meta.description},{hid:"keywords",name:"keywords",content:this.meta.keywords},{hid:"twitter:title",property:"twitter:title",content:this.meta.title},{hid:"twitter:description",property:"twitter:description",content:this.meta.description},{hid:"og:description",property:"og:description",content:this.meta.description},{hid:"og:title",property:"og:title",content:this.meta.title},{hid:"og:url",property:"og:url",content:t}],link:[{hid:"canonical",rel:"canonical",href:t}]}}}}}]);