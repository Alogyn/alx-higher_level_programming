#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
    PyListObject *list;
    Py_ssize_t i, size;

    printf("[*] Python list info\n");
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = Py_SIZE(list);

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GET_ITEM(list, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        } else if (PyFloat_Check(item)) {
            print_python_float(item);
        }
    }
}

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes;
    Py_ssize_t size, i;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;
    size = Py_SIZE(bytes);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (i = 0; i < 10 && i < size; i++) {
        printf("%02x", (unsigned char)bytes->ob_sval[i]);
        if (i < 9 && i < size - 1) {
            printf(" ");
        }
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    PyFloatObject *f;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p)) {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    f = (PyFloatObject *)p;
    printf("  value: %f\n", f->ob_fval);
}