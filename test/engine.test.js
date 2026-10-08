const test = require('node:test');
const assert = require('node:assert');
const {
  UI_TRANSLATIONS,
  SCENARIOS,
  getScenario,
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
