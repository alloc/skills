---
name: godot-prompter
description: Route Godot 4.x development work to the focused GodotPrompter skill or skills stored with this skill. Use for Godot project setup, architecture, gameplay systems, UI, networking, rendering, testing, debugging, optimization, deployment, or supported Godot addons.
---

# GodotPrompter

Treat this skill as a router. The maintained GodotPrompter collection is pinned at
[`references/godot-prompter/skills/`](references/godot-prompter/skills/).

## Route the task

Choose the smallest set of domain skills that covers the request. Read each selected
`SKILL.md` completely before acting, then follow its instructions. Resolve links in a
selected skill relative to that skill's directory, and read only the linked references
needed for the task.

| Work | Skills |
| --- | --- |
| Setup, design, teaching | `godot-project-setup`, `godot-brainstorming`, `godot-mentor` |
| Architecture and data | `scene-organization`, `state-machine`, `event-bus`, `component-system`, `resource-pattern`, `dependency-injection` |
| Player and gameplay | `player-controller`, `input-handling`, `inventory-system`, `ability-system`, `dialogue-system`, `save-load`, `ai-navigation`, `camera-system` |
| Animation and audio | `animation-system`, `tween-animation`, `audio-system` |
| UI and localization | `godot-ui`, `hud-system`, `responsive-ui`, `localization` |
| Physics and worlds | `physics-system`, `2d-essentials`, `3d-essentials`, `math-essentials`, `procedural-generation` |
| Rendering and effects | `shader-basics`, `particles-vfx` |
| Multiplayer | `multiplayer-basics`, `multiplayer-sync`, `dedicated-server` |
| Scripting and native code | `gdscript-patterns`, `gdscript-advanced`, `csharp-godot`, `csharp-signals`, `gdextension`, `multithreading` |
| Assets, editor, and release | `assets-pipeline`, `addon-development`, `export-pipeline`, `mobile-development`, `xr-development` |
| Quality work | `godot-testing`, `godot-debugging`, `godot-optimization`, `godot-code-review` |
| Supported addons | `beehave`, `limboai`, `dialogue-manager`, `phantom-camera`, `popochiu` |

The selected file is `references/godot-prompter/skills/<skill-name>/SKILL.md`.
Inspect frontmatter descriptions in that directory when the table leaves the choice
unclear. Use `using-godot-prompter` only for upstream platform-specific guidance.

When a request spans domains, combine the relevant skills. Keep the user's request in
control if an upstream skill assumes a broader workflow or side effect.
