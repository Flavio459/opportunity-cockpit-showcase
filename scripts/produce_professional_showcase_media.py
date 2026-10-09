import os
import asyncio
import subprocess
import edge_tts

base_dir = r"W:\workspaces antigravity\opportunity-cockpit-showcase"
assets_dir = os.path.join(base_dir, "assets")
audio_dir = os.path.join(assets_dir, "audio")
scenes_dir = os.path.join(assets_dir, "scenes")
os.makedirs(audio_dir, exist_ok=True)

# 1. Audio Voice Memos for Simulator
SIM_VOICES = [
    {
        "file": "voice_memo_en.mp3",
        "voice": "en-GB-RyanNeural",
        "text": "Flávio, we just received Apex Capital's revision. They want to proceed with Milestone 1 ($50k), but need the delivery onboarding moved to Thursday morning. Can we confirm this before their committee meets at 2 PM?"
    },
    {
        "file": "voice_memo_pt.mp3",
        "voice": "pt-BR-AntonioNeural",
        "text": "Flávio, acabamos de receber a revisão da Apex Capital. Eles querem avançar no Marco 1 de cinquenta mil dólares, mas precisam que o onboarding da entrega seja movido para quinta-feira de manhã. Podemos confirmar isso antes do comitê deles às duas da tarde?"
    },
    {
        "file": "voice_memo_ar.mp3",
        "voice": "ar-AE-HamdanNeural",
        "text": "فلافيو، لقد استلمنا تعديل شركة أبكس كابيتال. يرغبون في المتابعة في المرحلة الأولى بخمسين ألف دولار، ولكنهم يطلبون نقل جلسة العمل إلى صباح الخميس. هل يمكننا تأكيد ذلك قبل اجتماع لجنتهم في الثانية ظهرًا؟"
    }
]

# 2. Executive Narrations for 5-Scene Walkthrough
NARRATIONS = [
    {
        "lang": "en",
        "audio_file": "narration_walkthrough_en.mp3",
        "video_file": "walkthrough_executive.mp4",
        "voice": "en-GB-RyanNeural",
        "text": (
            "Welcome to the Executive AI Command Center. Designed specifically for leadership operations in fast-paced hubs like Dubai. "
            "Step 1: Real-time Ingestion. When a partner or VP sends an unstructured audio note, our engine transcribes and sanitizes all data in 1.2 seconds with zero leakage. "
            "Step 2: AI Strategic Synthesis. The system automatically extracts the core business impact, calculates capacity, and drafts the high-stakes client deliverable. "
            "Step 3: Corporate Governance. The non-negotiable rule: 100% Deterministic Control. Nothing leaves your company without explicit sign-off at the 1-Click Human Decision Gate. "
            "Finally: Value Realization. Recover 5 to 10 executive hours every single week. Sprint 1 starts delivering measurable results in under 14 days."
        )
    },
    {
        "lang": "pt",
        "audio_file": "narration_walkthrough_pt.mp3",
        "video_file": "walkthrough_executive_pt.mp4",
        "voice": "pt-BR-AntonioNeural",
        "text": (
            "Bem-vindo ao Centro de Comando Executivo de IA. Desenvolvido para operações de diretoria em polos dinâmicos como Dubai. "
            "Passo 1: Triagem e Ingestão. Quando um sócio envia um áudio no Slack ou WhatsApp, nosso motor privado transcreve e sanitiza os dados em 1.2 segundos com zero vazamento. "
            "Passo 2: Síntese Estratégica. O sistema extrai automaticamente o impacto no negócio e pré-redige a resposta executiva pronta para o cliente. "
            "Passo 3: Governança Corporativa. Regra inegociável: Controle 100% Determinístico. Nada sai da sua empresa sem a sua aprovação no Portão Humano em 1 clique. "
            "Resultado: Recupere de 5 a 10 horas da liderança toda semana. O Sprint 1 começa a gerar valor mensurável em menos de 14 dias."
        )
    },
    {
        "lang": "ar",
        "audio_file": "narration_walkthrough_ar.mp3",
        "video_file": "walkthrough_executive_ar.mp4",
        "voice": "ar-AE-HamdanNeural",
        "text": (
            "مرحبًا بكم في مركز القيادة التنفيذي للذكاء الاصطناعي، المصمم خصيصًا لإدارة العمليات التنفيذية في دبي. "
            "الخطوة الأولى: معالجة الصوت والبيانات. عندما يُرسل الشريك رسالة صوتية، يقوم نظامنا الخاص بتفريغ البيانات وتدقيقها في ثانية واحدة دون أي تسريب. "
            "الخطوة الثانية: التحليل الاستراتيجي. يستخرج النظام الأثر المالي فورًا ويُعد مسودة الرد التنفيذي الجاهزة للاعتماد. "
            "الخطوة الثالثة: الحوكمة المؤسسية. قاعدة حتمية: لا شيء يخرج من شركتكم دون موافقة صريحة عبر بوابة القرار البشري بنقرة واحدة. "
            "النتيجة: استعادة خمس إلى عشر ساعات أسبوعيًا للإدارة، ونشر المرحلة الأولى في أقل من أربعة عشر يومًا."
        )
    }
]

async def generate_audio(text, voice, out_path):
    print(f"Generating neural voice ({voice}) -> {os.path.basename(out_path)}...")
    comm = edge_tts.Communicate(text, voice)
    await comm.save(out_path)
    sz = os.path.getsize(out_path)
    print(f"[OK] Generated {os.path.basename(out_path)}: {sz} bytes")

def get_audio_duration(path):
    cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{path}"'
    res = subprocess.check_output(cmd, shell=True).decode().strip()
    return float(res)

def render_5_scene_video(narration_path, out_video_path):
    dur = get_audio_duration(narration_path)
    print(f"Rendering 5-scene 1080p video for {os.path.basename(out_video_path)} (Duration: {dur:.2f}s)...")
    
    # 5 scene timing:
    # Scene 1 (Intro): 18% of time
    # Scene 2 (Voice): 22% of time
    # Scene 3 (Synthesis): 22% of time
    # Scene 4 (Human Gate): 20% of time
    # Scene 5 (ROI & Roadmap): remaining (approx 18%)
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

    cmd = (
        f'ffmpeg -y '
        f'-loop 1 -t {t1} -i "{s1}" '
        f'-loop 1 -t {t2} -i "{s2}" '
        f'-loop 1 -t {t3} -i "{s3}" '
        f'-loop 1 -t {t4} -i "{s4}" '
        f'-loop 1 -t {t5} -i "{s5}" '
        f'-i "{narration_path}" '
        f'-filter_complex "[0:v][1:v][2:v][3:v][4:v]concat=n=5:v=1:a=0[v]" '
        f'-map "[v]" -map 5:a '
        f'-c:v libx264 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -shortest '
        f'"{out_video_path}"'
    )
    subprocess.check_call(cmd, shell=True)
    vsize = os.path.getsize(out_video_path)
    print(f"[OK] Rendered {os.path.basename(out_video_path)}: {vsize} bytes ({vsize/1024:.1f} KB)")

async def main():
    print("=== Generating Neural Simulator Voice Memos ===")
    for item in SIM_VOICES:
        p = os.path.join(audio_dir, item["file"])
        await generate_audio(item["text"], item["voice"], p)

    print("\n=== Generating Multilingual Walkthrough Narrations & Videos ===")
    for item in NARRATIONS:
        ap = os.path.join(audio_dir, item["audio_file"])
        vp = os.path.join(assets_dir, item["video_file"])
        await generate_audio(item["text"], item["voice"], ap)
        render_5_scene_video(ap, vp)

    print("\n=== Production Media Suite Generation Complete ===")

if __name__ == "__main__":
    asyncio.run(main())
