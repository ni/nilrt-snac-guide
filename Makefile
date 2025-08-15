
.DEFAULT_GOAL := all

# Directories
builddir  = build
srcdir    = source

# Binaries
PYTHON ?= python3

SPHINXOPTS    ?=
SPHINXBUILD   ?= $(PYTHON) -m sphinx


# REAL TARGETS #
################

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
% : Makefile fetch-usbguard-doc
	$(SPHINXBUILD) -M $@ "$(srcdir)" "$(builddir)" $(SPHINXOPTS) $(O)


# PHONY TARGETS #
#################
.PHONY : Makefile

# Build all supported output formats.
all : latexpdf
.PHONY : all

USBGUARD_DOC_REPO = https://github.com/ni/nilrt-docs
USBGUARD_DOC_PATH = docs/source/usbguard/usbguard.rst
USBGUARD_DOC_BRANCH_OR_COMMIT ?= 4daf8c90d493a4be340b9ac6e03bb6a1a5e757b0
USBGUARD_DOC_DEST = $(builddir)/nilrt-docs/usbguard.rst

.PHONY : fetch-usbguard-doc
fetch-usbguard-doc :
	@mkdir -p $(builddir)/nilrt-docs
	curl -sSL "$(USBGUARD_DOC_REPO)/raw/$(USBGUARD_DOC_BRANCH_OR_COMMIT)/$(USBGUARD_DOC_PATH)" -o $(USBGUARD_DOC_DEST)
	@echo "Downloaded usbguard.rst from branch '$(USBGUARD_DOC_BRANCH_OR_COMMIT)' to $(USBGUARD_DOC_DEST)"

clean :
	@rm -Rf $(builddir)
.PHONY : clean


help :
	@$(SPHINXBUILD) -M help "$(srcdir)" "$(builddir)" $(SPHINXOPTS) $(O)
.PHONY : help
