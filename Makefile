# Build the handbook and paper with TeX Live and latexmk. A user-local TinyTeX
# installation is also supported on machines without a system TeX tree.
tinytex_latexmk := $(firstword $(wildcard $(HOME)/.TinyTeX/bin/*/latexmk))
ifneq ($(tinytex_latexmk),)
export PATH := $(PATH):$(dir $(tinytex_latexmk))
endif

# Use the original handbook build date unless the caller supplies an epoch.
export SOURCE_DATE_EPOCH ?= 1795651200
export FORCE_SOURCE_DATE = 1

# pdfTeX normally includes the build path when generating its PDF trailer ID.
.PHONY: handbook paper
handbook paper:
	@set -eu; \
	mkdir -p output/pdf; \
	build_dir=$$(mktemp -d "$(CURDIR)/output/pdf/.$@.XXXXXXXX"); \
	trap 'rm -rf -- "$$build_dir"' EXIT; \
	cd docs; \
	latexmk -norc -pdf '-usepretex=\pdftrailerid{}' \
		-interaction=nonstopmode -halt-on-error -file-line-error \
		-outdir="$$build_dir" "$@.tex"; \
	mv -f -- "$$build_dir/$@.pdf" "$(CURDIR)/output/pdf/$@.pdf"

.PHONY: check
check:
	@set -eu; for test in checks/*.py; do \
		echo "$$test"; \
		case "$$test" in \
			checks/03-4.py) uv run --script "$$test" ;; \
			*) python3 "$$test" ;; \
		esac; \
	done
