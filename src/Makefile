PYINC = $(shell python-config --includes)
PYLIB = $(shell python-config --libs)
.SUFFIXES:
.SUFFIXES: .o .c .py
SRC = grapher_module.py grapher_clips.py
COBJ = ${SRC:.py=.c}
OBJ = grapher_cmd.o 
MOBJ = ${COBJ:.c=.o}
GCMD = grapher_cmd
GMOD = Grapher.so

all: $(SRC) $(GCMD) $(GMOD)
$(GCMD): $(OBJ)
	gcc -o $@ $(PYINC) $(OBJ) $(PYLIB)
$(GMOD): Grapher.pyx $(SRC)
	cython Grapher.pyx
	gcc -fPIC -c $(PYINC) Grapher.c
	gcc -shared -o $@ Grapher.o
grapher_cmd.c: grapher_cmd.pyx
	cython --embed grapher_cmd.pyx
grapher_cmd.o: grapher_cmd.c
	gcc -c $(PYINC)  grapher_cmd.c
clean:
	rm -f *.c *.o grapher_cmd *.so
