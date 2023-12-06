#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
  * print_python_bytes - prints some basic info about Python bytes objects
  *
  * @p: PyObject
  *
  * Return: None
  */

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    unsigned int i, size;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first 10 bytes: ");
    size = PyBytes_Size(p);
    size = size > 10 ? 10 : size;
    for (i = 0; i < size; i++)
    {
        printf("%02x", bytes->ob_sval[i] & 0xff);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

/**
  * print_python_list - prints some basic info about Python lists
  *
  * @p: PyObject
  *
  * Return: None
  */

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var = (PyVarObject *)p;
    unsigned int i, size;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", var->ob_size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0, size = var->ob_size; i < size; i++)
    {
        printf("Element %d: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
        if (PyBytes_Check(list->ob_item[i]))
            print_python_bytes(list->ob_item[i]);
    }
}