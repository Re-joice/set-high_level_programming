#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints Python bytes info
 * @p: Python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	char *str;
	Py_ssize_t size, i, limit;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = bytes->ob_base.ob_size;
	str = bytes->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	limit = size + 1;
	if (limit > 10)
		limit = 10;

	printf("  first %ld bytes:", limit);
	for (i = 0; i < limit; i++)
		printf(" %02x", (unsigned char)str[i]);
	printf("\n");
}

/**
 * print_python_list - prints Python list info
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t i, size;

	list = (PyListObject *)p;
	size = list->ob_base.ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];

		printf("Element %ld: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
