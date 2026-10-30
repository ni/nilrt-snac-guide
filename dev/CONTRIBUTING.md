# Contributing to nilrt-snac-guide

Thanks for taking an interest in the nilrt-snac-guide project!

* Clone the **source** from the canonical upstream at: [https://github.com/ni/nilrt-snac-guide](https://github.com/ni/nilrt-snac-guide).
* Send **code contributions** by forking the canonical upstream, and sending a PR with your changes against the `master` ref.
* File a **bug** by opening a new Issue on the canonical upstream's git repo.
* Report a **security** concern by sending an email to the contact listed in the [SECURITY.md](/dev/SECURITY.md) document.


## Building the Source

These documentation sources can be built locally, using the Python3 Sphinx module and some host tooling.

1. Install host tooling.

**Debian**
```bash
apt install \
	latexmk \
	texlive \
	texlive-fonts-extra \
	texlive-xetex \
	""
```

2. Create a Python virtual environment and install the pinned module dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Build the documentation using GNU `make`.

```bash
make                     # output :build/latex/SNAC.pdf
make html                # output :build/html
make generate-sections   # regenerate only the Section 3 sources
make update-nist-data    # refresh the NIST SP 800-171 data (review and commit the diff)
make check               # run the generator unit tests
make clean               # remove build output and generated sources
```


## Authoring Section 3 Dispositions

The Section 3 chapters (NIST SP 800-171 controls) and the Controls Summary table are **generated** at build time into `source/generated/` (git-ignored).
Do not edit them, and do not write reStructuredText tables by hand.
Instead, edit the YAML file for the control's family in [/dispositions](/dispositions) (e.g. `dispositions/3.1.yml`):

```yaml
3.1.1:
  status: end_user
  disposition:
    - First paragraph. Inline reStructuredText such as ``code`` or :ref:`links <appendix-5>` is allowed.
    - Second paragraph, rendered as its own cell.
```

* `status` is exactly one of `implemented`, `not_implemented`, `end_user`, `not_applicable`.
* Mapping keys must be unique strings, not YAML sequences or mappings (e.g. use `3.1.1:`, not `[3.1.1]:`).
  Invalid YAML keys are reported with the disposition file path and source location.
* `disposition` is a list of paragraphs; each becomes a row in the "Solution Implementation" table.
  A paragraph containing a line break is used verbatim (for lists or literal blocks).
* Every active (non-withdrawn) NIST control must have an entry and no other controls may. The build fails otherwise.
  Withdrawn controls are rendered automatically from the NIST data.
* Adding or deleting a disposition file triggers regeneration on the next build,
  so removed dispositions cannot silently leave stale generated content.

The NIST text (requirements, discussion, withdrawn status) comes from the committed [/tools/data/nist_sp_800_171r3.json](/tools/data/nist_sp_800_171r3.json).
To refresh it from the NIST CPRT, run `make update-nist-data` and commit the reviewed diff.
Run `make generate-sections` to regenerate only the Section 3 sources.
Unchanged generated files retain their timestamps for incremental Sphinx builds.
Make records successful generation in `source/generated/.section3.stamp` so
input changes that do not affect rendered content do not cause repeated generation.


## Running Tests

Generator unit tests: `make check`.

This project uses github-action based PR testing.
The logic is stored in the [.github](/.github) directory.


## Submitting Changes Upstream

1. Commit your changes into new git commits.
	* **Base** your changes on the canonical repo's `master` ref.
	* Remember to make your changes *atomic*. The overall state of the repository should be valid at each commit.
	* Please remember to sign off your commits (e.g., by using `git commit -s` if you are using the command line client). This amends your git commit message with a line of the form `Signed-off-by: Name Lastname <name.lastmail@emailaddress.com>`. Please include all authors of any given commit into the commit message with a `Signed-off-by` line. This indicates that you have read and signed the Developer Certificate of Origin (see below) and are able to legally submit your code to this repository.
2. Fork the canonical repository on github, and push your new commits as a branch on your fork.
3. Open a Pull Request on the canonical repo using your development branch as the source, and the `master` ref as the target.


## Developer Certificate of Origin (DCO)

	Developer's Certificate of Origin 1.1

	By making a contribution to this project, I certify that:

	(a) The contribution was created in whole or in part by me and I
	    have the right to submit it under the open source license
	    indicated in the file; or

	(b) The contribution is based upon previous work that, to the best
	    of my knowledge, is covered under an appropriate open source
	    license and I have the right under that license to submit that
	    work with modifications, whether created in whole or in part
	    by me, under the same open source license (unless I am
	    permitted to submit under a different license), as indicated
	    in the file; or

	(c) The contribution was provided directly to me by some other
	    person who certified (a), (b) or (c) and I have not modified
	    it.

	(d) I understand and agree that this project and the contribution
	    are public and that a record of the contribution (including all
	    personal information I submit with it, including my sign-off) is
	    maintained indefinitely and may be redistributed consistent with
	    this project or the open source license(s) involved.

(taken from [developercertificate.org](https://developercertificate.org/))

See [LICENSE](https://github.com/ni/nilrt-snac-guide/blob/main/LICENSE)
for details about how nilrt-snac-guide is licensed.
