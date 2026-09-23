import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { fileURLToPath } from 'node:url';

export default defineConfig({
  site: 'https://curso-poesia-grega-arcaacia.netlify.app',
  title: 'Poesia Grega Arcaica',
  description: 'Curso sobre Lírica, Iambografia e Eleja na Grécia Arcaica (séc. VIII–V a.C.)',
  logo: {
    src: '/logo.svg',
    alt: 'Poesia Grega Arcaica',
  },
  integrations: [
    starlight({
      title: 'Poesia Grega Arcaica — Curso',
      description: 'Lírica, Iambografia e Eleja na Grécia Arcaica',
      favicon: '/favicon.svg',
      head: [
        { tag: 'meta', attrs: { property: 'og:type', content: 'website' } },
        { tag: 'meta', attrs: { property: 'og:title', content: 'Poesia Grega Arcaica — Curso' } },
      ],
      sidebar: [
        { label: 'Curso', autogenerate: { directory: 'docs' } },
        { label: 'Recursos', autogenerate: { directory: 'docs/recursos' } },
        { label: 'Sobre', autogenerate: { directory: 'docs/sobre' } },
      ],
    }),
  ],
  vite: {
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },
  },
});
