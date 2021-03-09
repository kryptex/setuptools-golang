#include <Python.h>

/* Will come from go */
PyObject* sum(PyObject* , PyObject*);

/* To shim go's missing variadic function support */
int PyArg_ParseTuple_ll(PyObject* args, long* a, long* b) {
    return PyArg_ParseTuple(args, "ll", a, b);
}

/* demo that macro_defines works */
#if defined(SUM_A) && SUM_B >= 2
static struct PyMethodDef methods[] = {
    {"sum", (PyCFunction)sum, METH_VARARGS},
    {NULL, NULL}
};
#endif

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "sum",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_sum(void) {
    return PyModule_Create(&module);
}
