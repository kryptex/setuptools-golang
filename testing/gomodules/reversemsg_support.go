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
// #if PY_MAJOR_VERSION >= 3
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
// #else
// PyMODINIT_FUNC initgomodules(void) {
//     Py_InitModule3("gomodules", methods, NULL);
// }
// #endif
import "C"
