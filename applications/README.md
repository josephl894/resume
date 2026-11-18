# Applications

This directory is the record of which tailored resume was sent to which job.
`master_resume.tex` at the repo root stays the source resume. A tailored
resume lives here, next to the job it was made for, and is not copied back
into the master.

## Layout

```
applications/
  INDEX.csv
  README.md
  <YYYY-MM-DD>_<company-slug>_<role-slug>/
    job.md
    Li_Joseph_resume.tex
    Li_Joseph_resume.pdf
    resume.sty          # only when it differs from the repo root
```

The date is the packet date: the day that tailored resume was prepared.
`<company-slug>` and `<role-slug>` are lowercase words separated by hyphens.
The three parts are separated by underscores, so a company slug may itself
contain hyphens (`2026-10-29_maven-robotics_ai-research-engineer`).

`job.md` holds the company, role title, posting URL, posted time, req ID,
status, submit date, and the `master_resume.tex` commit the file was tailored
from. A field with nothing after the colon is unknown. Do not fill one in
by guessing.

Status is one of:

- `submitted` — the application was sent
- `held` — the resume was prepared or the application was paused, and it was not sent
- `unknown` — there is no record of whether it was sent

`resume.sty` is shared. The root `resume.sty` applies to every tailored
resume. A copy is stored in the application folder only when that resume was
built with a different style file. To compile a tailored file from its
folder when no local `resume.sty` is present:

```bash
TEXINPUTS=../..: xelatex Li_Joseph_resume.tex
```

## INDEX.csv

One row per application.

| Column | Meaning |
| --- | --- |
| `date` | Packet date, `YYYY-MM-DD` |
| `company` | Company name |
| `role` | Role title. Empty when the title is not known |
| `posting_url` | Posting URL. Empty when not known |
| `status` | `submitted`, `held`, or `unknown` |
| `folder` | Path of the application directory, relative to the repo root |
| `master_commit` | Full git commit of `master_resume.tex` the tailored resume was edited from. Empty when that commit cannot be determined |

## Add an application

Put the tailored `.tex` and `.pdf` through this script. It creates the
folder and `job.md`, copies `resume.sty` only if it differs from the root
file, and appends the `INDEX.csv` row.

```bash
python3 scripts/add_application.py \
  --date YYYY-MM-DD \
  --company "Company" \
  --company-slug company \
  --role "Role title" \
  --role-slug role-slug \
  --tex /path/to/Li_Joseph_resume.tex \
  --pdf /path/to/Li_Joseph_resume.pdf \
  --status submitted \
  --posting-url "https://example.com/jobs/123" \
  --posted "YYYY-MM-DD" \
  --req-id "REQ123" \
  --submit-date "YYYY-MM-DD" \
  --master-commit <git-sha> \
  --sty /path/to/resume.sty
```

`--role`, `--posting-url`, `--posted`, `--req-id`, `--submit-date`,
`--master-commit`, and `--sty` are optional. Omit a flag to leave that field
blank. `--status` is required and must be `submitted`, `held`, or `unknown`.

Then commit that application by itself so `git log` stays a history of
applications:

```bash
git add applications
git commit -m "apply: Company Role title (YYYY-MM-DD)"
```

The script prints that commit message, using the role slug when the role
title was left blank.
