__kernel void det(__global const float* a_g, __global const float* b_g, __global float* res_g)
{
    int gid = get_global_id(0);
    //res_g[0] = a_g[0] * b_g[1] - a_g[1] * b_g[0];
    res_g[0] = 3.1415;
}

__kernel void is_inside(__global const float* edges, __global bool* result)
{
    int tid = get_global_id(0);
    *result = false;
}