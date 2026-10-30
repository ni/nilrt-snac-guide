#!/usr/bin/env python3
"""Generate the Section 3 reStructuredText sources from NIST data and dispositions."""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from snac_docs import dispositions, nist, render  # noqa: E402

SUMMARY_TABLE = "controls_summary_table.inc"


def _write_if_changed(path, text):
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")


def generate(nist_data, controls, output):
    """Write one ``section_3_N.rst`` per family and return the paths."""
    dispositions.check_coverage(nist_data, controls)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    written = []
    for family in nist_data["families"]:
        path = output / f"section_{family['id'].replace('.', '_')}.rst"
        _write_if_changed(path, render.render_family(family, controls))
        written.append(path)
    for stale in output.glob("section_3_*.rst"):
        if stale not in written:
            stale.unlink()
    summary = output / SUMMARY_TABLE
    _write_if_changed(summary, render.render_summary_table(nist_data, controls))
    written.append(summary)
    return written


def main(argv=None):
    """Generate the Section 3 source files."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--nist-data", type=Path, default=nist.DATA_FILE)
    parser.add_argument("--dispositions", type=Path, default=ROOT / "dispositions")
    parser.add_argument("--output", type=Path, default=ROOT / "source" / "generated")
    args = parser.parse_args(argv)

    try:
        controls = dispositions.load_dispositions(args.dispositions)
        written = generate(nist.load_data(args.nist_data), controls, args.output)
    except dispositions.GenerationError as exc:
        print("Section 3 generation failed:", file=sys.stderr)
        for problem in exc.problems:
            print(f"  {problem}", file=sys.stderr)
        return 1
    print(f"Generated {len(written)} files in {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
