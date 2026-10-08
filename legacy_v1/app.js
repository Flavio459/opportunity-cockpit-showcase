const stateClass = {
  READY_FOR_REVIEW: "ready",
  NEEDS_INFORMATION: "info",
  HOLD: "hold"
};

const label = {
  READY_FOR_REVIEW: "Ready for review",
  NEEDS_INFORMATION: "Needs information",
  HOLD: "Hold"
};

let opportunities = [];

function safe(value) {
  return value ?? "not informed";
}

function renderSummary(items) {
  const counts = {
    total: items.length,
    ready: items.filter(x => x.state === "READY_FOR_REVIEW").length,
    info: items.filter(x => x.state === "NEEDS_INFORMATION").length,
    hold: items.filter(x => x.state === "HOLD").length
  };
  document.querySelector("#summary").innerHTML = `
    <div class="kpi"><span>Demo opportunities</span><b>${counts.total}</b></div>
    <div class="kpi"><span>Ready for review</span><b>${counts.ready}</b></div>
    <div class="kpi"><span>Needs information</span><b>${counts.info}</b></div>
    <div class="kpi"><span>Hold</span><b>${counts.hold}</b></div>
  `;
}

function renderCards(items) {
  const root = document.querySelector("#cards");
  if (!items.length) {
    root.innerHTML = '<div class="card"><p>No opportunities in this filter.</p></div>';
    return;
  }
  root.innerHTML = items.map(o => `
    <article class="card">
      <div class="head">
        <div>
          <span class="state ${stateClass[o.state]}">${label[o.state]}</span>
          <div class="title">${o.title}</div>
          <div class="meta">${o.company} · ${o.modality} · ${o.contract_type}</div>
        </div>
        <button class="gate" type="button" onclick="alert('Demo only: external actions remain behind a human gate.')">Human Gate</button>
      </div>

      <div class="grid">
        <div class="metric"><span>Fit</span><b>${o.fit}</b></div>
        <div class="metric"><span>Conditions</span><b>${o.conditions}</b></div>
        <div class="metric"><span>Compensation</span><b>${safe(o.compensation)}</b></div>
        <div class="metric"><span>Workload</span><b>${safe(o.workload)}</b></div>
      </div>

      <div class="signals">
        ${o.signals.map(s => `<span class="signal ${s.kind}">${s.text}</span>`).join("")}
      </div>

      <details>
        <summary>Inspect evidence and verifier output</summary>
        <div class="detailgrid">
          <section class="panel">
            <h3>Requirement evidence</h3>
            <ul>
              ${o.evidence.map(e => `<li><strong>${e.requirement}</strong>: ${e.status} — ${e.note}</li>`).join("")}
            </ul>
          </section>
          <section class="panel">
            <h3>Verifier</h3>
            <p>${o.verifier}</p>
            <p><strong>Next safe action:</strong> ${o.next_action}</p>
          </section>
        </div>
      </details>
    </article>
  `).join("");
}

async function load() {
  const res = await fetch("data/opportunities.json");
  opportunities = await res.json();
  renderSummary(opportunities);
  renderCards(opportunities);
}

document.querySelector("#filter").addEventListener("change", e => {
  const value = e.target.value;
  const items = value === "all" ? opportunities : opportunities.filter(x => x.state === value);
  renderCards(items);
});

load().catch(() => {
  document.querySelector("#cards").innerHTML = '<div class="card"><p>Could not load synthetic demo data.</p></div>';
});
