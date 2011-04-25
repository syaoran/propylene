PYTHON        = python2.6
PARSER        = propylene.py
UNITTEST      = tests.py
TEST_DIR      = ./test/
SRC           = base-test
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
	$(PYTHON) $(PARSER) $(TEST) --graphical-ast
	rm -rf *.pyc *.tmp .*.swp

clean:
	rm -rf *.pyc *.tmp .*.swp
