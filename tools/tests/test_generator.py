"""Tests for Section 3 data processing and source generation."""

import json
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import generate_section3  # noqa: E402
import pytest  # noqa: E402
from snac_docs import dispositions, nist, render  # noqa: E402


def element(kind, ident, text="", title=""):
    """Build a CPRT element fixture."""
    return {
        "element_type": kind,
        "element_identifier": ident,
        "title": title,
        "text": text,
        "doc_identifier": "DOC",
    }


RAW = {
    "documents": [{"doc_identifier": "DOC", "name": "N", "version": "1", "website": "w"}],
    "elements": [
        element("family", "03.01", title="Access Control"),
        element("requirement", "03.01.01", title="Account Management"),
        element("security_requirement", "SR-03.01.01"),
        element("security_requirement", "SR-03.01.01.b", "Disable within [Assignment: odp x]:"),
        element("security_requirement", "SR-03.01.01.a", "Define accounts."),
        element("security_requirement", "SR-03.01.01.b.02", "Second"),
        element("security_requirement", "SR-03.01.01.b.01", "First"),
        element(
            "discussion", "D-03.01.01", 'See <a href="#x?element=03.01.02">03.01.02</a> &amp; more.'
        ),
        element("odp", "A.03.01.01.ODP[01]", "should be dropped"),
        element("requirement", "03.01.02", title=""),
        element("withdraw_reason", "WR-03.01.02", "Incorporated into 03.01.01."),
    ],
}


@pytest.fixture
def data():
    """Return preprocessed fixture data."""
    return nist.preprocess(RAW)


def test_preprocess_structure(data):
    """Preprocessing builds the expected nested control structure."""
    family = data["families"][0]
    assert family["id"] == "3.1"
    active, withdrawn = family["requirements"]
    assert active["id"] == "3.1.1"
    assert [i["text"] for i in active["statement"]["items"]][0] == "Define accounts."
    nested = active["statement"]["items"][1]["items"]
    assert [i["text"] for i in nested] == ["First", "Second"]
    assert active["discussion"] == "See 3.1.2 & more."
    assert withdrawn == {"id": "3.1.2", "title": "", "withdrawn": "Incorporated into 3.1.1."}
    assert "ODP" not in json.dumps(data)


def test_render_requirement(data):
    """Requirement rendering includes content and correctly sized tables."""
    req = data["families"][0]["requirements"][0]
    text = render.render_requirement(
        req, {"status": "end_user", "disposition": ["First ``cell``.", "Second cell."]}
    )
    assert ".. _3-1-1--account-management:" in text
    assert "b. Disable within [*Assignment: odp x*]:" in text
    assert "| X | Must be implemented by end user" in text
    assert text.count("| X |") == 1
    assert "| First ``cell``." in text and "| Second cell." in text
    assert "\\newpage" in text
    widths = {
        len(line)
        for line in text.splitlines()
        if line.startswith(("+--", "+==", "| Sol", "| First"))
    }
    assert len(widths) <= 2


def test_render_withdrawn(data):
    """Withdrawn controls render without dispositions."""
    req = data["families"][0]["requirements"][1]
    text = render.render_requirement(req, None)
    assert ".. _3-1-2--withdrawn--incorporated-into-3-1-1-:" in text
    assert "3.1.2. Withdrawn: Incorporated into 3.1.1." in text


def test_summary_table(data):
    """The summary table links active controls and omits withdrawn ones."""
    table = render.render_summary_table(
        {
            "families": [
                {
                    "id": "3.1",
                    "title": "Access Control",
                    "requirements": data["families"][0]["requirements"],
                }
            ]
        },
        {"3.1.1": {"status": "implemented", "disposition": ["x"]}},
    )
    assert ":ref:`3.1. <3-1--access-control>`" in table
    assert ":ref:`Account Management <3-1-1--account-management>`" in table
    assert "Implemented by vendor" in table
    assert "3.1.2" not in table
    assert len({len(line) for line in table.splitlines()}) == 1


def write(tmp_path, name, content):
    """Write UTF-8 test input under a temporary directory."""
    (tmp_path / name).write_text(content, encoding="utf-8")


GOOD = "3.1.1:\n  status: end_user\n  disposition:\n    - Text.\n"


def test_load_and_coverage(tmp_path, data):
    """Valid dispositions pass schema validation and coverage checks."""
    write(tmp_path, "3.1.yml", GOOD)
    controls = dispositions.load_dispositions(tmp_path)
    dispositions.check_coverage(data, controls)


@pytest.mark.parametrize(
    "content, expected",
    [
        ("3.1.1:\n  status: bogus\n  disposition: [x]\n", "bogus"),
        ("3.1.1:\n  status: implemented\n", "disposition"),
        ("3.1.1:\n  status: implemented\n  disposition: []\n", "disposition"),
        ("3.1.1:\n  status: implemented\n  disposition: [x]\n  extra: 1\n", "extra"),
        (
            "3.1.1:\n  status: implemented\n  disposition: [x]\n3.1.1:\n  status: implemented\n  disposition: [x]\n",
            "duplicate",
        ),
        ("3.2.1:\n  status: implemented\n  disposition: [x]\n", "does not belong"),
        ("a: [\n", "invalid YAML"),
        ("[3.1.1]:\n  status: implemented\n  disposition: [x]\n", "unhashable key"),
        ("{id: 3.1.1}:\n  status: implemented\n  disposition: [x]\n", "unhashable key"),
        ("3.1.1:\n  [status]: implemented\n  disposition: [x]\n", "unhashable key"),
    ],
)
def test_invalid_yaml_reports_file(tmp_path, content, expected):
    """Invalid disposition files report their path and validation issue."""
    write(tmp_path, "3.1.yml", content)
    with pytest.raises(dispositions.GenerationError) as exc:
        dispositions.load_dispositions(tmp_path)
    assert "3.1.yml" in str(exc.value) and expected in str(exc.value)


def test_missing_and_extra_controls(tmp_path, data):
    """Coverage errors identify both missing and unexpected controls."""
    write(
        tmp_path,
        "3.1.yml",
        "3.1.2:\n  status: implemented\n  disposition: [x]\n3.1.9:\n  status: implemented\n  disposition: [x]\n",
    )
    controls = dispositions.load_dispositions(tmp_path)
    with pytest.raises(dispositions.GenerationError) as exc:
        dispositions.check_coverage(data, controls)
    message = str(exc.value)
    assert "3.1.1: no disposition defined" in message
    assert "3.1.2: disposition defined but control is withdrawn" in message
    assert "3.1.9: disposition defined but control is not a NIST" in message


def test_cli(tmp_path, data, capsys):
    """The CLI writes generated sources and reports invalid dispositions."""
    nist_file = tmp_path / "nist.json"
    nist.write_data(data, nist_file)
    disp = tmp_path / "d"
    disp.mkdir()
    write(disp, "3.1.yml", GOOD)
    out = tmp_path / "out"
    args = ["--nist-data", str(nist_file), "--dispositions", str(disp), "--output", str(out)]
    assert generate_section3.main(args) == 0
    assert (out / "section_3_1.rst").exists()
    assert (out / "controls_summary_table.inc").exists()
    write(disp, "3.1.yml", "")
    assert generate_section3.main(args) == 1
    assert "3.1.1: no disposition defined" in capsys.readouterr().err


def test_cli_unhashable_key(tmp_path, capsys):
    """Unhashable YAML keys produce a file-specific CLI error, not a traceback."""
    write(tmp_path, "3.1.yml", "[3.1.1]:\n  status: implemented\n  disposition: [x]\n")
    assert generate_section3.main(["--dispositions", str(tmp_path)]) == 1
    error = capsys.readouterr().err
    assert "Section 3 generation failed:" in error
    assert f"{tmp_path / '3.1.yml'}: invalid YAML:" in error
    assert "found unhashable key" in error
    assert "Traceback" not in error


def test_committed_data_is_consistent():
    """Committed NIST data has dispositions for every active control."""
    committed = nist.load_data()
    controls = dispositions.load_dispositions(TOOLS.parent / "dispositions")
    dispositions.check_coverage(committed, controls)
