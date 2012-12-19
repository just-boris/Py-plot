#include <Python.h>
#define FUNC_MODULE
#include "funcmodule.h"

#define  sqr(x)  ((x)*(x))
int xmin=-1, xmax=1;
double nr=0;

static PyObject * setX(PyObject *self, PyObject *args) {
    PyArg_ParseTuple(args, "id", &xmin, &xmax);
    nr = 1/sqrt(xmax-xmin);
    return Py_BuildValue("");
}


static PyObject * func_fi_p(PyObject *self, PyObject *args)
{
    int i;
    double x;
    PyArg_ParseTuple(args, "id", &i, &x);
    return Py_BuildValue("d", -nr*sqr((i+1) * M_PI/(xmax-xmin))*sin((i+1)*M_PI*(x-xmin)/(xmax-xmin)));
}

static PyObject * func_fi2_p(PyObject *self, PyObject *args) {
    int i;
    double x;
    PyArg_ParseTuple(args, "id", &i, &x);
    return Py_BuildValue("d", nr*sin((i+1)*M_PI*(x-xmin)/(xmax-xmin)));
}

static PyObject * func_HE_func(PyObject *self, PyObject *args)
{
    return Py_BuildValue("d");
}

static PyMethodDef FuncMethods[] = {
    {"setX", setX, METH_VARARGS, "setX function"},
    {"fi_p", func_fi_p, METH_VARARGS, "fi_p function"},
    {"fi2_p", func_fi2_p, METH_VARARGS, "fi2_p function"},
    {"HE_func", func_HE_func, METH_VARARGS, "HE_func function"},
    {NULL, NULL,  0, NULL}
};

PyMODINIT_FUNC
init_func(void) {
    PyObject *m;

    m = Py_InitModule("_func", FuncMethods);
    if (m == NULL)
        return;
}