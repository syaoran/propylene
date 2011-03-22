PYTHON = python2.6
PARSER = propylene.py
TEST_DIR = ./test/
SRC = base-test
TEST = $(TEST_DIR)$(SRC) 

#all:

parse:
	$(PYTHON) $(PARSER) $(TEST)
	mv parser.out ./parser_out
	rm -rf *.pyc *.tmp .*.swp

clean:
	rm -rf *.pyc *.tmp .*.swp
