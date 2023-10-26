import time
import numpy as np
import pyopencl as cl
from CollisionKernel import CollisionKernel

kernel = CollisionKernel()
kernel.build()

a_np = np.random.rand(10000).astype(np.float32)
b_np = np.random.rand(10000).astype(np.float32)

while True:
    t = time.time()
    res_np = kernel.sum(a_np, b_np)
    td = (time.time() - t)*1000
    print(f"Delay {td}ms")
    time.sleep(1)

# Check on CPU with Numpy:
print(res_np - (a_np + b_np))
print(np.linalg.norm(res_np - (a_np + b_np)))
assert np.allclose(res_np, a_np + b_np)