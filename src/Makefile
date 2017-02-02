PYINC = $(shell python-config --includes)
PYLIB = $(shell python-config --libs)
.SUFFIXES:
.SUFFIXES: .o .c .py
SRC = grapher.py 
COBJ = ${SRC:.py=.c}
OBJ = grapher_cmd.o ${COBJ:.c=.o}
GCMD = grapher_cmd

all: $(SRC) $(GCMD)
$(GCMD): $(OBJ)
	gcc -o $@ $(PYINC) $(OBJ) $(PYLIB)
grapher_cmd.c: grapher_cmd.py
	cython --embed grapher_cmd.py
grapher_cmd.o: grapher_cmd.c
	gcc -c $(PYINC)  grapher_cmd.c
.py.c:
	cython -o $@ $<
.c.o:
	gcc -c $(PYINC) $< -o $@
clean:
	rm -f *.c *.o grapher_cmd
