# CHECKLIST DE PADRÃO E CRITÉRIO DE ENTREGA EXECUTIVA (WOC)
**Status:** Obrigatório e Canônico  
**Autoridade:** Wii Ops Center / Governança Flávio Souza Barros  
**Objetivo:** Garantir que Flávio nunca seja utilizado como testador manual ou validador de cascas. Toda entrega deve passar pelos 5 portões antes de ser apresentada.

---

## Princípio Central
> *"Transformar decisões em mudanças observáveis e verificadas. Documentos, planos ou cascas vazias não são resultado por si só."*  
> — AGENTS.md (Wii Ops Center)

Nenhuma funcionalidade pode ser apresentada ao cliente ou à diretoria como "concluída" se contiver simulações parciais, botões quebrados, áudios robóticos genéricos ou elementos visuais mal acabados.

---

## Os 5 Portões Obrigatórios de Verificação (Quality Gates)

### 🔴 Gate 1: Proibição Absoluta de Placeholders ("Zero Shell Gate")
* **Regra:** Nunca apresentar uma interface onde uma ação prometida resulte em uma casca vazia.
* **Critério de Aceite:**
  - Se há um botão *"Watch Executive Walkthrough"*, deve existir um arquivo de vídeo físico real (`.mp4`), com áudio mixado, taxa de quadros estável (1080p / 30fps) e player HTML5 nativo com controles funcionais.
  - Se há um botão *"Play Voice"*, deve disparar um stream/áudio real, com feedback auditivo e animação de onda sincronizada.
  - Proibido containers com `setTimeout` fingindo que algo aconteceu quando o usuário espera mídia real.

---

### 🔴 Gate 2: Paridade Multilíngue e Mídia Real ("Audio & i18n Fidelity Gate")
* **Regra:** Em soluções para mercados globais e multilíngues (ex: Dubai / UAE), todos os idiomas prometidos devem ter paridade completa de dados e áudio.
* **Critério de Aceite:**
  - **Idiomas Canônicos:** Inglês (`en`), Árabe (`ar` com suporte nativo a `dir="rtl"`), Português (`pt`).
  - **Qualidade Sonora:** Proibido uso cru de síntese de voz nativa robótica do sistema operacional (`SpeechSynthesis`) em demonstrações de alto escalão. Uso mandatório de arquivos `.mp3` de alta fidelidade pré-renderizados para cada idioma.
  - **Comutação Dinâmica:** Trocar de idioma deve interromper qualquer áudio anterior e preparar a reprodução do idioma correto sem travamentos.

---

### 🔴 Gate 3: Geometria Visual & Ergonomia ("Anti-Slop & Button Gate")
* **Regra:** A interface deve seguir rigorosamente os princípios de *Design Craftsmanship* (Impeccable Design / 8pt Grid).
* **Critério de Aceite:**
  - **Proibido Pílulas Exageradas:** Evitar botões com `rounded-full` grotescos que espremem textos longos. Usar `rounded-lg` (8px) ou `rounded-md` (6px) com paddings proporcionais (`px-4 py-2.5`).
  - **Zero Duplicação de Ícones:** NUNCA concatenar ícone manual (`▶`) com strings de dicionário que já tragam o mesmo ícone (evita aberrações como `▶ ▶ Play Voice`).
  - **Tipografia Balanceada:** Textos de ação em `text-xs` com `font-semibold` ou `font-bold`. Se o texto for longo em alemão, português ou árabe, ajustar padding e evitar quebras estranhas.

---

### 🔴 Gate 4: Teste Automatizado TDD ("Continuous Verification Gate")
* **Regra:** Nenhum commit ou push é liberado sem execução de suíte de testes determinística.
* **Critério de Aceite:**
  - **Dicionários:** Teste unitário verificando que 100% das chaves i18n existem de forma simétrica em `en`, `ar` e `pt`.
  - **Cenários Executivos:** Verificação de que cada cenário (Triagem de Voz, RFP, Digest) possui transcrição, exatamente 3 bullets estratégicos e minutas calibradas.
  - **Integridade dos Assets:** Teste automatizado que confere a existência em disco e o tamanho mínimo em bytes dos arquivos `.mp4` e `.mp3`.
  - **Cálculos Financeiros:** Validação matemática dos valores de ROI e taxa horária acordada ($39.00/h).

---

### 🔴 Gate 5: Verificação de Renderização em Runtime ("Smoke & Headless Gate")
* **Regra:** O agente deve inspecionar a página renderizada no navegador (via Headless Chrome ou servidor local) antes da entrega final.
* **Critério de Aceite:**
  - Zero erros 404 de assets (imagens, áudios, vídeos).
  - Zero erros não capturados no console do navegador (`console.error`).
  - O elemento `<video>` carrega metadados e primeiro frame (`poster`) corretamente.

---

## Matriz de Execução Rápida do Agente

Antes de enviar qualquer mensagem de conclusão para o usuário, o agente deve rodar mentalmente e registrar:

```markdown
[x] Gate 1: Vídeo real embedado e funcional (walkthrough_executive.mp4 > 900KB)
[x] Gate 2: Áudios reais gravados para EN, AR e PT (voice_memo_*.mp3 > 100KB cada)
[x] Gate 3: Botões refinados (sem duplicação de símbolos, padding ergonômico)
[x] Gate 4: Suíte TDD 100% verde (node --test executado com 0 falhas)
[x] Gate 5: Runtime verificado sem erros de console ou links quebrados
```
