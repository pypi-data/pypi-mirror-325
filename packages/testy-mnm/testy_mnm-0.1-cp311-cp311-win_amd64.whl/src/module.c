#include <Python.h>

static PyObject* testy_mnm_test(PyObject* self, PyObject* args) {
    return Py_BuildValue("s", "Hello from testy_mnm!");
}

static PyMethodDef testy_mnm_methods[] = {
    {"test", testy_mnm_test, METH_VARARGS, "Test function"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef testy_mnm_module = {
    PyModuleDef_HEAD_INIT,
    "testy_mnm",
    "Test module",
    -1,
    testy_mnm_methods
};

PyMODINIT_FUNC PyInit_testy_mnm(void) {
    return PyModule_Create(&testy_mnm_module);
}