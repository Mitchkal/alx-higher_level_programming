#include <Python.h>
/**
 * print_python_list_info - prints the information about a python list
 * @p: the list object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0, size, allocated;

	if (!PyList_Check(p))
	{
		printf("Not python list");
		return;
	}
	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
