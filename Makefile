
.DEFAULT_GOAL := all

# Directories
builddir         = build
srcdir           = source
downloadedsrcdir = $(srcdir)/nilrt-docs
generateddir     = $(srcdir)/generated

# Binaries
PYTHON ?= python3

SPHINXOPTS    ?=
SPHINXBUILD   ?= $(PYTHON) -m sphinx $(SPHINXOPTS)
export SPHINXOPTS ?= --fail-on-warning --keep-going

NILRT_DOC_REPO = https://github.com/ni/nilrt-docs
NILRT_DOC_BRANCH_OR_COMMIT ?= 1615e865748379298bd65ceba723aa0d3ff99aa3

USBGUARD_DOC_PATH = docs/source/usbguard/usbguard.rst
USBGUARD_DOC_DEST = $(downloadedsrcdir)/usbguard.rst

CLAMAV_DOC_PATH = docs/source/clamav/clamav.rst
CLAMAV_DOC_DEST = $(downloadedsrcdir)/clamav.rst

# REAL TARGETS #
################

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
% : Makefile $(USBGUARD_DOC_DEST) $(CLAMAV_DOC_DEST) generate-sections
	$(SPHINXBUILD) -M $@ "$(srcdir)" "$(builddir)" $(SPHINXOPTS) $(O)


# PHONY TARGETS #
#################
.PHONY : Makefile

# Build all supported output formats.
all : latexpdf
.PHONY : all

lint :
	ni-python-styleguide lint tools/
.PHONY : lint

$(USBGUARD_DOC_DEST) :
	@mkdir -p $(downloadedsrcdir)
	curl -sSL "$(NILRT_DOC_REPO)/raw/$(NILRT_DOC_BRANCH_OR_COMMIT)/$(USBGUARD_DOC_PATH)" -o $(USBGUARD_DOC_DEST)
	@echo "Downloaded usbguard.rst from branch '$(NILRT_DOC_BRANCH_OR_COMMIT)' to $(USBGUARD_DOC_DEST)"

$(CLAMAV_DOC_DEST) :
	@mkdir -p $(downloadedsrcdir)
	curl -sSL "$(NILRT_DOC_REPO)/raw/$(NILRT_DOC_BRANCH_OR_COMMIT)/$(CLAMAV_DOC_PATH)" -o $(CLAMAV_DOC_DEST)
	@echo "Downloaded clamav.rst from branch '$(NILRT_DOC_BRANCH_OR_COMMIT)' to $(CLAMAV_DOC_DEST)"

# Generate the Section 3 sources from tools/data and dispositions/.
generate-sections :
	$(PYTHON) tools/generate_section3.py --output $(generateddir)
.PHONY : generate-sections

# Refresh the committed NIST SP 800-171 data from the NIST CPRT (manual).
update-nist-data :
	$(PYTHON) tools/fetch_nist_data.py
.PHONY : update-nist-data

check :
	$(PYTHON) -m pytest tools/tests
.PHONY : check

clean :
	@rm -Rf $(builddir)
	@rm -Rf $(generateddir)
	@rm -Rf $(downloadedsrcdir)
.PHONY : clean


help :
	@$(SPHINXBUILD) -M help "$(srcdir)" "$(builddir)" $(SPHINXOPTS) $(O)
.PHONY : help
