cc = gcc
EXE = foo
JAVAC = javac
JRE = java
TEST_OUT = test.out
EXP_OUT = expected.out
#DIR = ~/cs571/git/workspace/A2/
.PHONY: clean
.PHONY: run-py
.PHONY: run-c
.PHONY: run-java
.PHONY: test-java

run-c: $(EXE)
	./$(EXE)

run-py: foo.py
	python foo.py

foo.class: foo.java
	$(JAVAC) foo.java

run-java: foo.class
	$(JRE) foo > test.out

test-java: $(TEST_OUT) $(EXP_OUT)
	-@if diff $(TEST_OUT) $(EXP_OUT) &> /dev/null; then \
		echo "Passed!" ;\
	else \
		echo "Not the same!" ;\
	fi

clean:
	-rm *.class
	-rm *.o
	-rm foo
	-rm test.out


$(EXE): foo.o main.o
	$(cc) -o $(EXE) main.o foo.o
	$ make foo 

foo.o: foo.c foo.h
	$(cc) -c foo.c

main.o: main.c foo.h
	$(cc) -c main.c


