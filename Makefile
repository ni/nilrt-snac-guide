
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


# ==============================================================================
# REAL TARGETS #
# ==============================================================================

NILRT_DOC_REPO = https://github.com/ni/nilrt-docs
NILRT_DOC_BRANCH_OR_COMMIT ?= 1615e865748379298bd65ceba723aa0d3ff99aa3


CLAMAV_DOC_PATH = docs/source/clamav/clamav.rst
CLAMAV_DOC_DEST = $(downloadedsrcdir)/clamav.rst

$(CLAMAV_DOC_DEST) :
	@mkdir -p $(downloadedsrcdir)
	curl -sSL "$(NILRT_DOC_REPO)/raw/$(NILRT_DOC_BRANCH_OR_COMMIT)/$(CLAMAV_DOC_PATH)" -o $(CLAMAV_DOC_DEST)
	@echo "Downloaded clamav.rst from branch '$(NILRT_DOC_BRANCH_OR_COMMIT)' to $(CLAMAV_DOC_DEST)"


USBGUARD_DOC_PATH = docs/source/usbguard/usbguard.rst
USBGUARD_DOC_DEST = $(downloadedsrcdir)/usbguard.rst

$(USBGUARD_DOC_DEST) :
	@mkdir -p $(downloadedsrcdir)
	curl -sSL "$(NILRT_DOC_REPO)/raw/$(NILRT_DOC_BRANCH_OR_COMMIT)/$(USBGUARD_DOC_PATH)" -o $(USBGUARD_DOC_DEST)
	@echo "Downloaded usbguard.rst from branch '$(NILRT_DOC_BRANCH_OR_COMMIT)' to $(USBGUARD_DOC_DEST)"


# Generated Section 3 sources.
SECTION_FAMILIES = 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
SECTION_OUTPUTS = $(addprefix $(generateddir)/section_3_,$(addsuffix .rst,$(SECTION_FAMILIES))) \
	$(generateddir)/controls_summary_table.inc
SECTION_INPUTS = $(wildcard dispositions/*.yml tools/data/* tools/*.py tools/snac_docs/*.py) dispositions
SECTION_STAMP = $(generateddir)/.section3.stamp

# Record successful generation separately so unchanged outputs keep their mtimes.
# The directory prerequisite also detects added or deleted disposition files.
$(SECTION_INPUTS) : ;
$(SECTION_STAMP) : $(SECTION_INPUTS)
	$(PYTHON) tools/generate_section3.py --output $(generateddir)
	@touch $@

# Recover missing outputs without treating the newer stamp as a content change.
$(SECTION_OUTPUTS) &: | $(SECTION_STAMP)
	@for output in $(SECTION_OUTPUTS); do \
		if test ! -f "$$output"; then \
			$(PYTHON) tools/generate_section3.py --output $(generateddir) || exit $$?; \
			break; \
		fi; \
	done

# ==============================================================================
# PHONY TARGETS
# ==============================================================================

.PHONY : Makefile  # avoids circular dependencies


# Build all supported output formats.
all : latexpdf
.PHONY : all

check :
	$(PYTHON) -m pytest tools/tests
.PHONY : check

clean :
	@rm -Rf $(builddir)
	@rm -Rf $(generateddir)
	@rm -Rf $(downloadedsrcdir)
.PHONY : clean

generate-sections : $(SECTION_OUTPUTS)
.PHONY : generate-sections

help :
	@$(SPHINXBUILD) -M help "$(srcdir)" "$(builddir)" $(SPHINXOPTS) $(O)
.PHONY : help

lint :
	ni-python-styleguide lint tools/
.PHONY : lint

# Refresh the committed NIST SP 800-171 data from the NIST CPRT (manual).
update-nist-data :
	$(PYTHON) tools/fetch_nist_data.py
.PHONY : update-nist-data


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
% : Makefile $(USBGUARD_DOC_DEST) $(CLAMAV_DOC_DEST) $(SECTION_OUTPUTS)
	$(SPHINXBUILD) -M $@ "$(srcdir)" "$(builddir)" $(SPHINXOPTS) $(O)
