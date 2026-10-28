const { chromium } = require('playwright');
const C={paper:'#EFE3C8',ink:'#24211D',mus:'#D9A23A',teal:'#2F7C78',red:'#C23A2B',sheet:'#1F4F4C'};
const man=(x,y,s,fill,hat)=>{ // 24-unit grid
  const g=`<g transform="translate(${x},${y}) scale(${s/24})" fill="${fill}">
  <circle cx="12" cy="4.6" r="3.4"/>
  <path d="M6.5 9 h11 l1.2 8 h-2.4 l-0.6 -4.5 v11.5 h-3 v-7 h-1.4 v7 h-3 v-11.5 l-0.6 4.5 h-2.4z"/>
  ${hat==='fedora'?'<path d="M6.4 3.4 h11.2 v1.1 h-11.2z M8.4 -0.4 h7.2 l0.7 3.9 h-8.6z"/>':''}
  ${hat==='cap'?'<path d="M8.4 0.4 h7.2 v2.6 h-7.2z M7.4 2.8 h10 v1 h-10z"/>':''}
  </g>`;return g;};
const coin=(x,y,s,f)=>`<g transform="translate(${x},${y}) scale(${s/24})"><circle cx="12" cy="12" r="10" fill="${f}"/><rect x="11" y="6" width="2" height="12" fill="${C.paper}"/></g>`;
let iso=`<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><rect width="1920" height="1080" fill="${C.paper}"/>
<text x="120" y="170" font-family="Alfa Slab One" font-size="72" fill="${C.ink}">PROMOTION, 1925</text>
<text x="120" y="230" font-family="Archivo" font-weight="700" font-size="30" letter-spacing="3" fill="${C.ink}">ONE MAN LEAVES. ONE MAN MOVES UP.</text>`;
const rows=[{y:330,n:1,hat:'fedora',label:'THE BOSS'},{y:520,n:4,hat:'fedora',label:'MANAGEMENT'},{y:710,n:13,hat:null,label:'STAFF'}];
rows.forEach((r,ri)=>{iso+=`<rect x="120" y="${r.y+150}" width="1680" height="4" fill="${C.ink}"/><text x="120" y="${r.y+120}" font-family="Archivo" font-weight="700" font-size="24" letter-spacing="3" fill="${C.ink}">${r.label}</text>`;
 for(let i=0;i<r.n;i++){if(ri===1&&i===1){iso+=`<rect x="651" y="${r.y+4}" width="74" height="144" fill="none" stroke="${C.ink}" stroke-width="2" stroke-dasharray="8 6"/>`;continue;} iso+=man(560+i*88,r.y,150,ri===2?C.teal:C.ink,r.hat);}});
// boss slot: torrio leaving (outline ghost) + capone red
iso+=man(560,330,150,C.red,'fedora');
iso+=`<g opacity="0.25">${man(660,330,150,C.ink,'fedora')}</g><text x="770" y="420" font-family="Special Elite" font-size="28" fill="${C.ink}">← early retirement</text>`;
iso+=`<text x="1800" y="1030" text-anchor="end" font-family="Archivo" font-size="22" fill="${C.ink}">1 FIGURE = 1 EMPLOYEE · SAMPLE FRAME, ILLUSTRATIVE</text></svg>`;
// blueprint
let bp=`<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><rect width="1920" height="1080" fill="${C.sheet}"/>
<rect x="40" y="40" width="1840" height="1000" fill="none" stroke="${C.paper}" stroke-width="3"/>
<defs><pattern id="h" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="14" stroke="${C.paper}" stroke-width="1.5"/></pattern></defs>
<g stroke="${C.paper}" fill="none" stroke-width="5">
<rect x="220" y="180" width="1000" height="640"/>
<line x1="620" y1="180" x2="620" y2="560"/><line x1="220" y1="560" x2="900" y2="560"/>
</g>
<rect x="900" y="560" width="320" height="260" fill="${C.mus}" fill-opacity="0.6" stroke="${C.paper}" stroke-width="5"/>
<rect x="980" y="620" width="160" height="140" fill="url(#h)" stroke="${C.paper}" stroke-width="3"/>
<text x="1060" y="605" text-anchor="middle" font-family="Archivo" font-weight="700" font-size="22" letter-spacing="3" fill="${C.paper}">VAULT</text>
<text x="420" y="380" text-anchor="middle" font-family="Archivo" font-weight="700" font-size="22" letter-spacing="3" fill="${C.paper}">LOBBY</text>
<text x="920" y="380" text-anchor="middle" font-family="Archivo" font-weight="700" font-size="22" letter-spacing="3" fill="${C.paper}">OFFICES</text>
<path d="M120 960 L120 900 Q120 880 140 880 L 700 880 Q 760 880 760 860 L 760 860 L 1060 840 L1060 760" fill="none" stroke="${C.paper}" stroke-width="12" stroke-dasharray="26 14"/>
<path d="M120 960 L120 900 Q120 880 140 880 L 700 880 Q 760 880 760 860 L 760 860 L 1060 840 L1060 760" fill="none" stroke="${C.red}" stroke-width="7" stroke-dasharray="26 14"/>
<circle cx="1060" cy="760" r="10" fill="${C.red}" stroke="${C.paper}" stroke-width="2"/>
<g><ellipse cx="400" cy="470" rx="22" ry="12" fill="${C.paper}"/><circle cx="400" cy="470" r="9" fill="${C.sheet}" stroke="${C.paper}" stroke-width="2"/><ellipse cx="470" cy="470" rx="22" ry="12" fill="${C.paper}"/><circle cx="470" cy="470" r="9" fill="${C.sheet}" stroke="${C.paper}" stroke-width="2"/></g><text x="435" y="515" text-anchor="middle" font-family="Archivo" font-size="18" letter-spacing="2" fill="${C.paper}">GUARD × 2</text>
<g stroke="${C.paper}" stroke-width="2" fill="${C.paper}"><circle cx="1330" cy="700" r="22" fill="none"/><line x1="1308" y1="706" x2="1075" y2="835"/></g>
<text x="1330" y="709" text-anchor="middle" font-family="Archivo" font-weight="700" font-size="24" fill="${C.paper}">1</text>
<text x="1370" y="709" font-family="Special Elite" font-size="26" fill="${C.paper}">TUNNEL, ILLUSTRATIVE ROUTE</text>
<line x1="220" y1="140" x2="1220" y2="140" stroke="${C.paper}" stroke-width="1.5"/><line x1="220" y1="128" x2="220" y2="152" stroke="${C.paper}" stroke-width="1.5"/><line x1="1220" y1="128" x2="1220" y2="152" stroke="${C.paper}" stroke-width="1.5"/>
<text x="720" y="128" text-anchor="middle" font-family="Archivo" font-size="22" fill="${C.paper}">FLOOR PLAN, NOT TO SCALE</text>
<rect x="1400" y="840" width="440" height="160" fill="none" stroke="${C.paper}" stroke-width="3"/>
<line x1="1400" y1="890" x2="1840" y2="890" stroke="${C.paper}" stroke-width="1.5"/><line x1="1400" y1="945" x2="1840" y2="945" stroke="${C.paper}" stroke-width="1.5"/>
<text x="1420" y="876" font-family="Alfa Slab One" font-size="24" fill="${C.paper}">THE BANK, GROUND FLOOR</text>
<text x="1420" y="928" font-family="Archivo" font-size="20" letter-spacing="2" fill="${C.paper}">SHEET 04 OF 06 · SAMPLE</text>
<text x="1420" y="982" font-family="Archivo" font-size="20" letter-spacing="2" fill="${C.paper}">DRAWN BY: THE COMPETITION</text>
<g transform="translate(1700,200)" fill="${C.paper}"><path d="M0 -60 L18 20 L0 8 L-18 20Z"/><text y="60" text-anchor="middle" font-family="Archivo" font-weight="700" font-size="28">N</text></g>
</svg>`;
const fonts='/mnt/project-files/pilot-bakeoff/shared/fonts/';
const fs=require('fs');const f64=n=>fs.readFileSync(fonts+n).toString('base64');const css=`@font-face{font-family:'Alfa Slab One';src:url(data:font/ttf;base64,${f64('AlfaSlabOne-Regular.ttf')})}@font-face{font-family:'Archivo';src:url(data:font/ttf;base64,${f64('Archivo-Variable.ttf')})}@font-face{font-family:'Special Elite';src:url(data:font/ttf;base64,${f64('SpecialElite-Regular.ttf')})}body{margin:0}`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
for(const [n,s] of [['isotype-ledger-sample',iso],['blueprint-sample',bp]]){await p.setContent(`<style>${css}</style>${s}`);await p.waitForTimeout(500);await p.screenshot({path:`/mnt/project-files/style/face-free-samples/${n}.png`});}
await b.close();})();
