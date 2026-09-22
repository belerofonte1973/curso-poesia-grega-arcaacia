#!/usr/bin/env python3
"""Verificador de integridade do site Poesia Grega Arcaica."""
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DIST = ROOT / "dist"
CONTENT = ROOT / "src" / "content" / "docs"

def find_mdx_files():
    """Lista todos os arquivos .mdx no diretório de conteúdo."""
    return list(CONTENT.rglob("*.mdx"))

def check_frontmatter(content, filepath):
    """Verifica se o frontmatter YAML está presente e tem campos obrigatórios."""
    if not content.startswith("---"):
        return [f"Sem frontmatter: {filepath}"]
    
    errors = []
    # Extrair frontmatter
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return [f"Frontmatter malformado: {filepath}"]
    
    fm = match.group(1)
    if "title:" not in fm:
        errors.append(f"Sem 'title' no frontmatter: {filepath}")
    if "description:" not in fm:
        errors.append(f"Sem 'description' no frontmatter: {filepath}")
    
    # Verificar tamanho da description
    desc_match = re.search(r"description:\s*['\"](.+?)['\"]", fm)
    if desc_match and len(desc_match.group(1)) > 160:
        errors.append(f"Description > 160 chars: {filepath}")
    
    return errors

def check_content_quality(content, filepath):
    """Verifica qualidade básica do conteúdo."""
    errors = []
    warnings = []
    
    # Remover frontmatter para análise do corpo
    body = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)
    
    # Verificar tamanho mínimo (módulos precisam ter conteúdo)
    if filepath.name != "index.mdx" and len(body) < 5000:
        warnings.append(f"Conteúdo curto (<5KB): {filepath}")
    
    # Verificar presença de headings
    if body.count("## ") < 3:
        warnings.append(f"Poucos headings (##): {filepath}")
    
    # Verificar presença de bibliografia
    if "Bibliografia" not in body and filepath.name != "index.mdx" and filepath.name != "sobre.mdx":
        if filepath.parent.name != "recursos":
            warnings.append(f"Sem seção de Bibliografia: {filepath}")
    
    # Verificar presença de citações acadêmicas
    citations = re.findall(r"\([A-Z][a-záéíóú]+,?\s*\d{4}", body)
    if len(citations) < 3 and filepath.name != "index.mdx":
        warnings.append(f"Poucas citações acadêmicas: {filepath} ({len(citations)} encontradas)")
    
    return errors, warnings

def check_spanish_leak(content, filepath):
    """Detecta vazamento de espanhol em conteúdo PT-BR."""
    spanish_only = [
        r"\bel\b", r"\bla\b", r"\blos\b", r"\bdel\b",
        r"\bhay\b", r"\bhebreo\b", r"\bpueblo\b", r"\btierra\b", r"\bCanaán\b",
        r"\bAntiguo\b", r"\bsiglos\b"
    ]
    
    warnings = []
    body = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)
    
    for pattern in spanish_only:
        matches = re.findall(pattern, body)
        if matches:
            # Verificar se é parte de título legítimo (editora Siglo XXI, etc.)
            context_matches = re.findall(r".{0,30}" + pattern + r".{0,30}", body)
            for ctx in context_matches:
                if "Siglo XXI" in ctx or "Antiguo Oriente" in ctx:
                    continue
                warnings.append(f"Possível espanhol ({pattern}): {filepath} -> ...{ctx}...")
                break
    
    return warnings

def main():
    mdx_files = find_mdx_files()
    
    if not mdx_files:
        print("ERRO: Nenhum arquivo .mdx encontrado!")
        sys.exit(1)
    
    all_errors = []
    all_warnings = []
    
    for f in mdx_files:
        content = f.read_text(encoding="utf-8")
        
        # Frontmatter
        fm_errors = check_frontmatter(content, f.relative_to(ROOT))
        all_errors.extend(fm_errors)
        
        # Qualidade
        q_errors, q_warnings = check_content_quality(content, f.relative_to(CONTENT))
        all_errors.extend(q_errors)
        all_warnings.extend(q_warnings)
        
        # Espanhol
        sp_warnings = check_spanish_leak(content, f.relative_to(ROOT))
        all_warnings.extend(sp_warnings)
    
    # Relatório
    print(f"\n{'='*60}")
    print(f"VERIFICAÇÃO DO SITE — Poesia Grega Arcaica")
    print(f"{'='*60}")
    print(f"Arquivos verificados: {len(mdx_files)}")
    print(f"Falhas: {len(all_errors)}")
    print(f"Avisos: {len(all_warnings)}")
    
    if all_errors:
        print(f"\n--- FALHAS ---")
        for e in all_errors:
            print(f"  ✗ {e}")
    
    if all_warnings:
        print(f"\n--- AVISOS ---")
        for w in all_warnings:
            print(f"  ⚠ {w}")
    
    if all_errors:
        print(f"\nRESULTADO: REPROVADO ({len(all_errors)} falhas)")
        sys.exit(1)
    else:
        print(f"\nRESULTADO: APROVADO")
        if all_warnings:
            print(f"  ({len(all_warnings)} avisos para revisar)")
        sys.exit(0)

if __name__ == "__main__":
    main()
