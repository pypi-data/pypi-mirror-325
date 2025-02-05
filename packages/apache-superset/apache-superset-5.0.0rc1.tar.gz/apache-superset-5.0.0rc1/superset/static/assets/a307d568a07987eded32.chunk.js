"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[9039],{45418:(e,t,i)=>{i.d(t,{A:()=>g});var r=i(96540),n=i(46942),o=i.n(n),l=i(22553),a=i(77132),d=i(1051),s=i(96424),c=i(14277);const h=e=>{const{componentCls:t,sizePaddingEdgeHorizontal:i,colorSplit:r,lineWidth:n,textPaddingInline:o,orientationMargin:l,verticalMarginInline:s}=e;return{[t]:Object.assign(Object.assign({},(0,d.dF)(e)),{borderBlockStart:`${(0,a.zA)(n)} solid ${r}`,"&-vertical":{position:"relative",top:"-0.06em",display:"inline-block",height:"0.9em",marginInline:s,marginBlock:0,verticalAlign:"middle",borderTop:0,borderInlineStart:`${(0,a.zA)(n)} solid ${r}`},"&-horizontal":{display:"flex",clear:"both",width:"100%",minWidth:"100%",margin:`${(0,a.zA)(e.dividerHorizontalGutterMargin)} 0`},[`&-horizontal${t}-with-text`]:{display:"flex",alignItems:"center",margin:`${(0,a.zA)(e.dividerHorizontalWithTextGutterMargin)} 0`,color:e.colorTextHeading,fontWeight:500,fontSize:e.fontSizeLG,whiteSpace:"nowrap",textAlign:"center",borderBlockStart:`0 ${r}`,"&::before, &::after":{position:"relative",width:"50%",borderBlockStart:`${(0,a.zA)(n)} solid transparent`,borderBlockStartColor:"inherit",borderBlockEnd:0,transform:"translateY(50%)",content:"''"}},[`&-horizontal${t}-with-text-left`]:{"&::before":{width:`calc(${l} * 100%)`},"&::after":{width:`calc(100% - ${l} * 100%)`}},[`&-horizontal${t}-with-text-right`]:{"&::before":{width:`calc(100% - ${l} * 100%)`},"&::after":{width:`calc(${l} * 100%)`}},[`${t}-inner-text`]:{display:"inline-block",paddingBlock:0,paddingInline:o},"&-dashed":{background:"none",borderColor:r,borderStyle:"dashed",borderWidth:`${(0,a.zA)(n)} 0 0`},[`&-horizontal${t}-with-text${t}-dashed`]:{"&::before, &::after":{borderStyle:"dashed none none"}},[`&-vertical${t}-dashed`]:{borderInlineStartWidth:n,borderInlineEnd:0,borderBlockStart:0,borderBlockEnd:0},"&-dotted":{background:"none",borderColor:r,borderStyle:"dotted",borderWidth:`${(0,a.zA)(n)} 0 0`},[`&-horizontal${t}-with-text${t}-dotted`]:{"&::before, &::after":{borderStyle:"dotted none none"}},[`&-vertical${t}-dotted`]:{borderInlineStartWidth:n,borderInlineEnd:0,borderBlockStart:0,borderBlockEnd:0},[`&-plain${t}-with-text`]:{color:e.colorText,fontWeight:"normal",fontSize:e.fontSize},[`&-horizontal${t}-with-text-left${t}-no-default-orientation-margin-left`]:{"&::before":{width:0},"&::after":{width:"100%"},[`${t}-inner-text`]:{paddingInlineStart:i}},[`&-horizontal${t}-with-text-right${t}-no-default-orientation-margin-right`]:{"&::before":{width:"100%"},"&::after":{width:0},[`${t}-inner-text`]:{paddingInlineEnd:i}}})}},p=(0,s.OF)("Divider",(e=>{const t=(0,c.oX)(e,{dividerHorizontalWithTextGutterMargin:e.margin,dividerHorizontalGutterMargin:e.marginLG,sizePaddingEdgeHorizontal:0});return[h(t)]}),(e=>({textPaddingInline:"1em",orientationMargin:.05,verticalMarginInline:e.marginXS})),{unitless:{orientationMargin:!0}});const g=e=>{const{getPrefixCls:t,direction:i,divider:n}=r.useContext(l.QO),{prefixCls:a,type:d="horizontal",orientation:s="center",orientationMargin:c,className:h,rootClassName:g,children:m,dashed:u,variant:b="solid",plain:f,style:v}=e,$=function(e,t){var i={};for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&t.indexOf(r)<0&&(i[r]=e[r]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols){var n=0;for(r=Object.getOwnPropertySymbols(e);n<r.length;n++)t.indexOf(r[n])<0&&Object.prototype.propertyIsEnumerable.call(e,r[n])&&(i[r[n]]=e[r[n]])}return i}(e,["prefixCls","type","orientation","orientationMargin","className","rootClassName","children","dashed","variant","plain","style"]),x=t("divider",a),[w,y,A]=p(x),z=!!m,S="left"===s&&null!=c,k="right"===s&&null!=c,I=o()(x,null==n?void 0:n.className,y,A,`${x}-${d}`,{[`${x}-with-text`]:z,[`${x}-with-text-${s}`]:z,[`${x}-dashed`]:!!u,[`${x}-${b}`]:"solid"!==b,[`${x}-plain`]:!!f,[`${x}-rtl`]:"rtl"===i,[`${x}-no-default-orientation-margin-left`]:S,[`${x}-no-default-orientation-margin-right`]:k},h,g),Y=r.useMemo((()=>"number"==typeof c?c:/^\d+$/.test(c)?Number(c):c),[c]),C=Object.assign(Object.assign({},S&&{marginLeft:Y}),k&&{marginRight:Y});return w(r.createElement("div",Object.assign({className:I,style:Object.assign(Object.assign({},null==n?void 0:n.style),v)},$,{role:"separator"}),m&&"vertical"!==d&&r.createElement("span",{className:`${x}-inner-text`,style:C},m)))}},40458:(e,t,i)=>{i.d(t,{A:()=>a});var r=i(96453),n=i(2445);const o=r.I4.label`
  font-size: ${({theme:e})=>e.typography.sizes.s}px;
  color: ${({theme:e})=>e.colors.grayscale.base};
  margin-bottom: ${({theme:e})=>e.gridUnit}px;
`,l=r.I4.label`
  font-size: ${({theme:e})=>e.typography.sizes.s}px;
  color: ${({theme:e})=>e.colors.grayscale.base};
  margin-bottom: ${({theme:e})=>e.gridUnit}px;
  &::after {
    display: inline-block;
    margin-left: ${({theme:e})=>e.gridUnit}px;
    color: ${({theme:e})=>e.colors.error.base};
    font-size: ${({theme:e})=>e.typography.sizes.m}px;
    content: '*';
  }
`;function a({children:e,htmlFor:t,required:i=!1,className:r}){const a=i?l:o;return(0,n.Y)(a,{htmlFor:t,className:r,children:e})}},97987:(e,t,i)=>{i.d(t,{A:()=>S});var r,n=i(36255),o=i(27236),l=i(96453),a=i(17437),d=i(95579),s=i(31641),c=i(12249),h=i(46920),p=i(96540);function g(){return g=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var i=arguments[t];for(var r in i)({}).hasOwnProperty.call(i,r)&&(e[r]=i[r])}return e},g.apply(null,arguments)}const m=({title:e,titleId:t,...i},n)=>p.createElement("svg",g({xmlns:"http://www.w3.org/2000/svg",width:24,height:24,fill:"none",ref:n,"aria-labelledby":t},i),e?p.createElement("title",{id:t},e):null,r||(r=p.createElement("path",{fill:"currentColor",fillRule:"evenodd",d:"M12 7a1 1 0 0 0-1 1v4a1 1 0 1 0 2 0V8a1 1 0 0 0-1-1m0 8a1 1 0 1 0 0 2 1 1 0 0 0 0-2m9.71-7.44-5.27-5.27a1.05 1.05 0 0 0-.71-.29H8.27a1.05 1.05 0 0 0-.71.29L2.29 7.56a1.05 1.05 0 0 0-.29.71v7.46c.004.265.107.518.29.71l5.27 5.27c.192.183.445.286.71.29h7.46a1.05 1.05 0 0 0 .71-.29l5.27-5.27a1.05 1.05 0 0 0 .29-.71V8.27a1.05 1.05 0 0 0-.29-.71M20 15.31 15.31 20H8.69L4 15.31V8.69L8.69 4h6.62L20 8.69z",clipRule:"evenodd"}))),u=(0,p.forwardRef)(m);var b=i(86523),f=i(40458),v=i(2445);const $=(0,l.I4)(n.A)`
  margin: ${({theme:e})=>`${e.gridUnit}px 0 ${2*e.gridUnit}px`};
`,x=(0,l.I4)(n.A.Password)`
  margin: ${({theme:e})=>`${e.gridUnit}px 0 ${2*e.gridUnit}px`};
`,w=(0,l.I4)("div")`
  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
  margin-bottom: ${({theme:e})=>3*e.gridUnit}px;
  .ant-form-item {
    margin-bottom: 0;
  }
`,y=l.I4.div`
  display: flex;
  align-items: center;
`,A=(0,l.I4)(f.A)`
  margin-bottom: 0;
`,z=a.AH`
  &.anticon > * {
    line-height: 0;
  }
`,S=({label:e,validationMethods:t,errorMessage:i,helpText:r,required:n=!1,hasTooltip:l=!1,tooltipText:p,id:g,className:m,visibilityToggle:f,get_url:S,description:k,...I})=>(0,v.FD)(w,{className:m,children:[(0,v.FD)(y,{children:[(0,v.Y)(A,{htmlFor:g,required:n,children:e}),l&&(0,v.Y)(s.A,{tooltip:`${p}`})]}),(0,v.FD)(b.A,{css:e=>((e,t)=>a.AH`
  .ant-form-item-children-icon {
    display: none;
  }
  ${t&&`.ant-form-item-control-input-content {\n      position: relative;\n      &:after {\n        content: ' ';\n        display: inline-block;\n        background: ${e.colors.error.base};\n        mask: url(${u});\n        mask-size: cover;\n        width: ${4*e.gridUnit}px;\n        height: ${4*e.gridUnit}px;\n        position: absolute;\n        right: ${1.25*e.gridUnit}px;\n        top: ${2.75*e.gridUnit}px;\n      }\n    }`}
`)(e,!!i),validateTrigger:Object.keys(t),validateStatus:i?"error":"success",help:i||r,hasFeedback:!!i,children:[f||"password"===I.name?(0,v.Y)(x,{...I,...t,iconRender:e=>e?(0,v.Y)(o.A,{title:(0,d.t)("Hide password."),children:(0,v.Y)(c.A.EyeInvisibleOutlined,{iconSize:"m",css:z})}):(0,v.Y)(o.A,{title:(0,d.t)("Show password."),children:(0,v.Y)(c.A.EyeOutlined,{iconSize:"m",css:z})}),role:"textbox"}):(0,v.Y)($,{...I,...t}),S&&k?(0,v.FD)(h.A,{type:"link",htmlType:"button",buttonStyle:"default",onClick:()=>(window.open(S),!0),children:["Get ",k]}):(0,v.Y)("br",{})]})]})},40563:(e,t,i)=>{i.d(t,{lV:()=>a,eI:()=>d.A,lR:()=>s.A,MA:()=>c.A});var r=i(77925),n=i(96453),o=i(2445);const l=(0,n.I4)(r.A)`
  &.ant-form label {
    font-size: ${({theme:e})=>e.typography.sizes.s}px;
  }
  .ant-form-item {
    margin-bottom: ${({theme:e})=>4*e.gridUnit}px;
  }
`;function a(e){return(0,o.Y)(l,{...e})}var d=i(86523),s=i(40458),c=i(97987)},31641:(e,t,i)=>{i.d(t,{A:()=>h});var r=i(96453),n=i(19129),o=i(12249),l=i(2445);const a=(0,r.I4)(n.m)`
  cursor: pointer;
`,d=r.I4.span`
  display: -webkit-box;
  -webkit-line-clamp: 20;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
`,s={fontSize:"12px",lineHeight:"16px"},c="rgba(0,0,0,0.9)";function h({tooltip:e,iconStyle:t={},placement:i="right",trigger:n="hover",overlayStyle:h=s,bgColor:p=c,viewBox:g="0 -1 24 24"}){const m=(0,r.DP)(),u={...t,color:t.color||m.colors.grayscale.base};return(0,l.Y)(a,{title:(0,l.Y)(d,{children:e}),placement:i,trigger:n,overlayStyle:h,color:p,children:(0,l.Y)(o.A.InfoSolidSmall,{style:u,viewBox:g})})}},90868:(e,t,i)=>{i.d(t,{YI:()=>l,fs:()=>a,pd:()=>o});var r=i(63786),n=i(80566);const o=r.A,l=n.A,{TextArea:a}=r.A},69193:(e,t,i)=>{i.d(t,{s:()=>a});var r=i(75160),n=i(89516),o=i(2445);function l(e){return(0,o.Y)(n.A,{...e})}const a=Object.assign(r.Ay,{GroupWrapper:({spaceConfig:e,options:t,...i})=>{const r=t.map((e=>(0,o.Y)(a,{value:e.value,children:e.label},e.value)));return(0,o.Y)(a.Group,{...i,children:e?(0,o.Y)(l,{...e,children:r}):r})},Button:r.Ay.Button})},50317:(e,t,i)=>{i.d(t,{A:()=>g});var r=i(96540),n=i(17437),o=i(96453),l=i(95579),a=i(66537),d=i(19129),s=i(40563),c=i(12249),h=i(2445);const p=n.AH`
  &.anticon {
    font-size: unset;
    .anticon {
      line-height: unset;
      vertical-align: unset;
    }
  }
`,g=({name:e,label:t,description:i,validationErrors:g=[],renderTrigger:m=!1,rightNode:u,leftNode:b,onClick:f,hovered:v=!1,tooltipOnClick:$=()=>{},warning:x,danger:w})=>{const{gridUnit:y,colors:A}=(0,o.DP)(),z=(0,r.useRef)(!1),S=(0,r.useMemo)((()=>(g.length||(z.current=!0),z.current?g.length?A.error.base:"unset":A.warning.base)),[A.error.base,A.warning.base,g.length]);return t?(0,h.FD)("div",{className:"ControlHeader",children:[(0,h.Y)("div",{className:"pull-left",children:(0,h.FD)(s.lR,{css:e=>n.AH`
            margin-bottom: ${.5*e.gridUnit}px;
            position: relative;
          `,children:[b&&(0,h.Y)("span",{children:b}),(0,h.Y)("span",{role:"button",tabIndex:0,onClick:f,style:{cursor:f?"pointer":""},children:t})," ",x&&(0,h.FD)("span",{children:[(0,h.Y)(d.m,{id:"error-tooltip",placement:"top",title:x,children:(0,h.Y)(c.A.AlertSolid,{iconColor:A.warning.base,iconSize:"s"})})," "]}),w&&(0,h.FD)("span",{children:[(0,h.Y)(d.m,{id:"error-tooltip",placement:"top",title:w,children:(0,h.Y)(c.A.ErrorSolid,{iconColor:A.error.base,iconSize:"s"})})," "]}),(null==g?void 0:g.length)>0&&(0,h.FD)("span",{children:[(0,h.Y)(d.m,{id:"error-tooltip",placement:"top",title:null==g?void 0:g.join(" "),children:(0,h.Y)(c.A.ExclamationCircleOutlined,{css:n.AH`
                    ${p};
                    color: ${S};
                  `})})," "]}),v?(0,h.FD)("span",{css:()=>n.AH`
          position: absolute;
          top: 50%;
          right: 0;
          padding-left: ${y}px;
          transform: translate(100%, -50%);
          white-space: nowrap;
        `,children:[i&&(0,h.FD)("span",{children:[(0,h.Y)(d.m,{id:"description-tooltip",title:i,placement:"top",children:(0,h.Y)(c.A.InfoCircleOutlined,{css:p,onClick:$})})," "]}),m&&(0,h.FD)("span",{children:[(0,h.Y)(a.W,{label:(0,l.t)("bolt"),tooltip:(0,l.t)("Changing this control takes effect instantly"),placement:"top",icon:"bolt"})," "]})]}):null]})}),u&&(0,h.Y)("div",{className:"pull-right",children:u}),(0,h.Y)("div",{className:"clearfix"})]}):null}},87615:(e,t,i)=>{i.r(t),i.d(t,{default:()=>h});var r=i(96453),n=i(96627),o=i(96540),l=i(39074),a=i(67874),d=i(2445);const s=(0,r.I4)(a.j3)`
  display: flex;
  align-items: center;
  overflow-x: auto;

  & .ant-tag {
    margin-right: 0;
  }
`,c=r.I4.div`
  display: flex;
  height: 100%;
  max-width: 100%;
  width: 100%;
  & > div,
  & > div:hover {
    ${({validateStatus:e,theme:t})=>{var i;return e&&`border-color: ${null==(i=t.colors[e])?void 0:i.base}`}}
  }
`;function h(e){var t;const{setDataMask:i,setHoveredFilter:r,unsetHoveredFilter:a,setFocusedFilter:h,unsetFocusedFilter:p,setFilterActive:g,width:m,height:u,filterState:b,inputRef:f,isOverflowingFilterBar:v=!1}=e,$=(0,o.useCallback)((e=>{const t=e&&e!==n.WC;i({extraFormData:t?{time_range:e}:{},filterState:{value:t?e:void 0}})}),[i]);return(0,o.useEffect)((()=>{$(b.value)}),[b.value]),null!=(t=e.formData)&&t.inView?(0,d.Y)(s,{width:m,height:u,children:(0,d.Y)(c,{ref:f,validateStatus:b.validateStatus,onFocus:h,onBlur:p,onMouseEnter:r,onMouseLeave:a,children:(0,d.Y)(l.Ay,{value:b.value||n.WC,name:e.formData.nativeFilterId||"time_range",onChange:$,onOpenPopover:()=>g(!0),onClosePopover:()=>{g(!1),a(),p()},isOverflowingFilterBar:v})})}):null}},67874:(e,t,i)=>{i.d(t,{JF:()=>a,Mo:()=>d,YH:()=>o,j3:()=>l});var r=i(96453),n=i(86523);const o=0,l=r.I4.div`
  min-height: ${({height:e})=>e}px;
  width: ${({width:e})=>e===o?"100%":`${e}px`};
`,a=(0,r.I4)(n.A)`
  &.ant-row.ant-form-item {
    margin: 0;
  }
`,d=r.I4.div`
  color: ${({theme:e,status:t="error"})=>{var i;return null==(i=e.colors[t])?void 0:i.base}};
`}}]);