#!/usr/bin/env python3
"""Generate the Section 3 reStructuredText sources from NIST data and dispositions."""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from snac_docs import dispositions, nist, render  # noqa: E402

SUMMARY_TABLE = "controls_summary_table.inc"


def generate(nist_data, controls, output):
    """Write one ``section_3_N.rst`` per family and return the paths."""
    dispositions.check_coverage(nist_data, controls)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    for stale in output.glob("section_3_*.rst"):
        stale.unlink()
    written = []
    for family in nist_data["families"]:
        path = output / f"section_{family['id'].replace('.', '_')}.rst"
        path.write_text(render.render_family(family, controls), encoding="utf-8")
        written.append(path)
    summary = output / SUMMARY_TABLE
    summary.write_text(render.render_summary_table(nist_data, controls), encoding="utf-8")
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
