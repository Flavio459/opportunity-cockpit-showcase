const https = require('https');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const audioDir = path.join(__dirname, '..', 'assets', 'audio');
const assetsDir = path.join(__dirname, '..', 'assets');

const items = [
  {
    file: 'narration_walkthrough_pt.mp3',
    videoFile: 'walkthrough_executive_pt.mp4',
    lang: 'pt',
    chunks: [
      "Bem-vindo ao Centro de Comando Executivo de IA.",
      "Este sistema transforma modelos generativos em rotinas executivas confiaveis e seguras.",
      "Capturamos audios e mensagens, extraimos prioridades estrategicas e mantemos um Portao Humano em um clique.",
      "Recupere de cinco a dez horas semanais da diretoria desde o primeiro Sprint, com zero risco de IA descontrolada."
    ]
  },
  {
    file: 'narration_walkthrough_ar.mp3',
    videoFile: 'walkthrough_executive_ar.mp4',
    lang: 'ar',
    chunks: [
      "مرحبًا بكم في مركز القيادة التنفيذي للذكاء الاصطناعي.",
      "يحول هذا النظام الذكاء الاصطناعي إلى ممارسات تنفيذية موثوقة وآمنة.",
      "نقوم بمعالجة الرسائل الصوتية، واستخراج الأولويات الاستراتيجية مع بوابة قرار بشري بنقرة واحدة.",
      "استعد من خمس إلى عشر ساعات أسبوعيًا للإدارة منذ الأسبوع الأول دون أي فوضى."
    ]
  }
];

function downloadChunk(text, lang, tempFile) {
  return new Promise((resolve, reject) => {
    const url = `https://translate.google.com/translate_tts?ie=UTF-8&q=${encodeURIComponent(text.trim())}&tl=${lang}&client=tw-ob`;
    const fileStream = fs.createWriteStream(tempFile);

    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (res) => {
      if (res.statusCode !== 200) {
        return reject(new Error(`Status ${res.statusCode} on chunk: ${text.substring(0, 30)}`));
      }
      res.pipe(fileStream);
      fileStream.on('finish', () => {
        fileStream.close();
        resolve();
      });
    }).on('error', (err) => {
      fs.unlink(tempFile, () => {});
      reject(err);
    });
  });
}

async function processItem(item) {
  const tempFiles = [];
  try {
    for (let i = 0; i < item.chunks.length; i++) {
      const tempPath = path.join(audioDir, `temp_narr_${item.lang}_${i}.mp3`);
      await downloadChunk(item.chunks[i], item.lang, tempPath);
      tempFiles.push(tempPath);
    }

    const destAudio = path.join(audioDir, item.file);
    const concatList = tempFiles.map(f => `file '${f.replace(/\\/g, '/')}'`).join('\n');
    const listFile = path.join(audioDir, `concat_narr_${item.lang}.txt`);
    fs.writeFileSync(listFile, concatList, 'utf8');

    execSync(`ffmpeg -y -f concat -safe 0 -i "${listFile}" -c copy "${destAudio}"`, { stdio: 'pipe' });
    fs.unlinkSync(listFile);
    tempFiles.forEach(f => fs.unlinkSync(f));

    const audioStats = fs.statSync(destAudio);
    console.log(`✓ Generated narration ${item.file} (${audioStats.size} bytes)`);

    // Get duration of narration audio using ffprobe
    const durationOutput = execSync(`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "${destAudio}"`).toString().trim();
    const duration = parseFloat(durationOutput) || 24;
    console.log(`Duration for ${item.lang}: ${duration}s`);

    const img1 = path.join(assetsDir, 'hero_executive_dubai.jpg');
    const img2 = path.join(assetsDir, 'showcase_i18n_preview.png');
    const outMp4 = path.join(assetsDir, item.videoFile);

    const t1 = Math.min(8, Math.floor(duration * 0.35));
    const t2 = (duration - t1 + 0.5).toFixed(1);

    const ffmpegCmd = `ffmpeg -y -loop 1 -t ${t1} -i "${img1}" -loop 1 -t ${t2} -i "${img2}" -i "${destAudio}" -filter_complex "[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1[v0]; [1:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1[v1]; [v0][v1]concat=n=2:v=1:a=0[v]" -map "[v]" -map 2:a -c:v libx264 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -shortest "${outMp4}"`;

    console.log(`Encoding ${item.videoFile}...`);
    execSync(ffmpegCmd, { stdio: 'pipe' });
    const videoStats = fs.statSync(outMp4);
    console.log(`✓ Successfully generated ${item.videoFile} (${videoStats.size} bytes)`);

  } catch (err) {
    tempFiles.forEach(f => { if (fs.existsSync(f)) fs.unlinkSync(f); });
    console.error(`✗ Error processing ${item.lang}:`, err.message);
  }
}

async function run() {
  console.log("Generating multilingual walkthrough videos for PT and AR...");
  for (const item of items) {
    await processItem(item);
  }
  console.log("All multilingual walkthrough videos completed!");
}

run();
