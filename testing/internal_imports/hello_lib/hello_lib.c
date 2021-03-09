#include <Python.h>

/* Will come from go */
PyObject* ohai(PyObject*);

/* To shim go's missing variadic function support */
int PyArg_ParseTuple_U(PyObject* args, PyObject** obj) {
    return PyArg_ParseTuple(args, "U", obj);
}

/* To shim go's lack of C macro support */
void PyHelloLib_DECREF(PyObject* obj) {
    Py_DECREF(obj);
}

const char* PyHelloLib_Bytes_AsString(PyObject* s) {
    return PyBytes_AS_STRING(s);
}

static struct PyMethodDef methods[] = {
    {"ohai", (PyCFunction)ohai, METH_VARARGS},
    {NULL, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "hello_lib",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_hello_lib(void) {
    return PyModule_Create(&module);
}
