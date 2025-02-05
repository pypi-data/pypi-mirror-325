"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[2246],{47163:(e,t,n)=>{n.d(t,{A:()=>i});var a=n(96540);const i=()=>{const[e,t]=(0,a.useState)(0),[n,i]=(0,a.useState)(!1),l=(0,a.useRef)(null),o=(0,a.useRef)(null);return(0,a.useLayoutEffect)((()=>{var e;const n=()=>{const e=l.current;if(!e)return;const n=o.current,{scrollWidth:a,clientWidth:r,childNodes:s}=e;if(a>r){const e=6,a=(null==n?void 0:n.offsetWidth)||0,l=r-e,o=s.length;let d=0,c=0;for(let e=0;e<o;e+=1)l-d-a<=0&&(c+=1),d+=s[e].offsetWidth;o>1&&c?(i(!0),t(c)):(i(!1),t(1))}else i(!1),t(0)},a=new ResizeObserver(n),r=null==(e=l.current)?void 0:e.parentElement;return r&&a.observe(r),n(),()=>{a.disconnect()}}),[o.current]),[l,o,e,n]}},41621:(e,t,n)=>{n.d(t,{A:()=>d});var a=n(33149),i=n(96453),l=n(96540),o=n(62221),r=n(2445);const s=i.I4.div`
  position: absolute;
  height: 100%;

  :hover .sidebar-resizer::after {
    background-color: ${({theme:e})=>e.colors.primary.base};
  }

  .sidebar-resizer {
    // @z-index-above-sticky-header (100) + 1 = 101
    z-index: 101;
  }

  .sidebar-resizer::after {
    display: block;
    content: '';
    width: 1px;
    height: 100%;
    margin: 0 auto;
  }
`,d=({id:e,initialWidth:t,minWidth:n,maxWidth:i,enable:d,children:c})=>{const[h,g]=function(e,t){const n=(0,l.useRef)(),[a,i]=(0,l.useState)(t);return(0,l.useEffect)((()=>{var t;n.current=null!=(t=n.current)?t:(0,o.Gq)(o.Hh.CommonResizableSidebarWidths,{}),n.current[e]&&i(n.current[e])}),[e]),[a,function(t){i(t),(0,o.SO)(o.Hh.CommonResizableSidebarWidths,{...n.current,[e]:t})}]}(e,t);return(0,r.FD)(r.FK,{children:[(0,r.Y)(s,{children:(0,r.Y)(a.c,{enable:{right:d},handleClasses:{right:"sidebar-resizer",bottom:"hidden",bottomRight:"hidden",bottomLeft:"hidden"},size:{width:h,height:"100%"},minWidth:n,maxWidth:i,onResizeStop:(e,t,n,a)=>g(h+a.width)})}),c(h)]})}},78704:(e,t,n)=>{n.d(t,{A:()=>d});var a=n(17437),i=n(96453),l=n(16784),o=n(12249),r=n(19129),s=n(2445);const d=function({warningMarkdown:e,size:t,marginRight:n}){const d=(0,i.DP)();return(0,s.Y)(r.m,{id:"warning-tooltip",title:(0,s.Y)(l.A,{source:e}),children:(0,s.Y)(o.A.AlertSolid,{iconColor:d.colors.warning.base,iconSize:t,css:(0,a.AH)({marginRight:null!=n?n:2*d.gridUnit},"","")})})}},29130:(e,t,n)=>{n.r(t),n.d(t,{datasetReducer:()=>lt,default:()=>rt});var a=n(96540),i=n(61574),l=n(35742),o=n(95579),r=n(5362),s=n(58561),d=n.n(s),c=n(95272);const h=(e,t)=>{const[n,i]=(0,a.useState)([]),s=t?encodeURIComponent(t):void 0,h=(0,a.useCallback)((async e=>{let t,n=[],a=0;for(;void 0===t||n.length<t;){const i=d().encode_uri({filters:e,page:a});try{const e=await l.A.get({endpoint:`/api/v1/dataset/?q=${i}`});({count:t}=e.json);const{json:{result:o}}=e;n=[...n,...o],a+=1}catch(e){(0,c.iB)((0,o.t)("There was an error fetching dataset")),r.A.error((0,o.t)("There was an error fetching dataset"),e)}}i(n)}),[]);(0,a.useEffect)((()=>{const n=[{col:"database",opr:"rel_o_m",value:null==e?void 0:e.id},{col:"schema",opr:"eq",value:s},{col:"sql",opr:"dataset_is_null_or_empty",value:!0}];t&&h(n)}),[null==e?void 0:e.id,t,s,h]);const g=(0,a.useMemo)((()=>null==n?void 0:n.map((e=>e.table_name))),[n]);return{datasets:n,datasetNames:g}};var g,u=n(51848),p=n(46920),m=n(12249),b=n(6749);!function(e){e[e.SelectDatabase=0]="SelectDatabase",e[e.SelectCatalog=1]="SelectCatalog",e[e.SelectSchema=2]="SelectSchema",e[e.SelectTable=3]="SelectTable",e[e.ChangeDataset=4]="ChangeDataset"}(g||(g={}));var f=n(96453),y=n(17437);const v=f.I4.div`
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  background-color: ${({theme:e})=>e.colors.grayscale.light5};
`,x=f.I4.div`
  width: ${({theme:e,width:t})=>null!=t?t:80*e.gridUnit}px;
  max-width: ${({theme:e,width:t})=>null!=t?t:80*e.gridUnit}px;
  flex-direction: column;
  flex: 1 0 auto;
`,$=f.I4.div`
  display: flex;
  flex-direction: column;
  flex-grow: 1;
`,w=f.I4.div`
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
`,S=(0,f.I4)(w)`
  flex: 1 0 auto;
  position: relative;
`,U=(0,f.I4)(w)`
  flex: 1 0 auto;
  height: auto;
`,Y=(0,f.I4)(w)`
  flex: 0 0 auto;
  height: ${({theme:e})=>16*e.gridUnit}px;
  z-index: 0;
`,I=f.I4.div`
  ${({theme:e})=>`\n  flex: 0 0 auto;\n  height: ${16*e.gridUnit}px;\n  border-bottom: 2px solid ${e.colors.grayscale.light2};\n\n  .header-with-actions {\n    height: ${15.5*e.gridUnit}px;\n  }\n  `}
`,_=f.I4.div`
  ${({theme:e})=>`\n  margin: ${4*e.gridUnit}px;\n  font-size: ${e.typography.sizes.xl}px;\n  font-weight: ${e.typography.weights.bold};\n  `}
`,C=f.I4.div`
  ${({theme:e})=>`\n  height: 100%;\n  border-right: 1px solid ${e.colors.grayscale.light2};\n  `}
`,T=f.I4.div`
  width: 100%;
  position: relative;
`,A=f.I4.div`
  ${({theme:e})=>`\n  border-left: 1px solid ${e.colors.grayscale.light2};\n  color: ${e.colors.success.base};\n  `}
`,D=f.I4.div`
  ${({theme:e})=>`\n  height: ${16*e.gridUnit}px;\n  width: 100%;\n  border-top: 1px solid ${e.colors.grayscale.light2};\n  border-bottom: 1px solid ${e.colors.grayscale.light2};\n  color: ${e.colors.info.base};\n  border-top: ${e.gridUnit/4}px solid\n    ${e.colors.grayscale.light2};\n  padding: ${4*e.gridUnit}px;\n  display: flex;\n  justify-content: flex-end;\n  background-color: ${e.colors.grayscale.light5};\n  z-index: ${e.zIndex.max}\n  `}
`,k=f.I4.div`
  .antd5-btn {
    span {
      margin-right: 0;
    }

    &:disabled {
      svg {
        color: ${({theme:e})=>e.colors.grayscale.light1};
      }
    }
  }
`,z=e=>y.AH`
  width: ${21.5*e.gridUnit}px;

  &:disabled {
    background-color: ${e.colors.grayscale.light3};
    color: ${e.colors.grayscale.light1};
  }
`;var F=n(2445);const E=(0,o.t)("New dataset"),N={text:(0,o.t)("Select a database table and create dataset"),placement:"bottomRight"},P=()=>(0,F.FD)(p.A,{buttonStyle:"primary",tooltip:null==N?void 0:N.text,placement:null==N?void 0:N.placement,disabled:!0,css:z,children:[(0,F.Y)(m.A.Save,{iconSize:"m"}),(0,o.t)("Save")]}),R=()=>(0,F.FD)(b.W1,{children:[(0,F.Y)(b.W1.Item,{children:(0,o.t)("Settings")}),(0,F.Y)(b.W1.Item,{children:(0,o.t)("Delete")})]});function L({setDataset:e,title:t=E,editing:n=!1}){const a={title:null!=t?t:E,placeholder:E,onSave:t=>{e({type:g.ChangeDataset,payload:{name:"dataset_name",value:t}})},canEdit:!1,label:(0,o.t)("dataset name")};return(0,F.Y)(k,{children:n?(0,F.Y)(u.U,{editableTitleProps:a,showTitlePanelItems:!1,showFaveStar:!1,faveStarProps:{itemId:1,saveFaveStar:()=>{}},titlePanelAdditionalItems:(0,F.Y)(F.FK,{}),rightPanelAdditionalItems:P(),additionalActionsMenu:R(),menuDropdownProps:{disabled:!0},tooltipProps:N}):(0,F.Y)(_,{children:t||E})})}var W=n(69945),j=n(48327),K=n(71519),M=n(62952),O=n(51003),q=n(50455),H=n(46e3),B=n(5261),X=n(50500),Q=n(39854),V=n(7089),G=n(47163),J=n(19129);const Z=f.I4.div`
  & > span {
    width: 100%;
    display: flex;

    .antd5-tooltip-open {
      display: inline;
    }
  }
`,ee=f.I4.span`
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  display: inline-block;
  width: 100%;
  vertical-align: bottom;
`,te=f.I4.span`
  &:not(:last-child)::after {
    content: ', ';
  }
`,ne=f.I4.div`
  .link {
    color: ${({theme:e})=>e.colors.grayscale.light5};
    display: block;
    text-decoration: underline;
  }
`,ae=f.I4.span`
  ${({theme:e})=>`\n  cursor: pointer;\n  color: ${e.colors.primary.dark1};\n  font-weight: ${e.typography.weights.normal};\n  `}
`;function ie({items:e,renderVisibleItem:t=e=>e,renderTooltipItem:n=e=>e,getKey:i=e=>e,maxLinks:l=20}){const[r,s,d,c]=(0,G.A)(),h=(0,a.useMemo)((()=>e.length>l?e.length-l:void 0),[e,l]),g=(0,a.useMemo)((()=>(0,F.Y)(ee,{ref:r,children:e.map((e=>(0,F.Y)(te,{children:t(e)},i(e))))})),[i,e,t]),u=(0,a.useMemo)((()=>e.slice(0,l).map((e=>(0,F.Y)(ne,{children:n(e)},i(e))))),[i,e,l,n]);return(0,F.Y)(Z,{children:(0,F.FD)(J.m,{placement:"top",title:d?(0,F.FD)(F.FK,{children:[u,h&&(0,F.Y)("span",{children:(0,o.t)("+ %s more",h)})]}):null,children:[g,c&&(0,F.FD)(ae,{ref:s,children:["+",d]})]})})}const le=e=>({key:e.id,to:`/superset/dashboard/${e.id}`,target:"_blank",rel:"noreferer noopener",children:e.dashboard_title}),oe=e=>y.AH`
  color: ${e.colors.grayscale.light5};
  text-decoration: underline;
  &:hover {
    color: inherit;
  }
`,re=[{key:"slice_name",title:(0,o.t)("Chart"),width:"320px",sorter:!0,render:(e,t)=>(0,F.Y)(K.N_,{to:t.url,children:t.slice_name})},{key:"owners",title:(0,o.t)("Chart owners"),width:"242px",render:(e,t)=>{var n,a;return(0,F.Y)(ie,{items:null!=(n=null==(a=t.owners)?void 0:a.map((e=>`${e.first_name} ${e.last_name}`)))?n:[]})}},{key:"last_saved_at",title:(0,o.t)("Chart last modified"),width:"209px",sorter:!0,defaultSortOrder:"descend",render:(e,t)=>t.last_saved_at?V.XV.utc(t.last_saved_at).fromNow():null},{key:"last_saved_by.first_name",title:(0,o.t)("Chart last modified by"),width:"216px",sorter:!0,render:(e,t)=>t.last_saved_by?`${t.last_saved_by.first_name} ${t.last_saved_by.last_name}`:null},{key:"dashboards",title:(0,o.t)("Dashboard usage"),width:"420px",render:(e,t)=>(0,F.Y)(ie,{items:t.dashboards,renderVisibleItem:e=>(0,F.Y)(K.N_,{...le(e)}),renderTooltipItem:e=>(0,F.Y)(K.N_,{...le(e),css:oe}),getKey:e=>e.id})}],se=e=>y.AH`
  && th.ant-table-cell {
    color: ${e.colors.grayscale.light1};
  }

  .ant-table-placeholder {
    display: none;
  }
`,de=(0,F.FD)(F.FK,{children:[(0,F.Y)(m.A.PlusOutlined,{iconSize:"m",css:y.AH`
        & > .anticon {
          line-height: 0;
        }
      `}),(0,o.t)("Create chart with dataset")]}),ce=(0,f.I4)(q.p)`
  margin: ${({theme:e})=>13*e.gridUnit}px 0;
`,he=({datasetId:e})=>{const{loading:t,recordCount:n,data:i,onChange:l}=(e=>{const{addDangerToast:t}=(0,B.Yf)(),n=(0,a.useMemo)((()=>[{id:"datasource_id",operator:Q.t.Equals,value:e}]),[e]),{state:{loading:i,resourceCount:l,resourceCollection:r},fetchData:s}=(0,X.RU)("chart",(0,o.t)("chart"),t,!0,[],n),d=(0,a.useMemo)((()=>r.map((e=>({...e,key:e.id})))),[r]),c=(0,a.useCallback)(((e,t,n)=>{var a,i;const l=(null!=(a=e.current)?a:1)-1,o=null!=(i=e.pageSize)?i:0,r=(0,M.A)(n).filter((({columnKey:e})=>"string"==typeof e)).map((({columnKey:e,order:t})=>({id:e,desc:"descend"===t})));s({pageIndex:l,pageSize:o,sortBy:r,filters:[]})}),[s]);return(0,a.useEffect)((()=>{s({pageIndex:0,pageSize:25,sortBy:[{id:"last_saved_at",desc:!0}],filters:[]})}),[s]),{loading:i,recordCount:l,data:d,onChange:c}})(e),r=(0,a.useCallback)((()=>window.open(`/explore/?dataset_type=table&dataset_id=${e}`,"_blank")),[e]);return(0,F.FD)("div",{css:i.length?null:se,children:[(0,F.Y)(O.Ay,{columns:re,data:i,size:O.QS.Middle,defaultPageSize:25,recordCount:n,loading:t,onChange:l}),i.length||t?null:(0,F.Y)(ce,{image:(0,F.Y)(H.A,{}),size:"large",title:(0,o.t)("No charts"),description:(0,o.t)("This dataset is not used to power any charts."),buttonText:de,buttonAction:r})]})},ge=(0,f.I4)(j.Ay)`
  ${({theme:e})=>`\n  margin-top: ${8.5*e.gridUnit}px;\n  padding-left: ${4*e.gridUnit}px;\n  padding-right: ${4*e.gridUnit}px;\n\n  .ant-tabs-top > .ant-tabs-nav::before {\n    width: ${50*e.gridUnit}px;\n  }\n  `}
`,ue=f.I4.div`
  ${({theme:e})=>`\n  .ant-badge {\n    width: ${8*e.gridUnit}px;\n    margin-left: ${2.5*e.gridUnit}px;\n  }\n  `}
`,pe={USAGE_TEXT:(0,o.t)("Usage"),COLUMNS_TEXT:(0,o.t)("Columns"),METRICS_TEXT:(0,o.t)("Metrics")},me=({id:e})=>{const{usageCount:t}=(e=>{const[t,n]=(0,a.useState)(0),i=(0,a.useCallback)((()=>l.A.get({endpoint:`/api/v1/dataset/${e}/related_objects`}).then((({json:e})=>{n(null==e?void 0:e.charts.count)})).catch((e=>{(0,c.iB)((0,o.t)("There was an error fetching dataset's related objects")),r.A.error(e)}))),[e]);return(0,a.useEffect)((()=>{e&&i()}),[e,i]),{usageCount:t}})(e),n=(0,F.FD)(ue,{children:[(0,F.Y)("span",{children:pe.USAGE_TEXT}),t>0&&(0,F.Y)(W.A,{count:t})]});return(0,F.FD)(ge,{moreIcon:null,fullWidth:!1,children:[(0,F.Y)(j.Ay.TabPane,{tab:pe.COLUMNS_TEXT},"1"),(0,F.Y)(j.Ay.TabPane,{tab:pe.METRICS_TEXT},"2"),(0,F.Y)(j.Ay.TabPane,{tab:n,children:(0,F.Y)(he,{datasetId:e})},"3")]})};var be=n(32132),fe=n(25946),ye=n(39197);const ve=f.I4.div`
  padding: ${({theme:e})=>8*e.gridUnit}px
    ${({theme:e})=>6*e.gridUnit}px;

  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
`,xe=(0,f.I4)(q.p)`
  max-width: 50%;

  p {
    width: ${({theme:e})=>115*e.gridUnit}px;
  }
`,$e=(0,o.t)("Datasets can be created from database tables or SQL queries. Select a database table to the left or "),we=(0,o.t)("create dataset from SQL query"),Se=(0,o.t)(" to open SQL Lab. From there you can save the query as a dataset."),Ue=(0,o.t)("Select dataset source"),Ye=(0,o.t)("No table columns"),Ie=(0,o.t)("This database table does not contain any data. Please select a different table."),_e=(0,o.t)("An Error Occurred"),Ce=(0,o.t)("Unable to load columns for the selected table. Please select a different table."),Te=e=>{const{hasError:t,tableName:n,hasColumns:a}=e;let i="empty-dataset.svg",l=Ue,o=(0,F.FD)(F.FK,{children:[$e,(0,F.Y)(K.N_,{to:"/sqllab",children:(0,F.Y)("span",{role:"button",tabIndex:0,children:we})}),Se]});return t?(l=_e,o=(0,F.Y)(F.FK,{children:Ce}),i=void 0):n&&!a&&(i="no-columns.svg",l=Ye,o=(0,F.Y)(F.FK,{children:Ie})),(0,F.Y)(ve,{children:(0,F.Y)(xe,{image:i,size:"large",title:l,description:o})})};var Ae;!function(e){e.ABSOLUTE="absolute",e.RELATIVE="relative"}(Ae||(Ae={}));const De=f.I4.div`
  ${({theme:e,position:t})=>`\n  position: ${t};\n  margin: ${4*e.gridUnit}px\n    ${3*e.gridUnit}px\n    ${3*e.gridUnit}px\n    ${6*e.gridUnit}px;\n  font-size: ${6*e.gridUnit}px;\n  font-weight: ${e.typography.weights.medium};\n  padding-bottom: ${3*e.gridUnit}px;\n\n  white-space: nowrap;\n  overflow: hidden;\n  text-overflow: ellipsis;\n\n  .anticon:first-of-type {\n    margin-right: ${4*e.gridUnit}px;\n  }\n\n  .anticon:nth-of-type(2) {\n    margin-left: ${4*e.gridUnit}px;\n  `}
`,ke=f.I4.div`
  ${({theme:e})=>`\n  margin-left: ${6*e.gridUnit}px;\n  margin-bottom: ${3*e.gridUnit}px;\n  font-weight: ${e.typography.weights.bold};\n  `}
`,ze=f.I4.div`
  ${({theme:e})=>`\n  padding: ${8*e.gridUnit}px\n    ${6*e.gridUnit}px;\n  box-sizing: border-box;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  height: 100%;\n  position: absolute;\n  top: 0;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  `}
`,Fe=f.I4.div`
  ${({theme:e})=>`\n  max-width: 50%;\n  width: 200px;\n\n  img {\n    width: 120px;\n    margin-left: 40px;\n  }\n\n  div {\n    width: 100%;\n    margin-top: ${3*e.gridUnit}px;\n    text-align: center;\n    font-weight: ${e.typography.weights.normal};\n    font-size: ${e.typography.sizes.l}px;\n    color: ${e.colors.grayscale.light1};\n  }\n  `}
`,Ee=f.I4.div`
  ${({theme:e})=>`\n  position: relative;\n  margin: ${3*e.gridUnit}px;\n  margin-left: ${6*e.gridUnit}px;\n  height: calc(100% - ${60*e.gridUnit}px);\n  overflow: auto;\n  `}
`,Ne=f.I4.div`
  ${({theme:e})=>`\n  position: relative;\n  margin: ${3*e.gridUnit}px;\n  margin-left: ${6*e.gridUnit}px;\n  height: calc(100% - ${30*e.gridUnit}px);\n  overflow: auto;\n  `}
`,Pe=f.I4.div`
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
`,Re=(0,f.I4)(fe.A)`
  ${({theme:e})=>`\n  border: 1px solid ${e.colors.info.base};\n  padding: ${4*e.gridUnit}px;\n  margin: ${6*e.gridUnit}px ${6*e.gridUnit}px\n    ${8*e.gridUnit}px;\n  .view-dataset-button {\n    position: absolute;\n    top: ${4*e.gridUnit}px;\n    right: ${4*e.gridUnit}px;\n    font-weight: ${e.typography.weights.normal};\n\n    &:hover {\n      color: ${e.colors.secondary.dark3};\n      text-decoration: underline;\n    }\n  }\n  `}
`,Le=(0,o.t)("Refreshing columns"),We=(0,o.t)("Table columns"),je=(0,o.t)("Loading"),Ke=["5","10","15","25"],Me=[{title:"Column Name",dataIndex:"name",key:"name",sorter:(e,t)=>e.name.localeCompare(t.name)},{title:"Datatype",dataIndex:"type",key:"type",width:"100px",sorter:(e,t)=>e.name.localeCompare(t.name)}],Oe=(0,o.t)("This table already has a dataset associated with it. You can only associate one dataset with a table.\n"),qe=(0,o.t)("View Dataset"),He=({tableName:e,columnList:t,loading:n,hasError:a,datasets:i})=>{const l=(0,f.DP)(),r=Boolean((null==t?void 0:t.length)>0),s=null==i?void 0:i.map((e=>e.table_name)),d=null==i?void 0:i.find((t=>t.table_name===e));let c,h;return n&&(h=(0,F.Y)(ze,{children:(0,F.FD)(Fe,{children:[(0,F.Y)("img",{alt:je,src:ye}),(0,F.Y)("div",{children:Le})]})})),n||(c=!n&&e&&r&&!a?(0,F.FD)(F.FK,{children:[(0,F.Y)(ke,{children:We}),d?(0,F.Y)(Ee,{children:(0,F.Y)(Pe,{children:(0,F.Y)(O.Ay,{loading:n,size:O.QS.Small,columns:Me,data:t,pageSizeOptions:Ke,defaultPageSize:25})})}):(0,F.Y)(Ne,{children:(0,F.Y)(Pe,{children:(0,F.Y)(O.Ay,{loading:n,size:O.QS.Small,columns:Me,data:t,pageSizeOptions:Ke,defaultPageSize:25})})})]}):(0,F.Y)(Te,{hasColumns:r,hasError:a,tableName:e})),(0,F.FD)(F.FK,{children:[e&&(0,F.FD)(F.FK,{children:[(null==s?void 0:s.includes(e))&&(g=d,(0,F.Y)(Re,{closable:!1,type:"info",showIcon:!0,message:(0,o.t)("This table already has a dataset"),description:(0,F.FD)(F.FK,{children:[Oe,(0,F.Y)("span",{role:"button",onClick:()=>{window.open(null==g?void 0:g.explore_url,"_blank","noreferrer noopener popup=false")},tabIndex:0,className:"view-dataset-button",children:qe})]})})),(0,F.FD)(De,{position:!n&&r?Ae.RELATIVE:Ae.ABSOLUTE,title:e||"",children:[e&&(0,F.Y)(m.A.Table,{iconColor:l.colors.grayscale.base}),e]})]}),c,h]});var g},Be=({tableName:e,dbId:t,catalog:n,schema:i,setHasColumns:s,datasets:d})=>{const[h,g]=(0,a.useState)([]),[u,p]=(0,a.useState)(!1),[m,b]=(0,a.useState)(!1),f=(0,a.useRef)(e);return(0,a.useEffect)((()=>{f.current=e,e&&i&&t&&(async e=>{const{dbId:t,tableName:a,schema:i}=e;p(!0),null==s||s(!1);const d=`/api/v1/database/${t}/table_metadata/${(0,be.zJ)({name:a,catalog:n,schema:i})}`;try{const e=await l.A.get({endpoint:d});if((e=>{let t=!0;if("string"!=typeof(null==e?void 0:e.name)&&(t=!1),t&&!Array.isArray(e.columns)&&(t=!1),t&&e.columns.length>0){const n=e.columns.some(((e,t)=>{const n=(e=>{let t=!0;const n="The object provided to isITableColumn does match the interface.";return"string"!=typeof(null==e?void 0:e.name)&&(t=!1,console.error(`${n} The property 'name' is required and must be a string`)),t&&"string"!=typeof(null==e?void 0:e.type)&&(t=!1,console.error(`${n} The property 'type' is required and must be a string`)),t})(e);return n||console.error(`The provided object does not match the IDatabaseTable interface. columns[${t}] is invalid and does not match the ITableColumn interface`),!n}));t=!n}return t})(null==e?void 0:e.json)){const t=e.json;t.name===f.current&&(g(t.columns),null==s||s(t.columns.length>0),b(!1))}else g([]),null==s||s(!1),b(!0),(0,c.iB)((0,o.t)("The API response from %s does not match the IDatabaseTable interface.",d)),r.A.error((0,o.t)("The API response from %s does not match the IDatabaseTable interface.",d))}catch(e){g([]),null==s||s(!1),b(!0)}finally{p(!1)}})({tableName:e,dbId:t,schema:i})}),[e,t,i]),(0,F.Y)(He,{columnList:h,hasError:m,loading:u,tableName:e,datasets:d})};var Xe=n(8791),Qe=n(62221);const Ve=f.I4.div`
  ${({theme:e})=>`\n    padding: ${4*e.gridUnit}px;\n    height: 100%;\n    background-color: ${e.colors.grayscale.light5};\n    position: relative;\n    .emptystate {\n      height: auto;\n      margin-top: ${17.5*e.gridUnit}px;\n    }\n    .section-title {\n      margin-top: ${5.5*e.gridUnit}px;\n      margin-bottom: ${11*e.gridUnit}px;\n      font-weight: ${e.typography.weights.bold};\n    }\n    .table-title {\n      margin-top: ${11*e.gridUnit}px;\n      margin-bottom: ${6*e.gridUnit}px;\n      font-weight: ${e.typography.weights.bold};\n    }\n    .options-list {\n      overflow: auto;\n      position: absolute;\n      bottom: 0;\n      top: ${92.25*e.gridUnit}px;\n      left: ${3.25*e.gridUnit}px;\n      right: 0;\n\n      .no-scrollbar {\n        margin-right: ${4*e.gridUnit}px;\n      }\n\n      .options {\n        cursor: pointer;\n        padding: ${1.75*e.gridUnit}px;\n        border-radius: ${e.borderRadius}px;\n        :hover {\n          background-color: ${e.colors.grayscale.light4}\n        }\n      }\n\n      .options-highlighted {\n        cursor: pointer;\n        padding: ${1.75*e.gridUnit}px;\n        border-radius: ${e.borderRadius}px;\n        background-color: ${e.colors.primary.dark1};\n        color: ${e.colors.grayscale.light5};\n      }\n\n      .options, .options-highlighted {\n        display: flex;\n        align-items: center;\n        justify-content: space-between;\n      }\n    }\n    form > span[aria-label="refresh"] {\n      position: absolute;\n      top: ${69*e.gridUnit}px;\n      left: ${42.75*e.gridUnit}px;\n      font-size: ${4.25*e.gridUnit}px;\n    }\n    .table-form {\n      margin-bottom: ${8*e.gridUnit}px;\n    }\n    .loading-container {\n      position: absolute;\n      top: ${89.75*e.gridUnit}px;\n      left: 0;\n      right: 0;\n      text-align: center;\n      img {\n        width: ${20*e.gridUnit}px;\n        margin-bottom: ${2.5*e.gridUnit}px;\n      }\n      p {\n        color: ${e.colors.grayscale.light1};\n      }\n    }\n`}
`;function Ge({setDataset:e,dataset:t,datasetNames:n}){const{addDangerToast:i}=(0,B.Yf)(),l=(0,a.useCallback)((t=>{e({type:g.SelectDatabase,payload:{db:t}})}),[e]);(0,a.useEffect)((()=>{const e=(0,Qe.Gq)(Qe.Hh.Database,null);e&&l(e)}),[l]);const r=(0,a.useCallback)((e=>(0,F.Y)(Xe.cs,{table:null!=n&&n.includes(e.value)?{...e,extra:{warning_markdown:(0,o.t)("This table already has a dataset")}}:e})),[n]);return(0,F.Y)(Ve,{children:(0,F.Y)(Xe.Ay,{database:null==t?void 0:t.db,handleError:i,emptyState:(0,F.Y)(q.p,{image:"empty.svg",title:(0,o.t)("No databases available"),description:(0,F.FD)("span",{children:[(0,o.t)("Manage your databases")," ",(0,F.Y)("a",{href:"/databaseview/list",children:(0,o.t)("here")})]}),size:"small"}),onDbChange:l,onCatalogChange:t=>{t&&e({type:g.SelectCatalog,payload:{name:"catalog",value:t}})},onSchemaChange:t=>{t&&e({type:g.SelectSchema,payload:{name:"schema",value:t}})},onTableSelectChange:t=>{e({type:g.SelectTable,payload:{name:"table_name",value:t}})},sqlLabMode:!1,customTableOptionLabelRenderer:r,...(null==t?void 0:t.catalog)&&{catalog:t.catalog},...(null==t?void 0:t.schema)&&{schema:t.schema}})})}var Je=n(7735),Ze=n(35700);const et=["db","schema","table_name"],tt=[Ze.ci,Ze.q0,Ze.ar,Ze.R2],nt=(0,B.Ay)((function({datasetObject:e,addDangerToast:t,hasColumns:n=!1,datasets:a}){const l=(0,i.W6)(),{createResource:r}=(0,X.fn)("dataset",(0,o.t)("dataset"),t),s=(0,o.t)("Select a database table."),d=(0,o.t)("Create dataset and create chart"),c=!(null!=e&&e.table_name)||!n||(null==a?void 0:a.includes(null==e?void 0:e.table_name));return(0,F.FD)(F.FK,{children:[(0,F.Y)(p.A,{onClick:()=>{if(e){const t=(e=>{let t=0;const n=Object.keys(e).reduce(((n,a)=>(et.includes(a)&&e[a]&&(t+=1),t)),0);return tt[n]})(e);(0,Je.logEvent)(t,e)}else(0,Je.logEvent)(Ze.ci,{});l.goBack()},children:(0,o.t)("Cancel")}),(0,F.Y)(p.A,{buttonStyle:"primary",disabled:c,tooltip:null!=e&&e.table_name?void 0:s,onClick:()=>{if(e){var t;const n={database:null==(t=e.db)?void 0:t.id,catalog:e.catalog,schema:e.schema,table_name:e.table_name};r(n).then((t=>{t&&"number"==typeof t&&((0,Je.logEvent)(Ze.oA,e),l.push(`/chart/add/?dataset=${e.table_name}`))}))}},children:d})]})}));var at=n(41621);function it({header:e,leftPanel:t,datasetPanel:n,rightPanel:a,footer:i}){const l=(0,f.DP)();return(0,F.FD)(v,{children:[e&&(0,F.Y)(I,{children:e}),(0,F.FD)(S,{children:[t&&(0,F.Y)(at.A,{id:"dataset",initialWidth:80*l.gridUnit,minWidth:80*l.gridUnit,enable:!0,children:e=>(0,F.Y)(x,{width:e,children:(0,F.Y)(C,{children:t})})}),(0,F.FD)($,{children:[(0,F.FD)(U,{children:[n&&(0,F.Y)(T,{children:n}),a&&(0,F.Y)(A,{children:a})]}),(0,F.Y)(Y,{children:i&&(0,F.Y)(D,{children:i})})]})]})]})}function lt(e,t){const n={...e||{}};switch(t.type){case g.SelectDatabase:return{...n,...t.payload,catalog:null,schema:null,table_name:null};case g.SelectCatalog:return{...n,[t.payload.name]:t.payload.value,schema:null,table_name:null};case g.SelectSchema:return{...n,[t.payload.name]:t.payload.value,table_name:null};case g.SelectTable:return{...n,[t.payload.name]:t.payload.value};case g.ChangeDataset:return{...n,[t.payload.name]:t.payload.value};default:return null}}const ot="/tablemodelview/list/?pageIndex=0&sortColumn=changed_on_delta_humanized&sortOrder=desc";function rt(){const[e,t]=(0,a.useReducer)(lt,null),[n,l]=(0,a.useState)(!1),[o,r]=(0,a.useState)(!1),{datasets:s,datasetNames:d}=h(null==e?void 0:e.db,null==e?void 0:e.schema),{datasetId:c}=(0,i.g)();return(0,a.useEffect)((()=>{Number.isNaN(parseInt(c,10))||r(!0)}),[c]),(0,F.Y)(it,{header:(0,F.Y)(L,{setDataset:t,title:null==e?void 0:e.table_name}),leftPanel:o?null:(0,F.Y)(Ge,{setDataset:t,dataset:e,datasetNames:d}),datasetPanel:o?(0,F.Y)(me,{id:c}):(0,F.Y)(Be,{tableName:null==e?void 0:e.table_name,dbId:null==e||null==(g=e.db)?void 0:g.id,catalog:null==e?void 0:e.catalog,schema:null==e?void 0:e.schema,setHasColumns:l,datasets:s}),footer:(0,F.Y)(nt,{url:ot,datasetObject:e,hasColumns:n,datasets:d})});var g}}}]);