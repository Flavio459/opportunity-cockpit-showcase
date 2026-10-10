// Executive AI Command Center — Multilingual Simulator Engine
// Developed for C-Suite Leadership Operations (Dubai / Worldwide Remote)

let currentLang = "en";
let currentScenario = "audio_memo";
let isShortTone = false;
let isApproved = false;
let audioContext = null;
let waveInterval = null;
let simAudioInstance = null;

// Helper to access i18n
function getI18n() {
  return window.SHOWCASE_I18N || {};
}

// Initialize sound context on user interaction
function getAudioContext() {
  if (!audioContext) {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (AudioCtx) {
      audioContext = new AudioCtx();
    }
  }
  if (audioContext && audioContext.state === 'suspended') {
    audioContext.resume();
  }
  return audioContext;
}

// Play pleasant acoustic executive chime
function playChime(type = "success") {
  try {
    const ctx = getAudioContext();
    if (!ctx) return;

    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);

    if (type === "success") {
      osc.type = "sine";
      osc.frequency.setValueAtTime(523.25, ctx.currentTime); // C5
      osc.frequency.exponentialRampToValueAtTime(659.25, ctx.currentTime + 0.08); // E5
      osc.frequency.exponentialRampToValueAtTime(783.99, ctx.currentTime + 0.2); // G5
      gain.gain.setValueAtTime(0.12, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.5);
      osc.start();
      osc.stop(ctx.currentTime + 0.5);
    } else {
      osc.type = "sine";
      osc.frequency.setValueAtTime(440, ctx.currentTime); // A4
      gain.gain.setValueAtTime(0.08, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.15);
      osc.start();
      osc.stop(ctx.currentTime + 0.15);
    }
  } catch (e) {
    console.log("Audio chime feedback fallback", e);
  }
}

// Set Active Language
function setLanguage(lang) {
  currentLang = lang;
  const htmlRoot = document.getElementById("htmlRoot");
  const i18n = getI18n();
  const dict = (i18n.UI_TRANSLATIONS && i18n.UI_TRANSLATIONS[lang]) || {};

  // Stop any playing audio when switching language
  if (simAudioInstance) {
    simAudioInstance.pause();
    simAudioInstance = null;
    stopWaveAnimation();
    const btnIcon = document.getElementById("simAudioIcon");
    const btnLabel = document.getElementById("simAudioLabel");
    if (btnIcon && btnLabel) {
      btnIcon.innerText = "▶";
      btnLabel.innerText = dict.playVoiceBtn || "Play Voice";
    }
  }

  // RTL direction for Arabic
  if (lang === "ar") {
    htmlRoot.setAttribute("dir", "rtl");
  } else {
    htmlRoot.setAttribute("dir", "ltr");
  }

  // Update Language Buttons
  ["en", "ar", "pt"].forEach((l) => {
    const btn = document.getElementById(`lang-btn-${l}`);
    if (btn) {
      if (l === lang) {
        btn.className = "px-2.5 py-1 rounded-md transition font-semibold bg-cyan-500 text-black";
      } else {
        btn.className = "px-2.5 py-1 rounded-md transition text-slate-400 hover:text-white";
      }
    }
  });

  // Update all [data-i18n] text
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    if (dict[key]) {
      el.innerText = dict[key];
    }
  });

  // Re-render current scenario in selected language
  loadScenario(currentScenario);
  updateWalkthroughVideo(lang);
  playChime("click");
}

// Load Scenario
function loadScenario(scenarioId) {
  currentScenario = scenarioId;
  const i18n = getI18n();
  const data = (i18n.getScenario && i18n.getScenario(scenarioId, currentLang)) || null;
  if (!data) return;

  isShortTone = false;
  isApproved = false;

  // Stop any active audio and reset player UI when switching scenario tabs
  if (simAudioInstance) {
    simAudioInstance.pause();
    simAudioInstance.currentTime = 0;
    simAudioInstance = null;
    stopWaveAnimation();
    const btnIcon = document.getElementById("simAudioIcon");
    const btnLabel = document.getElementById("simAudioLabel");
    if (btnIcon && btnLabel) {
      btnIcon.innerText = "▶";
      const dict = (i18n.UI_TRANSLATIONS && i18n.UI_TRANSLATIONS[currentLang]) || {};
      btnLabel.innerText = dict.playVoiceBtn || "Play Voice";
    }
  }

  // Update Scenario Tabs
  ["audio_memo", "proposal_request", "board_digest"].forEach((id, idx) => {
    const btn = document.getElementById(`btn-scenario-${idx + 1}`);
    if (btn) {
      if (id === scenarioId) {
        btn.className = "px-3 py-1.5 rounded-md text-xs font-semibold font-mono transition bg-cyan-500 text-black";
      } else {
        btn.className = "px-3 py-1.5 rounded-md text-xs font-medium font-mono transition text-slate-400 hover:text-white";
      }
    }
  });

  // Populate Ingestion Card
  document.getElementById("inputChannelBadge").innerText = data.channelBadge;
  document.getElementById("senderName").innerText = data.senderName;
  document.getElementById("memoDuration").innerText = data.duration;
  document.getElementById("rawInputTranscript").innerText = `"${data.transcript}"`;

  // Bullets
  const bulletsContainer = document.getElementById("synthesisBullets");
  bulletsContainer.innerHTML = data.bullets.map(b => `
    <li class="flex items-start gap-2 bg-slate-950 p-2.5 rounded-lg border border-slate-800/80">
      <span class="text-emerald-400 font-bold font-mono">${b.id}.</span>
      <span><strong>${b.title}:</strong> ${b.desc}</span>
    </li>
  `).join("");

  // Draft Text
  document.getElementById("draftActionText").innerText = data.draft;

  // Reset Gate State
  const dict = (i18n.UI_TRANSLATIONS && i18n.UI_TRANSLATIONS[currentLang]) || {};
  const gateState = document.getElementById("gateStateText");
  gateState.className = "text-[11px] font-mono text-amber-400 font-semibold";
  gateState.innerText = dict.gatePendingText || "● AWAITING HUMAN APPROVAL";

  const approveBtn = document.getElementById("approveBtn");
  approveBtn.className = "py-2.5 px-4 bg-emerald-500 hover:bg-emerald-400 active:scale-95 text-black font-semibold text-xs rounded-lg flex items-center justify-center gap-1.5 transition shadow-md";
  approveBtn.disabled = false;
  document.getElementById("approveBtnLabel").innerText = dict.btnApprove || "✓ Approve & Dispatch";

  const calibrateBtnLabel = document.getElementById("calibrateBtnLabel");
  if (calibrateBtnLabel) {
    calibrateBtnLabel.innerText = dict.btnCalibrateShort || "⚡ Shorter Tone";
  }

  document.getElementById("executionNotice").classList.add("hidden");
}

// Real Voice Audio Playback via pre-rendered executive MP3s + Waveform Animation
function playSimulationAudio() {
  getAudioContext();
  playChime("click");

  const i18n = getI18n();
  const dict = (i18n.UI_TRANSLATIONS && i18n.UI_TRANSLATIONS[currentLang]) || {};
  const btnIcon = document.getElementById("simAudioIcon");
  const btnLabel = document.getElementById("simAudioLabel");

  // If already playing, stop
  if (simAudioInstance && !simAudioInstance.paused) {
    simAudioInstance.pause();
    simAudioInstance.currentTime = 0;
    simAudioInstance = null;
    stopWaveAnimation();
    btnIcon.innerText = "▶";
    btnLabel.innerText = dict.playVoiceBtn || "Play Voice";
    return;
  }

  // Create real audio instance for current scenario and language (en, ar, pt)
  const audioSrc = (i18n.getScenarioAudioPath && i18n.getScenarioAudioPath(currentScenario, currentLang))
    || `assets/audio/scenario_${currentScenario}_${currentLang}.mp3`;
  simAudioInstance = new Audio(audioSrc);

  startWaveAnimation();
  btnIcon.innerText = "⏹";
  btnLabel.innerText = dict.playingVoiceBtn || "Playing...";

  simAudioInstance.onended = () => {
    stopWaveAnimation();
    btnIcon.innerText = "▶";
    btnLabel.innerText = dict.playVoiceBtn || "Play Voice";
    simAudioInstance = null;
  };

  simAudioInstance.onerror = (e) => {
    console.warn("Audio file playback error, falling back", e);
    stopWaveAnimation();
    btnIcon.innerText = "▶";
    btnLabel.innerText = dict.playVoiceBtn || "Play Voice";
    simAudioInstance = null;
  };

  simAudioInstance.play().catch(err => {
    console.warn("Audio play blocked or requires user gesture:", err);
    setTimeout(() => {
      stopWaveAnimation();
      btnIcon.innerText = "▶";
      btnLabel.innerText = dict.playVoiceBtn || "Play Voice";
      simAudioInstance = null;
    }, 4000);
  });
}

function startWaveAnimation() {
  const bars = document.querySelectorAll(".waveform-bar");
  if (waveInterval) clearInterval(waveInterval);
  waveInterval = setInterval(() => {
    bars.forEach(bar => {
      const h = Math.floor(Math.random() * 22) + 4;
      bar.style.height = `${h}px`;
    });
  }, 100);
}

function stopWaveAnimation() {
  if (waveInterval) {
    clearInterval(waveInterval);
    waveInterval = null;
  }
  const bars = document.querySelectorAll(".waveform-bar");
  bars.forEach(b => b.style.height = "8px");
}

// Toggle Draft Tone
function calibrateTone() {
  const i18n = getI18n();
  const data = (i18n.getScenario && i18n.getScenario(currentScenario, currentLang)) || null;
  if (!data) return;

  const draftBox = document.getElementById("draftActionText");
  const calibrateBtnLabel = document.getElementById("calibrateBtnLabel");
  const dict = (i18n.UI_TRANSLATIONS && i18n.UI_TRANSLATIONS[currentLang]) || {};

  isShortTone = !isShortTone;
  if (isShortTone) {
    draftBox.innerText = data.shortDraft;
    calibrateBtnLabel.innerText = dict.btnCalibrateStandard || "⚡ Standard Tone";
  } else {
    draftBox.innerText = data.draft;
    calibrateBtnLabel.innerText = dict.btnCalibrateShort || "⚡ Shorter Tone";
  }
  playChime("click");
}

// Execute 1-Click Human Decision Gate
function executeHumanApproval() {
  isApproved = true;
  playChime("success");

  const i18n = getI18n();
  const dict = (i18n.UI_TRANSLATIONS && i18n.UI_TRANSLATIONS[currentLang]) || {};
  const data = (i18n.getScenario && i18n.getScenario(currentScenario, currentLang)) || {};

  // Animate button
  const approveBtn = document.getElementById("approveBtn");
  approveBtn.className = "py-2.5 px-4 bg-emerald-600 text-white font-semibold text-xs rounded-lg flex items-center justify-center gap-1.5 transition shadow-sm";
  document.getElementById("approveBtnLabel").innerText = dict.btnApproved || "✓ Approved & Executed";
  approveBtn.disabled = true;

  // Gate label
  const gateState = document.getElementById("gateStateText");
  gateState.className = "text-[11px] font-mono text-emerald-400 font-bold";
  gateState.innerText = dict.gateApprovedText || "✓ AUTHORIZED BY HUMAN GATE (Flávio Barros)";

  // Notice
  const notice = document.getElementById("executionNotice");
  document.getElementById("executionSubnotice").innerText = data.executedNotice || "Workflow dispatched successfully.";
  notice.classList.remove("hidden");

  // Update Tickers with $39/hr formula
  const savings = i18n.calculateSavings ? i18n.calculateSavings(8.5, 0.7, 39.0) : { totalHours: 9.2, totalValue: 358.80 };
  const hoursTicker = document.getElementById("hoursSavedTicker");
  hoursTicker.innerText = `${savings.totalHours} hrs (+0.7h)`;
  hoursTicker.classList.add("text-emerald-300");

  const valueTicker = document.getElementById("valueSavedTicker");
  valueTicker.innerText = `$${savings.totalValue.toFixed(2)}`;

  const salesBadge = document.getElementById("salesStatusBadge");
  salesBadge.className = "px-2 py-0.5 bg-emerald-950 text-emerald-400 font-mono text-[10px] font-bold rounded";
  salesBadge.innerText = "RESOLVED";
}

// Switch Walkthrough Video per Language
function updateWalkthroughVideo(lang) {
  const video = document.getElementById("walkthroughVideo");
  const durationBadge = document.getElementById("videoDurationBadge");
  if (!video) return;

  const isPlaying = !video.paused && !video.ended;
  let targetSrc = "assets/walkthrough_executive.mp4?v=20261010_v4";
  let durationText = "00:57 · 1080p MP4";

  if (lang === "ar") {
    targetSrc = "assets/walkthrough_executive_ar.mp4?v=20261010_v4";
    durationText = "01:00 · 1080p MP4";
  } else if (lang === "pt") {
    targetSrc = "assets/walkthrough_executive_pt.mp4?v=20261010_v4";
    durationText = "00:54 · 1080p MP4";
  }

  if (durationBadge) {
    durationBadge.innerText = durationText;
  }

  if (!video.src.includes(targetSrc)) {
    video.src = targetSrc;
    video.load();
    if (isPlaying) {
      video.play().catch(e => console.log("Video play request on lang switch:", e));
    }
  }
}

// Toggle Video Walkthrough section
function toggleVideoWalkthrough() {
  const section = document.getElementById("videoWalkthroughSection");
  const video = document.getElementById("walkthroughVideo");
  if (section.classList.contains("hidden")) {
    section.classList.remove("hidden");
    section.scrollIntoView({ behavior: "smooth" });
    if (video) {
      video.play().catch(e => console.log("User interaction required for video play:", e));
    }
  } else {
    section.classList.add("hidden");
    if (video) {
      video.pause();
    }
  }
}

// Walkthrough Audio Progress Simulator
let audioPlaying = false;
let audioTimer = null;
let currentSeconds = 0;
const totalDuration = 65;

const narrationLines = [
  { at: 0, text: '"Welcome. In this 60-second walkthrough, observe how executive leadership in Dubai eliminates operational bottlenecks with zero rogue AI."' },
  { at: 10, text: '"Step 1: The CEO or VP simply sends an audio note via Slack or WhatsApp. Notice how our ingestion layer transcribes and sanitizes it in 1.2 seconds."' },
  { at: 22, text: '"Step 2: The AI extracts the 3 core business impacts, calculates resource capacity, and drafts the executive response ready for sign-off."' },
  { at: 38, text: '"Step 3: The non-negotiable rule — Zero Rogue AI. The system pauses at the Human Decision Gate. Nothing is dispatched externally until you click Approve."' },
  { at: 50, text: '"With 1 click, the workflow triggers, the client receives the confirmation, and leadership recovers 5 to 10 hours every week."' },
  { at: 60, text: '"Think Big, Start Small, Scale Fast. Sprint 1 starts delivering value in under 14 days."' }
];

function toggleWalkthroughAudio() {
  const playBtn = document.getElementById("playAudioBtn");
  const trackStatus = document.getElementById("audioTrackStatus");
  const i18n = getI18n();
  const dict = (i18n.UI_TRANSLATIONS && i18n.UI_TRANSLATIONS[currentLang]) || {};

  if (audioPlaying) {
    clearInterval(audioTimer);
    audioPlaying = false;
    playBtn.innerText = "▶";
    trackStatus.innerText = dict.walkthroughStatusPaused || "Paused";
  } else {
    audioPlaying = true;
    playBtn.innerText = "⏸";
    trackStatus.innerText = dict.walkthroughStatusPlaying || "Playing Voice Track...";
    playChime("click");

    audioTimer = setInterval(() => {
      currentSeconds++;
      if (currentSeconds > totalDuration) {
        clearInterval(audioTimer);
        audioPlaying = false;
        currentSeconds = 0;
        playBtn.innerText = "▶";
        trackStatus.innerText = dict.walkthroughStatusDone || "Completed";
        return;
      }

      const pct = (currentSeconds / totalDuration) * 100;
      document.getElementById("audioProgressBar").style.width = `${pct}%`;

      const mins = String(Math.floor(currentSeconds / 60)).padStart(2, "0");
      const secs = String(currentSeconds % 60).padStart(2, "0");
      document.getElementById("videoTimer").innerText = `${mins}:${secs} / 01:05`;

      const matched = [...narrationLines].reverse().find(l => currentSeconds >= l.at);
      if (matched) {
        document.getElementById("narrationText").innerText = matched.text;
      }
    }, 1000);
  }
}

// Initial boot
document.addEventListener("DOMContentLoaded", () => {
  setLanguage("en");
});
