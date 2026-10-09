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
    # Common head with executive fonts, blueprint grid, and ambient glow
    head = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&family=Plus+Jakarta+Sans:wght@700;800&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1920px;
    height: 1080px;
    overflow: hidden;
    background: #060911;
    color: #F8FAFC;
    font-family: 'Inter', sans-serif;
    position: relative;
    -webkit-font-smoothing: antialiased;
    background-image: 
      linear-gradient(rgba(30, 41, 59, 0.22) 1px, transparent 1px),
      linear-gradient(90deg, rgba(30, 41, 59, 0.22) 1px, transparent 1px);
    background-size: 48px 48px;
  }
  .hud-pill {
    position: absolute;
    top: 32px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(13, 20, 36, 0.96);
    border: 1px solid rgba(56, 189, 248, 0.35);
    box-shadow: 0 8px 32px rgba(0,0,0,0.6), 0 0 24px rgba(56, 189, 248, 0.2);
    border-radius: 9999px;
    padding: 10px 32px;
    display: flex;
    align-items: center;
    gap: 18px;
    z-index: 50;
  }
  .hud-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 800;
    padding: 4px 12px;
    border-radius: 6px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  .hud-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    font-weight: 800;
    letter-spacing: 0.5px;
    color: #FFFFFF;
  }
  .glass-card {
    background: rgba(13, 20, 36, 0.92);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(51, 65, 85, 0.8);
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
  }
</style>
</head>
"""

    # SCENE 1: Executive Command Center Overview (Burj Khalifa Penthouse)
    scene1_html = head + f"""
<body>
  <div style="position:absolute;inset:0;background:url('file:///{hero_img_path}') center/cover no-repeat;filter:brightness(0.72);"></div>
  <div style="position:absolute;inset:0;background:radial-gradient(circle at center, rgba(6,9,17,0.35) 0%, rgba(6,9,17,0.85) 100%);"></div>

  <div class="hud-pill">
    <span class="hud-tag" style="background:#0284C7;color:#FFFFFF;">EXECUTIVE BRIEFING</span>
    <span class="hud-title">EXECUTIVE AI COMMAND CENTER · DUBAI C-SUITE OPERATIONS</span>
  </div>

  <div style="position:absolute;bottom:64px;left:70px;right:70px;display:flex;justify-content:space-between;align-items:flex-end;">
    <div class="glass-card" style="max-width:920px;border-radius:24px;padding:38px 46px;border:1px solid rgba(56,189,248,0.3);">
      <div style="display:flex;gap:12px;margin-bottom:14px;">
        <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:800;background:rgba(2,132,199,0.25);color:#38BDF8;padding:4px 12px;border-radius:6px;border:1px solid #0284C7;">DUBAI, UAE (GST UTC+4)</span>
        <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:800;background:rgba(22,163,74,0.25);color:#4ADE80;padding:4px 12px;border-radius:6px;border:1px solid #16A34A;">ZERO ROGUE AI ACTIVE</span>
        <span style="font-family:'JetBrains Mono';font-size:12px;font-weight:800;background:rgba(217,119,6,0.25);color:#FBBF24;padding:4px 12px;border-radius:6px;border:1px solid #D97706;">EXPERT TIER $39/HR</span>
      </div>
      <h1 style="font-family:'Plus Jakarta Sans';font-size:44px;font-weight:800;line-height:1.15;color:#FFFFFF;margin-bottom:14px;">Turning Raw AI Models into Trusted Leadership Habits</h1>
      <p style="font-size:18px;color:#94A3B8;line-height:1.55;">A disciplined operational framework for CEOs and Department Leads in Dubai. Ingest unstructured voice communications, synthesize decision digests, and enforce 1-click deterministic governance.</p>
    </div>

    <div style="display:flex;gap:20px;">
      <div class="glass-card" style="border-radius:20px;padding:28px 36px;text-align:center;min-width:230px;border:1px solid rgba(22,163,74,0.45);">
        <div style="font-family:'JetBrains Mono';font-size:44px;font-weight:800;color:#4ADE80;line-height:1;">5–10h</div>
        <div style="font-size:13px;font-weight:700;color:#94A3B8;text-transform:uppercase;margin-top:8px;letter-spacing:0.5px;">Weekly Recovered</div>
        <div style="font-family:'JetBrains Mono';font-size:11px;color:#16A34A;margin-top:4px;font-weight:800;">SPRINT 01 PILOT</div>
      </div>
      <div class="glass-card" style="border-radius:20px;padding:28px 36px;text-align:center;min-width:230px;border:1px solid rgba(56,189,248,0.45);">
        <div style="font-family:'JetBrains Mono';font-size:44px;font-weight:800;color:#38BDF8;line-height:1;">100%</div>
        <div style="font-size:13px;font-weight:700;color:#94A3B8;text-transform:uppercase;margin-top:8px;letter-spacing:0.5px;">Deterministic</div>
        <div style="font-family:'JetBrains Mono';font-size:11px;color:#0284C7;margin-top:4px;font-weight:800;">HUMAN GATE IN 1-CLICK</div>
      </div>
    </div>
  </div>
</body>
</html>
"""

    # SCENE 2: Real-time Ingestion & Voice Triage (Rich Full-Bleed 1920x1080)
    scene2_html = head + """
<body>
  <!-- Ambient Glow -->
  <div style="position:absolute;top:10%;left:15%;width:600px;height:600px;background:radial-gradient(circle, rgba(2,132,199,0.18) 0%, transparent 70%);pointer-events:none;"></div>
  <div style="position:absolute;bottom:10%;right:15%;width:600px;height:600px;background:radial-gradient(circle, rgba(22,163,74,0.15) 0%, transparent 70%);pointer-events:none;"></div>

  <div class="hud-pill">
    <span class="hud-tag" style="background:#16A34A;color:#FFFFFF;">STEP 01: INTAKE</span>
    <span class="hud-title">REAL-TIME VOICE INGESTION · SANITIZED IN 1.2s · ZERO LEAKAGE</span>
  </div>

  <div style="position:absolute;inset:104px 60px 48px 60px;display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:stretch;">
    
    <!-- Left Column: Audio Intake Stream -->
    <div class="glass-card" style="border-radius:22px;padding:32px 36px;display:flex;flex-direction:column;justify-content:space-between;border:1px solid rgba(56,189,248,0.35);">
      
      <div>
        <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #1E293B;padding-bottom:16px;margin-bottom:20px;">
          <div style="display:flex;align-items:center;gap:16px;">
            <div style="width:54px;height:54px;border-radius:14px;background:#0369A1;display:flex;align-items:center;justify-content:center;font-size:26px;box-shadow:0 0 20px rgba(3,105,161,0.5);">🎙️</div>
            <div>
              <div style="font-size:20px;font-weight:800;color:#FFFFFF;">VP of Operations (Dubai)</div>
              <div style="font-family:'JetBrains Mono';font-size:13px;color:#38BDF8;">WhatsApp & Slack Corporate Intake Gateway</div>
            </div>
          </div>
          <span style="font-family:'JetBrains Mono';font-size:13px;font-weight:800;background:rgba(22,163,74,0.2);color:#4ADE80;border:1px solid #16A34A;padding:6px 14px;border-radius:8px;">0:32 HD AUDIO MEMO</span>
        </div>

        <!-- High-End Soundwave Visualizer -->
        <div style="background:#080C16;border:1px solid #1E293B;border-radius:16px;padding:22px 26px;margin-bottom:22px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
            <span style="font-family:'JetBrains Mono';font-size:12px;color:#94A3B8;text-transform:uppercase;">Stereo Frequency Waveform</span>
            <span style="font-family:'JetBrains Mono';font-size:12px;color:#4ADE80;font-weight:700;">● Active Stream · 24kHz Opus</span>
          </div>
          <div style="display:flex;align-items:center;gap:6px;height:64px;">
            <div style="width:7px;height:24px;background:#38BDF8;border-radius:4px;"></div>
            <div style="width:7px;height:48px;background:#0284C7;border-radius:4px;"></div>
            <div style="width:7px;height:32px;background:#38BDF8;border-radius:4px;"></div>
            <div style="width:7px;height:58px;background:#4ADE80;border-radius:4px;"></div>
            <div style="width:7px;height:36px;background:#0284C7;border-radius:4px;"></div>
            <div style="width:7px;height:52px;background:#38BDF8;border-radius:4px;"></div>
            <div style="width:7px;height:44px;background:#4ADE80;border-radius:4px;"></div>
            <div style="width:7px;height:64px;background:#0284C7;border-radius:4px;"></div>
            <div style="width:7px;height:48px;background:#38BDF8;border-radius:4px;"></div>
            <div style="width:7px;height:30px;background:#0284C7;border-radius:4px;"></div>
            <div style="width:7px;height:56px;background:#4ADE80;border-radius:4px;"></div>
            <div style="width:7px;height:36px;background:#38BDF8;border-radius:4px;"></div>
            <div style="width:7px;height:62px;background:#0284C7;border-radius:4px;"></div>
            <div style="width:7px;height:42px;background:#4ADE80;border-radius:4px;"></div>
            <div style="width:7px;height:28px;background:#38BDF8;border-radius:4px;"></div>
            <div style="width:7px;height:50px;background:#0284C7;border-radius:4px;"></div>
            <div style="width:7px;height:34px;background:#4ADE80;border-radius:4px;"></div>
            <div style="width:7px;height:20px;background:#38BDF8;border-radius:4px;"></div>
          </div>
        </div>

        <!-- Transcript with glowing tags -->
        <div style="background:#080C16;border:1px solid #1E293B;border-radius:16px;padding:22px;font-family:'JetBrains Mono';font-size:15.5px;line-height:1.65;color:#CBD5E1;">
          “Flávio, we just received <span style="color:#38BDF8;font-weight:800;border-bottom:2px solid #0284C7;">Apex Capital's</span> revision. They want to proceed with <span style="color:#4ADE80;font-weight:800;border-bottom:2px solid #16A34A;">Milestone 1 ($50k)</span>, but need delivery onboarding moved to <span style="color:#FBBF24;font-weight:800;border-bottom:2px solid #D97706;">Thursday morning</span>. Can we confirm this before their committee meets at 2 PM?”
        </div>
      </div>

      <div style="display:flex;gap:12px;margin-top:16px;">
        <span style="font-family:'JetBrains Mono';font-size:12px;color:#64748B;">Origin: WhatsApp Voice Note · Encrypted · Sheikh Zayed Rd Executive Ingestion</span>
      </div>
    </div>

    <!-- Right Column: Security Radar & Extracted Entities -->
    <div style="display:flex;flex-direction:column;gap:20px;justify-content:space-between;">
      
      <!-- Top Security Banner -->
      <div class="glass-card" style="border-radius:20px;padding:26px 32px;display:flex;align-items:center;gap:20px;border:1.5px solid #16A34A;box-shadow:0 0 30px rgba(22,163,74,0.2);">
        <div style="width:52px;height:52px;border-radius:50%;background:#16A34A;color:#FFFFFF;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:900;shrink:0;">✓</div>
        <div>
          <div style="font-size:20px;font-weight:800;color:#4ADE80;margin-bottom:2px;">Sanitized & Parsed in 1.2 Seconds</div>
          <div style="font-family:'JetBrains Mono';font-size:13.5px;color:#94A3B8;">PII Strip Active · Enterprise Private API Tier · Zero Model Training on Data</div>
        </div>
      </div>

      <!-- Entity Extraction Matrix -->
      <div class="glass-card" style="border-radius:20px;padding:30px 34px;display:flex;flex-direction:column;gap:14px;">
        <div style="font-family:'JetBrains Mono';font-size:13px;font-weight:800;color:#38BDF8;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;">Structured Entity Extraction:</div>
        
        <div style="display:flex;align-items:center;justify-content:space-between;background:#080C16;padding:14px 20px;border-radius:12px;border:1px solid #1E293B;">
          <span style="color:#94A3B8;font-size:15px;">Target Client Account:</span>
          <span style="color:#FFFFFF;font-weight:800;font-family:'JetBrains Mono';font-size:16px;">Apex Capital (UAE Strategic Account)</span>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;background:#080C16;padding:14px 20px;border-radius:12px;border:1px solid #1E293B;">
          <span style="color:#94A3B8;font-size:15px;">Revenue Milestone:</span>
          <span style="color:#4ADE80;font-weight:800;font-family:'JetBrains Mono';font-size:17px;">$50,000 USD (Milestone 1 Approved)</span>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;background:#080C16;padding:14px 20px;border-radius:12px;border:1px solid #1E293B;">
          <span style="color:#94A3B8;font-size:15px;">Capacity & Onboarding:</span>
          <span style="color:#38BDF8;font-weight:800;font-family:'JetBrains Mono';font-size:16px;">Thursday 10:00 AM GST (Capacity Locked)</span>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;background:#080C16;padding:14px 20px;border-radius:12px;border:1px solid #1E293B;">
          <span style="color:#94A3B8;font-size:15px;">Governance Constraint:</span>
          <span style="color:#FBBF24;font-weight:800;font-family:'JetBrains Mono';font-size:16px;">Requires 1-Click Sign-Off Before 2:00 PM</span>
        </div>
      </div>

      <!-- Bottom Status Pill -->
      <div style="background:rgba(13,20,36,0.85);border:1px solid #1E293B;border-radius:14px;padding:14px 24px;display:flex;justify-content:space-between;align-items:center;">
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
  <!-- Ambient Glow -->
  <div style="position:absolute;top:20%;left:10%;width:600px;height:600px;background:radial-gradient(circle, rgba(22,163,74,0.18) 0%, transparent 70%);pointer-events:none;"></div>
  <div style="position:absolute;bottom:15%;right:10%;width:600px;height:600px;background:radial-gradient(circle, rgba(2,132,199,0.18) 0%, transparent 70%);pointer-events:none;"></div>

  <div class="hud-pill">
    <span class="hud-tag" style="background:#0284C7;color:#FFFFFF;">STEP 02: SYNTHESIS</span>
    <span class="hud-title">AI STRATEGIC SYNTHESIS · 3-BULLET DIGEST · PRE-DRAFTED ACTIONS</span>
  </div>

  <div style="position:absolute;inset:104px 60px 48px 60px;display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:stretch;">
    
    <!-- Left Column: 3 Strategic Decision Bullets -->
    <div style="display:flex;flex-direction:column;gap:18px;justify-content:space-between;">
      
      <div>
        <div style="font-family:'Plus Jakarta Sans';font-size:26px;font-weight:800;color:#FFFFFF;margin-bottom:6px;">Executive Decision Digest</div>
        <div style="font-size:15px;color:#94A3B8;margin-bottom:20px;">Instant board-level triage: 3 high-impact bullets generated in &lt;1.5 seconds.</div>

        <div style="display:flex;flex-direction:column;gap:16px;">
          <div class="glass-card" style="border-radius:18px;padding:24px 28px;display:flex;gap:20px;align-items:flex-start;border:1px solid rgba(22,163,74,0.35);">
            <div style="font-family:'JetBrains Mono';font-size:22px;font-weight:900;color:#4ADE80;background:rgba(22,163,74,0.18);border:1px solid #16A34A;width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;shrink:0;">01</div>
            <div>
              <div style="font-size:18px;font-weight:800;color:#FFFFFF;margin-bottom:4px;">Revenue Milestone Approved</div>
              <div style="font-size:14.5px;color:#94A3B8;line-height:1.5;">Confirms $50,000 for Milestone 1 under approved commercial terms. Risk of scope creep mitigated.</div>
            </div>
          </div>

          <div class="glass-card" style="border-radius:18px;padding:24px 28px;display:flex;gap:20px;align-items:flex-start;border:1px solid rgba(56,189,248,0.35);">
            <div style="font-family:'JetBrains Mono';font-size:22px;font-weight:900;color:#38BDF8;background:rgba(2,132,199,0.18);border:1px solid #0284C7;width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;shrink:0;">02</div>
            <div>
              <div style="font-size:18px;font-weight:800;color:#FFFFFF;margin-bottom:4px;">Calendar & Delivery Alignment</div>
              <div style="font-size:14.5px;color:#94A3B8;line-height:1.5;">Onboarding shifted to Thursday 10:00 AM GST. Engineering leads reserved without meeting overload.</div>
            </div>
          </div>

          <div class="glass-card" style="border-radius:18px;padding:24px 28px;display:flex;gap:20px;align-items:flex-start;border:1px solid rgba(245,158,11,0.35);">
            <div style="font-family:'JetBrains Mono';font-size:22px;font-weight:900;color:#FBBF24;background:rgba(217,119,6,0.18);border:1px solid #D97706;width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;shrink:0;">03</div>
            <div>
              <div style="font-size:18px;font-weight:800;color:#FFFFFF;margin-bottom:4px;">Time-Sensitive Authorization</div>
              <div style="font-size:14.5px;color:#94A3B8;line-height:1.5;">Requires 1-click leadership sign-off prior to Apex 2:00 PM GST committee meeting.</div>
            </div>
          </div>
        </div>
      </div>

      <div style="font-family:'JetBrains Mono';font-size:12.5px;color:#64748B;">Audit Status: Extracted with 100% deterministic accuracy · Zero hallucination check passed</div>

    </div>

    <!-- Right Column: Pre-Drafted Client Deliverable -->
    <div class="glass-card" style="border-radius:22px;padding:34px 38px;display:flex;flex-direction:column;justify-content:space-between;border:1px solid rgba(56,189,248,0.35);">
      <div>
        <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #1E293B;padding-bottom:16px;margin-bottom:18px;">
          <div>
            <div style="font-family:'JetBrains Mono';font-size:13px;font-weight:800;color:#38BDF8;text-transform:uppercase;">Pre-Drafted Deliverable (Waiting for Gate)</div>
            <div style="font-size:13px;color:#94A3B8;margin-top:2px;">Tailored to C-Suite Tone & Voice Guidelines</div>
          </div>
          <span style="font-family:'JetBrains Mono';font-size:11px;background:#1E293B;color:#4ADE80;padding:5px 10px;border-radius:6px;font-weight:700;">READY TO DISPATCH</span>
        </div>

        <div style="background:#080C16;border:1px solid #1E293B;border-radius:14px;padding:24px;font-family:'JetBrains Mono';font-size:14px;line-height:1.65;color:#E2E8F0;">
          <div style="color:#64748B;margin-bottom:12px;border-bottom:1px solid #1E293B;padding-bottom:8px;">
            To: Tariq Al-Mansoor &lt;tariq@apexcapital.ae&gt;<br>
            Subject: Confirmation: Apex Capital Milestone 1 & Thursday Onboarding
          </div>
          Dear Tariq,<br><br>
          Thank you for the update. We are pleased to confirm Milestone 1 ($50,000) under the agreed terms. Our technical delivery leads are already scheduled to kick off the executive onboarding session this Thursday at 10:00 AM GST.<br><br>
          Looking forward to our kickoff.<br>
          Best regards,<br>
          <strong style="color:#38BDF8;">[Executive Leadership]</strong>
        </div>
      </div>

      <div style="display:flex;gap:14px;margin-top:18px;">
        <div style="flex:1;background:rgba(56,189,248,0.12);border:1px solid #0284C7;border-radius:10px;padding:12px;text-align:center;font-size:13px;font-weight:700;color:#38BDF8;">
          ⚡ Alternative 2-Sentence CEO Tone Available in 1-Click
        </div>
      </div>
    </div>

  </div>
</body>
</html>
"""

    # SCENE 4: The Deterministic Human Gate (Rich Full-Bleed 1920x1080)
    scene4_html = head + """
<body>
  <!-- Ambient Glow -->
  <div style="position:absolute;top:30%;left:50%;transform:translate(-50%, -50%);width:900px;height:500px;background:radial-gradient(circle, rgba(22,163,74,0.2) 0%, transparent 70%);pointer-events:none;"></div>

  <div class="hud-pill">
    <span class="hud-tag" style="background:#D97706;color:#FFFFFF;">STEP 03: GOVERNANCE</span>
    <span class="hud-title">THE 1-CLICK HUMAN DECISION GATE · 100% DETERMINISTIC CONTROL</span>
  </div>

  <div style="position:absolute;inset:104px 70px 48px 70px;display:flex;flex-direction:column;justify-content:space-between;align-items:center;">
    
    <div style="max-width:1100px;text-align:center;margin-top:10px;">
      <h2 style="font-family:'Plus Jakarta Sans';font-size:46px;font-weight:800;color:#FFFFFF;margin-bottom:10px;">The Non-Negotiable Rule: Zero Rogue AI</h2>
      <p style="font-size:19px;color:#94A3B8;line-height:1.5;max-width:980px;margin:0 auto;">The system handles 100% of the heavy synthesis and drafting, but executive leadership retains the sovereign trigger before any external email, Slack notification, or contract dispatch.</p>
    </div>

    <!-- The Grand 1-Click Approval Gate Box (Full Width 1360px) -->
    <div class="glass-card" style="border:2px solid #16A34A;box-shadow:0 0 60px rgba(22,163,74,0.3), 0 24px 60px rgba(0,0,0,0.8);border-radius:24px;padding:36px 56px;display:flex;align-items:center;justify-content:space-between;max-width:1380px;width:100%;">
      
      <div style="flex:1;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
          <span style="width:14px;height:14px;border-radius:50%;background:#F59E0B;box-shadow:0 0 14px #F59E0B;display:inline-block;"></span>
          <span style="font-family:'JetBrains Mono';font-size:14px;font-weight:800;color:#FBBF24;text-transform:uppercase;letter-spacing:1px;">Gate State: Awaiting Leadership Review</span>
        </div>
        <div style="font-size:24px;font-weight:800;color:#FFFFFF;margin-bottom:6px;">Apex Capital Milestone 1 & Calendar Confirmation</div>
        <div style="font-family:'JetBrains Mono';font-size:13.5px;color:#64748B;">Audit Ref: WOC-GATE-8942 · Encrypted SHA-256 Validated · Ready to Dispatch</div>
      </div>

      <!-- The Big 3D Button -->
      <div style="background:linear-gradient(135deg, #16A34A 0%, #15803D 100%);color:#FFFFFF;padding:22px 44px;border-radius:18px;box-shadow:0 14px 35px rgba(22,163,74,0.5);border:1px solid #4ADE80;display:flex;align-items:center;gap:18px;cursor:pointer;">
        <span style="font-size:28px;font-weight:900;">✓</span>
        <div style="text-align:left;">
          <div style="font-family:'Plus Jakarta Sans';font-size:21px;font-weight:800;letter-spacing:0.4px;">APPROVE & DISPATCH</div>
          <div style="font-family:'JetBrains Mono';font-size:11.5px;opacity:0.9;">1-CLICK DETERMINISTIC GATE</div>
        </div>
      </div>

    </div>

    <!-- Governance Badges Across Bottom -->
    <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:24px;max-width:1380px;width:100%;">
      <div class="glass-card" style="border-radius:14px;padding:18px 24px;display:flex;align-items:center;gap:14px;border:1px solid #1E293B;">
        <span style="color:#4ADE80;font-size:22px;">🛡️</span>
        <div>
          <div style="font-size:15px;font-weight:700;color:#FFFFFF;">Zero Model Training</div>
          <div style="font-family:'JetBrains Mono';font-size:12px;color:#94A3B8;">Confidential data never leaks to public LLMs</div>
        </div>
      </div>

      <div class="glass-card" style="border-radius:14px;padding:18px 24px;display:flex;align-items:center;gap:14px;border:1px solid #1E293B;">
        <span style="color:#38BDF8;font-size:22px;">⚡</span>
        <div>
          <div style="font-size:15px;font-weight:700;color:#FFFFFF;">Synchronized Dispatch</div>
          <div style="font-family:'JetBrains Mono';font-size:12px;color:#94A3B8;">Email + ClickUp + Google Calendar updated</div>
        </div>
      </div>

      <div class="glass-card" style="border-radius:14px;padding:18px 24px;display:flex;align-items:center;gap:14px;border:1px solid #1E293B;">
        <span style="color:#FBBF24;font-size:22px;">🔒</span>
        <div>
          <div style="font-size:15px;font-weight:700;color:#FFFFFF;">Immutable Audit Trail</div>
          <div style="font-family:'JetBrains Mono';font-size:12px;color:#94A3B8;">Timestamped log signed by Flávio Barros</div>
        </div>
      </div>
    </div>

  </div>
</body>
</html>
"""

    # SCENE 5: Value Realization & ROI Roadmap (Rich Full-Bleed 1920x1080)
    scene5_html = head + """
<body>
  <!-- Ambient Glow -->
  <div style="position:absolute;top:15%;right:20%;width:700px;height:700px;background:radial-gradient(circle, rgba(124,58,237,0.18) 0%, transparent 70%);pointer-events:none;"></div>
  <div style="position:absolute;bottom:15%;left:20%;width:700px;height:700px;background:radial-gradient(circle, rgba(2,132,199,0.15) 0%, transparent 70%);pointer-events:none;"></div>

  <div class="hud-pill">
    <span class="hud-tag" style="background:#7C3AED;color:#FFFFFF;">STEP 04: VALUE & ROI</span>
    <span class="hud-title">WEEKLY ROI AUDIT · SPRINT 1 LIVE IN LESS THAN 14 DAYS</span>
  </div>

  <div style="position:absolute;inset:104px 60px 48px 60px;display:flex;flex-direction:column;justify-content:space-between;">
    
    <!-- Top: 3 Big Metrics Cards -->
    <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:28px;">
      
      <div class="glass-card" style="border-radius:20px;padding:30px 36px;border:1px solid rgba(22,163,74,0.45);">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
          <span style="font-family:'JetBrains Mono';font-size:13px;font-weight:800;color:#4ADE80;text-transform:uppercase;">Time Recovered</span>
          <span style="background:rgba(22,163,74,0.25);color:#4ADE80;font-size:11px;font-weight:800;padding:3px 10px;border-radius:6px;border:1px solid #16A34A;">WEEK 1 AUDIT</span>
        </div>
        <div style="font-family:'JetBrains Mono';font-size:48px;font-weight:800;color:#4ADE80;line-height:1;">9.2 hrs</div>
        <div style="font-size:14.5px;color:#94A3B8;margin-top:8px;">Saved from administrative triage and synchronous meeting overload.</div>
      </div>

      <div class="glass-card" style="border-radius:20px;padding:30px 36px;border:1px solid rgba(56,189,248,0.45);">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
          <span style="font-family:'JetBrains Mono';font-size:13px;font-weight:800;color:#38BDF8;text-transform:uppercase;">Financial Return</span>
          <span style="background:rgba(2,132,199,0.25);color:#38BDF8;font-size:11px;font-weight:800;padding:3px 10px;border-radius:6px;border:1px solid #0284C7;">@ $39.00 / HR</span>
        </div>
        <div style="font-family:'JetBrains Mono';font-size:48px;font-weight:800;color:#38BDF8;line-height:1;">$358.80</div>
        <div style="font-size:14.5px;color:#94A3B8;margin-top:8px;">Immediate weekly value back to business from the very first sprint.</div>
      </div>

      <div class="glass-card" style="border-radius:20px;padding:30px 36px;border:1px solid rgba(245,158,11,0.45);">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
          <span style="font-family:'JetBrains Mono';font-size:13px;font-weight:800;color:#FBBF24;text-transform:uppercase;">Safety & Governance</span>
          <span style="background:rgba(217,119,6,0.25);color:#FBBF24;font-size:11px;font-weight:800;padding:3px 10px;border-radius:6px;border:1px solid #D97706;">ZERO INCIDENTS</span>
        </div>
        <div style="font-family:'JetBrains Mono';font-size:48px;font-weight:800;color:#FBBF24;line-height:1;">100%</div>
        <div style="font-size:14.5px;color:#94A3B8;margin-top:8px;">Human-in-the-loop compliance across all external dispatches.</div>
      </div>

    </div>

    <!-- Middle: 3-Sprint Roadmap Cards -->
    <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:24px;">
      
      <div class="glass-card" style="border-radius:18px;padding:26px 30px;border:1.5px solid #16A34A;box-shadow:0 0 25px rgba(22,163,74,0.15);">
        <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
          <span style="font-family:'JetBrains Mono';font-size:13px;font-weight:800;color:#4ADE80;">SPRINT 01</span>
          <span style="font-family:'JetBrains Mono';font-size:11px;color:#86EFAC;">WEEKS 1–2</span>
        </div>
        <div style="font-size:19px;font-weight:800;color:#FFFFFF;margin-bottom:6px;">Friction Audit & Quick-Win Pilot</div>
        <div style="font-size:14px;color:#94A3B8;line-height:1.45;">Deploy 1 safe pilot to recover your first 5–10 hours/week in under 14 days. Zero bureaucracy.</div>
      </div>

      <div class="glass-card" style="border-radius:18px;padding:26px 30px;border:1px solid #1E293B;">
        <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
          <span style="font-family:'JetBrains Mono';font-size:13px;font-weight:800;color:#38BDF8;">SPRINT 02</span>
          <span style="font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;">WEEKS 3–6</span>
        </div>
        <div style="font-size:19px;font-weight:800;color:#FFFFFF;margin-bottom:6px;">Department Workflow Integration</div>
        <div style="font-size:14px;color:#94A3B8;line-height:1.45;">Expand proven workflows across Sales, Operations, and Delivery leads with connected tools.</div>
      </div>

      <div class="glass-card" style="border-radius:18px;padding:26px 30px;border:1px solid #1E293B;">
        <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
          <span style="font-family:'JetBrains Mono';font-size:13px;font-weight:800;color:#C084FC;">SPRINT 03</span>
          <span style="font-family:'JetBrains Mono';font-size:11px;color:#94A3B8;">WEEKS 7–12</span>
        </div>
        <div style="font-size:19px;font-weight:800;color:#FFFFFF;margin-bottom:6px;">Living SOPs & Team Autonomy</div>
        <div style="font-size:14px;color:#94A3B8;line-height:1.45;">Document all workflows into living Playbooks. Zero vendor lock-in: your team retains mastery.</div>
      </div>

    </div>

    <!-- Bottom Ribbon -->
    <div class="glass-card" style="border-radius:14px;padding:16px 30px;display:flex;justify-content:space-between;align-items:center;">
      <span style="font-size:14px;color:#94A3B8;">Ready for immediate deployment with scheduled UAE business hours alignment.</span>
      <span style="font-family:'JetBrains Mono';font-size:14px;font-weight:800;color:#38BDF8;">Flávio Barros · Upwork Proposal Asset</span>
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
