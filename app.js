// Executive AI Command Center — Interactive Simulator Engine
// Developed for C-Suite Leadership Operations (Dubai / Worldwide Remote)

const scenarios = {
  audio_memo: {
    channelBadge: "Slack Voice Audio",
    senderName: "VP of Operations (Dubai)",
    duration: "0:32 audio memo",
    transcript: '"Flávio, we just received Apex Capital\'s revision. They want to proceed with Milestone 1 ($50k), but need the delivery onboarding moved to Thursday morning. Can we confirm this before their committee meets at 2 PM?"',
    bullets: [
      { id: "01", title: "Revenue Milestone", desc: "Confirms $50,000 for Milestone 1 with approved commercial terms." },
      { id: "02", title: "Calendar Alignment", desc: "Onboarding shifted to Thursday 10:00 AM GST (Delivery team capacity reserved)." },
      { id: "03", title: "Time Sensitivity", desc: "Requires 1-click authorization prior to Apex 2:00 PM GST committee meeting." }
    ],
    draft: `Subject: Confirmation: Apex Capital Milestone 1 & Thursday Onboarding

Dear Tariq,
Thank you for the update. We are pleased to confirm Milestone 1 ($50,000) under the agreed terms. Our technical delivery leads are already scheduled to kick off the executive onboarding session this Thursday at 10:00 AM GST.

Looking forward to our kickoff.
Best regards,
[Executive Leadership]`,
    shortDraft: `Tariq: Milestone 1 ($50k) is confirmed. Executive onboarding locked for Thursday at 10:00 AM GST. See you then. - [Leadership]`,
    executedNotice: "Email sent to Apex Capital · ClickUp sprint updated · Calendar locked"
  },
  proposal_request: {
    channelBadge: "Inbound RFP / Email",
    senderName: "Managing Director, Emaar Strategic Projects",
    duration: "Direct Enterprise Inquiry",
    transcript: '"We are seeking an AI Implementation Consultant to audit our commercial asset workflows and build an automated lead routing system. Estimated budget is $85,000 over 3 months. Can you submit the executive proposal today?"',
    bullets: [
      { id: "01", title: "Enterprise Lead", desc: "Commercial asset intake workflow ($85,000 project size)." },
      { id: "02", title: "SLA Expectation", desc: "Response requested within current business day." },
      { id: "03", title: "Governance Need", desc: "Requires Human Decision Gate across all external client quotes." }
    ],
    draft: `Subject: Executive Proposal & Roadmap: Commercial Asset Workflow AI Integration

Dear Director,
Thank you for inviting our consultation. We specialize in zero-friction AI implementations for C-Suite leadership in Dubai. We have structured a 3-sprint phased deployment with Sprint 1 delivering measurable efficiency in under 14 days.

Attached is our 1-page Executive Strategy Blueprint for your review.
Best regards,
Flávio Barros`,
    shortDraft: `Director: Proposal received and acknowledged. We operate on a Sprint-driven model with quick wins in Week 1. Strategy blueprint attached for 1-click review. - Flávio Barros`,
    executedNotice: "Proposal dispatched to Emaar · CRM record created · Executive follow-up scheduled"
  },
  board_digest: {
    channelBadge: "Cross-Department Aggregator",
    senderName: "Automated Operations Synthesizer",
    duration: "End-of-Week Executive Digest",
    transcript: '"Consolidating weekly logs across Operations, Client Sales, and Delivery. 42 workflow executions completed with 100% human-in-the-loop compliance. Total leadership hours saved: 8.5h."',
    bullets: [
      { id: "01", title: "Executive Time Recovered", desc: "8.5 direct leadership hours saved from administrative triage." },
      { id: "02", title: "Operational Zero-Error", desc: "100% compliance on Human Decision Gates (Zero unapproved emails sent)." },
      { id: "03", title: "Action Required", desc: "1-click sign-off to distribute weekly brief to Board of Directors." }
    ],
    draft: `Executive Weekly Summary for Board of Directors:

1. Operational Efficiency: Leadership recovered 8.5 hours this week via AI workflow triage.
2. Department SLAs: 96% of cross-department inquiries resolved without synchronous meetings.
3. Security & Safety: 100% of client deliverables approved through the Human Decision Gate.
4. Next Sprint Focus: Deploying automated delivery handoffs for client accounts.`,
    shortDraft: `Board Digest: 8.5h saved this week, zero rogue AI incidents, 96% SLA met without extra meetings. Sprint 2 ready. - Flávio Barros`,
    executedNotice: "Digest published to Board portal · Slack executive channel notified · Archived to Notion"
  }
};

let currentScenario = "audio_memo";
let isShortTone = false;
let isApproved = false;
let audioContext = null;

// Initialize sound context on user interaction
function getAudioContext() {
  if (!audioContext) {
    audioContext = new (window.AudioContext || window.webkitAudioContext)();
  }
  return audioContext;
}

// Play pleasant acoustic executive chime
function playChime(type = "success") {
  try {
    const ctx = getAudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);

    if (type === "success") {
      osc.type = "sine";
      osc.frequency.setValueAtTime(523.25, ctx.currentTime); // C5
      osc.frequency.exponentialRampToValueAtTime(659.25, ctx.currentTime + 0.1); // E5
      osc.frequency.exponentialRampToValueAtTime(783.99, ctx.currentTime + 0.25); // G5
      gain.gain.setValueAtTime(0.15, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.6);
      osc.start();
      osc.stop(ctx.currentTime + 0.6);
    } else {
      osc.type = "triangle";
      osc.frequency.setValueAtTime(440, ctx.currentTime); // A4
      gain.gain.setValueAtTime(0.1, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.2);
      osc.start();
      osc.stop(ctx.currentTime + 0.2);
    }
  } catch (e) {
    console.log("Audio feedback: ", e);
  }
}

// Load Scenario
function loadScenario(scenarioId) {
  currentScenario = scenarioId;
  const data = scenarios[scenarioId];
  isShortTone = false;
  isApproved = false;

  // Update tabs
  ["audio_memo", "proposal_request", "board_digest"].forEach((id, idx) => {
    const btn = document.getElementById(`btn-scenario-${idx + 1}`);
    if (id === scenarioId) {
      btn.className = "px-3.5 py-1.5 rounded-xl text-xs font-semibold font-mono transition bg-cyan-500 text-black font-bold";
    } else {
      btn.className = "px-3.5 py-1.5 rounded-xl text-xs font-semibold font-mono transition text-slate-400 hover:text-white";
    }
  });

  // Populate data
  document.getElementById("inputChannelBadge").innerText = data.channelBadge;
  document.getElementById("senderName").innerText = data.senderName;
  document.getElementById("memoDuration").innerText = data.duration;
  document.getElementById("rawInputTranscript").innerText = data.transcript;

  // Bullets
  const bulletsContainer = document.getElementById("synthesisBullets");
  bulletsContainer.innerHTML = data.bullets.map(b => `
    <li class="flex items-start gap-2 bg-slate-950 p-2.5 rounded-xl border border-slate-800/80">
      <span class="text-emerald-400 font-bold font-mono">${b.id}.</span>
      <span><strong>${b.title}:</strong> ${b.desc}</span>
    </li>
  `).join("");

  // Draft
  document.getElementById("draftActionText").innerText = data.draft;

  // Reset Gate State
  const gateState = document.getElementById("gateStateText");
  gateState.className = "text-[11px] font-mono text-amber-400 font-semibold";
  gateState.innerText = "● AWAITING HUMAN APPROVAL";

  const approveBtn = document.getElementById("approveBtn");
  approveBtn.className = "py-3 px-4 bg-emerald-500 hover:bg-emerald-400 active:scale-95 text-black font-extrabold text-xs rounded-xl flex items-center justify-center gap-2 transition shadow-lg shadow-emerald-500/20";
  approveBtn.innerHTML = "<span>✓ APPROVE & DISPATCH</span>";
  approveBtn.disabled = false;

  document.getElementById("executionNotice").classList.add("hidden");
  playChime("click");
}

// Play simulation audio wave animation
let waveInterval = null;
function playSimulationAudio() {
  playChime("click");
  const bars = document.querySelectorAll(".waveform-bar");
  const btn = document.getElementById("simAudioBtn");
  
  if (waveInterval) {
    clearInterval(waveInterval);
    waveInterval = null;
    btn.innerText = "▶ Play Voice";
    bars.forEach(b => b.style.height = "12px");
    return;
  }

  btn.innerText = "⏹ Playing...";
  waveInterval = setInterval(() => {
    bars.forEach(bar => {
      const h = Math.floor(Math.random() * 24) + 6;
      bar.style.height = `${h}px`;
    });
  }, 100);

  setTimeout(() => {
    if (waveInterval) {
      clearInterval(waveInterval);
      waveInterval = null;
      btn.innerText = "▶ Play Voice";
      bars.forEach(b => b.style.height = "12px");
    }
  }, 4000);
}

// Toggle Draft Tone
function calibrateTone() {
  const data = scenarios[currentScenario];
  const draftBox = document.getElementById("draftActionText");
  const calibrateBtn = document.getElementById("calibrateBtn");

  isShortTone = !isShortTone;
  if (isShortTone) {
    draftBox.innerText = data.shortDraft;
    calibrateBtn.innerHTML = "<span>⚡ Standard Executive Tone</span>";
  } else {
    draftBox.innerText = data.draft;
    calibrateBtn.innerHTML = "<span>⚡ Shorter Executive Tone</span>";
  }
  playChime("click");
}

// Execute 1-Click Human Decision Gate
function executeHumanApproval() {
  isApproved = true;
  playChime("success");

  // Animate button
  const approveBtn = document.getElementById("approveBtn");
  approveBtn.className = "py-3 px-4 bg-emerald-600 text-white font-extrabold text-xs rounded-xl flex items-center justify-center gap-2 transition shadow-lg";
  approveBtn.innerHTML = "<span>✓ APPROVED & EXECUTED</span>";
  approveBtn.disabled = true;

  // Gate label
  const gateState = document.getElementById("gateStateText");
  gateState.className = "text-[11px] font-mono text-emerald-400 font-bold";
  gateState.innerText = "✓ AUTHORIZED BY HUMAN GATE (Flávio Barros)";

  // Notice
  const notice = document.getElementById("executionNotice");
  notice.querySelector("span:last-child").innerText = scenarios[currentScenario].executedNotice;
  notice.classList.remove("hidden");

  // Update Tickers
  const hoursTicker = document.getElementById("hoursSavedTicker");
  hoursTicker.innerText = "9.2 hrs (+0.7h)";
  hoursTicker.classList.add("text-emerald-300");

  const valueTicker = document.getElementById("valueSavedTicker");
  valueTicker.innerText = "$1,580.00";

  const salesBadge = document.getElementById("salesStatusBadge");
  salesBadge.className = "px-2 py-0.5 bg-emerald-950 text-emerald-400 font-mono text-[10px] font-bold rounded";
  salesBadge.innerText = "RESOLVED";
}

// Toggle Video Walkthrough section
function toggleVideoWalkthrough() {
  const section = document.getElementById("videoWalkthroughSection");
  if (section.classList.contains("hidden")) {
    section.classList.remove("hidden");
    section.scrollIntoView({ behavior: "smooth" });
  } else {
    section.classList.add("hidden");
  }
}

// Simulated Walkthrough Audio Playback
let audioPlaying = false;
let audioTimer = null;
let currentSeconds = 0;
const totalDuration = 65; // 1:05 min

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

  if (audioPlaying) {
    clearInterval(audioTimer);
    audioPlaying = false;
    playBtn.innerText = "▶";
    trackStatus.innerText = "Paused";
  } else {
    audioPlaying = true;
    playBtn.innerText = "⏸";
    trackStatus.innerText = "Playing Voice Track...";
    playChime("click");

    audioTimer = setInterval(() => {
      currentSeconds++;
      if (currentSeconds > totalDuration) {
        clearInterval(audioTimer);
        audioPlaying = false;
        currentSeconds = 0;
        playBtn.innerText = "▶";
        trackStatus.innerText = "Completed";
        return;
      }

      // Progress bar
      const pct = (currentSeconds / totalDuration) * 100;
      document.getElementById("audioProgressBar").style.width = `${pct}%`;

      // Timer display
      const mins = String(Math.floor(currentSeconds / 60)).padStart(2, "0");
      const secs = String(currentSeconds % 60).padStart(2, "0");
      document.getElementById("videoTimer").innerText = `${mins}:${secs} / 01:05`;

      // Update subtitle line
      const matched = [...narrationLines].reverse().find(l => currentSeconds >= l.at);
      if (matched) {
        document.getElementById("narrationText").innerText = matched.text;
      }
    }, 1000);
  }
}

// Initial scenario load
document.addEventListener("DOMContentLoaded", () => {
  loadScenario("audio_memo");
});
