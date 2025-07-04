from numba.openmp import njit
from numba.openmp import openmp_context as openmp
from numba.openmp import omp_get_thread_num

@njit
def hello():
	with openmp("parallel"):
		print("Hello from thread", omp_get_thread_num())

hello()
