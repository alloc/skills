---
name: terminal-screencast-svg
description: Create terminal screencast SVGs from command-line demos using asciinema and svg-term-cli, including recording, rendering, timing, framing, and README/docs embeds.
---

# Terminal Screencast SVG

## Default Stance

- Prefer the 60devs pattern: record with `asciinema`, render with `svg-term-cli`, then embed the resulting SVG.
- Prefer local `.cast` files unless the user explicitly wants to upload to asciinema.org; uploads may expose commands, paths, prompts, and output.
- Keep demos short, deterministic, and clean enough to re-record rather than repair frame-by-frame.
- Use `--window` framing and a max idle time around 2 seconds by default.
- Add useful alt text and a constrained display width when embedding.

## Start Here

1. Identify the exact command-line behavior to demonstrate and where the SVG will be embedded.
2. Check for secrets before recording. Cast files are text-like session logs; treat them as publishable artifacts.
3. Verify tools or install them:
   ```bash
   asciinema --version
   svg-term --help
   # Common installs:
   brew install asciinema          # macOS/Homebrew option
   npm install -g svg-term-cli     # provides the `svg-term` command
   ```
4. Read [60devs-terminal-svg-screencasts.md](./references/60devs-terminal-svg-screencasts.md) when you need the source blog's exact commands, install notes, or embed snippet.

## Workflow

1. Prepare the terminal.
   - Use a reasonably narrow terminal width so the SVG embeds well in READMEs.
   - Use a clean prompt, clear the screen, and pre-stage files or fixtures.
   - Script or rehearse long command sequences before recording.
2. Record a local cast.
   ```bash
   asciinema rec -i 2 demo.cast
   # perform the demo
   # press Ctrl-D to stop
   ```
   If `asciinema rec -i 2` starts an interactive upload/save flow on the installed version, choose local save unless the user requested a public cast.
3. Render the SVG.
   ```bash
   terminal-screencast-svg/scripts/render_cast_svg.py demo.cast demo.svg
   ```
   Equivalent raw commands:
   ```bash
   cat demo.cast | svg-term --out demo.svg --window
   svg-term --cast=CAST_ID --out demo.svg --window
   ```
4. Inspect the SVG in a browser and re-record if the demo contains typos, secrets, long pauses, wrapping, or confusing intermediate state.
5. Embed the result.
   ```html
   <p align="center">
     <img src="./demo.svg" width="572" alt="Terminal demo showing the CLI workflow" />
   </p>
   ```
   For raw GitHub URLs or older GitHub rendering paths, append `?sanitize=true` to the raw SVG URL.

## Helper Script

Use `scripts/render_cast_svg.py` to normalize local-file, asciinema cast ID, and asciinema.org URL rendering:

```bash
# Local cast file
terminal-screencast-svg/scripts/render_cast_svg.py demo.cast demo.svg

# Uploaded asciinema cast ID or URL
terminal-screencast-svg/scripts/render_cast_svg.py 123456 demo.svg
terminal-screencast-svg/scripts/render_cast_svg.py https://asciinema.org/a/123456 demo.svg

# See the exact svg-term command without running it
terminal-screencast-svg/scripts/render_cast_svg.py --dry-run demo.cast demo.svg
```

The script still requires `svg-term` to be installed for real rendering. Pass `--no-window` only when the user explicitly wants the SVG without terminal chrome.

## Quality Checklist

- The recording is local unless upload permission is explicit.
- The `.cast` and SVG contain no tokens, private hostnames, personal paths, or accidental output.
- Idle time is capped (`-i 2` by default) and the final animation is not overly long.
- The terminal width avoids awkward line wrapping in the target README/docs layout.
- The SVG is committed or referenced from a stable path, with alt text and width set in the embed snippet.
- The final answer includes the recording command, render command, output path, and embed snippet.

## Troubleshooting

- `svg-term: command not found`: install `svg-term-cli` with npm or pass `--svg-term` to the helper script.
- The asciinema cast requires a player: render it to SVG with `svg-term`; do not embed the raw `.cast` in a README.
- The animation is too slow or contains long pauses: re-record with `asciinema rec -i 2 demo.cast`.
- The SVG is too wide: narrow the terminal and re-record; post-render resizing cannot fix wrapped lines cleanly.
- A secret was recorded: delete the cast/SVG artifacts, rotate the secret if needed, and re-record from a sanitized environment.
