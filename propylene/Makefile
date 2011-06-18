PYTHON        = python2.6
PARSER        = propylene.py
UNITTEST      = tests.py
TEST_DIR      = ./test/
SRC           = base-test
VIS_SRC       = $(TEST_DIR)e2011-test
ARGS_TEST_SRC = $(TEST_DIR)args-test
TEST          = $(TEST_DIR)$(SRC) 

#all:

unit-test:
	$(PYTHON) $(UNITTEST)

test-args:
	$(PYTHON) $(PARSER) $(ARGS_TEST_SRC)
	rm -rf *.pyc *.tmp .*.swp

parse:
	$(PYTHON) $(PARSER) $(TEST)
	#mv parser.out ./parser_out
	rm -rf *.pyc *.tmp .*.swp

parse-and-visual:
	$(PYTHON) $(PARSER) $(VIS_SRC) --graphical-ast
	rm -rf *.pyc *.tmp .*.swp
	xpdf strategy-ir.pdf

clean:
	rm -rf *.pyc *.tmp .*.swp
