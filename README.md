# uv-workspace-source-overrides

Companion repository for the article at https://monorepo.nicedx.com/uv-workspace-source-overrides/.

A polyglot-monorepo pattern: how `[tool.uv.sources]` redirects a dependency away from the registry to a workspace member, a local path, or a git URL — while keeping the registry name on `project.dependencies` so the same package still installs cleanly outside the workspace. The repo walks four commits, each leaving the workspace in a runnable state.

## What this project demonstrates

1. A two-package uv workspace (`app` consumes `lib`) with a registry-shaped `project.dependencies` declaration.
2. The default resolution path: without `[tool.uv.sources]`, uv tries to fetch `lib` from PyPI and the install fails because the package only exists locally.
3. The fix: a single `[tool.uv.sources]` block routing `lib` to the workspace member, with the import-time behavior identical to a registry install.
4. Local-path override (a sibling checkout outside the workspace) and a git-URL override with a pinned revision — and what the lockfile records in each case.

## Tech stack

- Python 3.12 (uv-managed toolchain)
- uv 0.5+ (workspace + sources)
- pytest 8 (sanity check at every commit)

## Prerequisites

- Python 3.12 or newer. uv will install a compatible interpreter on its own if you skip the system install.
- uv. One-liner from the upstream installer: `curl -LsSf https://astral.sh/uv/install.sh | sh`. See https://github.com/astral-sh/uv for other platforms.
- git, which you almost certainly already have.

## Quick start

```bash
git clone https://github.com/vytharion/uv-workspace-source-overrides
cd uv-workspace-source-overrides
uv sync                # installs app + lib + pytest into .venv
uv run pytest -q       # 2 passed
```

Expected output: `2 passed` after a brief resolve + install. The lockfile is checked in, so the resolve step is deterministic.

## Commit walkthrough

Step through the lessons chronologically. Each commit leaves the tree in a runnable state — `uv run pytest -q` works at every commit.

| Step | Commit | Description |
|---|---|---|
| 0 | init | Scaffold the README + `.gitignore` (no Python code yet). |
| 1 | workspace skeleton | Define `[tool.uv.workspace]` + create `app` and `lib` packages with trivial code + tests. |
| 2 | workspace-member source | Add `lib` as a dependency of `app` and route it through `[tool.uv.sources]` with `{workspace = true}`. |
| 3 | path source for sibling checkout | Override the same `lib` name with a `path = "../lib-fork"` source — what changes in the lockfile. |
| 4 | git source with rev pin | Replace the path source with `{ git = "...", rev = "..." }` — registry fallback semantics + lock entries. |

To replay a specific step:

```bash
git checkout <step-sha>
uv sync
uv run pytest -q
```

## Repo layout

```
packages/
  app/         — the consumer; imports lib.greet and calls it
  lib/         — the producer; ships a single greet() function
tests/         — top-level smoke test stitched across both packages
pyproject.toml — workspace root (no top-level package; just [tool.uv.workspace])
uv.lock        — checked in, evolves per commit
```

## License

MIT.
