import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

base_dir = r"W:\workspaces antigravity\opportunity-cockpit-showcase\assets"
preview_path = os.path.join(base_dir, "showcase_preview.png")
hero_path = os.path.join(base_dir, "hero_executive_dubai.jpg")
scenes_dir = os.path.join(base_dir, "scenes")
os.makedirs(scenes_dir, exist_ok=True)

preview_img = Image.open(preview_path).convert("RGBA")
hero_img = Image.open(hero_path).convert("RGBA")
pw, ph = preview_img.size

# Fonts
try:
    font_title = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 46)
    font_sub = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 26)
    font_bold = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 30)
    font_body = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 22)
    font_mono = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 20)
    font_tag = ImageFont.truetype(r"C:\Windows\Fonts\consolab.ttf", 16)
except Exception:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_bold = font_title
    font_body = font_title
    font_mono = font_title
    font_tag = font_title

def create_base_canvas():
    bg = Image.new("RGBA", (1920, 1080), (7, 11, 20, 255))
    draw = ImageDraw.Draw(bg)
    # Subtle dark blue/cyan radial glow at center
    for r in range(500, 0, -50):
        alpha = int(25 * (1 - r / 500))
        draw.ellipse([(960 - r, 540 - r), (960 + r, 540 + r)], fill=(6, 182, 212, alpha))
    return bg

# --- SCENE 1: DUBAI INTRO ---
def build_scene1():
    canvas = Image.new("RGBA", (1920, 1080), (7, 11, 20, 255))
    # Resize hero image to fill 1920x1080
    hero_scaled = hero_img.resize((1920, 1080), Image.LANCZOS)
    # Darken with vignette
    overlay = Image.new("RGBA", (1920, 1080), (7, 11, 20, 160))
    canvas.paste(hero_scaled, (0, 0))
    canvas.paste(overlay, (0, 0), overlay)

    draw = ImageDraw.Draw(canvas)
    
    # Header tag
    draw.rounded_rectangle([710, 280, 1210, 325], radius=8, fill=(15, 23, 42, 220), outline=(6, 182, 212, 200), width=1)
    draw.text((735, 292), "⚡ PRINCIPLE: THINK BIG · START SMALL · SCALE FAST", font=font_tag, fill=(6, 182, 212, 255))

    # Main Card
    draw.rounded_rectangle([360, 350, 1560, 750], radius=24, fill=(13, 20, 36, 235), outline=(30, 41, 59, 255), width=2)
    
    # Title
    draw.text((420, 400), "Executive AI Command Center", font=font_title, fill=(255, 255, 255, 255))
    draw.text((420, 465), "Tailored for C-Suite Leadership & Executive Operations in Dubai", font=font_sub, fill=(148, 163, 184, 255))
    
    # Badges
    badges = [
        ("5–10h / Week", "Leadership Time Saved", (16, 185, 129)),
        ("100% Control", "Deterministic 1-Click Human Gate", (6, 182, 212)),
        ("< 14 Days", "Sprint 1 Quick-Win Pilot", (168, 85, 247))
    ]
    for i, (b_title, b_sub, color) in enumerate(badges):
        bx = 420 + i * 380
        draw.rounded_rectangle([bx, 550, bx + 340, 680], radius=16, fill=(15, 23, 42, 255), outline=(30, 41, 59, 255), width=1)
        draw.text((bx + 25, 570), b_title, font=font_bold, fill=color)
        draw.text((bx + 25, 620), b_sub, font=font_body, fill=(148, 163, 184, 255))

    canvas.save(os.path.join(scenes_dir, "scene1.png"))
    print("[OK] Scene 1 generated")

# --- SCENE 2: VOICE INGESTION ---
def build_scene2():
    canvas = create_base_canvas()
    draw = ImageDraw.Draw(canvas)

    # Top Navigation Bar simulation
    draw.rectangle([0, 0, 1920, 70], fill=(13, 20, 36, 255))
    draw.line([(0, 70), (1920, 70)], fill=(30, 41, 59, 255), width=1)
    draw.text((60, 20), "Ω  Executive AI Command Center  ·  Dubai Operations Cockpit", font=font_bold, fill=(255, 255, 255, 255))
    draw.rounded_rectangle([1550, 15, 1860, 55], radius=6, fill=(6, 78, 59, 200), outline=(16, 185, 129, 255))
    draw.text((1575, 25), "● 1-CLICK HUMAN GATE ACTIVE", font=font_tag, fill=(16, 185, 129, 255))

    # Crop the Voice Ingestion Card from showcase_preview.png
    # Coordinates in 1280x2400: x=40..450, y=550..1200
    crop_voice = preview_img.crop((35, 540, 455, 1240))
    # Scale to height 850 preserving aspect ratio
    vh = 850
    vw = int(crop_voice.width * (vh / crop_voice.height))
    crop_voice_scaled = crop_voice.resize((vw, vh), Image.LANCZOS)

    # Paste on left
    canvas.paste(crop_voice_scaled, (100, 130), crop_voice_scaled)
    # Add border around cropped module
    draw.rounded_rectangle([98, 128, 102 + vw, 132 + vh], radius=16, outline=(6, 182, 212, 180), width=2)

    # Right side: Executive explanation card
    draw.rounded_rectangle([100 + vw + 60, 130, 1820, 980], radius=20, fill=(13, 20, 36, 240), outline=(30, 41, 59, 255), width=2)
    
    rx = 100 + vw + 110
    draw.rounded_rectangle([rx, 180, rx + 240, 220], radius=6, fill=(15, 23, 42, 255), outline=(6, 182, 212, 200))
    draw.text((rx + 15, 190), "STEP 01: VOICE INGESTION", font=font_tag, fill=(6, 182, 212, 255))

    draw.text((rx, 250), "Instant Executive Triage", font=font_title, fill=(255, 255, 255, 255))
    draw.text((rx, 315), "From Unstructured Audio to Structured Business Intelligence", font=font_sub, fill=(148, 163, 184, 255))

    points = [
        ("🎙️ Multi-Channel Capture", "The CEO or VP simply sends a voice note via Slack or WhatsApp on the go."),
        ("⚡ 1.2s Real-Time Processing", "Whisper-tier neural transcription extracts dates, dollar amounts, and deadlines."),
        ("🛡️ Zero Data Leakage", "All PII (client names, account details) sanitized before private model inference."),
        ("🛑 Zero Hallucination", "The system never extrapolates or invents deliverables not present in the brief.")
    ]
    for i, (p_title, p_desc) in enumerate(points):
        py = 390 + i * 135
        draw.rounded_rectangle([rx, py, 1770, py + 115], radius=12, fill=(15, 23, 42, 220), outline=(30, 41, 59, 200), width=1)
        draw.text((rx + 25, py + 20), p_title, font=font_bold, fill=(255, 255, 255, 255))
        draw.text((rx + 25, py + 65), p_desc, font=font_body, fill=(148, 163, 184, 255))

    canvas.save(os.path.join(scenes_dir, "scene2.png"))
    print("[OK] Scene 2 generated")
    print("[OK] Scene 3 generated")
    print("[OK] Scene 4 generated")
    print("[OK] Scene 5 generated")

# --- SCENE 3: AI SYNTHESIS ---
def build_scene3():
    canvas = create_base_canvas()
    draw = ImageDraw.Draw(canvas)

    # Top Bar
    draw.rectangle([0, 0, 1920, 70], fill=(13, 20, 36, 255))
    draw.line([(0, 70), (1920, 70)], fill=(30, 41, 59, 255), width=1)
    draw.text((60, 20), "Ω  Executive AI Command Center  ·  Strategic Synthesis Engine", font=font_bold, fill=(255, 255, 255, 255))

    # Crop the Center Column (Synthesis + Draft)
    crop_center = preview_img.crop((440, 540, 960, 1240))
    vh = 850
    vw = int(crop_center.width * (vh / crop_center.height))
    crop_center_scaled = crop_center.resize((vw, vh), Image.LANCZOS)

    canvas.paste(crop_center_scaled, (100, 130), crop_center_scaled)
    draw.rounded_rectangle([98, 128, 102 + vw, 132 + vh], radius=16, outline=(16, 185, 129, 180), width=2)

    # Right side explanation
    rx = 100 + vw + 60
    draw.rounded_rectangle([rx, 130, 1820, 980], radius=20, fill=(13, 20, 36, 240), outline=(30, 41, 59, 255), width=2)
    
    tx = rx + 50
    draw.rounded_rectangle([tx, 180, tx + 240, 220], radius=6, fill=(15, 23, 42, 255), outline=(16, 185, 129, 200))
    draw.text((tx + 15, 190), "STEP 02: AI SYNTHESIS", font=font_tag, fill=(16, 185, 129, 255))

    draw.text((tx, 250), "3-Bullet Decision Digest", font=font_title, fill=(255, 255, 255, 255))
    draw.text((tx, 315), "Pre-Drafted Executive Deliverables Ready for Sign-Off", font=font_sub, fill=(148, 163, 184, 255))

    points = [
        ("🎯 Immediate Strategic Impact", "Extracts revenue at risk ($50k Milestone), resource blockers, and deadline shifts."),
        ("📝 Pre-Drafted Client Response", "Professional, high-stakes communication drafted in the CEO's precise voice."),
        ("⚡ 1-Click Tone Calibration", "Toggle instantly between full executive context and concise WhatsApp tone."),
        ("📊 Zero Context Switching", "Leadership makes million-dollar operational decisions in under 15 seconds.")
    ]
    for i, (p_title, p_desc) in enumerate(points):
        py = 390 + i * 135
        draw.rounded_rectangle([tx, py, 1770, py + 115], radius=12, fill=(15, 23, 42, 220), outline=(30, 41, 59, 200), width=1)
        draw.text((tx + 25, py + 20), p_title, font=font_bold, fill=(255, 255, 255, 255))
        draw.text((tx + 25, py + 65), p_desc, font=font_body, fill=(148, 163, 184, 255))

    canvas.save(os.path.join(scenes_dir, "scene3.png"))
    print("[OK] Scene 3 generated")

# --- SCENE 4: HUMAN DECISION GATE ---
def build_scene4():
    canvas = create_base_canvas()
    draw = ImageDraw.Draw(canvas)

    # Top Bar
    draw.rectangle([0, 0, 1920, 70], fill=(13, 20, 36, 255))
    draw.line([(0, 70), (1920, 70)], fill=(30, 41, 59, 255), width=1)
    draw.text((60, 20), "Ω  Executive AI Command Center  ·  Corporate Governance Gate", font=font_bold, fill=(255, 255, 255, 255))

    # Center Hero Card for Gate
    draw.rounded_rectangle([200, 140, 1720, 960], radius=24, fill=(13, 20, 36, 245), outline=(16, 185, 129, 255), width=2)
    
    # Tag
    draw.rounded_rectangle([760, 180, 1160, 225], radius=8, fill=(15, 23, 42, 255), outline=(245, 158, 11, 255))
    draw.text((790, 192), "● STEP 03: GOVERNANCE & SAFETY GATE", font=font_tag, fill=(245, 158, 11, 255))

    draw.text((540, 250), "The 1-Click Human Decision Gate", font=font_title, fill=(255, 255, 255, 255))
    draw.text((560, 315), "Nothing leaves your company without explicit executive sign-off.", font=font_sub, fill=(148, 163, 184, 255))

    # Big interactive gate button mockup in center
    draw.rounded_rectangle([320, 380, 1600, 680], radius=16, fill=(15, 23, 42, 255), outline=(30, 41, 59, 255), width=2)
    
    draw.text((360, 420), "GOVERNANCE STATE:", font=font_mono, fill=(148, 163, 184, 255))
    draw.text((580, 418), "● AWAITING HUMAN APPROVAL (CEO / VP)", font=font_bold, fill=(245, 158, 11, 255))
    
    # Action Buttons
    draw.rounded_rectangle([360, 490, 960, 590], radius=12, fill=(16, 185, 129, 255))
    draw.text((510, 525), "✓ Approve & Dispatch", font=font_bold, fill=(0, 0, 0, 255))

    draw.rounded_rectangle([1000, 490, 1560, 590], radius=12, fill=(30, 41, 59, 255), outline=(71, 85, 105, 255))
    draw.text((1180, 525), "⚡ Shorter Tone", font=font_bold, fill=(255, 255, 255, 255))

    draw.text((360, 620), "Immutable Audit Trail: Dispatched via encrypted SMTP · ClickUp Sprint sync · Calendar locked", font=font_mono, fill=(100, 116, 139, 255))

    # Bottom 3 guarantees
    guarantees = [
        ("🛡️ Zero Rogue AI", "No unauthorized emails or external client dispatches."),
        ("📜 Full Audit Log", "Every sign-off tracked with timestamp and approver ID."),
        ("⚖️ Enterprise Safe", "Compliant with C-Suite governance protocols in Dubai.")
    ]
    for i, (g_title, g_desc) in enumerate(guarantees):
        gx = 320 + i * 440
        draw.rounded_rectangle([gx, 720, gx + 400, 890], radius=12, fill=(15, 23, 42, 200), outline=(30, 41, 59, 255))
        draw.text((gx + 25, 750), g_title, font=font_bold, fill=(16, 185, 129, 255))
        draw.text((gx + 25, 800), g_desc, font=font_body, fill=(148, 163, 184, 255))

    canvas.save(os.path.join(scenes_dir, "scene4.png"))
    print("[OK] Scene 4 generated")

# --- SCENE 5: ROI & ROADMAP ---
def build_scene5():
    canvas = create_base_canvas()
    draw = ImageDraw.Draw(canvas)

    # Top Bar
    draw.rectangle([0, 0, 1920, 70], fill=(13, 20, 36, 255))
    draw.line([(0, 70), (1920, 70)], fill=(30, 41, 59, 255), width=1)
    draw.text((60, 20), "Ω  Executive AI Command Center  ·  Implementation Roadmap & ROI", font=font_bold, fill=(255, 255, 255, 255))

    # Top Stats Bar
    stats = [
        ("5–10 Hours", "Recovered Every Week", (16, 185, 129)),
        ("$358.80 / wk", "Value Recovered ($39/hr)", (6, 182, 212)),
        ("0 Incidents", "Rogue AI Protection", (168, 85, 247)),
        ("< 14 Days", "Sprint 1 Pilot Live", (245, 158, 11))
    ]
    for i, (st, ss, color) in enumerate(stats):
        sx = 120 + i * 430
        draw.rounded_rectangle([sx, 120, sx + 390, 230], radius=14, fill=(13, 20, 36, 240), outline=(30, 41, 59, 255))
        draw.text((sx + 30, 140), st, font=font_bold, fill=color)
        draw.text((sx + 30, 185), ss, font=font_body, fill=(148, 163, 184, 255))

    # 3 Sprints Roadmap Cards
    sprints = [
        ("SPRINT 01", "WEEKS 1–2", "Friction Audit & Quick-Win Pilot", "We map your highest-friction daily bottleneck. Within 14 days, we deploy 1 safe pilot to recover your first 5–10 hours/week.", (6, 182, 212)),
        ("SPRINT 02", "WEEKS 3–6", "Department Workflow Automation", "Expand proven workflows to key department leads (Sales, Operations, Delivery). Deterministic Human Decision Gates across all stacks.", (16, 185, 129)),
        ("SPRINT 03", "WEEKS 7–12", "Living SOPs & Team Autonomy", "Document all workflows into living Playbooks and train internal leads. Zero vendor lock-in: your team retains full mastery.", (168, 85, 247))
    ]
    for i, (stag, sweeks, stitle, sdesc, color) in enumerate(sprints):
        bx = 120 + i * 575
        draw.rounded_rectangle([bx, 280, bx + 535, 840], radius=20, fill=(13, 20, 36, 250), outline=color, width=2)
        draw.rounded_rectangle([bx + 35, 320, bx + 160, 360], radius=6, fill=(15, 23, 42, 255), outline=color)
        draw.text((bx + 50, 330), stag, font=font_tag, fill=color)
        draw.text((bx + 180, 330), sweeks, font=font_mono, fill=(148, 163, 184, 255))
        
        draw.text((bx + 35, 400), stitle, font=font_bold, fill=(255, 255, 255, 255))
        
        # Word wrap description
        words = sdesc.split()
        lines = []
        cur = []
        for w in words:
            cur.append(w)
            if len(" ".join(cur)) > 30:
                lines.append(" ".join(cur))
                cur = []
        if cur: lines.append(" ".join(cur))
        
        for li, line in enumerate(lines):
            draw.text((bx + 35, 480 + li * 36), line, font=font_body, fill=(148, 163, 184, 255))

    # Bottom Callout
    draw.rounded_rectangle([120, 890, 1800, 990], radius=16, fill=(6, 78, 59, 150), outline=(16, 185, 129, 255), width=1)
    draw.text((460, 925), "⚡ Think Big, Start Small, Scale Fast · Available for Immediate Sprint 1 Kickoff", font=font_bold, fill=(16, 185, 129, 255))

    canvas.save(os.path.join(scenes_dir, "scene5.png"))
    print("[OK] Scene 5 generated")

build_scene1()
build_scene2()
build_scene3()
build_scene4()
build_scene5()
print("All 5 pristine 1920x1080 scenes generated successfully!")
