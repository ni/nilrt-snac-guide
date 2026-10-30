#!/usr/bin/env python3
"""Download NIST SP 800-171 Rev 3 from the CPRT and refresh the committed data.

Run this manually when NIST publishes changes, then review and commit the
resulting diff of tools/data/nist_sp_800_171r3.json.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from snac_docs import nist  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", default=nist.DATA_FILE, type=Path)
    args = parser.parse_args()

    data = nist.preprocess(nist.fetch_raw())
    nist.write_data(data, args.output)
    count = sum(len(f["requirements"]) for f in data["families"])
    print(f"Wrote {len(data['families'])} families / {count} requirements to {args.output}")


if __name__ == "__main__":
    main()
