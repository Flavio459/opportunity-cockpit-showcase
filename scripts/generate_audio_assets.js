const https = require('https');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const audioDir = path.join(__dirname, '..', 'assets', 'audio');
if (!fs.existsSync(audioDir)) {
  fs.mkdirSync(audioDir, { recursive: true });
}

const items = [
  {
    file: 'voice_memo_en.mp3',
    lang: 'en',
    chunks: [
      "Flavio, we just received Apex Capital's revision.",
      "They want to proceed with Milestone 1 ($50k), but need delivery onboarding moved to Thursday morning.",
      "Can we confirm before their committee meets at 2 PM?"
    ]
  },
  {
    file: 'voice_memo_ar.mp3',
    lang: 'ar',
    chunks: [
      "فلافيو، لقد استلمنا تعديل شركة أبكس كابيتال.",
      "يرغبون في المتابعة في المرحلة الأولى، ويطلبون نقل جلسة العمل إلى صباح الخميس.",
      "هل يمكننا تأكيد ذلك قبل اجتماع لجنتهم؟"
    ]
  },
  {
    file: 'voice_memo_pt.mp3',
    lang: 'pt',
    chunks: [
      "Flavio, acabamos de receber a revisao da Apex Capital.",
      "Eles querem avancar no Marco 1 de cinquenta mil dolares, mas precisam que o onboarding seja movido para quinta de manha.",
      "Podemos confirmar isso antes do comite deles as duas da tarde?"
    ]
  },
  {
    file: 'narration_walkthrough_en.mp3',
    lang: 'en',
    chunks: [
      "Welcome to the Executive AI Command Center.",
      "This system turns generative models into trusted executive habits without risk.",
      "We ingest unstructured voice memos, extract core strategic priorities, and maintain a deterministic 1-Click Human Decision Gate.",
      "Recover 5 to 10 leadership hours every week from Sprint 1 with zero rogue AI."
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
      const tempPath = path.join(audioDir, `temp_${path.parse(item.file).name}_${i}.mp3`);
      await downloadChunk(item.chunks[i], item.lang, tempPath);
      tempFiles.push(tempPath);
    }

    const dest = path.join(audioDir, item.file);
    if (tempFiles.length === 1) {
      fs.copyFileSync(tempFiles[0], dest);
      fs.unlinkSync(tempFiles[0]);
    } else {
      // Concat using ffmpeg
      const concatList = tempFiles.map(f => `file '${f.replace(/\\/g, '/')}'`).join('\n');
      const listFile = path.join(audioDir, `concat_${path.parse(item.file).name}.txt`);
      fs.writeFileSync(listFile, concatList, 'utf8');

      execSync(`ffmpeg -y -f concat -safe 0 -i "${listFile}" -c copy "${dest}"`, { stdio: 'pipe' });
      fs.unlinkSync(listFile);
      tempFiles.forEach(f => fs.unlinkSync(f));
    }

    const stats = fs.statSync(dest);
    console.log(`✓ Successfully generated ${item.file} (${stats.size} bytes)`);
  } catch (err) {
    tempFiles.forEach(f => { if (fs.existsSync(f)) fs.unlinkSync(f); });
    console.error(`✗ Error generating ${item.file}:`, err.message);
  }
}

async function run() {
  console.log('Generating chunked audio assets via FFmpeg and TTS...');
  for (const item of items) {
    await processItem(item);
  }
  console.log('Done generating all audio assets!');
}

run();
