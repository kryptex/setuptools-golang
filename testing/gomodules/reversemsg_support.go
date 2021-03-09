package main

// #include <Python.h>
//
// PyObject* reversemsg();
//
// static struct PyMethodDef methods[] = {
//     {"reversemsg", (PyCFunction)reversemsg, METH_NOARGS},
//     {NULL, NULL}
// };
//
// static struct PyModuleDef module = {
//     PyModuleDef_HEAD_INIT,
//     "gomodules",
//     NULL,
//     -1,
//     methods
// };
//
// PyMODINIT_FUNC PyInit_gomodules(void) {
//     return PyModule_Create(&module);
// }
import "C"
