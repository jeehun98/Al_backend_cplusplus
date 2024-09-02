#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "matrix_operations.cpp"

namespace py = pybind11;

PYBIND11_MODULE(matrix_ops, m){
    m.def("matrix_add", &matrix_add, "A function that adds two matrices");
    m.def("matrix_multiply", &matrix_multiply, "A function that multiplies two matrices");
}