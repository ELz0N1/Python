#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>


double** allocateMatrix(int rows, int cols) {
    double** matrix = (double**)malloc(rows * sizeof(double*));
    for (int i = 0; i < rows; i++) {
        matrix[i] = (double*)malloc(cols * sizeof(double));
    }
    return matrix;
}

void deallocateMatrix(double** matrix, int rows) {
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

void initializeMatrix(double** matrix, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = 0.0;
        }
    }
}

void multiplyMatrices(double** A, double** B, double** result, int rowsA, int colsA, int colsB) {
    for (int i = 0; i < rowsA; i++) {
        for (int j = 0; j < colsB; j++) {
            result[i][j] = 0;
            for (int k = 0; k < colsA; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

double** powerMatrix(double** matrix, int size, int power) {
    if (power == 0) {
        double** result = allocateMatrix(size, size);
        initializeMatrix(result, size, size);
        for (int i = 0; i < size; i++) {
            result[i][i] = 1.0;
        }
        return result;
    } else if (power == 1) {
        double** result = allocateMatrix(size, size);
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                result[i][j] = matrix[i][j];
            }
        }
        return result;
    } else {
        double** temp = powerMatrix(matrix, size, power / 2);
        double** result = allocateMatrix(size, size);
        multiplyMatrices(temp, temp, result, size, size, size);
        if (power % 2 == 0) {
            deallocateMatrix(temp, size);
            return result;
        } else {
            double** finalResult = allocateMatrix(size, size);
            multiplyMatrices(result, matrix, finalResult, size, size, size);
            deallocateMatrix(temp, size);
            deallocateMatrix(result, size);
            return finalResult;
        }
    }
}

typedef struct {
    double** ptr;
    size_t size;
} Matrix;

Matrix newMatrix(size_t n) {
    Matrix matrix;
    matrix.ptr = allocateMatrix(n, n);
    matrix.size = n;
    return matrix;
}

Matrix newIdentityMatrix(size_t n) {
    Matrix matrix = newMatrix(n);
    initializeMatrix(matrix.ptr, n, n);
    for (size_t i = 0; i < n; i++) {
        matrix.ptr[i][i] = 1;
    }
    return matrix;
}

void freeMatrix(Matrix* matrix) {
    deallocateMatrix(matrix->ptr, matrix->size);
}

Matrix pow_matrix(Matrix* matrix, size_t pow) {
    Matrix result;
    result = newIdentityMatrix(matrix->size);
    for (size_t h = 0; h < pow; h++) {
        Matrix temp;
        temp.ptr = powerMatrix(matrix->ptr, matrix->size, 1);
        temp.size = matrix->size;
        Matrix multiplied = newMatrix(matrix->size);
        multiplyMatrices(temp.ptr, result.ptr, multiplied.ptr, matrix->size, matrix->size, matrix->size);
        freeMatrix(&result);
        result = multiplied;
        freeMatrix(&temp);
    }
    return result;
}

int convert_matrix(PyObject* obj, void* addr) {
    Matrix* matrix = addr;
    size_t n = PyList_Size(obj);
    *matrix = newMatrix(n);

    for (size_t i = 0; i < n; i++) {
        PyObject* row = PyList_GetItem(obj, i);
        for (size_t j = 0; j < matrix->size; j++)
            matrix->ptr[i][j] = PyFloat_AsDouble(PyList_GetItem(row, j));
    }

    return 1;
}

PyObject* pythonizeMatrix(Matrix* src) {
    size_t n = src->size;
    PyObject* matrix = PyList_New(n);
    for (size_t i = 0; i < n; i++) {
        PyObject* row = PyList_New(n);
        for (size_t j = 0; j < n; j++)
            PyList_SetItem(row, j, PyFloat_FromDouble(src->ptr[i][j]));
        PyList_SetItem(matrix, i, row);
    }
    return matrix;
}   


PyObject* foreign_matrix_power(PyObject* self, PyObject* args) {
    Matrix matrix;
    size_t pow;
    if (!PyArg_ParseTuple(args, "O&n", convert_matrix, &matrix, &pow))
        return NULL;
    Matrix result = pow_matrix(&matrix, pow);
    PyObject* python_result = pythonizeMatrix(&result);
    freeMatrix(&matrix);
    freeMatrix(&result);
    return python_result;
}

static PyMethodDef ForeignMethods[] = {
    {"foreign_matrix_power",
     foreign_matrix_power, METH_VARARGS,
     NULL
    },
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef foreignmodule = {
    PyModuleDef_HEAD_INIT,
    "foreign",
    NULL,
    -1,
    ForeignMethods
};

PyMODINIT_FUNC PyInit_foreign(void) {
    return PyModule_Create(&foreignmodule);
};