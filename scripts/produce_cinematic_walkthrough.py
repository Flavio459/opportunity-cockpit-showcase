import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

base_dir = r"W:\workspaces antigravity\opportunity-cockpit-showcase"
assets_dir = os.path.join(base_dir, "assets")
preview_path = os.path.join(assets_dir, "showcase_preview.png")
scenes_dir = os.path.join(assets_dir, "scenes")
audio_dir = os.path.join(assets_dir, "audio")
os.makedirs(scenes_dir, exist_ok=True)

preview = Image.open(preview_path).convert("RGBA")
pw, ph = preview.size

# Fonts
try:
    font_hud_title = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 20)
    font_hud_tag = ImageFont.truetype(r"C:\Windows\Fonts\consolab.ttf", 15)
except Exception:
    font_hud_title = ImageFont.load_default()
    font_hud_tag = font_hud_title

# 5 Perfectly Balanced 16:9 Viewports (1280x720)
SCENE_DEFS = [
    {
        "name": "scene1.png",
        "crop_y": 0,
        "tag": "EXECUTIVE BRIEFING",
        "title": "EXECUTIVE AI COMMAND CENTER · DUBAI C-SUITE OPERATIONS",
        "accent": (6, 182, 212) # cyan
    },
    {
        "name": "scene2.png",
        "crop_y": 480,
        "tag": "STEP 01: INTAKE",
        "title": "REAL-TIME VOICE INGESTION · SANITIZED IN 1.2s · ZERO LEAKAGE",
        "accent": (16, 185, 129) # emerald
    },
    {
        "name": "scene3.png",
        "crop_y": 660,
        "tag": "STEP 02: SYNTHESIS",
        "title": "AI STRATEGIC SYNTHESIS · 3-BULLET DIGEST · PRE-DRAFTED ACTIONS",
        "accent": (16, 185, 129) # emerald
    },
    {
        "name": "scene4.png",
        "crop_y": 820,
        "tag": "STEP 03: GOVERNANCE",
        "title": "THE 1-CLICK HUMAN DECISION GATE · 100% DETERMINISTIC CONTROL",
        "accent": (245, 158, 11) # amber
    },
    {
        "name": "scene5.png",
        "crop_y": 1360,
        "tag": "STEP 04: VALUE & ROI",
        "title": "WEEKLY ROI AUDIT ($358.80 RECOVERED) · SPRINT 1 LIVE IN < 14 DAYS",
        "accent": (168, 85, 247) # purple
    }
]

def generate_scene_slides():
    print("Generating full-bleed 1920x1080 UI scene slides...")
    for s in SCENE_DEFS:
        cy = s["crop_y"]
        # Crop exactly 1280x720 (native 16:9)
        cropped = preview.crop((0, cy, 1280, cy + 720))
        # Upscale with LANCZOS to 1920x1080
        scaled = cropped.resize((1920, 1080), Image.LANCZOS)
        
        # Add subtle top and bottom vignette to draw focus to center UI
        overlay = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
        draw_ov = ImageDraw.Draw(overlay)
        
        # Top gradient bar for HUD
        for y in range(80):
            a = int(180 * (1 - y / 80))
            draw_ov.line([(0, y), (1920, y)], fill=(7, 11, 20, a))
        
        # Floating Executive HUD Pill at Top
        pill_w = 780
        pill_x = (1920 - pill_w) // 2
        draw_ov.rounded_rectangle([pill_x, 20, pill_x + pill_w, 64], radius=10, fill=(13, 20, 36, 235), outline=(30, 41, 59, 255), width=1)
        
        # Tag badge
        draw_ov.rounded_rectangle([pill_x + 12, 28, pill_x + 185, 56], radius=6, fill=(15, 23, 42, 255), outline=s["accent"], width=1)
        draw_ov.text((pill_x + 22, 33), s["tag"], font=font_hud_tag, fill=s["accent"])
        
        # Title text
        draw_ov.text((pill_x + 200, 31), s["title"], font=font_hud_title, fill=(241, 245, 249, 255))
        
        final_frame = Image.alpha_composite(scaled, overlay)
        final_frame.convert("RGB").save(os.path.join(scenes_dir, s["name"]), quality=95)
        print(f"[OK] Generated {s['name']} (1920x1080, Full-Bleed UI)")

def get_duration(audio_path):
    cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{audio_path}"'
    res = subprocess.check_output(cmd, shell=True).decode().strip()
    return float(res)

def render_cinematic_video(audio_filename, out_video_filename):
    audio_path = os.path.join(audio_dir, audio_filename)
    out_video_path = os.path.join(assets_dir, out_video_filename)
    dur = get_duration(audio_path)
    print(f"\nEncoding Cinematic Video for {out_video_filename} (Duration: {dur:.2f}s)...")
    
    # 5 scene timing
    t1 = round(dur * 0.18, 2)
    t2 = round(dur * 0.22, 2)
    t3 = round(dur * 0.22, 2)
    t4 = round(dur * 0.20, 2)
    t5 = round(dur - (t1 + t2 + t3 + t4) + 0.5, 2)

    s1 = os.path.join(scenes_dir, "scene1.png")
    s2 = os.path.join(scenes_dir, "scene2.png")
    s3 = os.path.join(scenes_dir, "scene3.png")
    s4 = os.path.join(scenes_dir, "scene4.png")
    s5 = os.path.join(scenes_dir, "scene5.png")

    # High-quality Ken Burns zoom & smooth pan on each scene + concat
    filter_complex = (
        f"[0:v]zoompan=z='min(zoom+0.0006,1.06)':d={int(t1*30)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fps=30[v0]; "
        f"[1:v]zoompan=z='min(zoom+0.0006,1.06)':d={int(t2*30)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fps=30[v1]; "
        f"[2:v]zoompan=z='min(zoom+0.0006,1.06)':d={int(t3*30)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fps=30[v2]; "
        f"[3:v]zoompan=z='min(zoom+0.0006,1.06)':d={int(t4*30)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fps=30[v3]; "
        f"[4:v]zoompan=z='min(zoom+0.0006,1.06)':d={int(t5*30)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fps=30[v4]; "
        f"[v0][v1][v2][v3][v4]concat=n=5:v=1:a=0[vout]; "
        # Generate subtle ambient harmonic synth drone at -24dB in background
        f"aevalsrc=exprs='0.015*sin(2*PI*110*t)+0.012*sin(2*PI*164.81*t)+0.008*sin(2*PI*220*t)':s=48000:d={dur}[amb]; "
        # Mix narration audio with ambient bed
        f"[5:a]volume=1.0[voice]; "
        f"[amb]volume=0.25,lowpass=f=800[bgpad]; "
        f"[voice][bgpad]amix=inputs=2:duration=first:dropout_transition=2[aout]"
    )

    cmd = (
        f'ffmpeg -y '
        f'-loop 1 -t {t1} -i "{s1}" '
        f'-loop 1 -t {t2} -i "{s2}" '
        f'-loop 1 -t {t3} -i "{s3}" '
        f'-loop 1 -t {t4} -i "{s4}" '
        f'-loop 1 -t {t5} -i "{s5}" '
        f'-i "{audio_path}" '
        f'-filter_complex "{filter_complex}" '
        f'-map "[vout]" -map "[aout]" '
        f'-c:v libx264 -pix_fmt yuv420p -preset fast -crf 20 -c:a aac -b:a 192k -shortest '
        f'"{out_video_path}"'
    )
    subprocess.check_call(cmd, shell=True)
    vsize = os.path.getsize(out_video_path)
    print(f"[OK] Successfully rendered {out_video_filename}: {vsize/1024:.1f} KB")

if __name__ == "__main__":
    from render_rich_scenes import generate_html_scenes
    generate_html_scenes()
    render_cinematic_video("narration_walkthrough_en.mp3", "walkthrough_executive.mp4")
    render_cinematic_video("narration_walkthrough_pt.mp3", "walkthrough_executive_pt.mp4")
    render_cinematic_video("narration_walkthrough_ar.mp3", "walkthrough_executive_ar.mp4")
    print("\nAll 3 cinematic walkthrough videos completed successfully with rich 1080p scenes!")
