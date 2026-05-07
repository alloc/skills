# 60devs Blog Notes: Terminal Screencast SVGs

Source: Oleksii Rudenko, “Create Beautiful Screencasts from Your Terminal,” 60devs, 2018-12-02: https://60devs.com/create-beautiful-screencasts-from-your-terminal.html

## Core Pattern

The blog recommends avoiding screen-recorded video/GIF output for terminal-only demos. Instead:

1. Record the terminal session with `asciinema`.
2. Convert the cast to a standalone SVG with `svg-term-cli`.
3. Embed the SVG in GitHub READMEs or other docs.

Reason: asciinema casts normally require a player, while the generated SVG can be embedded more broadly.

## Blog Commands

Install tools as presented in the blog:

```bash
npm i asciinema -g
npm i svg-term-cli -g
```

Modern environments may prefer `brew install asciinema`, `pipx install asciinema`, or package-manager equivalents for `asciinema`; `svg-term-cli` is still commonly installed from npm and provides the `svg-term` executable.

Record with a 2-second max idle time:

```bash
asciinema rec -i 2
```

Stop recording with `Ctrl-D`.

Render from an uploaded asciinema cast:

```bash
svg-term --cast=YOUR_CAST_ID --out demo.svg --window
```

Render from a local cast file:

```bash
cat path-to-your-cast-file | svg-term --out demo.svg --window
```

## Embed Pattern

The blog's GitHub README-style HTML embed centers the SVG, sets a fixed width, provides alt text, and uses a raw GitHub SVG URL with `?sanitize=true`:

```html
<p align="center">
  <img src="https://raw.githubusercontent.com/OWNER/REPO/BRANCH/demo.svg?sanitize=true" width="572" alt="terminal demo">
</p>
```

Use a relative `./demo.svg` path when embedding inside the same repository if the host supports it. Keep `?sanitize=true` for raw GitHub URLs or when matching the blog's pattern.

## Operational Adjustments

- Prefer explicit local recording paths such as `asciinema rec -i 2 demo.cast` so the generated source artifact is reproducible.
- Upload to asciinema.org only when the user wants a public hosted cast.
- Re-record rather than heavily editing casts when the terminal size, prompt, timing, or output is wrong.
- Review both `.cast` and `.svg` before publishing because terminal sessions can reveal secrets and local environment details.
