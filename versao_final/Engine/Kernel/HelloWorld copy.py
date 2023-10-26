#!/usr/bin/env python
from ctypes import sizeof
import math
import random
import pyopencl as cl
import numpy as np

a = [1.0, 2.0]
b = [3.0, 4.0]
a_np = np.array(a)
b_np = np.array(b)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
a_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
b_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)

kernel = open("CollisionKernel.cl", "r").read()
prg = cl.Program(ctx, kernel).build()

res_g = cl.Buffer(ctx, mf.WRITE_ONLY, 4)
knl = prg.det  # Use this Kernel object for repeated calls
knl(queue, a_np.shape, None, a_g, b_g, res_g)

res_np = float(0)
cl.enqueue_copy(queue, res_np, res_g)

# Check on CPU with Numpy:
print(float(res_np[0]))
#print(np.linalg.norm(res_np - (a_np + b_np)))
#assert np.allclose(res_np, a_np + b_np)