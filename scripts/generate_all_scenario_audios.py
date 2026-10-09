import os
import asyncio
import edge_tts

base_dir = r"W:\workspaces antigravity\opportunity-cockpit-showcase"
audio_dir = os.path.join(base_dir, "assets", "audio")
os.makedirs(audio_dir, exist_ok=True)

# 3 Scenarios x 3 Languages = 9 Audio files
SCENARIOS_AUDIO = [
    # Scenario 1: audio_memo
    {
        "file": "scenario_audio_memo_en.mp3",
        "voice": "en-GB-RyanNeural",
        "text": "Flávio, we just received Apex Capital's revision. They want to proceed with Milestone 1 ($50k), but need the delivery onboarding moved to Thursday morning. Can we confirm this before their committee meets at 2 PM?"
    },
    {
        "file": "scenario_audio_memo_pt.mp3",
        "voice": "pt-BR-AntonioNeural",
        "text": "Flávio, acabamos de receber a revisão da Apex Capital. Eles querem avançar no Marco 1 de cinquenta mil dólares, mas precisam que o onboarding da entrega seja movido para quinta-feira de manhã. Podemos confirmar isso antes do comitê deles às duas da tarde?"
    },
    {
        "file": "scenario_audio_memo_ar.mp3",
        "voice": "ar-AE-HamdanNeural",
        "text": "فلافيو، لقد استلمنا تعديل شركة أبكس كابيتال. يرغبون في المتابعة في المرحلة الأولى بخمسين ألف دولار، ولكنهم يطلبون نقل جلسة العمل إلى صباح الخميس. هل يمكننا تأكيد ذلك قبل اجتماع لجنتهم في الثانية ظهرًا؟"
    },

    # Scenario 2: proposal_request (Emaar RFP)
    {
        "file": "scenario_proposal_request_en.mp3",
        "voice": "en-GB-RyanNeural",
        "text": "We are seeking an AI Implementation Consultant to audit our commercial asset workflows and build an automated lead routing system. Estimated budget is $85,000 over 3 months. Can you submit the executive proposal today?"
    },
    {
        "file": "scenario_proposal_request_pt.mp3",
        "voice": "pt-BR-AntonioNeural",
        "text": "Buscamos um Consultor de IA para auditar os fluxos de ativos comerciais e criar um sistema automatizado de roteamento de leads. Orçamento estimado em 85 mil dólares em 3 meses. Consegue enviar a proposta executiva hoje?"
    },
    {
        "file": "scenario_proposal_request_ar.mp3",
        "voice": "ar-AE-HamdanNeural",
        "text": "نبحث عن استشاري لتطبيق الذكاء الاصطناعي لتدقيق تدفقات الأصول التجارية وبناء نظام آلي لتوجيه العملاء المحتملين. الميزانية التقديرية 85,000 دولار على 3 أشهر. هل يمكنك تقديم العرض التنفيذي اليوم؟"
    },

    # Scenario 3: board_digest (Weekly Ops Brief)
    {
        "file": "scenario_board_digest_en.mp3",
        "voice": "en-GB-RyanNeural",
        "text": "Consolidating weekly logs across Operations, Client Sales, and Delivery. 42 workflow executions completed with 100% human-in-the-loop compliance. Total leadership hours saved: 8.5 hours."
    },
    {
        "file": "scenario_board_digest_pt.mp3",
        "voice": "pt-BR-AntonioNeural",
        "text": "Consolidando registros semanais de Operações, Vendas e Entrega. 42 execuções concluídas com 100% de conformidade com o portão humano. Total de horas da liderança economizadas: 8,5 horas."
    },
    {
        "file": "scenario_board_digest_ar.mp3",
        "voice": "ar-AE-HamdanNeural",
        "text": "دمج السجلات الأسبوعية للعمليات والمبيعات والتنفيذ. تم إكمال 42 إجراء بنسبة التزام بشري 100%. إجمالي الساعات الموفرة للقيادة: 8.5 ساعة."
    }
]

async def generate_audio(item):
    out_path = os.path.join(audio_dir, item["file"])
    print(f"Generating {item['file']} ({item['voice']})...")
    comm = edge_tts.Communicate(item["text"], item["voice"])
    await comm.save(out_path)
    sz = os.path.getsize(out_path)
    print(f"  [OK] {item['file']} -> {sz} bytes")

async def main():
    print("=== Generating 9 Dedicated Neural Voice Memos ===")
    for item in SCENARIOS_AUDIO:
        await generate_audio(item)
    
    # Also ensure legacy voice_memo_{en,pt,ar}.mp3 are kept in sync
    for lang in ["en", "pt", "ar"]:
        src = os.path.join(audio_dir, f"scenario_audio_memo_{lang}.mp3")
        dst = os.path.join(audio_dir, f"voice_memo_{lang}.mp3")
        if os.path.exists(src):
            with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
                fdst.write(fsrc.read())
            print(f"  [OK] Synced legacy voice_memo_{lang}.mp3")

    print("\nAll 9 Scenario Audio Assets Successfully Generated!")

if __name__ == "__main__":
    asyncio.run(main())
