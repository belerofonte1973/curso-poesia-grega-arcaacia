# Curso: Poesia Grega Arcaica — Lírica, Iambografia e Eleja

## Visão Geral

Curso acadêmico progressivo sobre a poesia grega arcaica **não épica**, cobrindo lírica monódica, lírica coral, iambo e eleja. Público: todos os níveis (iniciante a pesquisador), com escada didática progressiva.

**Formato:** Website acadêmico interativo (Astro + Starlight)
**Idioma:** PT-BR
**Conteúdo:** ~8 módulos, ~40 páginas de conteúdo

---

## Módulos do Curso

### Módulo 1 — Fundamentos: O Mundo da Poesia Arcaica
1.1. Contexto histórico: Grécia arcaica (séc. VIII–VI a.C.)
1.2. Oralidade, performance e texto escrito
1.3. Métrica grega essencial (dactílio, jambo, coríambo, ditrofo)
1.4. A kithara e o aulos: acompanhamento musical
1.5. Géneros poéticos: lírica, iambo, eleja, épico

### Módulo 2 — A Lírica Monódica: Lesbos e Ática
2.1. Sáfo de Mitilene: a voz da intimidade
   - Fragmentos principais (Ode a Afrodita, Fragmento 31)
   - Temas: amor, beleza, rivalidade, mundo feminino
   - Transmissão e história da recepção
2.2. Alceu de Mitilene: política e banquet
   - Fragmentos políticos e de simposião
   - A linguagem alccana: metáfora náutica
   - Relação com Sáfo
2.3. Anacreonte de Teos: o poeta do simposio
   - Anacreônticas: autoria e tradição
   - Temas: vinho, juventude, eros
2.4. Corina e os poetas de Tanagra

### Módulo 3 — A Lírica Coral
3.1. Estesícoro de Himara: o criador do coro narrativo
   - Palinódia, Gerioneida, Orestes
   - Estrutura triádica (stropha, antistropha, epodos)
3.2. Íbacos de Régio: eros e atletismo
   - Fragmento a Croisos
   - Relação com a escultura arcaica
3.3. Simônides de Ceos: o poeta da encomia
   - Epitáfios das Termópilas
   - Dísticos célebres: "o limite humano"
   - Relação com a tirania e os Pisistrátidas
3.4. Bacquílides: o sobrinho e o ditirambo
3.5. Píndaro: o apogeu da lírica coral
   - Olímpicas, Píticas, Nemeísticas, Ístmicas
   - Mito, vitória e ética aristocrática

### Módulo 4 — O Iambo: Poesia da Agressão e do Real
4.1. Arquiloco de Paros: o inventor do jambo
   - Fragmentos satíricos e polêmicos
   - A epoché de Neobule: iambo como performance
   - Inscrição de Micenas e a cultura do guerreiro
4.2. Semónides (Hipônax) de Éfeso: misoginia e paródia
   - O catálogo das mulheres (fr. 7)
   - O iambo como linguagem do rebaixamento
4.3. Solão de Atenas: iambo político e legislativo
   - Eunomia e os fragmentos elegíacos
   - A lei e a poesia

### Módulo 5 — A Eleja: O Verso da Reflexão
5.1. Calino de Éfeso: a eleja guerreira
   - Hinos e exhortação
5.2. Tirteo de Esparta: a disciplina hoplita
   - Eunomia e os poemas de guerra
   - A recepção espartana
5.3. Mimnermo de Colofão: o lirismo hedonista
   - Fragmentos sobre a velhice e o amor
   - Relação com a elegia helenística
5.4. Xenófanes de Colofão: a eleja filosófica
   - Crítica da religião antropomórfica

### Módulo 6 — Tradições e Geografias
6.1. A Lesbos de Sáfo e Alceu: círculos e educação
6.2. Atenas arcaica: Simónides, Solão e o simposio
6.3. Esparta e a poesia guerreira
6.4. A Jônia: Anacreonte, Xenófates e a fronteira grego-pérsica
6.5. Sicília e Magna Grécia: Estesícoro e Estesícoro

### Módulo 7 — Texto, Transmissão e Crítica Textual
7.1. A transmissão manuscrita dos fragmentos
7.2. Papirologia: Oxyrhynchus e novos achados
7.3. Fragmentologia: metodologia de edição
7.4. Principais edições críticas (Lobel-Page, Davies, West)

### Módulo 8 — Recepção e Fortuna
8.1. A Antiguidade Tardia e Bizâncio
8.2. O Renascimento: edição aldina e humanismo
8.3. A tradição latim (Catulo, Horácio, Ovídio)
8.4. Leituras modernas: Hegel, Nietzsche, os românticos
8.5. Traduções brasileiras e comentários em PT-BR

---

## Estrutura Técnica do Site

```
poesia-grega-arcaacia/
├── astro.config.mjs
├── src/
│   ├── content.config.ts
│   ├── content/docs/
│   │   ├── index.mdx           # Home/Landing
│   │   ├── modulo-1/           # Fundamentos
│   │   ├── modulo-2/           # Lírica Monódica
│   │   ├── modulo-3/           # Lírica Coral
│   │   ├── modulo-4/           # Iambo
│   │   ├── modulo-5/           # Eleja
│   │   ├── modulo-6/           # Tradições
│   │   ├── modulo-7/           # Texto/Transmissão
│   │   ├── modulo-8/           # Recepção
│   │   ├── recursos/           # Bibliografia, glossário
│   │   └── sobre.mdx
│   ├── components/
│   ├── styles/
│   └── layouts/
├── templates/
│   ├── briefing-modulo.md
│   └── validar-conteudo.py
├── scripts/
│   └── verificar-site.py
├── netlify.toml
└── README.md
```

## Calibração

- Modelo principal: longcat-2.0:free (1M ctx)
- Subagentes: deepseek-v4-flash (reasoning high)
- Profundidade: aprovado (triangulação de fontes)
- Idioma: PT-BR
- Citação: autor, ano, p.X — sempre que possível

---

## Produção (Ordem)

1. Scaffold do site Astro + Starlight
2. Módulo 1 (Fundamentos) — escrito pelo pai
3. Módulos 2–3 (Lírica Monódica e Coral) — subagentes
4. Módulos 4–5 (Iambo e Eleja) — subagentes
5. Módulos 6–8 — subagentes
6. Recursos (bibliografia, glossário)
7. Build + validação
8. Correções finais

---

**Data de criação:** 22/09/2026
**Versão:** 1.0
