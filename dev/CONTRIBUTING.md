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

2. Install python module dependencies.

```bash
pip install -r requirements.txt
```

3. Build the documentation using GNU `make`.

```bash
make latexpdf  # output :build/latex/SNAC.pdf
```


## Running Tests

This project has no automated testing.


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
