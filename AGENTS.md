# Repository Instructions

## Skill Layout

- Every skill must live at exactly `CATEGORY/SKILL_NAME/SKILL.md` relative to this repository.
- This means every `SKILL.md` must have two parent directories: the skill category and the skill root.
- Do not place `SKILL.md` files directly at the repository root.
- Do not nest skills deeper than `CATEGORY/SKILL_NAME/SKILL.md`.
- Categories must be specific and meaningful. Broad catch-all categories such as `packages` are prohibited.
- Acceptable category examples include `frontend`, `desktop`, `documentation`, `codex`, `media`, `protocols`, and `workflows`.
- Keep each skill's bundled resources, such as `agents/`, `references/`, `scripts/`, or `demos/`, inside that skill root.

Before finishing changes that add, move, or remove skills, verify the layout:

```sh
rg --files -g 'SKILL.md' | awk -F/ '{ if (NF != 3 || $1 == "packages") { print "bad " $0; bad=1 } } END { exit bad }'
```
