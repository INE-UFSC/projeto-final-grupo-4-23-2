import numpy as np
import pyopencl as cl

class CollisionKernel:
    def __init__(self):
        self.ctx = None
        self.queue = None
    
    def build(self):
        self.ctx = cl.create_some_context()
        self.queue = cl.CommandQueue(self.ctx)
        self.kernel = cl.Program(self.ctx, """
            __kernel void sum(__global const float *a_g, __global const float *b_g, __global float *res_g)
            {
                int gid = get_global_id(0);
                res_g[gid] = a_g[gid] + b_g[gid];
            }
            
            __kernel void will_collide(__global const float *a_g, __global const float *b_g, __global float *res_g)
            {
                int gid = get_global_id(0);
                res_g[gid] = a_g[gid] + b_g[gid];
            }
            
            __kernel void get__collisions(__global const float *a_g, __global const float *b_g, __global float *res_g)
            {
                int gid = get_global_id(0);
                res_g[gid] = a_g[gid] + b_g[gid];
            }
        """).build()
    
    def sum(self, a, b):
        ctx = self.get_ctx()
        mf = cl.mem_flags
        
        a_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
        b_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)
                
        res_g = cl.Buffer(ctx, mf.WRITE_ONLY, a.nbytes)
        knl = self.kernel.sum  # Use this Kernel object for repeated calls
        knl(self.queue, a.shape, None, a_g, b_g, res_g)

        res = np.empty_like(a)
        cl.enqueue_copy(self.queue, res, res_g)
        return res

        
    def will_collide(self): 
        pass
    
    def get_collisions(self, a, b, c):
        pass
    
    def get_ctx(self): return self.ctx