import os
import subprocess
import time

base_dir = r"W:\workspaces antigravity\opportunity-cockpit-showcase"
assets_dir = os.path.join(base_dir, "assets")
scenes_dir = os.path.join(assets_dir, "scenes")
audio_dir = os.path.join(assets_dir, "audio")
os.makedirs(scenes_dir, exist_ok=True)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
hero_img_path = os.path.join(assets_dir, "hero_executive_dubai.jpg").replace("\\", "/")

def generate_html_scenes():
    head = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&family=Space+Grotesk:wght@600;700;800&family=Plus+Jakarta+Sans:wght@700;800&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1920px;
    height: 1080px;
    overflow: hidden;
    background: #040711;
    color: #F8FAFC;
    font-family: 'Inter', sans-serif;
    position: relative;
    -webkit-font-smoothing: antialiased;
    background-image: 
      linear-gradient(rgba(30, 41, 59, 0.22) 1px, transparent 1px),
      linear-gradient(90deg, rgba(30, 41, 59, 0.22) 1px, transparent 1px);
    background-size: 40px 40px;
  }
  .hud-pill {
    position: absolute;
    top: 24px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(10, 16, 30, 0.96);
    border: 1px solid rgba(56, 189, 248, 0.4);
    box-shadow: 0 12px 36px rgba(0,0,0,0.7), 0 0 24px rgba(56, 189, 248, 0.25);
    border-radius: 9999px;
    padding: 10px 32px;
    display: flex;
    align-items: center;
    gap: 16px;
    z-index: 50;
  }
  .hud-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 800;
    padding: 4px 14px;
    border-radius: 6px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  .hud-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 16.5px;
    font-weight: 700;
    letter-spacing: 0.8px;
    color: #FFFFFF;
  }
  .glass-card {
    background: rgba(10, 16, 30, 0.92);
    backdrop-filter: blur(24px);
    border: 1px solid rgba(51, 65, 85, 0.7);
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.08);
  }
  .glow-cyan {
    box-shadow: 0 0 40px rgba(56, 189, 248, 0.25);
  }
  .glow-emerald {
    box-shadow: 0 0 40px rgba(34, 197, 94, 0.25);
  }
  .glow-amber {
    box-shadow: 0 0 40px rgba(245, 158, 11, 0.25);
  }
</style>
</head>
"""

    # SCENE 1: Executive Command Center Overview (Burj Khalifa Penthouse View + Live Market Ticker)
    scene1_html = head + f"""
<body>
  <div style="position:absolute;inset:0;background:url('file:///{hero_img_path}') center/cover no-repeat;filter:brightness(0.66) contrast(1.15);"></div>
  <div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 40%, rgba(4,7,17,0.3) 0%, rgba(4,7,17,0.88) 100%);"></div>
  <div style="position:absolute;top:0;left:0;right:0;height:120px;background:linear-gradient(180deg, rgba(4,7,17,0.92) 0%, transparent 100%);"></div>

  <!-- Top Financial / Operations HUD Ticker -->
  <div style="position:absolute;top:28px;left:60px;font-family:'JetBrains Mono';font-size:12px;color:#94A3B8;letter-spacing:0.8px;display:flex;align-items:center;gap:10px;">
    <span style="display:flex;align-items:center;gap:6px;background:rgba(2,132,199,0.3);border:1px solid #0284C7;color:#38BDF8;padding:5px 12px;border-radius:6px;font-weight:700;">
      <span style="width:7px;height:7px;border-radius:50%;background:#38BDF8;box-shadow:0 0 8px #38BDF8;"></span>
      DUBAI DIFC COCKPIT · GST
    </span>
    <span style="background:rgba(10,16,30,0.85);padding:5px 10px;border-radius:6px;border:1px solid #1E293B;">DFM: 4,520 (+1.2%)</span>
  </div>

  <div class="hud-pill">
    <span class="hud-tag" style="background:#0284C7;color:#FFFFFF;">EXECUTIVE BRIEFING</span>
    <span class="hud-title">EXECUTIVE AI COMMAND CENTER · DUBAI C-SUITE OPERATIONS</span>
  </div>

  <div style="position:absolute;top:28px;right:60px;font-family:'JetBrains Mono';font-size:12px;color:#4ADE80;letter-spacing:1px;font-weight:700;display:flex;align-items:center;gap:8px;background:rgba(22,163,74,0.2);border:1px solid #16A34A;padding:5px 14px;border-radius:6px;">
    <span style="width:7px;height:7px;border-radius:50%;background:#4ADE80;box-shadow:0 0 8px #4ADE80;"></span>
    SOVEREIGN GOVERNANCE ACTIVE
  </div>

  <!-- Bottom Hero Bar -->
  <div style="position:absolute;bottom:48px;left:60px;right:60px;display:flex;justify-content:space-between;align-items:flex-end;gap:30px;">
    <div class="glass-card" style="flex:1;border-radius:24px;padding:36px 44px;border:1px solid rgba(56,189,248,0.35);">
      <div style="display:flex;gap:12px;margin-bottom:14px;flex-wrap:wrap;">
        <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:800;background:rgba(2,132,199,0.25);color:#38BDF8;padding:5px 12px;border-radius:6px;border:1px solid #0284C7;">DUBAI C-SUITE STACK</span>
        <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:800;background:rgba(22,163,74,0.25);color:#4ADE80;padding:5px 12px;border-radius:6px;border:1px solid #16A34A;">ZERO ROGUE AI POLICY</span>
        <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:800;background:rgba(245,158,11,0.25);color:#FBBF24;padding:5px 12px;border-radius:6px;border:1px solid #D97706;">EXPERT TIER $39/HR</span>
        <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:800;background:rgba(168,85,247,0.25);color:#C084FC;padding:5px 12px;border-radius:6px;border:1px solid #9333EA;">SPRINT 1 &lt; 14 DAYS</span>
      </div>
      <h1 style="font-family:'Space Grotesk';font-size:46px;font-weight:800;line-height:1.15;color:#FFFFFF;margin-bottom:14px;letter-spacing:-0.5px;">
        Turning Raw AI Models into <span style="background:linear-gradient(90deg, #38BDF8, #4ADE80);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Trusted Leadership Habits</span>
      </h1>
      <p style="font-size:18px;color:#94A3B8;line-height:1.55;max-width:980px;">
        A disciplined operational framework for CEOs and Department Leads in Dubai. Ingest unstructured voice communications, synthesize 3-bullet decision digests, and enforce 1-click deterministic governance.
      </p>
      <div style="display:flex;gap:28px;margin-top:20px;padding-top:18px;border-top:1px solid rgba(51,65,85,0.7);font-family:'JetBrains Mono';font-size:12.5px;color:#CBD5E1;">
        <span>⚡ <strong>Ingestion Latency:</strong> 1.2s</span>
        <span>🛡️ <strong>PII Leakage:</strong> 0.00% Guaranteed</span>
        <span>🎯 <strong>Audit Trail:</strong> 100% Deterministic</span>
        <span>⏱️ <strong>UAE Business Hours:</strong> Fully Aligned</span>
      </div>
    </div>

    <!-- Right Metric Badges -->
    <div style="display:flex;flex-direction:column;gap:18px;">
      <div class="glass-card glow-emerald" style="border-radius:20px;padding:24px 34px;text-align:center;min-width:260px;border:1.5px solid rgba(34,197,94,0.5);">
        <div style="font-family:'JetBrains Mono';font-size:44px;font-weight:800;color:#4ADE80;line-height:1;">5–10h</div>
        <div style="font-size:13px;font-weight:700;color:#94A3B8;text-transform:uppercase;margin-top:8px;letter-spacing:0.5px;">Weekly Recovered</div>
        <div style="font-family:'JetBrains Mono';font-size:11.5px;color:#16A34A;margin-top:4px;font-weight:800;">SPRINT 01 QUICK-WIN</div>
      </div>
      <div class="glass-card glow-cyan" style="border-radius:20px;padding:24px 34px;text-align:center;min-width:260px;border:1.5px solid rgba(56,189,248,0.5);">
        <div style="font-family:'JetBrains Mono';font-size:44px;font-weight:800;color:#38BDF8;line-height:1;">100%</div>
        <div style="font-size:13px;font-weight:700;color:#94A3B8;text-transform:uppercase;margin-top:8px;letter-spacing:0.5px;">Deterministic</div>
        <div style="font-family:'JetBrains Mono';font-size:11.5px;color:#0284C7;margin-top:4px;font-weight:800;">1-CLICK HUMAN GATE</div>
      </div>
    </div>
  </div>
</body>
</html>
"""

    # SCENE 2: Real-time Ingestion & Voice Triage
    scene2_html = head + """
<body>
  <div style="position:absolute;top:8%;left:15%;width:650px;height:650px;background:radial-gradient(circle, rgba(2,132,199,0.18) 0%, transparent 70%);pointer-events:none;"></div>
  <div style="position:absolute;bottom:8%;right:15%;width:650px;height:650px;background:radial-gradient(circle, rgba(22,163,74,0.16) 0%, transparent 70%);pointer-events:none;"></div>

  <div class="hud-pill">
    <span class="hud-tag" style="background:#16A34A;color:#FFFFFF;">STEP 01: INTAKE</span>
    <span class="hud-title">REAL-TIME VOICE INGESTION · SANITIZED IN 1.2s · ZERO LEAKAGE</span>
  </div>

  <div style="position:absolute;top:92px;bottom:32px;left:60px;right:60px;display:grid;grid-template-columns:1.05fr 0.95fr;gap:24px;">
    
    <!-- Left Column: Audio Intake Stream, Spectrogram & Tokenization -->
    <div class="glass-card" style="border-radius:24px;padding:26px 30px;display:flex;flex-direction:column;gap:14px;border:1px solid rgba(56,189,248,0.35);">
      
      <!-- Audio Memo Header -->
      <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #1E293B;padding-bottom:12px;">
        <div style="display:flex;align-items:center;gap:14px;">
          <div style="width:48px;height:48px;border-radius:14px;background:linear-gradient(135deg, #0284C7, #0369A1);display:flex;align-items:center;justify-content:center;font-size:24px;box-shadow:0 0 20px rgba(3,105,161,0.6);">🎙️</div>
          <div>
            <div style="font-size:19px;font-weight:800;color:#FFFFFF;">VP of Operations (Dubai DIFC)</div>
            <div style="font-family:'JetBrains Mono';font-size:12px;color:#38BDF8;">WhatsApp & Slack Corporate Intake Gateway</div>
          </div>
        </div>
        <span style="font-family:'JetBrains Mono';font-size:11.5px;font-weight:800;background:rgba(22,163,74,0.25);color:#4ADE80;border:1px solid #16A34A;padding:5px 12px;border-radius:8px;">0:32 HD OPUS MEMO</span>
      </div>

      <!-- High-End Soundwave Visualizer -->
      <div style="background:#070B14;border:1px solid #1E293B;border-radius:14px;padding:14px 20px;box-shadow:inset 0 2px 10px rgba(0,0,0,0.6);">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
          <span style="font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;text-transform:uppercase;">Stereo Frequency Waveform</span>
          <span style="font-family:'JetBrains Mono';font-size:11px;color:#4ADE80;font-weight:700;">● Active Stream · 24kHz Opus · Dynamic Range -16 LUFS</span>
        </div>
        
        <div style="display:flex;align-items:center;justify-content:space-between;height:52px;padding:0 6px;">
          <div style="width:6px;height:22px;background:#38BDF8;border-radius:3px;"></div>
          <div style="width:6px;height:42px;background:#0284C7;border-radius:3px;"></div>
          <div style="width:6px;height:28px;background:#38BDF8;border-radius:3px;"></div>
          <div style="width:6px;height:50px;background:#4ADE80;border-radius:3px;"></div>
          <div style="width:6px;height:36px;background:#0284C7;border-radius:3px;"></div>
          <div style="width:6px;height:46px;background:#38BDF8;border-radius:3px;"></div>
          <div style="width:6px;height:40px;background:#4ADE80;border-radius:3px;"></div>
          <div style="width:6px;height:52px;background:#0284C7;border-radius:3px;"></div>
          <div style="width:6px;height:44px;background:#38BDF8;border-radius:3px;"></div>
          <div style="width:6px;height:30px;background:#0284C7;border-radius:3px;"></div>
          <div style="width:6px;height:48px;background:#4ADE80;border-radius:3px;"></div>
          <div style="width:6px;height:38px;background:#38BDF8;border-radius:3px;"></div>
          <div style="width:6px;height:52px;background:#0284C7;border-radius:3px;"></div>
          <div style="width:6px;height:42px;background:#4ADE80;border-radius:3px;"></div>
          <div style="width:6px;height:28px;background:#38BDF8;border-radius:3px;"></div>
          <div style="width:6px;height:46px;background:#0284C7;border-radius:3px;"></div>
          <div style="width:6px;height:32px;background:#4ADE80;border-radius:3px;"></div>
          <div style="width:6px;height:48px;background:#38BDF8;border-radius:3px;"></div>
          <div style="width:6px;height:38px;background:#0284C7;border-radius:3px;"></div>
          <div style="width:6px;height:50px;background:#4ADE80;border-radius:3px;"></div>
          <div style="width:6px;height:34px;background:#38BDF8;border-radius:3px;"></div>
          <div style="width:6px;height:44px;background:#0284C7;border-radius:3px;"></div>
          <div style="width:6px;height:28px;background:#4ADE80;border-radius:3px;"></div>
          <div style="width:6px;height:38px;background:#38BDF8;border-radius:3px;"></div>
        </div>

        <div style="display:flex;align-items:center;gap:12px;margin-top:8px;">
          <span style="font-family:'JetBrains Mono';font-size:11px;color:#38BDF8;">0:28</span>
          <div style="flex:1;height:4px;background:#1E293B;border-radius:2px;position:relative;">
            <div style="width:87%;height:100%;background:linear-gradient(90deg, #0284C7, #4ADE80);border-radius:2px;"></div>
            <div style="position:absolute;left:87%;top:-4px;width:12px;height:12px;border-radius:50%;background:#4ADE80;box-shadow:0 0 8px #4ADE80;"></div>
          </div>
          <span style="font-family:'JetBrains Mono';font-size:11px;color:#64748B;">0:32</span>
        </div>
      </div>

      <!-- Diarization & Audio Metrics -->
      <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:10px;">
        <div style="background:#070B14;border:1px solid #1E293B;border-radius:10px;padding:8px 12px;text-align:center;">
          <div style="font-family:'JetBrains Mono';font-size:10px;color:#94A3B8;text-transform:uppercase;">Speaker</div>
          <div style="font-family:'JetBrains Mono';font-size:12.5px;font-weight:700;color:#38BDF8;margin-top:2px;">Tareq M. (VP Ops)</div>
        </div>
        <div style="background:#070B14;border:1px solid #1E293B;border-radius:10px;padding:8px 12px;text-align:center;">
          <div style="font-family:'JetBrains Mono';font-size:10px;color:#94A3B8;text-transform:uppercase;">Audio Noise Gate</div>
          <div style="font-family:'JetBrains Mono';font-size:12.5px;font-weight:700;color:#4ADE80;margin-top:2px;">-42dB Studio Clean</div>
        </div>
        <div style="background:#070B14;border:1px solid #1E293B;border-radius:10px;padding:8px 12px;text-align:center;">
          <div style="font-family:'JetBrains Mono';font-size:10px;color:#94A3B8;text-transform:uppercase;">Match Accuracy</div>
          <div style="font-family:'JetBrains Mono';font-size:12.5px;font-weight:700;color:#FBBF24;margin-top:2px;">99.8% Grounded</div>
        </div>
      </div>

      <!-- Live Streamed Transcript -->
      <div style="background:#070B14;border:1px solid #1E293B;border-radius:14px;padding:16px 20px;font-family:'JetBrains Mono';font-size:14px;line-height:1.6;color:#CBD5E1;">
        <div style="font-size:11px;color:#64748B;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">Live Audio Transcription:</div>
        “Flávio, we just received <span style="color:#38BDF8;font-weight:800;border-bottom:2px solid #0284C7;">Apex Capital's</span> revision. They want to proceed with <span style="color:#4ADE80;font-weight:800;border-bottom:2px solid #16A34A;">Milestone 1 ($50k)</span>, but need delivery onboarding moved to <span style="color:#FBBF24;font-weight:800;border-bottom:2px solid #D97706;">Thursday morning</span>. Can we confirm this before their committee meets at 2 PM?”
      </div>

      <!-- Vault Tokenization Matrix -->
      <div style="background:#070B14;border:1px solid #1E293B;border-radius:14px;padding:14px 18px;display:flex;flex-direction:column;gap:8px;">
        <div style="font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;text-transform:uppercase;letter-spacing:0.8px;">Tokenized Security Payload (Air-Gapped Sandbox):</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;font-family:'JetBrains Mono';font-size:11.5px;">
          <div style="background:rgba(2,132,199,0.15);padding:6px 10px;border-radius:6px;border:1px solid #0284C7;color:#38BDF8;">
            Entity: [Apex Capital] ➔ <strong style="color:#FFFFFF;">VAULT-APX-894</strong>
          </div>
          <div style="background:rgba(22,163,74,0.15);padding:6px 10px;border-radius:6px;border:1px solid #16A34A;color:#4ADE80;">
            Milestone: [$50,000 USD] ➔ <strong style="color:#FFFFFF;">MS1_SECURE_VAL</strong>
          </div>
          <div style="background:rgba(245,158,11,0.15);padding:6px 10px;border-radius:6px;border:1px solid #D97706;color:#FBBF24;">
            Schedule: [Thu 10:00 AM] ➔ <strong style="color:#FFFFFF;">DIFC_SLOT_094</strong>
          </div>
          <div style="background:rgba(168,85,247,0.15);padding:6px 10px;border-radius:6px;border:1px solid #9333EA;color:#C084FC;">
            Committee: [Apex Board] ➔ <strong style="color:#FFFFFF;">AUTH_BOARD_GATE</strong>
          </div>
        </div>
      </div>

      <!-- PII Shield Active -->
      <div style="background:rgba(22,163,74,0.12);border:1px solid rgba(34,197,94,0.3);border-radius:12px;padding:10px 16px;display:flex;align-items:center;gap:12px;font-family:'JetBrains Mono';font-size:12px;color:#86EFAC;">
        <span style="font-size:18px;">🛡️</span>
        <div><strong>PII Shield Enforced:</strong> Zero client data transmitted to public LLM training sets. SOC2 Type II Aligned.</div>
      </div>

      <!-- Footer Bar -->
      <div style="display:flex;justify-content:space-between;align-items:center;padding-top:8px;border-top:1px solid #1E293B;">
        <span style="font-family:'JetBrains Mono';font-size:11px;color:#64748B;">Origin: WhatsApp Voice Note · Encrypted Gateway</span>
        <span style="font-family:'JetBrains Mono';font-size:11px;color:#38BDF8;font-weight:700;">SHA-256 Validated</span>
      </div>
    </div>

    <!-- Right Column: Pipeline Stepper, Structured Entity Matrix & Governance -->
    <div style="display:flex;flex-direction:column;gap:14px;">
      
      <!-- Pipeline Stepper -->
      <div class="glass-card" style="border-radius:20px;padding:18px 24px;border:1.5px solid #16A34A;box-shadow:0 0 35px rgba(22,163,74,0.22);display:flex;flex-direction:column;gap:10px;">
        <div style="display:flex;justify-content:space-between;align-items:center;">
          <div style="display:flex;align-items:center;gap:10px;">
            <div style="width:34px;height:34px;border-radius:50%;background:#16A34A;color:#FFFFFF;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:900;">✓</div>
            <div>
              <div style="font-size:17px;font-weight:800;color:#4ADE80;">Sanitized & Parsed in 1.18s Total</div>
              <div style="font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;">Air-Gapped Private VPC · Enterprise SLA &lt; 1.5s</div>
            </div>
          </div>
          <span style="font-family:'JetBrains Mono';font-size:11px;background:rgba(22,163,74,0.25);color:#4ADE80;padding:4px 10px;border-radius:6px;font-weight:800;">LATENCY: 1,180ms</span>
        </div>

        <div style="display:grid;grid-template-columns:repeat(4, 1fr);gap:8px;font-family:'JetBrains Mono';font-size:11px;text-align:center;">
          <div style="background:#070B14;border:1px solid #16A34A;padding:8px 4px;border-radius:8px;color:#4ADE80;">
            ✓ 1. Audio Ingest<br><span style="color:#64748B;font-size:10px;">0.22s</span>
          </div>
          <div style="background:#070B14;border:1px solid #16A34A;padding:8px 4px;border-radius:8px;color:#4ADE80;">
            ✓ 2. PII Scrubber<br><span style="color:#64748B;font-size:10px;">0.31s</span>
          </div>
          <div style="background:#070B14;border:1px solid #16A34A;padding:8px 4px;border-radius:8px;color:#4ADE80;">
            ✓ 3. Entity Extract<br><span style="color:#64748B;font-size:10px;">0.38s</span>
          </div>
          <div style="background:#070B14;border:1px solid #16A34A;padding:8px 4px;border-radius:8px;color:#4ADE80;">
            ✓ 4. JSON Schema<br><span style="color:#64748B;font-size:10px;">0.27s</span>
          </div>
        </div>
      </div>

      <!-- Entity Extraction Matrix -->
      <div class="glass-card" style="border-radius:20px;padding:22px 26px;display:flex;flex-direction:column;gap:10px;">
        <div style="font-family:'JetBrains Mono';font-size:12px;font-weight:800;color:#38BDF8;text-transform:uppercase;letter-spacing:1px;margin-bottom:2px;">Structured Entity Extraction:</div>
        
        <div style="display:flex;align-items:center;justify-content:space-between;background:#070B14;padding:12px 16px;border-radius:10px;border:1px solid #1E293B;">
          <span style="color:#94A3B8;font-size:13.5px;">Target Client Account:</span>
          <span style="color:#FFFFFF;font-weight:800;font-family:'JetBrains Mono';font-size:14px;">Apex Capital (UAE Strategic Account)</span>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;background:#070B14;padding:12px 16px;border-radius:10px;border:1px solid #1E293B;">
          <span style="color:#94A3B8;font-size:13.5px;">Revenue Milestone:</span>
          <span style="color:#4ADE80;font-weight:800;font-family:'JetBrains Mono';font-size:14.5px;">$50,000 USD (Milestone 1 Approved)</span>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;background:#070B14;padding:12px 16px;border-radius:10px;border:1px solid #1E293B;">
          <span style="color:#94A3B8;font-size:13.5px;">Capacity & Onboarding:</span>
          <span style="color:#38BDF8;font-weight:800;font-family:'JetBrains Mono';font-size:14px;">Thursday 10:00 AM GST (Capacity Locked)</span>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;background:#070B14;padding:12px 16px;border-radius:10px;border:1px solid #1E293B;">
          <span style="color:#94A3B8;font-size:13.5px;">Governance Constraint:</span>
          <span style="color:#FBBF24;font-weight:800;font-family:'JetBrains Mono';font-size:14px;">Requires 1-Click Sign-Off Before 2:00 PM</span>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;background:#070B14;padding:12px 16px;border-radius:10px;border:1px solid #1E293B;">
          <span style="color:#94A3B8;font-size:13.5px;">Target Reviewer:</span>
          <span style="color:#C084FC;font-weight:800;font-family:'JetBrains Mono';font-size:14px;">Apex Investment Committee</span>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;background:#070B14;padding:12px 16px;border-radius:10px;border:1px solid #1E293B;">
          <span style="color:#94A3B8;font-size:13.5px;">Output Action:</span>
          <span style="color:#38BDF8;font-weight:800;font-family:'JetBrains Mono';font-size:14px;">Route to Step 02 (Strategic Synthesis)</span>
        </div>
      </div>

      <!-- Security & Compliance Attestation -->
      <div class="glass-card" style="border-radius:16px;padding:14px 20px;border:1px solid #1E293B;display:grid;grid-template-columns:repeat(3, 1fr);gap:10px;">
        <div>
          <span style="font-family:'JetBrains Mono';font-size:10.5px;color:#94A3B8;text-transform:uppercase;display:block;">DIFC Law No. 5</span>
          <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:700;color:#4ADE80;">✓ 100% Compliant</span>
        </div>
        <div>
          <span style="font-family:'JetBrains Mono';font-size:10.5px;color:#94A3B8;text-transform:uppercase;display:block;">Public LLM Opt-Out</span>
          <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:700;color:#38BDF8;">✓ Enforced Gateway</span>
        </div>
        <div>
          <span style="font-family:'JetBrains Mono';font-size:10.5px;color:#94A3B8;text-transform:uppercase;display:block;">SLA Delivery</span>
          <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:700;color:#FBBF24;">⚡ &lt; 1,500ms</span>
        </div>
      </div>

      <!-- Executive Contrast Card -->
      <div class="glass-card" style="border-radius:16px;padding:16px 20px;border:1px solid rgba(245,158,11,0.4);display:flex;justify-content:space-between;align-items:center;gap:16px;">
        <div style="font-size:12.5px;color:#CBD5E1;line-height:1.45;">
          <strong style="color:#FBBF24;display:block;margin-bottom:2px;font-family:'JetBrains Mono';">THE EXECUTIVE CONTRAST:</strong>
          Consumer AI leaks client data to public training. This cockpit isolates every voice note into an air-gapped private sandbox.
        </div>
        <span style="font-family:'JetBrains Mono';font-size:11px;color:#4ADE80;font-weight:800;background:rgba(22,163,74,0.2);padding:6px 12px;border-radius:8px;border:1px solid #16A34A;shrink:0;">100% PROTECTED</span>
      </div>

      <!-- Bottom Status Bar -->
      <div style="background:rgba(10,16,30,0.9);border:1px solid #1E293B;border-radius:14px;padding:12px 18px;display:flex;justify-content:space-between;align-items:center;">
        <span style="font-family:'JetBrains Mono';font-size:12px;color:#94A3B8;">Next Stage: Synthesize 3-Bullet Board Brief & Pre-Draft Reply</span>
        <span style="font-family:'JetBrains Mono';font-size:12px;color:#4ADE80;font-weight:700;">Status: Ready for Synthesis →</span>
      </div>

    </div>

  </div>
</body>
</html>
"""

    # SCENE 3: AI Strategic Synthesis & Pre-Drafts
    scene3_html = head + """
<body>
  <div style="position:absolute;top:15%;left:10%;width:650px;height:650px;background:radial-gradient(circle, rgba(22,163,74,0.18) 0%, transparent 70%);pointer-events:none;"></div>
  <div style="position:absolute;bottom:15%;right:10%;width:650px;height:650px;background:radial-gradient(circle, rgba(2,132,199,0.18) 0%, transparent 70%);pointer-events:none;"></div>

  <div class="hud-pill">
    <span class="hud-tag" style="background:#0284C7;color:#FFFFFF;">STEP 02: SYNTHESIS</span>
    <span class="hud-title">AI STRATEGIC SYNTHESIS · 3-BULLET DIGEST · PRE-DRAFTED ACTIONS</span>
  </div>

  <div style="position:absolute;top:92px;bottom:32px;left:60px;right:60px;display:grid;grid-template-columns:1fr 1fr;gap:24px;">
    
    <!-- Left Column: 3 Strategic Decision Bullets + AI Reasoning Matrix + Benchmark -->
    <div style="display:flex;flex-direction:column;gap:12px;">
      
      <!-- Title -->
      <div>
        <div style="font-family:'Space Grotesk';font-size:25px;font-weight:800;color:#FFFFFF;margin-bottom:2px;">Executive Decision Digest</div>
        <div style="font-size:13.5px;color:#94A3B8;">Instant board-level triage: 3 high-impact bullets generated in &lt;1.4 seconds.</div>
      </div>

      <!-- 3 Rich Decision Cards -->
      <div class="glass-card" style="border-radius:16px;padding:18px 22px;display:flex;gap:16px;align-items:flex-start;border:1px solid rgba(22,163,74,0.35);">
        <div style="font-family:'JetBrains Mono';font-size:20px;font-weight:900;color:#4ADE80;background:rgba(22,163,74,0.18);border:1px solid #16A34A;width:44px;height:44px;border-radius:10px;display:flex;align-items:center;justify-content:center;shrink:0;">01</div>
        <div style="flex:1;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:2px;">
            <span style="font-size:16.5px;font-weight:800;color:#FFFFFF;">Revenue Milestone Approved</span>
            <span style="font-family:'JetBrains Mono';font-size:10.5px;background:rgba(22,163,74,0.2);color:#4ADE80;padding:2px 8px;border-radius:4px;border:1px solid #16A34A;font-weight:700;">+$50,000 USD</span>
          </div>
          <div style="font-size:13px;color:#94A3B8;line-height:1.45;">Confirms $50,000 for Milestone 1 under approved commercial terms. Risk of scope creep mitigated through locked milestone boundaries.</div>
          <div style="font-family:'JetBrains Mono';font-size:11px;color:#86EFAC;margin-top:4px;">Commercial Terms: $25k at Kickoff · $25k at Sprint 1 Acceptance</div>
        </div>
      </div>

      <div class="glass-card" style="border-radius:16px;padding:18px 22px;display:flex;gap:16px;align-items:flex-start;border:1px solid rgba(56,189,248,0.35);">
        <div style="font-family:'JetBrains Mono';font-size:20px;font-weight:900;color:#38BDF8;background:rgba(2,132,199,0.18);border:1px solid #0284C7;width:44px;height:44px;border-radius:10px;display:flex;align-items:center;justify-content:center;shrink:0;">02</div>
        <div style="flex:1;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:2px;">
            <span style="font-size:16.5px;font-weight:800;color:#FFFFFF;">Calendar & Delivery Alignment</span>
            <span style="font-family:'JetBrains Mono';font-size:10.5px;background:rgba(2,132,199,0.2);color:#38BDF8;padding:2px 8px;border-radius:4px;border:1px solid #0284C7;font-weight:700;">THU 10:00 AM GST</span>
          </div>
          <div style="font-size:13px;color:#94A3B8;line-height:1.45;">Onboarding shifted to Thursday 10:00 AM GST. Technical delivery leads reserved with zero meeting schedule overlap.</div>
          <div style="font-family:'JetBrains Mono';font-size:11px;color:#38BDF8;margin-top:4px;">Participants: Apex Technical Steering Committee + Flávio Barros</div>
        </div>
      </div>

      <div class="glass-card" style="border-radius:16px;padding:18px 22px;display:flex;gap:16px;align-items:flex-start;border:1px solid rgba(245,158,11,0.35);">
        <div style="font-family:'JetBrains Mono';font-size:20px;font-weight:900;color:#FBBF24;background:rgba(217,119,6,0.18);border:1px solid #D97706;width:44px;height:44px;border-radius:10px;display:flex;align-items:center;justify-content:center;shrink:0;">03</div>
        <div style="flex:1;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:2px;">
            <span style="font-size:16.5px;font-weight:800;color:#FFFFFF;">Time-Sensitive Authorization</span>
            <span style="font-family:'JetBrains Mono';font-size:10.5px;background:rgba(217,119,6,0.2);color:#FBBF24;padding:2px 8px;border-radius:4px;border:1px solid #D97706;font-weight:700;">DEADLINE: 2:00 PM GST</span>
          </div>
          <div style="font-size:13px;color:#94A3B8;line-height:1.45;">Requires 1-click leadership sign-off prior to Apex 2:00 PM GST committee meeting. 1h 18m remaining.</div>
          <div style="font-family:'JetBrains Mono';font-size:11px;color:#FBBF24;margin-top:4px;">Governance Rule: Never dispatch unapproved commitments to clients</div>
        </div>
      </div>

      <!-- Decision Grounding & Compliance Guardrails Card -->
      <div class="glass-card" style="border-radius:16px;padding:14px 20px;display:flex;flex-direction:column;gap:8px;border:1px solid #1E293B;">
        <div style="font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;text-transform:uppercase;letter-spacing:0.8px;">Autonomous Guardrail Verification:</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;font-family:'JetBrains Mono';font-size:11.5px;">
          <div style="background:#070B14;padding:7px 10px;border-radius:6px;border:1px solid #1E293B;color:#4ADE80;">
            ✓ Authority Limit: &lt; $100k Cap
          </div>
          <div style="background:#070B14;padding:7px 10px;border-radius:6px;border:1px solid #1E293B;color:#4ADE80;">
            ✓ Calendar: 0 Slot Clashes
          </div>
          <div style="background:#070B14;padding:7px 10px;border-radius:6px;border:1px solid #1E293B;color:#4ADE80;">
            ✓ Tone: Formal Board Protocol
          </div>
          <div style="background:#070B14;padding:7px 10px;border-radius:6px;border:1px solid #1E293B;color:#4ADE80;">
            ✓ Scope: Locked to Milestone 1
          </div>
        </div>
      </div>

      <!-- AI Grounding & Confidence Metrics Card -->
      <div class="glass-card" style="border-radius:14px;padding:12px 18px;display:grid;grid-template-columns:repeat(3, 1fr);gap:10px;border:1px solid #1E293B;">
        <div>
          <span style="font-family:'JetBrains Mono';font-size:10.5px;color:#94A3B8;text-transform:uppercase;display:block;">Model Engine</span>
          <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:700;color:#38BDF8;">Claude 3.5 Private API</span>
        </div>
        <div>
          <span style="font-family:'JetBrains Mono';font-size:10.5px;color:#94A3B8;text-transform:uppercase;display:block;">Grounding Score</span>
          <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:700;color:#4ADE80;">100% Deterministic</span>
        </div>
        <div>
          <span style="font-family:'JetBrains Mono';font-size:10.5px;color:#94A3B8;text-transform:uppercase;display:block;">Hallucination Risk</span>
          <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:700;color:#FBBF24;">&lt; 0.01% (Air-Gapped)</span>
        </div>
      </div>

      <!-- Acceleration Metric Card -->
      <div class="glass-card glow-cyan" style="border-radius:16px;padding:16px 22px;border:1px solid rgba(56,189,248,0.45);display:flex;justify-content:space-between;align-items:center;">
        <div>
          <span style="font-family:'JetBrains Mono';font-size:11px;font-weight:800;color:#38BDF8;text-transform:uppercase;letter-spacing:1px;display:block;margin-bottom:3px;">OPERATIONAL ACCELERATION BENCHMARK:</span>
          <span style="font-size:13.5px;color:#E2E8F0;">Manual C-Suite Triage: <strong>35–45 min</strong> ➔ Autonomous Cockpit: <strong>1.4 sec</strong></span>
        </div>
        <div style="text-align:right;">
          <span style="font-family:'JetBrains Mono';font-size:24px;font-weight:900;color:#4ADE80;display:block;">⚡ 96.5%</span>
          <span style="font-family:'JetBrains Mono';font-size:10.5px;color:#94A3B8;">TIME RECLAIMED</span>
        </div>
      </div>

    </div>

    <!-- Right Column: Pre-Drafted Client Deliverable in Superhuman C-Suite Client -->
    <div class="glass-card" style="border-radius:24px;padding:24px 28px;display:flex;flex-direction:column;gap:14px;border:1px solid rgba(56,189,248,0.35);">
      
      <!-- Window Title Bar with macOS Chrome Dots -->
      <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #1E293B;padding-bottom:10px;">
        <div style="display:flex;align-items:center;gap:12px;">
          <div style="display:flex;gap:6px;">
            <div style="width:11px;height:11px;border-radius:50%;background:#EF4444;"></div>
            <div style="width:11px;height:11px;border-radius:50%;background:#F59E0B;"></div>
            <div style="width:11px;height:11px;border-radius:50%;background:#10B981;"></div>
          </div>
          <div>
            <div style="font-family:'JetBrains Mono';font-size:12px;font-weight:800;color:#38BDF8;text-transform:uppercase;">Superhuman Executive Client · Outbox Vault</div>
            <div style="font-size:11px;color:#94A3B8;">Draft Status: Held for 1-Click Human Decision Gate</div>
          </div>
        </div>
        <span style="font-family:'JetBrains Mono';font-size:11px;background:#1E293B;color:#4ADE80;padding:4px 10px;border-radius:6px;font-weight:700;">HELD IN VAULT</span>
      </div>

      <!-- Email Client Window with Full Realistic Body -->
      <div style="background:#070B14;border:1px solid #1E293B;border-radius:14px;padding:18px 22px;font-family:'JetBrains Mono';font-size:13px;line-height:1.6;color:#E2E8F0;box-shadow:inset 0 2px 10px rgba(0,0,0,0.6);display:flex;flex-direction:column;gap:10px;">
        <div style="color:#64748B;border-bottom:1px solid #1E293B;padding-bottom:8px;font-size:12px;line-height:1.5;">
          <div><strong>To:</strong> Tariq Al-Mansoor &lt;tariq@apexcapital.ae&gt;</div>
          <div><strong>From:</strong> Flávio Barros &lt;f.barros@wii-operations.com&gt;</div>
          <div><strong>Subject:</strong> Confirmation: Apex Capital Milestone 1 & Thursday Onboarding</div>
          <div style="color:#38BDF8;margin-top:2px;"><strong>Security:</strong> TLS 1.3 · Signed Private Key · Zero Tracking Pixels</div>
        </div>
        <div>
          Dear Tariq,<br><br>
          Thank you for the update. We are pleased to confirm Milestone 1 ($50,000 USD) under our agreed commercial terms.<br><br>
          Our technical delivery leads are locked in to kick off the executive onboarding session this Thursday at 10:00 AM GST. We will review the initial telemetry and sprint milestone milestones together.<br><br>
          Looking forward to an exceptional kickoff.<br><br>
          Best regards,<br>
          <strong style="color:#38BDF8;">Flávio Barros</strong><br>
          <span style="color:#94A3B8;font-size:11.5px;">Founder & AI Solutions Architect · Dubai Operations</span>
        </div>
      </div>

      <!-- Attachment Chips -->
      <div style="display:flex;gap:10px;">
        <div style="flex:1;background:#070B14;border:1px solid #1E293B;padding:8px 12px;border-radius:8px;font-family:'JetBrains Mono';font-size:11px;color:#CBD5E1;display:flex;align-items:center;gap:6px;">
          <span>📄</span> <span>Apex_Milestone1_Scope_Signed.pdf (1.2 MB)</span>
        </div>
        <div style="flex:1;background:#070B14;border:1px solid #1E293B;padding:8px 12px;border-radius:8px;font-family:'JetBrains Mono';font-size:11px;color:#CBD5E1;display:flex;align-items:center;gap:6px;">
          <span>📅</span> <span>Thu_10AM_GST_Calendar_Invite.ics</span>
        </div>
      </div>

      <!-- 1-Click Tone Toggle & Security Hash -->
      <div style="display:flex;flex-direction:column;gap:8px;">
        <div style="display:flex;gap:8px;">
          <div style="flex:1;background:rgba(56,189,248,0.15);border:1px solid #0284C7;border-radius:8px;padding:9px;text-align:center;font-size:11.5px;font-weight:700;color:#38BDF8;">
            ✓ Formal Board Protocol (Active)
          </div>
          <div style="flex:1;background:#070B14;border:1px solid #1E293B;border-radius:8px;padding:9px;text-align:center;font-size:11.5px;font-weight:700;color:#94A3B8;">
            ⚡ 2-Sentence CEO Memo
          </div>
          <div style="flex:1;background:#070B14;border:1px solid #1E293B;border-radius:8px;padding:9px;text-align:center;font-size:11.5px;font-weight:700;color:#94A3B8;">
            🤝 Strategic Growth Focus
          </div>
        </div>
        <div style="font-family:'JetBrains Mono';font-size:11px;color:#64748B;text-align:center;">
          Immutable SHA-256 Draft Hash: 9f83a1b4e2... · Awaiting Step 03 Human Release Trigger
        </div>
      </div>

    </div>

  </div>
</body>
</html>
"""

    # SCENE 4: The Deterministic Human Gate (Grand Sovereign Vault, Filled Cards, Balanced Vertical Alignment)
    scene4_html = head + """
<body>
  <div style="position:absolute;top:30%;left:50%;transform:translate(-50%, -50%);width:950px;height:520px;background:radial-gradient(circle, rgba(22,163,74,0.22) 0%, transparent 70%);pointer-events:none;"></div>

  <div class="hud-pill">
    <span class="hud-tag" style="background:#D97706;color:#FFFFFF;">STEP 03: GOVERNANCE</span>
    <span class="hud-title">THE 1-CLICK HUMAN DECISION GATE · 100% DETERMINISTIC CONTROL</span>
  </div>

  <div style="position:absolute;top:92px;bottom:32px;left:60px;right:60px;display:flex;flex-direction:column;justify-content:space-between;gap:14px;">
    
    <!-- Title Area -->
    <div style="text-align:center;">
      <h2 style="font-family:'Space Grotesk';font-size:38px;font-weight:800;color:#FFFFFF;margin-bottom:4px;">The Non-Negotiable Rule: Zero Rogue AI</h2>
      <p style="font-size:16.5px;color:#94A3B8;line-height:1.45;max-width:1100px;margin:0 auto;">
        The system handles 100% of the heavy synthesis and drafting, but executive leadership retains the sovereign trigger before any external email, Slack notification, or contract dispatch.
      </p>
    </div>

    <!-- Center Stage: Grand Side-by-Side Contrast & Sovereign Approval Vault -->
    <div style="display:grid;grid-template-columns:0.95fr 1.05fr;gap:24px;align-items:stretch;">
      
      <!-- Left: The Unacceptable Risk of Rogue AI -->
      <div class="glass-card" style="border-radius:22px;padding:26px 30px;border:1.5px solid rgba(239,68,68,0.5);box-shadow:0 0 40px rgba(239,68,68,0.15);display:flex;flex-direction:column;gap:14px;">
        <div style="display:flex;align-items:center;gap:10px;">
          <span style="width:10px;height:10px;border-radius:50%;background:#EF4444;box-shadow:0 0 10px #EF4444;"></span>
          <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:800;color:#F87171;text-transform:uppercase;letter-spacing:1px;">THE UNACCEPTABLE RISK: CONSUMER AI</span>
        </div>
        <div style="font-size:19px;font-weight:800;color:#FFFFFF;">What Happens When AI Dispatches Autonomously?</div>
        
        <!-- 4 Distinct Detailed Risk Blocks -->
        <div style="display:flex;flex-direction:column;gap:10px;">
          <div style="background:#070B14;border:1px solid rgba(239,68,68,0.3);padding:12px 14px;border-radius:10px;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#F87171;font-weight:800;font-size:13.5px;">✕ Hallucinated Commercial Promises</span>
              <span style="font-family:'JetBrains Mono';font-size:10px;color:#EF4444;background:rgba(239,68,68,0.15);padding:2px 6px;border-radius:4px;">FINANCIAL LOSS</span>
            </div>
            <div style="font-size:12px;color:#94A3B8;margin-top:3px;">AI invents unapproved discounts, scope expansions, or tight turnaround dates without executive review.</div>
          </div>

          <div style="background:#070B14;border:1px solid rgba(239,68,68,0.3);padding:12px 14px;border-radius:10px;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#F87171;font-weight:800;font-size:13.5px;">✕ Proprietary Data Contamination</span>
              <span style="font-family:'JetBrains Mono';font-size:10px;color:#EF4444;background:rgba(239,68,68,0.15);padding:2px 6px;border-radius:4px;">REGULATORY FINE</span>
            </div>
            <div style="font-size:12px;color:#94A3B8;margin-top:3px;">Client financial statements and confidential terms ingested into public model weights.</div>
          </div>

          <div style="background:#070B14;border:1px solid rgba(239,68,68,0.3);padding:12px 14px;border-radius:10px;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#F87171;font-weight:800;font-size:13.5px;">✕ Irreversible State Mutations</span>
              <span style="font-family:'JetBrains Mono';font-size:10px;color:#EF4444;background:rgba(239,68,68,0.15);padding:2px 6px;border-radius:4px;">OPERATIONAL CHAOS</span>
            </div>
            <div style="font-size:12px;color:#94A3B8;margin-top:3px;">External emails, CRM deal stages, and calendars mutated without human leadership verification.</div>
          </div>

          <div style="background:#070B14;border:1px solid rgba(239,68,68,0.3);padding:12px 14px;border-radius:10px;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#F87171;font-weight:800;font-size:13.5px;">✕ Zero Legal Accountability Trail</span>
              <span style="font-family:'JetBrains Mono';font-size:10px;color:#EF4444;background:rgba(239,68,68,0.15);padding:2px 6px;border-radius:4px;">GOVERNANCE BREACH</span>
            </div>
            <div style="font-size:12px;color:#94A3B8;margin-top:3px;">No cryptographic audit trail linking decisions to an authorized corporate executive or board signatory.</div>
          </div>
        </div>

        <div style="background:rgba(239,68,68,0.12);border:1px solid #DC2626;border-radius:10px;padding:12px 14px;font-family:'JetBrains Mono';font-size:11.5px;color:#FCA5A5;text-align:center;">
          SOVEREIGN RULE: ZERO AUTONOMOUS DISPATCHES · PROHIBITED IN C-SUITE
        </div>
      </div>

      <!-- Right: The Sovereign 1-Click Vault -->
      <div class="glass-card glow-emerald" style="border-radius:24px;padding:26px 30px;border:2px solid #16A34A;display:flex;flex-direction:column;gap:14px;">
        
        <div style="display:flex;justify-content:space-between;align-items:center;">
          <div style="display:flex;align-items:center;gap:8px;">
            <span style="width:10px;height:10px;border-radius:50%;background:#F59E0B;box-shadow:0 0 10px #F59E0B;"></span>
            <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:800;color:#FBBF24;text-transform:uppercase;letter-spacing:1px;">GATE STATE: AWAITING HUMAN REVIEW</span>
          </div>
          <span style="font-family:'JetBrains Mono';font-size:11.5px;color:#4ADE80;font-weight:700;">DUBAI 13:42:08 GST</span>
        </div>

        <div>
          <div style="font-size:20.5px;font-weight:800;color:#FFFFFF;">Apex Capital Milestone 1 & Calendar Confirmation</div>
          <div style="font-family:'JetBrains Mono';font-size:11.5px;color:#94A3B8;margin-top:2px;">Audit Ref: WOC-GATE-8942 · Encrypted SHA-256 Validated · Ready to Dispatch</div>
        </div>

        <!-- Action Payload Summary Box -->
        <div style="background:#070B14;border:1px solid #1E293B;border-radius:12px;padding:12px 16px;font-family:'JetBrains Mono';font-size:12px;color:#CBD5E1;display:grid;grid-template-columns:1fr 1fr;gap:8px;">
          <div><span style="color:#64748B;">Recipient:</span> Tariq Al-Mansoor</div>
          <div><span style="color:#64748B;">Milestone:</span> $50,000 USD</div>
          <div><span style="color:#64748B;">Kickoff Slot:</span> Thu 10:00 AM GST</div>
          <div><span style="color:#64748B;">Sync Stack:</span> Gmail + Cal + ClickUp</div>
        </div>

        <!-- The Sovereign 3D Button -->
        <div style="background:linear-gradient(135deg, #16A34A 0%, #15803D 100%);color:#FFFFFF;padding:20px 30px;border-radius:14px;box-shadow:0 14px 40px rgba(22,163,74,0.6);border:1.5px solid #4ADE80;display:flex;align-items:center;justify-content:space-between;cursor:pointer;">
          <div style="display:flex;align-items:center;gap:14px;">
            <span style="font-size:30px;font-weight:900;">✓</span>
            <div>
              <div style="font-family:'Space Grotesk';font-size:22px;font-weight:800;letter-spacing:0.5px;">APPROVE & DISPATCH</div>
              <div style="font-family:'JetBrains Mono';font-size:11.5px;opacity:0.95;">1-CLICK DETERMINISTIC GATE · AIR-GAPPED TRANSMISSION</div>
            </div>
          </div>
          <span style="background:rgba(255,255,255,0.2);padding:6px 12px;border-radius:6px;font-family:'JetBrains Mono';font-size:11.5px;font-weight:800;">100% SAFE</span>
        </div>

        <!-- Live Audit Trail Log Preview -->
        <div style="background:#070B14;border:1px solid #1E293B;border-radius:12px;padding:12px 16px;font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;display:flex;flex-direction:column;gap:4px;">
          <div style="color:#38BDF8;">[13:41:52] Voice memo sanitized via private Whisper VPC (1.18s)</div>
          <div style="color:#4ADE80;">[13:41:54] AI synthesis completed · 3-bullet digest grounded (100%)</div>
          <div style="color:#CBD5E1;">[13:42:00] Pre-drafted deliverable locked with SHA-256 hash</div>
          <div style="color:#FBBF24;font-weight:700;">[13:42:08] AWAITING SOVEREIGN HUMAN SIGN-OFF BEFORE OUTBOX RELEASE</div>
        </div>

        <!-- Secondary Controls & Security Guarantee -->
        <div style="display:flex;justify-content:space-between;align-items:center;padding-top:6px;border-top:1px solid rgba(51,65,85,0.7);font-family:'JetBrains Mono';font-size:11.5px;color:#86EFAC;">
          <div style="display:flex;gap:14px;">
            <span style="color:#38BDF8;cursor:pointer;">[ ✏️ Edit Draft ]</span>
            <span style="color:#FBBF24;cursor:pointer;">[ ⏸️ Hold for Review ]</span>
            <span style="color:#F87171;cursor:pointer;">[ 🛑 Reject ]</span>
          </div>
          <span>🔒 Air-gapped lock. Zero mutations occur until click.</span>
        </div>
      </div>

    </div>

    <!-- Governance Badges Across Bottom (Grid 4 items, full width) -->
    <div style="display:grid;grid-template-columns:repeat(4, 1fr);gap:16px;">
      <div class="glass-card" style="border-radius:14px;padding:14px 18px;display:flex;align-items:center;gap:12px;border:1px solid #1E293B;">
        <span style="color:#4ADE80;font-size:22px;">🛡️</span>
        <div>
          <div style="font-size:14px;font-weight:700;color:#FFFFFF;">Zero Model Training</div>
          <div style="font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;">Private API with zero data retention</div>
        </div>
      </div>

      <div class="glass-card" style="border-radius:14px;padding:14px 18px;display:flex;align-items:center;gap:12px;border:1px solid #1E293B;">
        <span style="color:#38BDF8;font-size:22px;">⚡</span>
        <div>
          <div style="font-size:14px;font-weight:700;color:#FFFFFF;">Atomic Synchronization</div>
          <div style="font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;">Email + Calendar + CRM in 1 click</div>
        </div>
      </div>

      <div class="glass-card" style="border-radius:14px;padding:14px 18px;display:flex;align-items:center;gap:12px;border:1px solid #1E293B;">
        <span style="color:#FBBF24;font-size:22px;">🔒</span>
        <div>
          <div style="font-size:14px;font-weight:700;color:#FFFFFF;">Immutable Audit Trail</div>
          <div style="font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;">Cryptographic SHA-256 log signed</div>
        </div>
      </div>

      <div class="glass-card" style="border-radius:14px;padding:14px 18px;display:flex;align-items:center;gap:12px;border:1px solid #1E293B;">
        <span style="color:#C084FC;font-size:22px;">⚖️</span>
        <div>
          <div style="font-size:14px;font-weight:700;color:#FFFFFF;">UAE & DIFC Compliant</div>
          <div style="font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;">Law No. 45/2021 Data Protection Ready</div>
        </div>
      </div>
    </div>

  </div>
</body>
</html>
"""

    # SCENE 5: Value Realization, Cumulative Growth & 3-Sprint Roadmap
    scene5_html = head + """
<body>
  <div style="position:absolute;top:15%;right:20%;width:700px;height:700px;background:radial-gradient(circle, rgba(124,58,237,0.18) 0%, transparent 70%);pointer-events:none;"></div>
  <div style="position:absolute;bottom:15%;left:20%;width:700px;height:700px;background:radial-gradient(circle, rgba(2,132,199,0.15) 0%, transparent 70%);pointer-events:none;"></div>

  <div class="hud-pill">
    <span class="hud-tag" style="background:#7C3AED;color:#FFFFFF;">STEP 04: VALUE & ROI</span>
    <span class="hud-title">WEEKLY ROI AUDIT · SPRINT 1 LIVE IN LESS THAN 14 DAYS</span>
  </div>

  <div style="position:absolute;top:92px;bottom:32px;left:60px;right:60px;display:flex;flex-direction:column;justify-content:space-between;gap:16px;">
    
    <!-- Top: 3 Big Metrics Cards -->
    <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:24px;">
      
      <div class="glass-card glow-emerald" style="border-radius:20px;padding:24px 28px;border:1.5px solid rgba(22,163,74,0.5);">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:2px;">
          <span style="font-family:'JetBrains Mono';font-size:12.5px;font-weight:800;color:#4ADE80;text-transform:uppercase;">Time Recovered</span>
          <span style="background:rgba(22,163,74,0.25);color:#4ADE80;font-size:11px;font-weight:800;padding:2px 8px;border-radius:4px;border:1px solid #16A34A;">WEEK 1 AUDIT</span>
        </div>
        <div style="font-family:'JetBrains Mono';font-size:46px;font-weight:800;color:#4ADE80;line-height:1;">9.2 hrs</div>
        <div style="font-size:13.5px;color:#94A3B8;margin-top:6px;">Eliminated administrative email triage & repetitive scheduling friction.</div>
        <div style="font-family:'JetBrains Mono';font-size:11.5px;color:#86EFAC;margin-top:8px;padding-top:8px;border-top:1px solid #1E293B;">
          Annualized: ~478 hours of executive focus reclaimed
        </div>
      </div>

      <div class="glass-card glow-cyan" style="border-radius:20px;padding:24px 28px;border:1.5px solid rgba(56,189,248,0.5);">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:2px;">
          <span style="font-family:'JetBrains Mono';font-size:12.5px;font-weight:800;color:#38BDF8;text-transform:uppercase;">Financial Return</span>
          <span style="background:rgba(2,132,199,0.25);color:#38BDF8;font-size:11px;font-weight:800;padding:2px 8px;border-radius:4px;border:1px solid #0284C7;">@ $39.00 / HR</span>
        </div>
        <div style="font-family:'JetBrains Mono';font-size:46px;font-weight:800;color:#38BDF8;line-height:1;">$358.80 / wk</div>
        <div style="font-size:13.5px;color:#94A3B8;margin-top:6px;">Direct operational value exceeding implementation burn from Sprint 1.</div>
        <div style="font-family:'JetBrains Mono';font-size:11.5px;color:#38BDF8;margin-top:8px;padding-top:8px;border-top:1px solid #1E293B;">
          Annualized Value: $18,657 per executive cockpit
        </div>
      </div>

      <div class="glass-card glow-amber" style="border-radius:20px;padding:24px 28px;border:1.5px solid rgba(245,158,11,0.5);">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:2px;">
          <span style="font-family:'JetBrains Mono';font-size:12.5px;font-weight:800;color:#FBBF24;text-transform:uppercase;">Safety & Governance</span>
          <span style="background:rgba(217,119,6,0.25);color:#FBBF24;font-size:11px;font-weight:800;padding:2px 8px;border-radius:4px;border:1px solid #D97706;">ZERO INCIDENTS</span>
        </div>
        <div style="font-family:'JetBrains Mono';font-size:46px;font-weight:800;color:#FBBF24;line-height:1;">100.0%</div>
        <div style="font-size:13.5px;color:#94A3B8;margin-top:6px;">Human-in-the-loop compliance across all external email and contract dispatches.</div>
        <div style="font-family:'JetBrains Mono';font-size:11.5px;color:#FBBF24;margin-top:8px;padding-top:8px;border-top:1px solid #1E293B;">
          Audit Trail: 100% Cryptographically Logged
        </div>
      </div>

    </div>

    <!-- Center: Cumulative Growth Projection Track -->
    <div class="glass-card" style="border-radius:18px;padding:20px 28px;border:1px solid rgba(56,189,248,0.35);display:flex;justify-content:space-between;align-items:center;">
      <div>
        <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:800;color:#38BDF8;text-transform:uppercase;letter-spacing:1px;display:block;margin-bottom:3px;">CUMULATIVE C-SUITE VALUE REALIZATION TRACK:</span>
        <span style="font-size:15px;color:#CBD5E1;">
          Month 1: <strong>36.8 hrs ($1,435)</strong> [Quick-Win Pilot] ➔ 
          Month 2: <strong>78.4 hrs ($3,057)</strong> [3 Core Depts] ➔ 
          Month 3: <strong>120.0 hrs ($4,680)</strong> [Autonomous SOPs]
        </span>
      </div>
      <div style="display:flex;align-items:center;gap:12px;">
        <span style="font-family:'JetBrains Mono';font-size:12.5px;color:#4ADE80;font-weight:800;background:rgba(22,163,74,0.2);padding:6px 14px;border-radius:8px;border:1px solid #16A34A;">10x NET ROI PROJECTION</span>
      </div>
    </div>

    <!-- Middle: 3-Sprint Roadmap Cards -->
    <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:24px;">
      
      <!-- Sprint 1 -->
      <div class="glass-card" style="border-radius:20px;padding:24px 26px;border:1.5px solid #16A34A;box-shadow:0 0 25px rgba(22,163,74,0.18);display:flex;flex-direction:column;gap:14px;">
        <div>
          <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
            <span style="font-family:'JetBrains Mono';font-size:12.5px;font-weight:800;color:#4ADE80;">SPRINT 01</span>
            <span style="font-family:'JetBrains Mono';font-size:11px;color:#86EFAC;">WEEKS 1–2</span>
          </div>
          <div style="font-size:18.5px;font-weight:800;color:#FFFFFF;margin-bottom:4px;">Friction Audit & Quick-Win Pilot</div>
          <div style="font-size:13px;color:#94A3B8;line-height:1.45;">Deploy 1 safe pilot to recover your first 5–10 hours/week in under 14 days. Zero bureaucracy.</div>
        </div>

        <div style="background:#070B14;border:1px solid #1E293B;border-radius:12px;padding:14px 16px;display:flex;flex-direction:column;gap:8px;font-family:'JetBrains Mono';font-size:11.5px;">
          <div style="color:#4ADE80;">✓ Live Audio Intake Gateway</div>
          <div style="color:#4ADE80;">✓ Air-Gapped Private Sandbox</div>
          <div style="color:#4ADE80;">✓ 1-Click Human Decision Gate</div>
        </div>

        <div style="display:flex;justify-content:space-between;align-items:center;padding-top:8px;border-top:1px solid #1E293B;font-family:'JetBrains Mono';font-size:11.5px;">
          <span style="color:#94A3B8;">Outcome:</span>
          <span style="color:#4ADE80;font-weight:700;">5–10 hrs/wk Recovered</span>
        </div>
      </div>

      <!-- Sprint 2 -->
      <div class="glass-card" style="border-radius:20px;padding:24px 26px;border:1px solid #1E293B;display:flex;flex-direction:column;gap:14px;">
        <div>
          <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
            <span style="font-family:'JetBrains Mono';font-size:12.5px;font-weight:800;color:#38BDF8;">SPRINT 02</span>
            <span style="font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;">WEEKS 3–6</span>
          </div>
          <div style="font-size:18.5px;font-weight:800;color:#FFFFFF;margin-bottom:4px;">Department Workflow Integration</div>
          <div style="font-size:13px;color:#94A3B8;line-height:1.45;">Expand proven workflows across Sales, Operations, and Delivery leads with connected tools.</div>
        </div>

        <div style="background:#070B14;border:1px solid #1E293B;border-radius:12px;padding:14px 16px;display:flex;flex-direction:column;gap:8px;font-family:'JetBrains Mono';font-size:11.5px;">
          <div style="color:#38BDF8;">✓ WhatsApp + Slack + CRM Sync</div>
          <div style="color:#38BDF8;">✓ Calendar & Contract Pre-Drafts</div>
          <div style="color:#38BDF8;">✓ Cross-Functional Lead Routing</div>
        </div>

        <div style="display:flex;justify-content:space-between;align-items:center;padding-top:8px;border-top:1px solid #1E293B;font-family:'JetBrains Mono';font-size:11.5px;">
          <span style="color:#94A3B8;">Outcome:</span>
          <span style="color:#38BDF8;font-weight:700;">3 Core Depts Operational</span>
        </div>
      </div>

      <!-- Sprint 3 -->
      <div class="glass-card" style="border-radius:20px;padding:24px 26px;border:1px solid #1E293B;display:flex;flex-direction:column;gap:14px;">
        <div>
          <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
            <span style="font-family:'JetBrains Mono';font-size:12.5px;font-weight:800;color:#C084FC;">SPRINT 03</span>
            <span style="font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;">WEEKS 7–12</span>
          </div>
          <div style="font-size:18.5px;font-weight:800;color:#FFFFFF;margin-bottom:4px;">Living SOPs & Team Autonomy</div>
          <div style="font-size:13px;color:#94A3B8;line-height:1.45;">Document all workflows into living Playbooks. Zero vendor lock-in: your team retains mastery.</div>
        </div>

        <div style="background:#070B14;border:1px solid #1E293B;border-radius:12px;padding:14px 16px;display:flex;flex-direction:column;gap:8px;font-family:'JetBrains Mono';font-size:11.5px;">
          <div style="color:#C084FC;">✓ Markdown Architecture Docs</div>
          <div style="color:#C084FC;">✓ Self-Healing Error Watchdogs</div>
          <div style="color:#C084FC;">✓ 100% Client Team Ownership</div>
        </div>

        <div style="display:flex;justify-content:space-between;align-items:center;padding-top:8px;border-top:1px solid #1E293B;font-family:'JetBrains Mono';font-size:11.5px;">
          <span style="color:#94A3B8;">Outcome:</span>
          <span style="color:#C084FC;font-weight:700;">Zero Vendor Lock-In</span>
        </div>
      </div>

    </div>

    <!-- Bottom Ribbon with High-Impact Upwork CTA -->
    <div class="glass-card" style="border-radius:16px;padding:16px 28px;display:flex;justify-content:space-between;align-items:center;">
      <div style="display:flex;align-items:center;gap:10px;">
        <span style="width:8px;height:8px;border-radius:50%;background:#4ADE80;box-shadow:0 0 8px #4ADE80;"></span>
        <span style="font-size:13.5px;color:#CBD5E1;">Ready for immediate deployment with scheduled UAE business hours alignment.</span>
      </div>
      <div style="font-family:'JetBrains Mono';font-size:13.5px;font-weight:800;color:#38BDF8;display:flex;align-items:center;gap:14px;">
        <span>Flávio Barros · Upwork Expert Tier ($39/hr)</span>
        <span style="background:rgba(2,132,199,0.25);border:1px solid #0284C7;color:#38BDF8;padding:5px 12px;border-radius:6px;">Start Pilot &lt; 14 Days →</span>
      </div>
    </div>

  </div>
</body>
</html>
"""

    scenes = [
        ("scene1.html", "scene1.png", scene1_html),
        ("scene2.html", "scene2.png", scene2_html),
        ("scene3.html", "scene3.png", scene3_html),
        ("scene4.html", "scene4.png", scene4_html),
        ("scene5.html", "scene5.png", scene5_html),
    ]

    print("Rendering 5 Rich 1920x1080 HTML Scenes via Chrome Headless...")
    for html_name, png_name, html_content in scenes:
        html_file = os.path.join(scenes_dir, html_name)
        png_file = os.path.join(scenes_dir, png_name)
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        cmd = [
            chrome_path,
            "--headless=new",
            f"--screenshot={png_file}",
            "--window-size=1920,1080",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            f"file:///{html_file}"
        ]
        subprocess.run(cmd, check=True)
        time.sleep(0.5)
        sz = os.path.getsize(png_file)
        print(f"  [OK] Rendered {png_name}: {sz/1024:.1f} KB")

if __name__ == "__main__":
    generate_html_scenes()
