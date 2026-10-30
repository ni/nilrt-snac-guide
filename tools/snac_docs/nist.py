"""Fetch, preprocess and load NIST SP 800-171 Rev 3 data from the NIST CPRT."""

import html
import json
import re
from pathlib import Path

import requests

CPRT_URL = (
    "https://csrc.nist.gov/extensions/nudp/services/json/nudp/framework/"
    "version/{doc}/export/json?element=all"
)
CPRT_DOC = "sp_800_171_3_0_0"
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "nist_sp_800_171r3.json"

_PADDED_ID = re.compile(r"\b0(\d)\.0?(\d+)\.0?(\d+)\b")
_ANCHOR = re.compile(r"<a\b[^>]*>(.*?)</a>", re.DOTALL)
_TAG = re.compile(r"<[^>]+>")


def fetch_raw(doc=CPRT_DOC, timeout=120):
    """Download the raw CPRT export for a document."""
    response = requests.get(CPRT_URL.format(doc=doc), timeout=timeout)
    response.raise_for_status()
    return response.json()["response"]["elements"]


def _unpad(text):
    """Turn CPRT ids such as ``03.01.02`` into the guide's ``3.1.2``."""
    return _PADDED_ID.sub(r"\1.\2.\3", text)


def _clean(text):
    text = _ANCHOR.sub(r"\1", text)
    text = html.unescape(_TAG.sub("", text))
    return _unpad(" ".join(text.split()))


def _label_key(label):
    return (len(label), label)


def _statement(elements, req_id):
    """Build the nested statement tree for a requirement."""
    prefix = f"SR-{req_id}"
    root = {"text": "", "items": []}
    nodes = {prefix: root}
    parts = sorted(
        (e for e in elements.values()
         if e["element_type"] == "security_requirement"
         and e["element_identifier"].startswith(prefix)),
        key=lambda e: [_label_key(p) for p in e["element_identifier"].split(".")],
    )
    for element in parts:
        ident = element["element_identifier"]
        node = nodes.setdefault(ident, {"text": "", "items": []})
        node["text"] = _clean(element["text"])
        if ident == prefix:
            continue
        nodes[ident.rsplit(".", 1)[0]]["items"].append(node)
    return root


def preprocess(raw):
    """Reduce a CPRT export to the data the guide needs.

    Organization-defined parameter (ODP) elements, assessment objectives and
    references are intentionally dropped.
    """
    elements = {e["element_identifier"]: e for e in raw["elements"]}
    families = []
    for fam in sorted(
        (e for e in raw["elements"] if e["element_type"] == "family"),
        key=lambda e: e["element_identifier"],
    ):
        fam_id = fam["element_identifier"]
        requirements = []
        for req in sorted(
            (e for e in raw["elements"]
             if e["element_type"] == "requirement"
             and e["element_identifier"].startswith(fam_id + ".")),
            key=lambda e: e["element_identifier"],
        ):
            req_id = req["element_identifier"]
            entry = {"id": _unpad(req_id), "title": req["title"]}
            reason = elements.get(f"WR-{req_id}")
            if reason is not None:
                entry["withdrawn"] = _clean(reason["text"])
            else:
                discussion = elements.get(f"D-{req_id}")
                entry["statement"] = _statement(elements, req_id)
                entry["discussion"] = _clean(discussion["text"]) if discussion else ""
            requirements.append(entry)
        families.append(
            {"id": ".".join(str(int(p)) for p in fam_id.split(".")), "title": fam["title"], "requirements": requirements}
        )
    document = raw["documents"][0]
    return {
        "document": document["doc_identifier"],
        "name": document["name"],
        "version": document["version"],
        "website": document["website"],
        "families": families,
    }


def write_data(data, path=DATA_FILE):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_data(path=DATA_FILE):
    return json.loads(Path(path).read_text(encoding="utf-8"))
