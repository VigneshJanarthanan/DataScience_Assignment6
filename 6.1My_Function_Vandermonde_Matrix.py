My Function for Vander matrix with Increasing is 'True'
----------------------------------------------------------
import numpy as np
x = np.array([1, 2, 3, 5])
N = 4
np.column_stack([x**(i) for i in range(N)])
----------------------------------------------------------

My Function for Vander matrix with Increasing is 'False'
----------------------------------------------------------
x = np.array([1, 2, 3, 5])
N = 4
np.column_stack([x**(N-1-i) for i in range(N)])
----------------------------------------------------------

Bulit-in Vander function with N-th value
----------------------------------------------------------
x = np.array([1, 2, 3, 5])
N=3
np.vander(x, N)
----------------------------------------------------------

Bulit-in Vander function with increasing=True
----------------------------------------------------------
x = np.array([1, 2, 3, 5])
np.vander(x)
print(np.vander(x))
np.vander(x, increasing=True)
----------------------------------------------------------

Bulit-in Vander function with increasing=False
----------------------------------------------------------
x = np.array([1, 2, 3, 5])
np.vander(x)
print(np.vander(x))
np.vander(x, increasing=False)
----------------------------------------------------------