// speexdsp_ns.i


%module speexdsp_ns

%begin %{
#define SWIG_PYTHON_STRICT_BYTE_CHAR
%}

%include "std_string.i"

%{
#include "noise_suppression.h"
%}

%include "noise_suppression.h"

