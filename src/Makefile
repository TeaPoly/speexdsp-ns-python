

SWIG := swig

CXXFLAGS :=  -fPIC -std=c++11 -I. $(shell pkg-config --cflags speexdsp)  $(shell python-config --cflags)
LDFLAGS := -shared $(shell pkg-config --libs speexdsp) $(shell python-config --ldflags)
CXX := g++


all: _speexdsp_ns.so

speexdsp_ns_wrap.cpp: speexdsp_ns.i
	$(SWIG) -I. -c++ -python -o $@ $^

_speexdsp_ns.so: speexdsp_ns_wrap.o noise_suppression.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $^

clean:
	-rm -f speexdsp_ns_wrap.cpp *.o _speexdsp_ns.so speexdsp_ns.py *.pyc 
