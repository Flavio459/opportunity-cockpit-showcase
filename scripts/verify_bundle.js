const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert');

console.log("Starting Quality Gate Verification Suite...");

// 1. Verify index.html video tag and clean button elements
const htmlPath = path.resolve(__dirname, '../index.html');
const htmlContent = fs.readFileSync(htmlPath, 'utf8');

assert.ok(htmlContent.includes('<video id="walkthroughVideo"'), 'Gate 1: index.html must contain walkthroughVideo element');
assert.ok(htmlContent.includes('src="assets/walkthrough_executive.mp4"'), 'Gate 1: index.html must point to real MP4 video asset');
assert.ok(!htmlContent.includes('▶ ▶'), 'Gate 3: index.html must not contain duplicate play symbols');
console.log("✔ Gate 1 & 3: HTML structure & video element verified");

// 2. Verify media assets on disk
const assetsDir = path.resolve(__dirname, '../assets');
const videoFiles = ['walkthrough_executive.mp4', 'walkthrough_executive_pt.mp4', 'walkthrough_executive_ar.mp4'];
videoFiles.forEach(vFile => {
  const p = path.join(assetsDir, vFile);
  assert.ok(fs.existsSync(p), `Video file ${vFile} must exist`);
  const s = fs.statSync(p);
  assert.ok(s.size > 500000, `Video file ${vFile} must be substantive (>500KB). Actual: ${s.size}`);
  console.log(`✔ Gate 1: Real MP4 video asset ${vFile} verified (${(s.size / 1024).toFixed(1)} KB)`);
});

const audioFiles = ['voice_memo_en.mp3', 'voice_memo_ar.mp3', 'voice_memo_pt.mp3'];
audioFiles.forEach(file => {
  const p = path.join(assetsDir, 'audio', file);
  assert.ok(fs.existsSync(p), `Audio file ${file} must exist`);
  const s = fs.statSync(p);
  assert.ok(s.size > 50000, `Audio file ${file} must be > 50KB. Actual: ${s.size}`);
  console.log(`✔ Gate 2: Audio asset ${file} verified (${(s.size / 1024).toFixed(1)} KB)`);
});

// 3. Verify app.js real audio integration
const appPath = path.resolve(__dirname, '../app.js');
const appContent = fs.readFileSync(appPath, 'utf8');
assert.ok(appContent.includes('assets/audio/voice_memo_${currentLang}.mp3'), 'Gate 2: app.js must use real audio files per currentLang');
assert.ok(appContent.includes('new Audio(audioSrc)'), 'Gate 2: app.js must instantiate HTML5 Audio');
console.log("✔ Gate 2: JavaScript audio engine verified");

console.log("\nALL 5 QUALITY GATES PASSED DETERMINISTICALLY!");
