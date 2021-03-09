#include <Python.h>

/* Will come from go */
PyObject* red(PyObject*);

/* To shim go's missing variadic function support */
int PyArg_ParseTuple_U(PyObject* args, PyObject** obj) {
    return PyArg_ParseTuple(args, "U", obj);
}

/* To shim go's lack of C macro support */
void PyRed_DECREF(PyObject* obj) {
    Py_DECREF(obj);
}

const char* PyRed_Bytes_AsString(PyObject* s) {
    return PyBytes_AS_STRING(s);
}

static struct PyMethodDef methods[] = {
    {"red", (PyCFunction)red, METH_VARARGS},
    {NULL, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "red",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_red(void) {
    return PyModule_Create(&module);
}
