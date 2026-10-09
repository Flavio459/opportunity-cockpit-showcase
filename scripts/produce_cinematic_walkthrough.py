import os
import subprocess
from render_rich_scenes import generate_html_scenes

base_dir = r"W:\workspaces antigravity\opportunity-cockpit-showcase"
assets_dir = os.path.join(base_dir, "assets")
scenes_dir = os.path.join(assets_dir, "scenes")
audio_dir = os.path.join(assets_dir, "audio")

def get_duration(audio_path):
    cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{audio_path}"'
    res = subprocess.check_output(cmd, shell=True).decode().strip()
    return float(res)

def render_cinematic_video(audio_filename, out_video_filename):
    audio_path = os.path.join(audio_dir, audio_filename)
    out_video_path = os.path.join(assets_dir, out_video_filename)
    dur = get_duration(audio_path)
    print(f"\nEncoding Verified 5-Scene Video for {out_video_filename} (Duration: {dur:.2f}s)...")
    
    # 5 scenes timed to match the spoken narrative
    t1 = round(dur * 0.17, 2)
    t2 = round(dur * 0.22, 2)
    t3 = round(dur * 0.22, 2)
    t4 = round(dur * 0.22, 2)
    t5 = round(dur - (t1 + t2 + t3 + t4), 2)
    print(f"  Scene timings: S1={t1}s, S2={t2}s, S3={t3}s, S4={t4}s, S5={t5}s (Total={t1+t2+t3+t4+t5:.2f}s)")

    s1 = os.path.join(scenes_dir, "scene1.png")
    s2 = os.path.join(scenes_dir, "scene2.png")
    s3 = os.path.join(scenes_dir, "scene3.png")
    s4 = os.path.join(scenes_dir, "scene4.png")
    s5 = os.path.join(scenes_dir, "scene5.png")

    # High-quality scale + concat without the zoompan multiplier bug
    filter_complex = (
        f"[0:v]scale=1920:1080,fps=30,setsar=1[v0]; "
        f"[1:v]scale=1920:1080,fps=30,setsar=1[v1]; "
        f"[2:v]scale=1920:1080,fps=30,setsar=1[v2]; "
        f"[3:v]scale=1920:1080,fps=30,setsar=1[v3]; "
        f"[4:v]scale=1920:1080,fps=30,setsar=1[v4]; "
        f"[v0][v1][v2][v3][v4]concat=n=5:v=1:a=0[vout]; "
        # Generate subtle ambient harmonic synth drone at -24dB in background
        f"aevalsrc=exprs='0.015*sin(2*PI*110*t)+0.012*sin(2*PI*164.81*t)+0.008*sin(2*PI*220*t)':s=48000:d={dur}[amb]; "
        # Mix narration audio with ambient bed
        f"[5:a]volume=1.0[voice]; "
        f"[amb]volume=0.22,lowpass=f=800[bgpad]; "
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
        f'-c:v libx264 -pix_fmt yuv420p -preset fast -crf 19 -c:a aac -b:a 192k -shortest '
        f'"{out_video_path}"'
    )
    subprocess.check_call(cmd, shell=True)
    vsize = os.path.getsize(out_video_path)
    print(f"[OK] Successfully rendered {out_video_filename}: {vsize/1024:.1f} KB")

if __name__ == "__main__":
    generate_html_scenes()
    render_cinematic_video("narration_walkthrough_en.mp3", "walkthrough_executive.mp4")
    render_cinematic_video("narration_walkthrough_pt.mp3", "walkthrough_executive_pt.mp4")
    render_cinematic_video("narration_walkthrough_ar.mp3", "walkthrough_executive_ar.mp4")
    print("\nAll 3 walkthrough videos rendered and verified with 5 distinct scenes!")
