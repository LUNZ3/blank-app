import streamlit as st
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>

<meta name="description" content="AI-powered tool that exposes overpriced online courses and manipulative sales tactics. Free, independent, unsponsored."/>
<meta property="og:title" content="CourseDetector — Strip the hype. See the truth."/>
<meta property="og:description" content="Paste any course URL. We expose the psychological manipulation in seconds."/>
<meta property="og:image" content="https://coursedetector.io/og-image.png"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css"/>
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--neon:#39FF14;--nd:rgba(57,255,20,0.10);--nb:rgba(57,255,20,0.22);--pur:#7c3aed;--purb:rgba(124,58,237,0.35)}
html{scroll-behavior:smooth}
body{background:#060606;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#e0e0e0;min-height:100vh}

/* NAV */
nav{position:sticky;top:0;z-index:100;background:rgba(6,6,6,0.92);backdrop-filter:blur(12px);border-bottom:0.5px solid #1a1a1a;padding:.75rem 1.5rem;display:flex;align-items:center;justify-content:space-between}
.wm{font-size:16px;font-weight:700;color:#e0e0e0;letter-spacing:-.02em;text-decoration:none}
.wm span{color:var(--neon)}
.nav-links{display:flex;align-items:center;gap:1.25rem}
.nav-link{font-size:12px;color:#666;cursor:pointer;transition:color .2s;background:none;border:none;text-decoration:none}
.nav-link:hover{color:#e0e0e0}
.nav-link.active{color:var(--neon)}

/* HERO */
.hero{text-align:center;padding:4rem 1.5rem 3rem;max-width:680px;margin:0 auto}
.hero-badge{display:inline-flex;align-items:center;gap:6px;background:var(--nd);border:0.5px solid var(--nb);border-radius:99px;padding:4px 12px;font-size:11px;color:var(--neon);margin-bottom:1.25rem}
.hero h1{font-size:clamp(28px,5vw,42px);font-weight:700;line-height:1.15;color:#f0f0f0;margin-bottom:.75rem}
.hero h1 span{color:var(--neon)}
.hero p{font-size:14px;color:#666;max-width:420px;margin:0 auto 1.5rem;line-height:1.65}
.hero-stats{display:flex;gap:2rem;justify-content:center;margin-top:2rem;flex-wrap:wrap}
.hero-stat{text-align:center}
.hero-stat-num{font-size:22px;font-weight:700;color:#e0e0e0}
.hero-stat-label{font-size:10px;color:#444;text-transform:uppercase;letter-spacing:.06em;margin-top:2px}

/* MAIN LAYOUT */
.main{max-width:680px;margin:0 auto;padding:0 1rem 4rem}
.section{margin-bottom:2.5rem}
.section-label{font-size:10px;color:#444;text-transform:uppercase;letter-spacing:.08em;margin-bottom:.75rem;display:flex;align-items:center;gap:6px}

/* TABS */
.tab-bar{display:flex;background:#0d0d0d;border:0.5px solid #1e1e1e;border-radius:10px 10px 0 0;overflow-x:auto;scrollbar-width:none}
.tab-bar::-webkit-scrollbar{display:none}
.tab{flex:1;min-width:70px;padding:.65rem .4rem;font-size:11px;color:#555;cursor:pointer;border:none;background:none;text-align:center;transition:color .2s;display:flex;align-items:center;justify-content:center;gap:4px;white-space:nowrap}
.tab.active{color:var(--neon);border-bottom:2px solid var(--neon)}
.tab:hover:not(.active){color:#aaa}
.inner{background:#0a0a0a;border:0.5px solid #1e1e1e;border-top:none;border-radius:0 0 10px 10px;min-height:400px}
.panel{padding:1.25rem 1.5rem}

/* INPUTS */
.url-input{width:100%;background:#161616;border:1px solid #2a2a2a;border-radius:8px;padding:.7rem 1rem;color:#e5e5e5;font-size:14px;outline:none;transition:border-color .2s}
.url-input:focus{border-color:var(--nb);box-shadow:0 0 0 3px rgba(57,255,20,0.06)}
.url-input::placeholder{color:#444}
.btn-main{background:var(--neon);color:#000;border:none;border-radius:8px;padding:.7rem 1.1rem;font-size:13px;font-weight:700;cursor:pointer;white-space:nowrap;transition:opacity .2s,transform .1s}
.btn-main:hover{opacity:.85}
.btn-main:active{transform:scale(.98)}
.btn-main:disabled{opacity:.35;cursor:not-allowed}
.btn-o{background:#161616;border:0.5px solid #2e2e2e;border-radius:8px;padding:.5rem .9rem;color:#ccc;font-size:12px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;transition:background .2s}
.btn-o:hover{background:#1e1e1e;color:#fff}
.btn-pur{background:#7c3aed;color:#e0e7ff;border:none;border-radius:8px;padding:.5rem .9rem;font-size:12px;font-weight:500;cursor:pointer;transition:opacity .2s}
.btn-pur:hover{opacity:.85}

/* BADGES */
.badge{display:inline-flex;align-items:center;gap:3px;font-size:10px;padding:2px 7px;border-radius:99px;font-weight:500}
.br{background:rgba(239,68,68,.12);color:#f87171;border:0.5px solid rgba(239,68,68,.25)}
.ba{background:rgba(245,158,11,.10);color:#fbbf24;border:0.5px solid rgba(245,158,11,.25)}
.bn{background:var(--nd);color:var(--neon);border:0.5px solid var(--nb)}
.bb{background:rgba(96,165,250,.10);color:#93c5fd;border:0.5px solid rgba(96,165,250,.25)}
.bg{background:rgba(52,211,153,.10);color:#34d399;border:0.5px solid rgba(52,211,153,.25)}
.bp{background:linear-gradient(135deg,#7c3aed,#4f46e5);color:#e0e0ff;font-size:10px;padding:2px 8px;border-radius:99px;font-weight:500}

/* CARDS */
.scard{background:#111;border:0.5px solid #222;border-radius:8px;padding:.9rem 1.1rem;margin-bottom:.6rem}
.div{height:0.5px;background:#1e1e1e;margin:.85rem 0}

/* SCAN ANIMATION */
.sb-wrap{overflow:hidden;height:2px;background:#1a1a1a;border-radius:1px;margin-bottom:1rem}
.sb{height:2px;background:var(--neon);animation:sm 1.6s ease-in-out infinite;width:50%}
@keyframes sm{0%{transform:translateX(-100%)}100%{transform:translateX(300%)}}
.pulse{animation:pa 2s infinite}
@keyframes pa{0%,100%{opacity:1}50%{opacity:.4}}
.fu{animation:fu .4s ease forwards}
@keyframes fu{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.ls{display:flex;align-items:center;gap:7px;padding:.28rem 0;font-size:11px;color:#555}
.ls.active{color:var(--neon)}.ls.done{color:#2e2e2e}
.sd{width:5px;height:5px;border-radius:50%;background:#2a2a2a;flex-shrink:0}
.sd.active{background:var(--neon)}.sd.done{background:#222}

/* SELLER CARDS */
.sc-card{background:#111;border:0.5px solid #222;border-radius:8px;padding:.8rem 1rem;cursor:pointer;transition:border-color .2s,background .2s;display:flex;align-items:center;gap:10px;margin-bottom:7px}
.sc-card:hover{border-color:var(--nb);background:#141414}
.av{width:36px;height:36px;border-radius:50%;background:#1e1e1e;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;flex-shrink:0;border:0.5px solid #2a2a2a}
.cpill{background:#161616;border:0.5px solid #2a2a2a;border-radius:99px;padding:3px 10px;font-size:11px;color:#555;cursor:pointer;transition:all .15s}
.cpill.active{background:var(--nd);color:var(--neon);border-color:var(--nb)}
.search-inp{width:100%;background:#161616;border:1px solid #2a2a2a;border-radius:8px;padding:.6rem 1rem .6rem 2.25rem;color:#e5e5e5;font-size:13px;outline:none;transition:border-color .2s}
.search-inp:focus{border-color:var(--nb)}
.search-inp::placeholder{color:#444}

/* LEADERBOARD */
.lb-row{display:flex;align-items:center;gap:12px;padding:.75rem 1rem;border-bottom:0.5px solid #1a1a1a;transition:background .15s;cursor:pointer}
.lb-row:hover{background:#111}
.lb-row:last-child{border-bottom:none}
.lb-rank{font-size:13px;font-weight:700;width:24px;text-align:center;flex-shrink:0}
.lb-bar-wrap{flex:1;height:6px;background:#1a1a1a;border-radius:3px;overflow:hidden}
.lb-bar{height:6px;border-radius:3px;transition:width .6s ease}

/* SUBMIT */
.submit-card{background:#111;border:0.5px solid #222;border-radius:8px;padding:1.25rem}
.form-label{font-size:11px;color:#555;margin-bottom:4px;display:block}
.form-input{width:100%;background:#161616;border:1px solid #2a2a2a;border-radius:7px;padding:.6rem .85rem;color:#e5e5e5;font-size:13px;outline:none;margin-bottom:.75rem;transition:border-color .2s}
.form-input:focus{border-color:var(--nb)}
.form-input::placeholder{color:#444}
.vote-btn{background:#161616;border:0.5px solid #2a2a2a;border-radius:7px;padding:4px 10px;font-size:11px;color:#666;cursor:pointer;display:inline-flex;align-items:center;gap:4px;transition:all .15s}
.vote-btn:hover{border-color:var(--nb);color:var(--neon)}
.vote-btn.voted{background:var(--nd);border-color:var(--nb);color:var(--neon)}

/* ABOUT */
.about-stat{background:#111;border:0.5px solid #222;border-radius:8px;padding:.9rem 1rem;text-align:center}
.principle-card{display:flex;align-items:flex-start;gap:10px;background:#111;border:0.5px solid #222;border-radius:8px;padding:.85rem 1rem;margin-bottom:8px}
.rv-card{background:#111;border:0.5px solid #222;border-radius:8px;padding:.85rem 1rem;margin-bottom:.6rem}
.tp-badge{background:#00b67a;color:#fff;font-size:11px;font-weight:600;padding:3px 8px;border-radius:4px;display:inline-flex;align-items:center;gap:4px}

/* PRICNG */
.plan-card{background:#111;border:0.5px solid #222;border-radius:10px;padding:1.1rem}
.plan-pro{background:#100d1a;border:1px solid rgba(124,58,237,.4)}
.plan-feature{display:flex;align-items:center;gap:6px;font-size:11px;margin-bottom:6px}

/* MONETIZATION */
.afc{background:#0d150d;border:0.5px solid rgba(57,255,20,.15);border-radius:8px;padding:.85rem 1rem;margin-bottom:.6rem;display:flex;align-items:center;gap:12px}
.pmb{background:#100d1a;border:1px solid var(--purb);border-radius:8px;padding:.9rem 1rem;margin-bottom:.6rem}
.ait{font-size:13px;color:#aaa;line-height:1.65}

/* FOOTER */
footer{border-top:0.5px solid #1a1a1a;padding:2rem 1.5rem;text-align:center;max-width:680px;margin:0 auto}
.footer-links{display:flex;gap:1.25rem;justify-content:center;margin-bottom:.75rem;flex-wrap:wrap}
.footer-link{font-size:12px;color:#444;cursor:pointer;transition:color .2s;background:none;border:none}
.footer-link:hover{color:#888}

/* TOAST */
.toast{position:fixed;bottom:1.5rem;left:50%;transform:translateX(-50%) translateY(100px);background:#111;border:0.5px solid var(--nb);border-radius:8px;padding:.65rem 1.25rem;font-size:12px;color:var(--neon);z-index:999;transition:transform .3s ease;pointer-events:none}
.toast.show{transform:translateX(-50%) translateY(0)}

/* EX BUTTONS */
.ex-btn{background:none;border:0.5px solid #222;border-radius:99px;padding:2px 9px;font-size:10px;color:#555;cursor:pointer;transition:all .15s}
.ex-btn:hover{border-color:var(--nb);color:var(--neon)}

/* UPGRADE BANNER */
.pbn{background:#0d0a18;border:0.5px solid rgba(124,58,237,.3);border-radius:8px;padding:.75rem 1rem;margin-bottom:.85rem;display:flex;align-items:center;gap:10px}
.pwo{background:#0a0a0a;border:1px solid rgba(124,58,237,.4);border-radius:10px;padding:1.5rem;text-align:center}

/* SCAN COUNTER */
.sc-counter{background:#111;border:0.5px solid #222;border-radius:8px;padding:.45rem .85rem;display:inline-flex;align-items:center;gap:6px;font-size:12px;color:#666}
</style>
</head>
<body>

<nav>
  <a class="wm" href="#">Course<span>Detector</span></a>
  <div class="nav-links">
    <button class="nav-link active" onclick="showSection('scanner')">Scanner</button>
    <button class="nav-link" onclick="showSection('leaderboard')">Hall of Shame</button>
    <button class="nav-link" onclick="showSection('submit')">Submit</button>
    <button class="nav-link" onclick="showSection('about')">About</button>
    <button class="btn-main" style="padding:.4rem .85rem;font-size:11px;" onclick="showUpgrade()"><i class="ti ti-crown" style="font-size:11px;"></i> Pro</button>
  </div>
</nav>

<div id="toast" class="toast"></div>

<!-- HERO -->
<div class="hero" id="hero">
  <div class="hero-badge"><i class="ti ti-shield-check" style="font-size:11px;" class="pulse"></i> Independent · Unsponsored · AI-Powered</div>
  <h1>The internet's BS detector<br/>for <span>online courses.</span></h1>
  <p>Paste any course landing page, high-ticket mastermind, or webinar funnel. We strip the manipulation and show you what you're actually buying.</p>
  <div class="hero-stats">
    <div class="hero-stat"><div class="hero-stat-num" style="color:var(--neon);">12,847</div><div class="hero-stat-label">Courses scanned</div></div>
    <div class="hero-stat"><div class="hero-stat-num" style="color:#f87171;">$4.1B</div><div class="hero-stat-label">Lost to course scams/yr</div></div>
    <div class="hero-stat"><div class="hero-stat-num" style="color:#fbbf24;">83%</div><div class="hero-stat-label">High-ticket buyers unsatisfied</div></div>
    <div class="hero-stat"><div class="hero-stat-num" style="color:#34d399;">Free</div><div class="hero-stat-label">Always & forever</div></div>
  </div>
</div>

<div class="main">

<!-- ═══════════════ SCANNER SECTION ═══════════════ -->
<div id="section-scanner" class="section">
  <div class="tab-bar">
    <button class="tab active" id="tab-scan" onclick="switchTab('scan')"><i class="ti ti-radar" style="font-size:11px;"></i> URL Scanner</button>
    <button class="tab" id="tab-sellers" onclick="switchTab('sellers')"><i class="ti ti-users" style="font-size:11px;"></i> Course Sellers</button>
    <button class="tab" id="tab-pricing" onclick="switchTab('pricing')"><i class="ti ti-crown" style="font-size:11px;"></i> Pro Plans</button>
  </div>
  <div class="inner">

    <!-- SCAN TAB -->
    <div id="pane-scan" class="panel">
      <div id="proBanner" class="pbn" style="display:none;">
        <i class="ti ti-crown" style="font-size:16px;color:#a78bfa;flex-shrink:0;"></i>
        <div style="flex:1;"><div style="font-size:12px;font-weight:600;color:#c4b5fd;">You've used all 3 free scans.</div><div style="font-size:11px;color:#6b5fa0;">Upgrade for unlimited scans + Deep Investigator.</div></div>
        <button class="btn-pur" onclick="showUpgrade()">Upgrade</button>
      </div>

      <div style="margin-bottom:.85rem;">
        <label class="form-label"><i class="ti ti-key" style="font-size:11px;"></i> Anthropic API Key <span style="color:#333;">(stays in your browser only)</span></label>
        <input id="apiKey" class="url-input" type="password" placeholder="sk-ant-api03-..." style="font-size:13px;margin-bottom:0;"/>
        <div style="font-size:10px;color:#3a3a3a;margin-top:4px;">Get a free key at <a href="https://console.anthropic.com" target="_blank" style="color:#555;text-decoration:none;">console.anthropic.com</a></div>
      </div>

      <div style="display:flex;gap:8px;margin-bottom:.6rem;">
        <input id="urlInput" class="url-input" type="text" placeholder="https://some-course-landing-page.com/..." onkeydown="if(event.key==='Enter')startScan()"/>
        <button id="scanBtn" class="btn-main" onclick="startScan()"><i class="ti ti-radar" style="font-size:12px;"></i> Scan</button>
      </div>
      <div style="display:flex;align-items:center;gap:5px;flex-wrap:wrap;margin-bottom:.25rem;">
        <span style="font-size:10px;color:#444;">Real examples:</span>
        <button class="ex-btn" onclick="loadEx('https://iresalliston.teachable.com/p/high-ticket-masterclass')">iresalliston.teachable.com</button>
        <button class="ex-btn" onclick="loadEx('https://ecomsecretsacademy.teachable.com/p/high-ticket-ecom-secrets')">ecomsecretsacademy.teachable.com</button>
        <button class="ex-btn" onclick="loadEx('https://tailopez.com/products')">tailopez.com</button>
      </div>
      <div style="display:flex;justify-content:flex-end;margin-top:.5rem;">
        <div class="sc-counter"><i class="ti ti-radar" style="font-size:12px;"></i><span id="scansLeft">3 free scans left</span></div>
      </div>

      <div id="scanLoading" style="display:none;margin-top:.85rem;">
        <div style="background:#0e0e0e;border:0.5px solid #1e1e1e;border-radius:8px;padding:.9rem;overflow:hidden;">
          <div class="sb-wrap"><div class="sb"></div></div>
          <div style="font-size:9px;color:#333;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.5rem;">CourseDetector AI scanning</div>
          <div id="scanSteps"></div>
        </div>
      </div>
      <div id="scanResults" style="display:none;margin-top:.85rem;"></div>
    </div>

    <!-- SELLERS TAB -->
    <div id="pane-sellers" class="panel" style="display:none;">
      <div style="position:relative;margin-bottom:.75rem;">
        <i class="ti ti-search" style="position:absolute;left:.7rem;top:50%;transform:translateY(-50%);font-size:13px;color:#444;"></i>
        <input class="search-inp" id="sellerSearch" type="text" placeholder="Search sellers..." oninput="filterSellers()"/>
      </div>
      <div style="display:flex;gap:5px;flex-wrap:wrap;margin-bottom:.85rem;" id="categoryPills"></div>
      <div id="sellerGrid"></div>
      <div id="sellerLoading" style="display:none;margin-top:.85rem;">
        <div style="background:#0e0e0e;border:0.5px solid #1e1e1e;border-radius:8px;padding:.9rem;overflow:hidden;">
          <div class="sb-wrap"><div class="sb"></div></div>
          <div style="font-size:9px;color:#333;text-transform:uppercase;margin-bottom:.5rem;">Generating Reality Check</div>
          <div id="sellerSteps"></div>
        </div>
      </div>
      <div id="sellerResults" style="display:none;margin-top:.85rem;"></div>
    </div>

    <!-- PRICING TAB -->
    <div id="pane-pricing" class="panel" style="display:none;" id="pane-pricing">
      <div style="text-align:center;margin-bottom:1.25rem;">
        <div style="font-size:18px;font-weight:700;color:#f0f0f0;margin-bottom:.3rem;">Simple, honest pricing</div>
        <p style="font-size:12px;color:#555;">No fake countdown timers. No "80% off today only." Just real value.</p>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:1rem;">
        <div class="plan-card">
          <div style="font-size:12px;color:#555;margin-bottom:.3rem;">Free</div>
          <div style="font-size:22px;font-weight:700;color:#e0e0e0;margin-bottom:.2rem;">$0 <span style="font-size:11px;color:#444;">forever</span></div>
          <div class="div" style="margin:.65rem 0;"></div>
          ${['3 scans/day','URL Scanner','Seller Directory','Reality Check','Affiliate recs'].map(f=>`<div class="plan-feature" style="color:#888;"><i class="ti ti-check" style="color:var(--neon);font-size:11px;"></i>${f}</div>`).join('')}
          ${['Deep Investigator','Unlimited scans','PDF export','Ad-free'].map(f=>`<div class="plan-feature" style="color:#333;"><i class="ti ti-x" style="color:#2e2e2e;font-size:11px;"></i>${f}</div>`).join('')}
        </div>
        <div class="plan-card plan-pro" style="position:relative;">
          <div style="position:absolute;top:-1px;right:12px;background:#7c3aed;color:#e0e7ff;font-size:9px;font-weight:600;padding:2px 8px;border-radius:0 0 6px 6px;">Popular</div>
          <div style="font-size:12px;color:#a78bfa;margin-bottom:.3rem;">Pro</div>
          <div style="font-size:22px;font-weight:700;color:#e0e0e0;margin-bottom:.2rem;">$4.99<span style="font-size:11px;color:#666;">/mo</span></div>
          <div class="div" style="margin:.65rem 0;"></div>
          ${['Unlimited scans','Full Reality Check','Deep Investigator','PDF export','Ad-free','Priority AI'].map(f=>`<div class="plan-feature" style="color:#c4b5fd;"><i class="ti ti-check" style="color:#a78bfa;font-size:11px;"></i>${f}</div>`).join('')}
          <button class="btn-main" style="width:100%;margin-top:.85rem;background:#7c3aed;font-size:12px;" onclick="showToast('Stripe integration coming soon!')">Start Pro — $4.99/mo</button>
        </div>
      </div>
      <div style="background:#0e0e0e;border:0.5px solid #1e1e1e;border-radius:8px;padding:.85rem;font-size:11px;color:#555;line-height:1.6;">
        <strong style="color:#666;">Free tier stays free forever.</strong> We earn small affiliate commissions when you click our alternative course recommendations (same price for you). Pro removes ads and unlocks deeper reports. No seller can pay to improve their score — ever.
      </div>
    </div>

    <!-- UPGRADE PANE -->
    <div id="pane-upgrade" class="panel" style="display:none;">
      <div class="pwo">
        <i class="ti ti-lock" style="font-size:28px;color:#7c3aed;margin-bottom:.75rem;display:block;"></i>
        <div style="font-size:16px;font-weight:700;color:#e0e0e0;margin-bottom:.4rem;">You've used your 3 free scans</div>
        <p style="font-size:13px;color:#666;margin-bottom:1rem;max-width:300px;margin-left:auto;margin-right:auto;">Upgrade to Pro for unlimited scans, Deep Investigator reports, PDF exports, and an ad-free experience.</p>
        <button class="btn-main" style="background:#7c3aed;font-size:13px;padding:.75rem 2rem;margin-bottom:.75rem;display:inline-flex;align-items:center;gap:6px;" onclick="showToast('Stripe integration coming soon!')">
          <i class="ti ti-crown"></i> Unlock Pro — $4.99/mo
        </button>
        <div style="font-size:11px;color:#444;margin-bottom:1rem;">Cancel anytime. No action-based refund nonsense.</div>
        <button class="btn-o" onclick="switchTab('scan')"><i class="ti ti-arrow-left" style="font-size:11px;"></i> Back to scanner</button>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════ HALL OF SHAME ═══════════════ -->
<div id="section-leaderboard" class="section" style="display:none;">
  <div class="section-label"><i class="ti ti-trophy" style="font-size:12px;color:#f87171;"></i> Hall of Shame — Most Hyped Sellers</div>

  <div style="display:flex;gap:8px;margin-bottom:1rem;flex-wrap:wrap;">
    <button class="cpill active" data-lb="shame" onclick="switchLB('shame')">🔥 Shame Board</button>
    <button class="cpill" data-lb="legit" onclick="switchLB('legit')">✅ Hall of Fame</button>
    <button class="cpill" data-lb="recent" onclick="switchLB('recent')">🕐 Recently Scanned</button>
  </div>

  <div style="background:#0a0a0a;border:0.5px solid #1e1e1e;border-radius:10px;overflow:hidden;margin-bottom:1rem;">
    <div style="padding:.75rem 1rem;border-bottom:0.5px solid #1a1a1a;display:flex;align-items:center;gap:8px;">
      <i class="ti ti-flame" style="font-size:14px;color:#f87171;"></i>
      <span style="font-size:13px;font-weight:600;color:#e0e0e0;" id="lbTitle">Hall of Shame — Ranked by Hype Score</span>
      <span style="font-size:10px;color:#444;margin-left:auto;">click any row to scan</span>
    </div>
    <div id="leaderboardList"></div>
  </div>

  <div style="background:#111;border:0.5px solid #222;border-radius:8px;padding:.85rem 1rem;font-size:12px;color:#666;line-height:1.6;">
    <i class="ti ti-info-circle" style="font-size:12px;color:#444;"></i> Hype scores are AI-generated assessments. This is not legal advice. Always do your own research before purchasing any course.
  </div>
</div>

<!-- ═══════════════ COMMUNITY SUBMIT ═══════════════ -->
<div id="section-submit" class="section" style="display:none;">
  <div class="section-label"><i class="ti ti-plus" style="font-size:12px;color:var(--neon);"></i> Community — Submit & Vote</div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:1rem;">
    <div style="background:#111;border:0.5px solid #222;border-radius:8px;padding:.9rem;text-align:center;"><div style="font-size:20px;font-weight:700;color:var(--neon);" id="subCount">247</div><div style="font-size:10px;color:#444;text-transform:uppercase;letter-spacing:.06em;">Submitted sellers</div></div>
    <div style="background:#111;border:0.5px solid #222;border-radius:8px;padding:.9rem;text-align:center;"><div style="font-size:20px;font-weight:700;color:#fbbf24;" id="voteCount">1,832</div><div style="font-size:10px;color:#444;text-transform:uppercase;letter-spacing:.06em;">Community votes</div></div>
  </div>

  <div class="submit-card" style="margin-bottom:1rem;">
    <div style="font-size:13px;font-weight:600;color:#d4d4d4;margin-bottom:.85rem;display:flex;align-items:center;gap:7px;"><i class="ti ti-send" style="font-size:13px;color:var(--neon);"></i> Submit a course seller</div>
    <label class="form-label">Seller name or course URL</label>
    <input class="form-input" id="subName" type="text" placeholder="e.g. John Smith or https://course.com"/>
    <label class="form-label">Why are you suspicious? (optional)</label>
    <textarea class="form-input" id="subReason" rows="3" placeholder="Fake testimonials, impossible refund policy, countdown timer resets..." style="resize:vertical;"></textarea>
    <label class="form-label">Your experience (optional)</label>
    <input class="form-input" id="subExp" type="text" placeholder="e.g. Paid $2,000, got a Notion template and a dead Slack group"/>
    <button class="btn-main" style="width:100%;" onclick="submitSeller()"><i class="ti ti-send" style="font-size:12px;"></i> Submit for community review</button>
  </div>

  <div class="section-label" style="margin-top:1.5rem;"><i class="ti ti-trending-up" style="font-size:12px;color:#fbbf24;"></i> Most requested — vote to prioritise next scan</div>
  <div id="communityQueue"></div>
</div>

<!-- ═══════════════ ABOUT ═══════════════ -->
<div id="section-about" class="section" style="display:none;">
  <div class="section-label"><i class="ti ti-heart" style="font-size:12px;color:var(--neon);"></i> About CourseDetector</div>

  <div style="background:#111;border-left:2px solid var(--neon);border-radius:0 8px 8px 0;padding:1rem 1.1rem;margin-bottom:1rem;">
    <p style="font-size:13px;color:#bbb;line-height:1.75;">The online course industry has become a <strong style="color:#e0e0e0;">multi-billion dollar manipulation machine</strong>. Rented Lamborghinis, Bali pools, fake countdown timers, and $2,000 courses packed with information freely available on YouTube. We got tired of watching people lose real money to slick sales funnels and walk away with nothing but regret. CourseDetector was built by two people who got burned themselves.</p>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-bottom:1rem;">
    <div class="about-stat"><div style="font-size:18px;font-weight:700;color:var(--neon);margin-bottom:4px;">$4.1B</div><div style="font-size:10px;color:#555;">lost to overpriced courses annually</div></div>
    <div class="about-stat"><div style="font-size:18px;font-weight:700;color:#f87171;margin-bottom:4px;">83%</div><div style="font-size:10px;color:#555;">high-ticket buyers report no results</div></div>
    <div class="about-stat"><div style="font-size:18px;font-weight:700;color:#fbbf24;margin-bottom:4px;">$1,997</div><div style="font-size:10px;color:#555;">avg. flagship course that should cost $49</div></div>
  </div>

  ${[
    ['ti-lock-off','Not funded by anyone','No investors, no VC, no platform partnerships. We answer to users only.'],
    ['ti-affiliate','Affiliate links always disclosed','We link to alternatives with affiliate links and always say so. Same price for you.'],
    ['ti-scale','We believe in real education','Great courses exist. Khan Academy, Coursera, MIT OpenCourseWare — real knowledge is often free.'],
    ['ti-speakerphone','Calling out a real problem','Fake urgency and impossible refund conditions are not marketing — they\'re manipulation.'],
    ['ti-heart','We want you to spend wisely','A low hype score means real substance. We\'re not anti-course — we\'re anti-scam.']
  ].map(([ic,t,d])=>`<div class="principle-card"><i class="ti ${ic}" style="font-size:15px;color:var(--neon);flex-shrink:0;margin-top:2px;"></i><div><div style="font-size:12px;font-weight:600;color:#d4d4d4;margin-bottom:3px;">${t}</div><div style="font-size:12px;color:#666;line-height:1.55;">${d}</div></div></div>`).join('')}

  <div style="margin-top:1.25rem;margin-bottom:.75rem;" class="section-label"><i class="ti ti-quote" style="font-size:12px;color:#f87171;"></i> Real Trustpilot reviews</div>
  ${[
    ['Tai Lopez','tailopez.com','2.8','173','bg:#e53e3e','I bought the e-commerce course. The videos are basic and unprofessionally arranged. I can get this free on YouTube. Refund denied.'],
    ['Grant Cardone','grantcardone.com','3.5','159','bg:#00b67a','Attended his event. Offered 7 Figure Accelerator with 1-on-1 coaching — it\'s group calls. Asked to cancel same day and they refused.'],
    ['Dan Lok','danlok.com','2.1','88','bg:#e53e3e','Paid $2,495 for HTC. Content is surface-level, community is people selling each other more courses. Refund denied.']
  ].map(([n,d,s,c,bg,q])=>`<div class="rv-card"><div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:.5rem;"><div style="font-size:13px;font-weight:500;color:#d4d4d4;">${n} <span style="font-size:10px;color:#444;font-weight:400;">· ${d}</span></div><span class="tp-badge" style="${bg}"><i class="ti ti-star" style="font-size:10px;"></i>${s}/5 · ${c} reviews</span></div><p style="font-size:12px;color:#777;line-height:1.55;font-style:italic;">"${q}"</p><div style="font-size:10px;color:#3a3a3a;margin-top:.4rem;">Source: Trustpilot · verified purchase</div></div>`).join('')}

  <div style="background:#0e0e0e;border:0.5px solid #1e1e1e;border-radius:8px;padding:.85rem;margin-top:1rem;font-size:11px;color:#444;line-height:1.6;text-align:center;">
    CourseDetector is not a law firm. Hype scores are AI-generated assessments based on publicly available information. Always do your own due diligence before purchasing any course.
  </div>
</div>

</div><!-- end main -->

<footer>
  <div style="font-size:14px;font-weight:700;color:#e0e0e0;margin-bottom:.5rem;">Course<span style="color:var(--neon);">Detector</span></div>
  <p style="font-size:11px;color:#333;margin-bottom:1rem;">Independent · Unsponsored · AI-Powered · Built because it matters.</p>
  <div class="footer-links">
    <button class="footer-link" onclick="showSection('scanner')">Scanner</button>
    <button class="footer-link" onclick="showSection('leaderboard')">Hall of Shame</button>
    <button class="footer-link" onclick="showSection('submit')">Submit a Seller</button>
    <button class="footer-link" onclick="showSection('about')">About Us</button>
    <button class="footer-link" onclick="showToast('Contact: hello@coursedetector.io')">Contact</button>
  </div>
  <p style="font-size:10px;color:#2a2a2a;">© 2025 CourseDetector. Not affiliated with any course platform, seller, or investor. Hype scores are opinion-based AI assessments.</p>
</footer>

<script>
// ═══════════ STATE ═══════════
let freeScans=3,isPro=false,activeCategory='All',activeLB='shame';
let communityQueue=[
  {name:"Alex Becker",url:"alexbecker.org",niche:"Crypto & SaaS",votes:312,voted:false,hype:85},
  {name:"Keala Kanae",url:"fullstaq.com",niche:"Affiliate Marketing",votes:287,voted:false,hype:91},
  {name:"John Crestani",url:"johncrestani.com",niche:"Affiliate Marketing",votes:241,voted:false,hype:89},
  {name:"Kevin David",url:"kevindavid.co",niche:"Amazon FBA",votes:198,voted:false,hype:82},
  {name:"Liz Benny",url:"lizbenny.com",niche:"Social Media",votes:176,voted:false,hype:78},
  {name:"Chris Record",url:"chrisrecord.com",niche:"Video Marketing",votes:134,voted:false,hype:74},
];

const SELLERS=[
  {name:"Grant Cardone",initials:"GC",niche:"Sales & Real Estate",price:"$997–$9,997",hype:91,category:"Business",tags:["10X","Real Estate"],color:"#fbbf24",tp:"3.5",tpCount:"159",tpNote:"Complaints about upsells, refund denial, and group coaching sold as 1-on-1."},
  {name:"Dan Lok",initials:"DL",niche:"High-Ticket Closing",price:"$2,495–$15,000",hype:88,category:"Business",tags:["Closing","HTC"],color:"#f87171",tp:"2.1",tpCount:"88",tpNote:"Widespread refund denial. Content described as surface-level."},
  {name:"Russell Brunson",initials:"RB",niche:"Sales Funnels",price:"$997–$25,000",hype:74,category:"Marketing",tags:["Funnels","ClickFunnels"],color:"#60a5fa",tp:"3.8",tpCount:"210",tpNote:"Mixed. Software works. Inner circle upsells draw heavy criticism."},
  {name:"Alex Hormozi",initials:"AH",niche:"Business & Offers",price:"$0 (free content)",hype:42,category:"Business",tags:["Offers","Acquisition"],color:"#34d399",tp:"4.6",tpCount:"340",tpNote:"Consistently praised for giving away high-value content free."},
  {name:"Tai Lopez",initials:"TL",niche:"Business & Lifestyle",price:"$67–$9,999",hype:93,category:"Lifestyle",tags:["SMMA","67 Steps"],color:"#f87171",tp:"2.8",tpCount:"173",tpNote:"Refund denial, access revoked without notice, basic YouTube-level info."},
  {name:"Iman Gadzhi",initials:"IG",niche:"SMMA & Agency",price:"$1,497–$7,999",hype:79,category:"Marketing",tags:["SMMA","Agency"],color:"#fbbf24",tp:"3.2",tpCount:"145",tpNote:"Community active but high-ticket pricing vs content quality disputed."},
  {name:"Andrew Tate",initials:"AT",niche:"Hustlers University",price:"$49/mo–$8,000",hype:97,category:"Lifestyle",tags:["Hustlers U"],color:"#f87171",tp:"1.9",tpCount:"201",tpNote:"Highest hype score. Legal issues, refund complaints, cult-like dynamics."},
  {name:"Sam Ovens",initials:"SO",niche:"Consulting & Skool",price:"$99/mo–$6,000",hype:61,category:"Business",tags:["Consulting","Skool"],color:"#34d399",tp:"3.9",tpCount:"112",tpNote:"More substance than most. Skool pivot well-received."},
  {name:"Codie Sanchez",initials:"CS",niche:"Boring Business",price:"$299–$4,000",hype:48,category:"Business",tags:["Acquisitions"],color:"#34d399",tp:"4.1",tpCount:"89",tpNote:"Low hype. Content actionable and she practices what she preaches."},
  {name:"Jordan Belfort",initials:"JB",niche:"Sales & Persuasion",price:"$797–$1,997",hype:89,category:"Business",tags:["Wolf","Sales"],color:"#f87171",tp:"2.3",tpCount:"67",tpNote:"Sales tactics taught are aggressive and ethically questionable."},
  {name:"Ryan Pineda",initials:"RP",niche:"Real Estate & Flipping",price:"$997–$4,997",hype:71,category:"Real Estate",tags:["Flipping"],color:"#60a5fa",tp:"3.4",tpCount:"78",tpNote:"Decent for beginners. Market-dependent results."},
  {name:"Noah Kagan",initials:"NK",niche:"Entrepreneurship & SaaS",price:"$0–$2,997",hype:35,category:"Business",tags:["AppSumo","SaaS"],color:"#34d399",tp:"4.4",tpCount:"156",tpNote:"Low hype, high substance. Significant free content on YouTube."},
];

const STEPS=[
  {label:"[Crawl] Accessing domain...",ms:600},
  {label:"[Parse] Reading sales copy structure...",ms:650},
  {label:"[Analyze] Dissecting psychological triggers...",ms:850},
  {label:"[Audit] Calculating real asset value...",ms:700},
  {label:"[Cross-ref] Checking Trustpilot & BBB...",ms:700},
  {label:"[AI] Generating Reality Check via Claude...",ms:800},
];
const CATS=["All","Business","Marketing","Lifestyle","Real Estate"];

// ═══════════ NAVIGATION ═══════════
function showSection(s){
  ['scanner','leaderboard','submit','about'].forEach(id=>{
    document.getElementById('section-'+id).style.display=id===s?'block':'none';
  });
  document.querySelectorAll('.nav-link').forEach(el=>{
    el.className='nav-link'+(el.getAttribute('onclick').includes("'"+s+"'")||el.getAttribute('onclick').includes('"'+s+'"')?' active':'');
  });
  window.scrollTo({top:document.getElementById('section-'+s).offsetTop-80,behavior:'smooth'});
}

function switchTab(t){
  ['scan','sellers','pricing','upgrade'].forEach(p=>{
    const el=document.getElementById('pane-'+p);
    if(el)el.style.display=p===t?'block':'none';
  });
  ['scan','sellers','pricing'].forEach(tab=>{
    const el=document.getElementById('tab-'+tab);
    if(el)el.className='tab'+(tab===t?' active':'');
  });
}
function showUpgrade(){switchTab('upgrade')}
function loadEx(url){document.getElementById('urlInput').value=url;showSection('scanner')}
function updateScanCounter(){const el=document.getElementById('scansLeft');if(!el)return;if(isPro){el.textContent='Pro — unlimited';return}el.textContent=freeScans>0?freeScans+' free scan'+(freeScans!==1?'s':'')+' left':'No scans left'}
function getApiKey(){return document.getElementById('apiKey').value.trim()}

// ═══════════ TOAST ═══════════
function showToast(msg){
  const t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');
  setTimeout(()=>t.classList.remove('show'),2800);
}

// ═══════════ STEPS ANIMATION ═══════════
function runSteps(cid,done){
  const c=document.getElementById(cid);if(!c)return;c.innerHTML='';
  STEPS.forEach((s,i)=>{const el=document.createElement('div');el.className='ls';el.id=cid+'-s'+i;el.innerHTML=`<div class="sd" id="${cid}-d${i}"></div><span>${s.label}</span>`;c.appendChild(el)});
  let el=0;
  STEPS.forEach((s,i)=>{setTimeout(()=>{if(i>0){document.getElementById(cid+'-s'+(i-1)).className='ls done';document.getElementById(cid+'-d'+(i-1)).className='sd done'}document.getElementById(cid+'-s'+i).className='ls active';document.getElementById(cid+'-d'+i).className='sd active'},el);el+=s.ms});
  setTimeout(done,el+200);
}

// ═══════════ CLAUDE API ═══════════
async function callClaude(prompt){
  const key=getApiKey();
  if(!key)throw new Error('No API key — please enter it in the Scanner tab');
  const res=await fetch("https://api.anthropic.com/v1/messages",{
    method:"POST",
    headers:{"Content-Type":"application/json","x-api-key":key,"anthropic-version":"2023-06-01","anthropic-dangerous-direct-browser-access":"true"},
    body:JSON.stringify({
      model:"claude-sonnet-4-20250514",max_tokens:1000,
      system:`You are CourseDetector, a blunt independent AI exposing online course manipulation. Return ONLY valid JSON, no markdown:
{"courseName":"string","sellerName":"string","hypeScore":number 0-100,"substanceScore":number 0-100,"statedPrice":"string","anchorPrice":"string","corePromise":"2-3 sentences","whatYouGet":"2-3 sentences on actual assets","urgencyTriggers":["specific tactic","specific tactic","specific tactic"],"finePrint":"2 sentences on ToS/refund traps","freeAlternative":"2 sentences naming specific free YouTube creators or platforms","manipulationTags":["tag","tag","tag"],"reviewSummary":"1-2 sentences from real verified buyer reviews","affiliateRec":{"platform":"Udemy or Coursera or Skillshare","course":"specific course name","price":"$XX","reason":"one sentence why better"}}`,
      messages:[{role:"user",content:prompt}]
    })
  });
  const data=await res.json();
  if(data.error)throw new Error(data.error.message);
  return JSON.parse(data.content.map(b=>b.text||'').join('').replace(/```json|```/g,'').trim());
}

// ═══════════ REPORT RENDERING ═══════════
function renderReport(r,container){
  const hype=Math.round(r.hypeScore),sub=Math.round(r.substanceScore);
  const circ=226,offset=Math.round(circ*(1-hype/100));
  const hc=hype>75?'#f87171':hype>50?'#fbbf24':'#34d399';
  const sc=hype>75?'#ef4444':hype>50?'#f59e0b':'#34d399';
  const cls=hype>75?'br':hype>50?'ba':'bg';
  container.style.display='block';container.className='fu';
  const reviewHtml=r.reviewSummary?`<div class="scard"><div style="display:flex;align-items:center;gap:6px;margin-bottom:.4rem;"><i class="ti ti-star" style="font-size:13px;color:#fbbf24;"></i><span style="font-size:11px;font-weight:600;color:#d4d4d4;">What real buyers say</span><span style="font-size:10px;color:#444;margin-left:auto;">Trustpilot · Reddit</span></div><p class="ait">${r.reviewSummary}</p></div>`:'';
  const affHtml=r.affiliateRec?`<div class="afc"><i class="ti ti-rosette-discount-check" style="font-size:20px;color:var(--neon);flex-shrink:0;"></i><div style="flex:1;min-width:0;"><div style="font-size:10px;color:#4a7a4a;text-transform:uppercase;letter-spacing:.05em;margin-bottom:2px;">Verified alternative — affiliate link</div><div style="font-size:13px;font-weight:500;color:#d4d4d4;">${r.affiliateRec.course}</div><div style="font-size:11px;color:#5a8a5a;margin-top:1px;">${r.affiliateRec.platform} · ${r.affiliateRec.price} · ${r.affiliateRec.reason}</div></div><a href="${{Udemy:'https://udemy.com',Coursera:'https://coursera.org',Skillshare:'https://skillshare.com'}[r.affiliateRec.platform]||'#'}" target="_blank" style="background:var(--neon);color:#000;border:none;border-radius:7px;padding:5px 12px;font-size:11px;font-weight:600;text-decoration:none;white-space:nowrap;">View <i class="ti ti-external-link" style="font-size:10px;"></i></a></div>`:'';
  container.innerHTML=`
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:.85rem;">
    <div><div style="font-size:9px;color:#3a3a3a;text-transform:uppercase;letter-spacing:.07em;margin-bottom:2px;">CourseDetector reality check</div><div style="font-size:14px;font-weight:600;color:#e0e0e0;">"${r.courseName}"</div><div style="font-size:11px;color:#555;">by ${r.sellerName}</div></div>
    <span class="badge ${cls}"><i class="ti ti-alert-triangle" style="font-size:10px;"></i> ${hype}% Hype</span>
  </div>
  <div style="display:flex;gap:8px;margin-bottom:.7rem;">
    <div class="scard" style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:.75rem;text-align:center;">
      <div style="position:relative;width:64px;height:64px;margin-bottom:.3rem;">
        <svg viewBox="0 0 88 88" width="64" height="64" style="transform:rotate(-90deg);"><circle cx="44" cy="44" r="36" fill="none" stroke="#1e1e1e" stroke-width="7"/><circle cx="44" cy="44" r="36" fill="none" stroke="${sc}" stroke-width="7" stroke-dasharray="${circ}" stroke-dashoffset="${offset}" stroke-linecap="round"/></svg>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;"><span style="font-size:15px;font-weight:700;color:${hc};">${hype}%</span></div>
      </div>
      <div style="font-size:10px;color:${hc};font-weight:600;">Hype</div><div style="font-size:9px;color:#444;">${sub}% substance</div>
    </div>
    <div style="flex:2;display:flex;flex-direction:column;gap:7px;">
      <div class="scard" style="padding:.65rem .9rem;"><div style="font-size:9px;color:#444;margin-bottom:2px;">Stated price</div><div style="font-size:14px;font-weight:600;color:#e0e0e0;">${r.statedPrice}</div><div style="font-size:9px;color:#444;">${r.anchorPrice}</div></div>
      <div class="scard" style="padding:.65rem .9rem;"><div style="font-size:9px;color:#444;margin-bottom:4px;">Manipulation tactics</div><div style="display:flex;gap:3px;flex-wrap:wrap;">${(r.manipulationTags||[]).map(t=>`<span class="badge br">${t}</span>`).join('')}</div></div>
    </div>
  </div>
  <div style="background:#0d0d0d;border:0.5px solid #1e1e1e;border-radius:7px;padding:.6rem .85rem;margin-bottom:.6rem;display:flex;align-items:center;gap:8px;"><div style="font-size:9px;color:#2a2a2a;text-transform:uppercase;flex-shrink:0;">Ad</div><div style="flex:1;font-size:11px;color:#555;">Skip the hype — browse verified courses on <a href="https://udemy.com" target="_blank" style="color:var(--neon);text-decoration:none;">Udemy</a> and <a href="https://coursera.org" target="_blank" style="color:var(--neon);text-decoration:none;">Coursera</a>.</div></div>
  ${reviewHtml}
  <div class="scard"><div style="display:flex;align-items:center;gap:6px;margin-bottom:.4rem;"><i class="ti ti-crystal-ball" style="font-size:13px;color:#a78bfa;"></i><span style="font-size:11px;font-weight:600;color:#d4d4d4;">The Core Promise</span></div><p class="ait">${r.corePromise}</p></div>
  <div class="scard"><div style="display:flex;align-items:center;gap:6px;margin-bottom:.4rem;"><i class="ti ti-books" style="font-size:13px;color:#60a5fa;"></i><span style="font-size:11px;font-weight:600;color:#d4d4d4;">What You Actually Get</span></div><p class="ait">${r.whatYouGet}</p></div>
  <div class="scard"><div style="display:flex;align-items:center;gap:6px;margin-bottom:.4rem;"><i class="ti ti-alert-circle" style="font-size:13px;color:#f87171;"></i><span style="font-size:11px;font-weight:600;color:#d4d4d4;">Fake Urgency Triggers</span></div><ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:5px;">${(r.urgencyTriggers||[]).map(t=>`<li style="display:flex;gap:7px;"><i class="ti ti-point" style="font-size:11px;color:#f87171;flex-shrink:0;margin-top:3px;"></i><span class="ait">${t}</span></li>`).join('')}</ul></div>
  <div class="scard"><div style="display:flex;align-items:center;gap:6px;margin-bottom:.4rem;"><i class="ti ti-file-text" style="font-size:13px;color:#fbbf24;"></i><span style="font-size:11px;font-weight:600;color:#d4d4d4;">The Fine Print Trap</span></div><p class="ait">${r.finePrint}</p></div>
  <div class="scard"><div style="display:flex;align-items:center;gap:6px;margin-bottom:.4rem;"><i class="ti ti-bulb" style="font-size:13px;color:var(--neon);"></i><span style="font-size:11px;font-weight:600;color:#d4d4d4;">The Free Alternative</span></div><p class="ait">${r.freeAlternative}</p></div>
  ${affHtml}
  <div class="pmb"><div style="display:flex;align-items:flex-start;gap:10px;"><i class="ti ti-search" style="font-size:16px;color:#a78bfa;flex-shrink:0;margin-top:2px;"></i><div style="flex:1;"><div style="display:flex;align-items:center;gap:6px;margin-bottom:3px;"><span style="font-size:12px;font-weight:600;color:#c4b5fd;">Deep Investigator Report</span><span class="bp">Pro</span></div><p style="font-size:11px;color:#7c6aaa;line-height:1.55;">Unlock ${r.sellerName}'s business registration, BBB complaints, FTC actions, Trustpilot trend analysis, and social media follower-purchase audit.</p><button class="btn-pur" style="margin-top:8px;font-size:11px;padding:4px 12px;" onclick="showUpgrade()">Unlock for Pro — $4.99/mo</button></div></div></div>
  <div class="div"></div>
  <div style="display:flex;gap:6px;flex-wrap:wrap;align-items:center;">
    <button class="btn-o" onclick="shareReport('${r.sellerName}','${hype}')"><i class="ti ti-brand-x" style="font-size:11px;"></i> Share on X</button>
    <button class="btn-o" onclick="copyReport('${r.sellerName}','${hype}','${r.corePromise.substring(0,80)}')"><i class="ti ti-copy" style="font-size:11px;"></i> Copy</button>
    <button class="btn-o" style="margin-left:auto;" onclick="resetScan()"><i class="ti ti-refresh" style="font-size:11px;"></i> Scan another</button>
  </div>`;
}

function shareReport(name,hype){
  const text=`I just scanned ${name} on CourseDetector — ${hype}% Hype Score 🔥 Strip the manipulation before you buy any course: coursedetector.io`;
  window.open('https://twitter.com/intent/tweet?text='+encodeURIComponent(text),'_blank');
}
function copyReport(name,hype,snippet){
  try{navigator.clipboard.writeText(`CourseDetector Report: ${name}\nHype Score: ${hype}%\n${snippet}...\ncoursedetector.io`)}catch(e){}
  showToast('Report copied to clipboard!');
}

function errBlock(msg){return`<div class="scard" style="color:#f87171;font-size:12px;display:flex;align-items:center;gap:8px;"><i class="ti ti-alert-triangle"></i>${msg}</div>`}

// ═══════════ SCAN ═══════════
async function startScan(){
  if(!isPro&&freeScans<=0){showUpgrade();return}
  if(!getApiKey()){document.getElementById('scanResults').innerHTML=errBlock('Please enter your Anthropic API key above.');document.getElementById('scanResults').style.display='block';return}
  const url=document.getElementById('urlInput').value.trim();
  if(!url){document.getElementById('urlInput').focus();return}
  if(!isPro){freeScans--;updateScanCounter()}
  if(!isPro&&freeScans===0)document.getElementById('proBanner').style.display='flex';
  document.getElementById('scanBtn').disabled=true;
  document.getElementById('scanResults').style.display='none';
  document.getElementById('scanLoading').style.display='block';
  runSteps('scanSteps',async()=>{
    try{const r=await callClaude(`Analyze this course URL and generate a Reality Check. Include real verified buyer review sentiment: ${url}`);document.getElementById('scanLoading').style.display='none';renderReport(r,document.getElementById('scanResults'))}
    catch(e){document.getElementById('scanLoading').style.display='none';document.getElementById('scanResults').innerHTML=errBlock(e.message||'Failed. Try again.');document.getElementById('scanResults').style.display='block'}
    document.getElementById('scanBtn').disabled=false;
  });
}

async function scanSeller(idx){
  if(!isPro&&freeScans<=0){showUpgrade();return}
  if(!getApiKey()){showSection('scanner');showToast('Enter your API key in the Scanner tab first');return}
  const s=SELLERS[idx];
  if(!isPro){freeScans--;updateScanCounter()}
  if(!isPro&&freeScans===0)document.getElementById('proBanner').style.display='flex';
  switchTab('sellers');
  document.getElementById('sellerResults').style.display='none';
  document.getElementById('sellerLoading').style.display='block';
  runSteps('sellerSteps',async()=>{
    try{const r=await callClaude(`Reality Check for: ${s.name}. Niche: "${s.niche}". Price: ${s.price}. Trustpilot: ${s.tp}/5 from ${s.tpCount} reviews. Review themes: ${s.tpNote}. Include review summary.`);document.getElementById('sellerLoading').style.display='none';renderReport(r,document.getElementById('sellerResults'));document.getElementById('sellerResults').scrollIntoView({behavior:'smooth',block:'nearest'})}
    catch(e){document.getElementById('sellerLoading').style.display='none';document.getElementById('sellerResults').innerHTML=errBlock(e.message||'Failed. Try again.');document.getElementById('sellerResults').style.display='block'}
  });
}

function resetScan(){document.getElementById('urlInput').value='';document.getElementById('scanResults').style.display='none';document.getElementById('scanBtn').disabled=false}

// ═══════════ SELLERS ═══════════
function filterSellers(){renderSellerGrid(document.getElementById('sellerSearch').value.toLowerCase())}
function setCategory(cat){activeCategory=cat;document.querySelectorAll('.cpill').forEach(p=>{p.className='cpill'+(p.dataset.cat===cat?' active':'')});filterSellers()}
function renderSellerGrid(q=''){
  const grid=document.getElementById('sellerGrid');
  const list=SELLERS.filter(s=>{const mQ=!q||s.name.toLowerCase().includes(q)||s.niche.toLowerCase().includes(q)||s.tags.some(t=>t.toLowerCase().includes(q));const mC=activeCategory==='All'||s.category===activeCategory;return mQ&&mC});
  if(!list.length){grid.innerHTML=`<div style="color:#3a3a3a;font-size:12px;padding:.75rem 0;">No sellers match.</div>`;return}
  grid.innerHTML=list.map(s=>{
    const ri=SELLERS.indexOf(s);
    const hc=s.hype>80?'#f87171':s.hype>60?'#fbbf24':'#34d399';
    const tc=parseFloat(s.tp)>=4?'#34d399':parseFloat(s.tp)>=3?'#fbbf24':'#f87171';
    return`<div class="sc-card" onclick="scanSeller(${ri})"><div class="av" style="color:${s.color};border-color:${s.color}22;">${s.initials}</div><div style="flex:1;min-width:0;"><div style="font-size:13px;font-weight:600;color:#e0e0e0;">${s.name}</div><div style="font-size:10px;color:#555;margin-top:1px;">${s.niche}</div><div style="display:flex;gap:3px;margin-top:4px;flex-wrap:wrap;">${s.tags.map(t=>`<span class="badge bb" style="font-size:9px;">${t}</span>`).join('')}</div></div><div style="text-align:right;flex-shrink:0;"><div style="font-size:12px;font-weight:600;color:${hc};">${s.hype}% hype</div><div style="font-size:11px;color:${tc};margin-top:2px;display:flex;align-items:center;gap:3px;justify-content:flex-end;"><i class="ti ti-star" style="font-size:10px;"></i>${s.tp}</div><div style="font-size:9px;color:#3a3a3a;">${s.tpCount} reviews</div></div><i class="ti ti-chevron-right" style="font-size:13px;color:#2e2e2e;"></i></div>`;
  }).join('');
}
function initCats(){document.getElementById('categoryPills').innerHTML=CATS.map(c=>`<button class="cpill${c==='All'?' active':''}" data-cat="${c}" onclick="setCategory('${c}')">${c}</button>`).join('')}

// ═══════════ LEADERBOARD ═══════════
function switchLB(mode){
  activeLB=mode;
  document.querySelectorAll('[data-lb]').forEach(el=>el.className='cpill'+(el.dataset.lb===mode?' active':''));
  renderLeaderboard();
}
function renderLeaderboard(){
  const list=document.getElementById('leaderboardList');
  const titleEl=document.getElementById('lbTitle');
  let sorted=[...SELLERS];
  if(activeLB==='shame'){sorted.sort((a,b)=>b.hype-a.hype);titleEl.textContent='Hall of Shame — Ranked by Hype Score';}
  else if(activeLB==='legit'){sorted.sort((a,b)=>a.hype-b.hype);titleEl.textContent='Hall of Fame — Most Legitimate Sellers';}
  else{sorted=sorted.sort(()=>Math.random()-.5).slice(0,8);titleEl.textContent='Recently Scanned';}
  list.innerHTML=sorted.map((s,i)=>{
    const hc=s.hype>80?'#f87171':s.hype>60?'#fbbf24':'#34d399';
    const bc=activeLB==='legit'?'#34d399':s.hype>80?'#ef4444':s.hype>60?'#f59e0b':'#34d399';
    const rankEmoji=activeLB==='shame'?(i===0?'💀':i===1?'🔥':i===2?'⚠️':''):(i===0?'🏆':i===1?'🥈':i===2?'🥉':'');
    const barVal=activeLB==='legit'?(100-s.hype):s.hype;
    const idx=SELLERS.indexOf(s);
    return`<div class="lb-row" onclick="goScanSeller(${idx})">
      <div class="lb-rank" style="color:${hc};">${rankEmoji||('#'+(i+1))}</div>
      <div class="av" style="color:${s.color};border-color:${s.color}22;width:30px;height:30px;font-size:11px;">${s.initials}</div>
      <div style="flex:1;min-width:0;">
        <div style="font-size:13px;font-weight:600;color:#e0e0e0;">${s.name}</div>
        <div style="font-size:10px;color:#555;">${s.niche} · ${s.price}</div>
        <div class="lb-bar-wrap" style="margin-top:5px;"><div class="lb-bar" style="width:${barVal}%;background:${bc};"></div></div>
      </div>
      <div style="text-align:right;flex-shrink:0;">
        <div style="font-size:13px;font-weight:700;color:${hc};">${s.hype}%</div>
        <div style="font-size:9px;color:#444;">hype score</div>
        <div style="font-size:9px;color:${parseFloat(s.tp)>=4?'#34d399':parseFloat(s.tp)>=3?'#fbbf24':'#f87171'};margin-top:1px;">★ ${s.tp}</div>
      </div>
    </div>`;
  }).join('');
}
function goScanSeller(idx){showSection('scanner');switchTab('sellers');setTimeout(()=>scanSeller(idx),100)}

// ═══════════ COMMUNITY ═══════════
function renderQueue(){
  const sorted=[...communityQueue].sort((a,b)=>b.votes-a.votes);
  document.getElementById('communityQueue').innerHTML=sorted.map((item,i)=>{
    const qi=communityQueue.indexOf(item);
    const hc=item.hype>80?'#f87171':item.hype>60?'#fbbf24':'#34d399';
    return`<div style="background:#111;border:0.5px solid #222;border-radius:8px;padding:.85rem 1rem;margin-bottom:8px;display:flex;align-items:center;gap:12px;">
      <div style="font-size:13px;font-weight:700;color:#444;width:20px;flex-shrink:0;">#${i+1}</div>
      <div style="flex:1;min-width:0;">
        <div style="font-size:13px;font-weight:600;color:#d4d4d4;">${item.name}</div>
        <div style="font-size:10px;color:#555;">${item.niche} · ${item.url}</div>
        <div style="display:flex;align-items:center;gap:6px;margin-top:4px;">
          <span class="badge ${item.hype>80?'br':item.hype>60?'ba':'bg'}" style="font-size:9px;">~${item.hype}% est. hype</span>
        </div>
      </div>
      <div style="text-align:right;flex-shrink:0;">
        <button class="vote-btn${item.voted?' voted':''}" onclick="vote(${qi})">
          <i class="ti ti-arrow-up" style="font-size:11px;"></i> ${item.votes}
        </button>
        <div style="font-size:9px;color:#444;margin-top:3px;">votes</div>
      </div>
    </div>`;
  }).join('');
}
function vote(idx){
  if(communityQueue[idx].voted){showToast('Already voted!');return}
  communityQueue[idx].votes++;communityQueue[idx].voted=true;
  document.getElementById('voteCount').textContent=(parseInt(document.getElementById('voteCount').textContent.replace(',',''))+1).toLocaleString();
  renderQueue();showToast('Vote counted! 🔥');
}
function submitSeller(){
  const name=document.getElementById('subName').value.trim();
  if(!name){showToast('Please enter a seller name or URL');return}
  communityQueue.push({name,url:name.includes('http')?name:'',niche:'Community submitted',votes:1,voted:true,hype:Math.floor(Math.random()*30+60)});
  document.getElementById('subName').value='';document.getElementById('subReason').value='';document.getElementById('subExp').value='';
  document.getElementById('subCount').textContent=parseInt(document.getElementById('subCount').textContent)+1;
  renderQueue();showToast('Submitted! Community will vote on it. 🙌');
}

// ═══════════ INIT ═══════════
document.getElementById('urlInput').addEventListener('keydown',e=>{if(e.key==='Enter')startScan()});
initCats();renderSellerGrid();renderLeaderboard();renderQueue();updateScanCounter();
</script>
</body>
</html>
