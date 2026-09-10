# clkup command map

This is a discovery index, not a substitute for command help. Before using a command not taught in `SKILL.md`, run `clkup GROUP ACTION --help` to confirm its arguments, required flags, mutation behavior, and availability in the installed version.

| Group | Available actions |
| --- | --- |
| `setup` | Configure the API token and default workspace |
| `auth` | `whoami`, `check` |
| `workspace` | `list`, `seats`, `plan` |
| `space` | `list`, `get`, `create`, `update`, `delete` |
| `folder` | `list`, `get`, `create`, `update`, `delete` |
| `list` | `list`, `get`, `create`, `update`, `delete`, `add-task`, `remove-task` |
| `task` | `list`, `search`, `get`, `create`, `update`, `delete`, `time-in-status`, `add-tag`, `remove-tag`, `add-dep`, `remove-dep`, `link`, `unlink`, `move`, `set-estimate`, `replace-estimates` |
| `checklist` | `create`, `update`, `delete`, `add-item`, `update-item`, `delete-item` |
| `comment` | `list`, `create`, `update`, `delete`, `replies`, `reply` |
| `tag` | `list`, `create`, `update`, `delete` |
| `field` | `list`, `set`, `unset` |
| `task-type` | `list` |
| `attachment` | `list`, `upload` |
| `time` | `list`, `get`, `current`, `create`, `update`, `delete`, `start`, `stop`, `tags`, `add-tags`, `remove-tags`, `rename-tag`, `history` |
| `goal` | `list`, `get`, `create`, `update`, `delete`, `add-kr`, `update-kr`, `delete-kr` |
| `view` | `list`, `get`, `create`, `update`, `delete`, `tasks` |
| `member` | `list` |
| `user` | `invite`, `get`, `update`, `remove` |
| `chat` (v3) | `channel-list`, `channel-create`, `channel-get`, `channel-update`, `channel-delete`, `channel-followers`, `channel-members`, `dm`, `message-list`, `message-send`, `message-update`, `message-delete`, `reaction-list`, `reaction-add`, `reaction-remove`, `reply-list`, `reply-send`, `tagged-users` |
| `doc` (v3) | `list`, `create`, `get`, `pages`, `add-page`, `page`, `edit-page`, `embed-image` |
| `webhook` | `list`, `create`, `update`, `delete` |
| `template` | `list`, `apply-task`, `apply-list`, `apply-folder` |
| `guest` (Enterprise) | `invite`, `get`, `update`, `remove`, `share-task`, `unshare-task`, `share-list`, `unshare-list`, `share-folder`, `unshare-folder` |
| `group` | `list`, `create`, `update`, `delete` |
| `role` (Enterprise) | `list` |
| `shared` | `list` |
| `audit-log` (Enterprise, v3) | `query` |
| `acl` (Enterprise, v3) | `update` |
| `agent-config` | `show`, `inject`, `init` |
| `mcp` | `serve` |
| `status` | Show active configuration with the token masked |
| `completions` | Generate completion scripts for `bash`, `zsh`, `fish`, or `powershell` |

The top-level global controls are `--token`, `--workspace`, `--output`, `--fields`, `--no-header`, `--all`, `--limit`, `--page`, `--cursor`, `--quiet`, and `--timeout`. Prefer stored configuration or environment variables over placing a token on the command line.
