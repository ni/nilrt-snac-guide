# Agent Instructions

These instructions apply to the entire worktree.

## Required Validation

Run commands from the worktree root with the project's virtual environment
activated (`source .venv/bin/activate`). See
[CONTRIBUTING.md](dev/CONTRIBUTING.md) for environment setup and build instructions.

- After every change, including documentation and disposition changes, run
  `make check` to execute the full generator unit-test suite.
- Whenever anything under `tools/` changes, including tests and data files,
  also run `make lint` to lint the tooling directory with `ni-python-styleguide`.
- Re-run the applicable checks after any subsequent edits. Fix failures caused
  by your changes before finishing. If a check cannot run or has unrelated
  failures, report the command and the blocker explicitly; do not claim it passed.
- In the final response, report which checks ran and their results.

## Generated Documentation

Edit Section 3 dispositions in `dispositions/*.yml`, not the generated files in
`source/generated/`. Follow the authoring rules in
[CONTRIBUTING.md](dev/CONTRIBUTING.md#authoring-section-3-dispositions).
After disposition or generator changes, also run `make generate-sections` to
validate generation.
