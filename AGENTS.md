# Resume folder conventions

## The `.tex` files are the only source of truth

Edit `Joseph_Li_Resume_<VERSION>.tex`, then render:

```bash
python3 build_resume.py            # every version
python3 build_resume.py BigTech    # one version
```

Versions: `MASTER`, `BigTech`, `AIAgentStartup`, `FDE`, `MASTER_ZH`.

`MASTER_ZH` is the Chinese translation of `MASTER`. It shares `resume.sty`, so
layout changes reach it automatically, but its content does **not** — when you
edit `MASTER`, translate the same edit into `MASTER_ZH`. It adds `xeCJK` with
`PingFang SC` in its own preamble because Arial has no CJK glyphs; its
`ItalicFont` is deliberately mapped to the upright face, since synthetically
slanted Chinese reads as broken.

**Never** hand-edit a `.pdf`. There is no second source: the
`Joseph_Li_Resume_*.md` research-note files were removed from the working tree
because keeping resume content in two places caused repeated silent drift,
where two pipelines wrote the same PDFs and whichever ran last won.

## Research notes live in git history

The four `.md` files (per-track posting research, bullet-revision rationale,
interview-prep detail behind each bullet, and the reviewer feedback that shaped
them) are preserved at the `notes-archive` tag. To read one:

```bash
git show notes-archive:Joseph_Li_Resume_MASTER.md | less
git show notes-archive:Joseph_Li_Resume_BigTech.md
git show notes-archive:Joseph_Li_Resume_AIAgentStartup.md
git show notes-archive:Joseph_Li_Resume_FDE.md
```

To restore one temporarily for reference (delete it again before committing):

```bash
git checkout notes-archive -- Joseph_Li_Resume_MASTER.md
```

Do not recreate `.md` copies of resume content. New research or interview
notes go in `notes/` as plain text, never as a parallel copy of a `.tex` body.

Shared formatting lives in `resume.sty`. Change it there once rather than in
each `.tex`.

## Do not switch the font back to Helvetica

`resume.sty` sets Arial on purpose. macOS `Helvetica.ttc` stores its ligature
table in Apple's AAT `morx` format, which XeTeX applies and fontspec cannot
disable — `Ligatures=NoCommon`, `RawFeature={-liga;-clig;-rlig}`,
`Renderer=OpenType`, and `Renderer=HarfBuzz` were all tested and every one
still emitted `ﬁ` (U+FB01) into the extracted text. Arial honours `-liga`,
extracts as clean ASCII, and is metrically compatible with Helvetica.

## `build_resume.py` gates every build

It fails the build when any of these regress:

- a version is more than one page
- an unresolved `fi`/`fl` ligature appears in extracted text
- a date gets detached from the role it belongs to

Those are ATS-parsing failures, so treat a non-zero exit as a real problem
rather than something to work around. Two-column rows use `\hfill` inside a
normal paragraph, never `tabular`, because parsers read tabular cells out of
document order.

## Content rules

- One page, always.
- No invented metrics. Every number must be defensible in an interview.
- Prefer multi-week ownership of a named component over small fixes, even when
  the small fix has a tidy number attached.
