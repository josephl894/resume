#!/usr/bin/env python3
"""Record one tailored resume as an application.

Creates applications/<YYYY-MM-DD>_<company-slug>_<role-slug>/, writes job.md,
copies the tailored .tex and .pdf, copies resume.sty only when it differs from
the repo root, and appends one row to applications/INDEX.csv.

Leave a fact blank by omitting its flag. Do not guess a posting URL, req ID,
role title, or submit date.

    python3 scripts/add_application.py \
        --date 2026-11-02 \
        --company "Anthropic" \
        --company-slug anthropic \
        --role "Research Engineer, Pretraining" \
        --role-slug pretraining \
        --tex /path/to/Li_Joseph_resume.tex \
        --pdf /path/to/Li_Joseph_resume.pdf \
        --status submitted \
        --posting-url "https://example.com/jobs/123" \
        --posted "2026-11-01" \
        --req-id "123" \
        --submit-date "2026-11-02" \
        --master-commit 77b0e52cf04d34feb62c0abc7a1320989767489f \
        --sty /path/to/resume.sty
"""

from __future__ import annotations

import argparse
import csv
import datetime
import filecmp
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS = ROOT / "applications"
INDEX_PATH = APPS / "INDEX.csv"
ROOT_STY = ROOT / "resume.sty"

COLUMNS = [
    "date",
    "company",
    "role",
    "posting_url",
    "status",
    "folder",
    "master_commit",
]
STATUSES = ("submitted", "held", "unknown")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA_RE = re.compile(r"^[0-9a-f]{7,40}$")


class AddError(Exception):
    pass


def _die(message: str) -> None:
    raise AddError(message)


def _field(label: str, value: str) -> str:
    value = value.strip()
    if value:
        return f"- {label}: {value}"
    return f"- {label}:"


def render_job_md(spec: dict) -> str:
    lines = [
        "# Application",
        "",
        _field("Company", spec["company"]),
        _field("Role", spec["role"]),
        _field("Posting URL", spec["posting_url"]),
        _field("Posted", spec["posted"]),
        _field("Req ID", spec["req_id"]),
        _field("Status", spec["status"]),
        _field("Submit date", spec["submit_date"]),
        _field("Master resume commit", spec["master_commit"]),
        "",
    ]
    return "\n".join(lines)


def folder_name(date: str, company_slug: str, role_slug: str) -> str:
    return f"{date}_{company_slug}_{role_slug}"


def resolve_commit(root: Path, sha: str) -> str:
    if not sha:
        return ""
    if not SHA_RE.match(sha):
        _die(f"master commit {sha!r} is not a hex sha")
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--verify", f"{sha}^{{commit}}"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError:
        _die(f"master commit {sha} is not in this repo")
    return out.stdout.strip()


def read_index(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != COLUMNS:
            _die(f"{path} header is {reader.fieldnames}, expected {COLUMNS}")
        return list(reader)


def write_index(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def add_application(root: Path, spec: dict) -> Path:
    """Create the application folder and append INDEX.csv. Returns the folder."""
    apps = root / "applications"
    index_path = apps / "INDEX.csv"
    name = folder_name(spec["date"], spec["company_slug"], spec["role_slug"])
    rel = f"applications/{name}"
    dest = apps / name

    rows = read_index(index_path) if index_path.exists() else []
    if dest.exists():
        _die(f"{rel} already exists")
    if any(row["folder"] == rel for row in rows):
        _die(f"{rel} is already in {index_path}")

    tex = Path(spec["tex"]).resolve()
    pdf = Path(spec["pdf"]).resolve()
    if not tex.is_file() or tex.suffix != ".tex":
        _die(f"tex is not a .tex file: {spec['tex']}")
    if not pdf.is_file() or pdf.suffix != ".pdf":
        _die(f"pdf is not a .pdf file: {spec['pdf']}")
    if not pdf.read_bytes().startswith(b"%PDF"):
        _die(f"pdf does not look like a PDF: {spec['pdf']}")

    master = spec["master_commit"]
    if master:
        master = resolve_commit(root, master)

    dest.mkdir(parents=True)
    try:
        shutil.copy2(tex, dest / tex.name)
        shutil.copy2(pdf, dest / pdf.name)
        sty_note = "not provided"
        sty_src = spec.get("sty")
        if sty_src:
            sty = Path(sty_src).resolve()
            if not sty.is_file():
                _die(f"sty is not a file: {sty_src}")
            root_sty = root / "resume.sty"
            if root_sty.is_file() and filecmp.cmp(sty, root_sty, shallow=False):
                sty_note = "omitted (identical to repo root resume.sty)"
            else:
                shutil.copy2(sty, dest / "resume.sty")
                sty_note = "copied (differs from repo root resume.sty)"
        job = render_job_md({**spec, "master_commit": master})
        (dest / "job.md").write_text(job)
        rows.append(
            {
                "date": spec["date"],
                "company": spec["company"],
                "role": spec["role"],
                "posting_url": spec["posting_url"],
                "status": spec["status"],
                "folder": rel,
                "master_commit": master,
            }
        )
        write_index(index_path, rows)
    except Exception:
        shutil.rmtree(dest, ignore_errors=True)
        raise

    role_for_message = spec["role"] or spec["role_slug"]
    print(f"folder: {rel}")
    print(f"resume.sty: {sty_note}")
    print(f"commit-message: apply: {spec['company']} {role_for_message} ({spec['date']})")
    return dest


def parse_args(argv: list[str]) -> dict:
    parser = argparse.ArgumentParser(
        description="Add one tailored resume to applications/ and INDEX.csv."
    )
    parser.add_argument("--date", required=True, help="Packet date, YYYY-MM-DD")
    parser.add_argument("--company", required=True, help="Company name")
    parser.add_argument(
        "--company-slug",
        required=True,
        help="Lowercase folder token for the company, e.g. maven-robotics",
    )
    parser.add_argument(
        "--role",
        default="",
        help="Role title. Omit when it is not known.",
    )
    parser.add_argument(
        "--role-slug",
        required=True,
        help="Lowercase folder token for the role, e.g. ai-research-engineer",
    )
    parser.add_argument("--tex", required=True, help="Tailored .tex file")
    parser.add_argument("--pdf", required=True, help="Tailored .pdf file")
    parser.add_argument(
        "--sty",
        default="",
        help="resume.sty used to build the PDF. Copied only if it differs from the repo root.",
    )
    parser.add_argument("--status", required=True, choices=STATUSES)
    parser.add_argument("--posting-url", default="")
    parser.add_argument("--posted", default="", help="When the job was posted, if known")
    parser.add_argument("--req-id", default="")
    parser.add_argument("--submit-date", default="", help="When the application was submitted, if known")
    parser.add_argument(
        "--master-commit",
        default="",
        help="Commit of master_resume.tex this resume was tailored from. Omit if unknown.",
    )
    args = parser.parse_args(argv)

    if not DATE_RE.match(args.date):
        _die("--date must be YYYY-MM-DD")
    year, month, day = (int(part) for part in args.date.split("-"))
    try:
        datetime.date(year, month, day)
    except ValueError:
        _die(f"--date is not a real date: {args.date}")
    if not SLUG_RE.match(args.company_slug):
        _die("--company-slug must be lowercase words separated by single hyphens")
    if not SLUG_RE.match(args.role_slug):
        _die("--role-slug must be lowercase words separated by single hyphens")
    if any(c in args.company for c in "\n\r"):
        _die("--company must be a single line")
    if any(c in args.role for c in "\n\r"):
        _die("--role must be a single line")

    return {
        "date": args.date,
        "company": args.company.strip(),
        "company_slug": args.company_slug,
        "role": args.role.strip(),
        "role_slug": args.role_slug,
        "tex": args.tex,
        "pdf": args.pdf,
        "sty": args.sty,
        "status": args.status,
        "posting_url": args.posting_url.strip(),
        "posted": args.posted.strip(),
        "req_id": args.req_id.strip(),
        "submit_date": args.submit_date.strip(),
        "master_commit": args.master_commit.strip(),
    }


def main(argv: list[str] | None = None) -> None:
    try:
        spec = parse_args(sys.argv[1:] if argv is None else argv)
        if not spec["company"]:
            _die("--company is empty")
        add_application(ROOT, spec)
    except AddError as exc:
        sys.exit(f"add_application: {exc}")


if __name__ == "__main__":
    main()
