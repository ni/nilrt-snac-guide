
.DEFAULT_GOAL := all

# Directories
builddir         = build
srcdir           = source
downloadedsrcdir = $(srcdir)/nilrt-docs

# Binaries
PYTHON ?= python3

SPHINXOPTS    ?=
SPHINXBUILD   ?= $(PYTHON) -m sphinx

NILRT_DOC_REPO = https://github.com/ni/nilrt-docs
NILRT_DOC_BRANCH_OR_COMMIT ?= 4daf8c90d493a4be340b9ac6e03bb6a1a5e757b0

USBGUARD_DOC_PATH = docs/source/usbguard/usbguard.rst
USBGUARD_DOC_DEST = $(downloadedsrcdir)/usbguard.rst

# REAL TARGETS #
################

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
% : Makefile $(USBGUARD_DOC_DEST)
	$(SPHINXBUILD) -M $@ "$(srcdir)" "$(builddir)" $(SPHINXOPTS) $(O)


# PHONY TARGETS #
#################
.PHONY : Makefile

# Build all supported output formats.
all : latexpdf
.PHONY : all

$(USBGUARD_DOC_DEST) :
	@mkdir -p $(downloadedsrcdir)
	curl -sSL "$(NILRT_DOC_REPO)/raw/$(NILRT_DOC_BRANCH_OR_COMMIT)/$(USBGUARD_DOC_PATH)" -o $(USBGUARD_DOC_DEST)
	@echo "Downloaded usbguard.rst from branch '$(NILRT_DOC_BRANCH_OR_COMMIT)' to $(USBGUARD_DOC_DEST)"

clean :
	@rm -Rf $(builddir)
	@rm -Rf $(downloadedsrcdir)
.PHONY : clean


help :
	@$(SPHINXBUILD) -M help "$(srcdir)" "$(builddir)" $(SPHINXOPTS) $(O)
.PHONY : help
