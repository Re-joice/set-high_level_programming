#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic information about Python lists
 * @p: pointer to a Python object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size, allocated;
	PyListObject *list;

	list = (PyListObject *)p;
	size = PyList_Size(p);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n",
		       i,
		       Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
