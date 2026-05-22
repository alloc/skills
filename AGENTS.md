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

## Skill Update Instructions

Skill update prompts are maintained in `updates.yaml` at the repository root. The top-level keys are skill categories, and each category contains skill-name keys whose values are multiline update prompts.

When asked to update a specific skill:

1. Locate the skill at `CATEGORY/SKILL_NAME/SKILL.md`.
2. Read its update prompt with:

   ```sh
   yq -r '.CATEGORY.SKILL_NAME' updates.yaml
   ```

   Replace `CATEGORY` and `SKILL_NAME` with the requested skill path components.
3. If `updates.yaml` is missing, the skill has no entry, or the resolved value is `null`, inform the user that no update instructions exist for that skill and decline to update it.
4. Resolve prompt variables before following the prompt. Variables use `$name` syntax and refer to strings under `rules` in the same file. For example, `$default` means the value from:

   ```sh
   yq -r '.rules.default' updates.yaml
   ```

   Replace each variable occurrence with its corresponding `rules.NAME` string. If a referenced rule is missing or resolves to `null`, inform the user and decline to update the skill.
5. Follow the fully resolved prompt before editing the skill.
