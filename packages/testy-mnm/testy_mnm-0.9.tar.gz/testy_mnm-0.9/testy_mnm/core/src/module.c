#include <Python.h>

static PyObject* testy_c_module_test(PyObject* self, PyObject* args) {
    return Py_BuildValue("s", "Hello from testy_c_module!");
}

static PyObject* testy_c_module_test2(PyObject* self, PyObject* args) {
    return Py_BuildValue("s", "Hello from testy_c_module 2222!");
}

static PyMethodDef testy_c_module_methods[] = {
    {"test", testy_c_module_test, METH_VARARGS, "Test function"},
    {"test2", testy_c_module_test2, METH_VARARGS, "Test function 2"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef testy_c_module_module = {
    PyModuleDef_HEAD_INIT,
    "testy_c_module",
    "Test module",
    -1,
    testy_c_module_methods
};

PyMODINIT_FUNC PyInit_testy_c_module(void) {
    return PyModule_Create(&testy_c_module_module);
}