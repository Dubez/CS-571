#!/bin/bash

# create and test the executable file
make -f Makefile

#run the foo.py file
make run-py 

#compile the foo.java file into a .class file
make foo.class

#run the java file
make run-java

#compare actual and expected outputs
make test-java

#clean unnecessary files
make clean
