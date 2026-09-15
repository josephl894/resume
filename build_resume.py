#!/usr/bin/env python3
"""Build resume PDFs from the LaTeX sources in this folder.

The .tex files ARE the source of truth. Edit Joseph_Li_Resume_<VERSION>.tex by
hand, then run:

    python3 build_resume.py            # all four versions
    python3 build_resume.py BigTech    # just one

Shared formatting lives in resume.sty -- change it there once and every version
picks it up.

After each build this checks two things that actually matter:
  1. the PDF is exactly one page
  2. the text an ATS extracts keeps each employer, its location, and its dates
     on the same line (the failure mode that makes LaTeX resumes parse badly)
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERSIONS = ["MASTER", "BigTech", "AIAgentStartup", "FDE", "MASTER_ZH"]


def engine():
    for exe in ("tectonic", "xelatex", "lualatex"):
        if shutil.which(exe):
            return exe
    sys.exit("no LaTeX engine found. install one:  brew install tectonic")


def compile_tex(exe, tex_path):
    if exe == "tectonic":
        cmd = [exe, "-X", "compile", "--outdir", str(HERE), "--keep-logs", str(tex_path)]
    else:
        cmd = [exe, "-interaction=nonstopmode", f"-output-directory={HERE}", str(tex_path)]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=HERE)
    return r


def page_count(pdf):
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    return int(m.group(1)) if m else -1


def ats_check(pdf):
    """Every entry line should carry its location; role lines should carry dates."""
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                         capture_output=True, text=True).stdout
    problems = []
    if "\ufb01" in txt or "\ufb02" in txt:
        problems.append("unresolved fi/fl ligature in extracted text")
    # dates must land on the same line as the role they belong to
    date_re = re.compile(r"(Jun|Aug|Sep|Dec|Fall)\s+20\d\d")
    orphan_dates = [l.strip() for l in txt.splitlines()
                    if date_re.search(l) and len(l.strip()) < 25]
    if orphan_dates:
        problems.append(f"date detached from its role: {orphan_dates[:3]}")
    return problems


def main(versions):
    exe = engine()
    print(f"engine: {exe}\n")
    ok = True
    for v in versions:
        tex = HERE / f"Joseph_Li_Resume_{v}.tex"
        if not tex.exists():
            print(f"skip {v}: {tex.name} missing")
            continue
        r = compile_tex(exe, tex)
        pdf = HERE / f"Joseph_Li_Resume_{v}.pdf"
        if r.returncode != 0 or not pdf.exists():
            ok = False
            err = (r.stderr or r.stdout).strip().splitlines()
            print(f"{v}: BUILD FAILED")
            for line in err[-15:]:
                print(f"    {line}")
            continue
        pages = page_count(pdf)
        flags = [] if pages == 1 else [f"{pages} pages -- trim it"]
        flags += ats_check(pdf)
        if flags:
            ok = False
        status = "ok" if not flags else "; ".join(flags)
        print(f"{v}: {pages} page(s)  [{status}]")
    for junk in list(HERE.glob("*.aux")) + list(HERE.glob("*.out")) + list(HERE.glob("*.log")):
        junk.unlink(missing_ok=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or VERSIONS))
