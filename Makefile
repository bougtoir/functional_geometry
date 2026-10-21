PYTHON := .venv/bin/python

.PHONY: all preflight setup acquire analysis manuscript qc test lint clean

all: preflight analysis manuscript test lint qc

preflight:
	@git status --short > .make_all_start_status

setup:
	python3 -m venv .venv
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

acquire:
	$(PYTHON) scripts/acquire_public_sources.py

analysis:
	$(PYTHON) scripts/run_analysis.py

manuscript:
	$(PYTHON) scripts/build_submission.py

test:
	$(PYTHON) -m pytest -q

lint:
	$(PYTHON) -m compileall -q scripts tests

qc:
	$(PYTHON) scripts/run_qc.py

clean:
	rm -rf submission review_render
	rm -f functional_geometry_JCLP_submission.zip functional_geometry_JCLP_submission_REVISED.zip functional_geometry_JCLP_submission_FINAL.zip
