const test = require('node:test');
const assert = require('node:assert');
const {
  UI_TRANSLATIONS,
  SCENARIOS,
  getScenario,
  getScenarioAudioPath,
  calculateSavings,
  validateDictionaries
} = require('../data/i18n.js');

test('TDD: Dictionaries must be complete across English, Arabic, and Portuguese', () => {
  const isValid = validateDictionaries();
  assert.strictEqual(isValid, true, 'All languages (en, ar, pt) must have matching translation keys');

  const enKeys = Object.keys(UI_TRANSLATIONS.en);
  const arKeys = Object.keys(UI_TRANSLATIONS.ar);
  const ptKeys = Object.keys(UI_TRANSLATIONS.pt);

  assert.strictEqual(arKeys.length, enKeys.length, 'Arabic keys count matches English');
  assert.strictEqual(ptKeys.length, enKeys.length, 'Portuguese keys count matches English');
  assert.ok(enKeys.includes('brandTitle'), 'Should contain brandTitle key');
  assert.ok(enKeys.includes('gateActiveBadge'), 'Should contain gateActiveBadge key');
});

test('TDD: Scenarios must provide valid multilingual content for Dubai operations', () => {
  const scenarioIds = ['audio_memo', 'proposal_request', 'board_digest'];
  const languages = ['en', 'ar', 'pt'];

  scenarioIds.forEach((id) => {
    languages.forEach((lang) => {
      const data = getScenario(id, lang);
      assert.ok(data, `Scenario ${id} in ${lang} must exist`);
      assert.ok(data.transcript && data.transcript.length > 10, `${id} in ${lang} has valid transcript`);
      assert.strictEqual(data.bullets.length, 3, `${id} in ${lang} must have exactly 3 strategic bullets`);
      assert.ok(data.draft && data.draft.length > 20, `${id} in ${lang} has valid draft`);
      assert.ok(data.shortDraft && data.shortDraft.length > 10, `${id} in ${lang} has valid shortDraft`);
    });
  });
});

test('TDD: Savings calculator accurately computes leadership hours and dollars saved at $39/hr', () => {
  const calc1 = calculateSavings(8.5, 0.7, 39.0);
  assert.strictEqual(calc1.totalHours, 9.2);
  assert.strictEqual(calc1.totalValue, 358.80);

  const calc2 = calculateSavings(10.0, 0, 39.0);
  assert.strictEqual(calc2.totalHours, 10.0);
  assert.strictEqual(calc2.totalValue, 390.00);
});

test('TDD: Fallback scenario retrieval defaults to English when language is unsupported', () => {
  const fallback = getScenario('audio_memo', 'es'); // Unsupported language
  assert.ok(fallback, 'Should return fallback');
  assert.strictEqual(fallback.senderName, 'VP of Operations (Dubai)', 'Should default to English VP sender name');
});

test('TDD: Audio and video media assets must exist on disk and meet quality standards', () => {
  const fs = require('node:fs');
  const path = require('node:path');

  const assetsDir = path.resolve(__dirname, '../assets');
  const requiredVideos = [
    'walkthrough_executive.mp4',
    'walkthrough_executive_pt.mp4',
    'walkthrough_executive_ar.mp4'
  ];

  requiredVideos.forEach(vFile => {
    const videoPath = path.join(assetsDir, vFile);
    assert.ok(fs.existsSync(videoPath), `${vFile} must exist`);
    const videoStats = fs.statSync(videoPath);
    assert.ok(videoStats.size > 500000, `Video file ${vFile} (${videoStats.size} bytes) must be > 500KB`);
  });

  const audioDir = path.join(assetsDir, 'audio');
  const requiredAudios = [
    'voice_memo_en.mp3',
    'voice_memo_ar.mp3',
    'voice_memo_pt.mp3',
    'narration_walkthrough_en.mp3',
    'narration_walkthrough_pt.mp3',
    'narration_walkthrough_ar.mp3'
  ];

  requiredAudios.forEach(fileName => {
    const audioPath = path.join(audioDir, fileName);
    assert.ok(fs.existsSync(audioPath), `Audio file ${fileName} must exist`);
    const audioStats = fs.statSync(audioPath);
    assert.ok(audioStats.size > 20000, `Audio file ${fileName} (${audioStats.size} bytes) must be > 20KB`);
  });
});

test('TDD: Dedicated scenario audio paths must exist on disk for all 3 tabs across 3 languages', () => {
  const fs = require('node:fs');
  const path = require('node:path');
  const audioDir = path.resolve(__dirname, '../assets/audio');

  const scenarios = ['audio_memo', 'proposal_request', 'board_digest'];
  const languages = ['en', 'ar', 'pt'];

  scenarios.forEach(scId => {
    languages.forEach(lang => {
      const relPath = getScenarioAudioPath(scId, lang);
      assert.strictEqual(relPath, `assets/audio/scenario_${scId}_${lang}.mp3`, 'Path format must match convention');
      
      const fullPath = path.resolve(__dirname, '..', relPath);
      assert.ok(fs.existsSync(fullPath), `Dedicated scenario audio ${fullPath} must exist on disk`);
      const stat = fs.statSync(fullPath);
      assert.ok(stat.size > 20000, `Scenario audio ${relPath} (${stat.size} bytes) must be non-empty and > 20KB`);
    });
  });
});

test('TDD: Client UX state transitions guarantee scenario isolation and distinct executive content', () => {
  const scenarios = ['audio_memo', 'proposal_request', 'board_digest'];
  const seenTranscripts = new Set();
  const seenSenders = new Set();

  scenarios.forEach(scId => {
    const scEn = getScenario(scId, 'en');
    assert.ok(!seenTranscripts.has(scEn.transcript), `Scenario ${scId} must have unique transcript`);
    seenTranscripts.add(scEn.transcript);

    assert.ok(!seenSenders.has(scEn.senderName), `Scenario ${scId} must have unique sender identity`);
    seenSenders.add(scEn.senderName);

    const scPt = getScenario(scId, 'pt');
    const scAr = getScenario(scId, 'ar');
    assert.ok(scPt.transcript.length > 20, `PT transcript for ${scId} is populated`);
    assert.ok(scAr.transcript.length > 20, `AR transcript for ${scId} is populated`);
  });
});
test('TDD: Conversion psychology, governance matrix, and audit keys exist across all languages', () => {
  const requiredConversionKeys = [
    'auditSignedTitle',
    'auditSignerLabel',
    'contrastHeading',
    'contrastRogueTitle',
    'contrastSovereignTitle',
    'ctaSectionEyebrow',
    'ctaSectionHeading',
    'btnUpworkContract',
    'btnScheduleCall',
    'ctaEscrowNotice'
  ];
  const languages = ['en', 'ar', 'pt'];

  languages.forEach((lang) => {
    const dict = UI_TRANSLATIONS[lang];
    requiredConversionKeys.forEach((key) => {
      assert.ok(dict[key], `Language ${lang} must include conversion key ${key}`);
      assert.ok(dict[key].length > 3, `Value for ${key} in ${lang} must be non-trivial`);
    });
  });
});
