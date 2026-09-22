# Curso: Poesia Grega Arcaica

Website acadêmico sobre a poesia grega arcaica não épica: lírica monódica, lírica coral, iambo e eleja. Construído com Astro + Starlight.

## Módulos

| # | Módulo | Conteúdo |
|---|--------|----------|
| 1 | Fundamentos | Contexto, oralidade, métrica, gêneros |
| 2 | Lírica Monódica | Sápo, Alceu, Anacreonte, Corina |
| 3 | Lírica Coral | Estesícoro, Íbaco, Simônides, Píndaro |
| 4 | Iambo | Arquiloco, Semónides, Solão |
| 5 | Eleja | Calino, Tirtea, Mimnermo, Xenófanes |
| 6 | Tradições e Geografias | Lesbos, Atenas, Esparta, Jônia, Magna Grécia |
| 7 | Texto e Transmissão | Papirologia, edições, fragmentologia |
| 8 | Recepção | Antiguidade Tardia, Renascimento, leituras modernas |

## Como usar

```bash
# Instalar dependências
npm install

# Servidor de desenvolvimento
npm run dev

# Build de produção
npm run build

# Verificação
python scripts/verificar-site.py
```

## Como editar

- **Conteúdo:** arquivos `.mdx` em `src/content/docs/`
- **Configuração:** `astro.config.mjs`
- **Estilos:** `src/styles/custom.css`
- **Validação:** `scripts/verificar-site.py`

## Estrutura

```
├── astro.config.mjs
├── package.json
├── scripts/
│   └── verificar-site.py
├── src/
│   ├── content/
│   │   ├── config.ts
│   │   └── docs/
│   │       ├── index.mdx
│   │       ├── modulo-1/
│   │       ├── modulo-2/
│   │       ├── modulo-3/
│   │       ├── modulo-4/
│   │       ├── modulo-5/
│   │       ├── modulo-6/
│   │       ├── modulo-7/
│   │       ├── modulo-8/
│   │       ├── recursos/
│   │       └── sobre.mdx
│   ├── components/
│   ├── layouts/
│   └── styles/
│       └── custom.css
└── netlify.toml
```

## Licença

CC-BY 4.0 — Compartilhe e adapte, cite a fonte.
