/* 
    def vector3_det(a:[float], b:[float]): 
        return a[0] * b[1] - a[1] * b[0] 
*/
float vector3_det(float* a_g, float* b_g)
{
    return a_g[0] * b_g[1] - a_g[1] * b_g[0];
}


/* 
    def vector3_is_inside(self_vec3:[float], edges:[[float]]):
        count = 0
        sx = self_vec3[0]
        sy = self_vec3[1]
        
        for e in edges:
            (x1, y1) = (e[0][0], e[0][1])
            (x2, y2) = (e[1][0], e[1][1])
            if (sy < y1) != (sy < y2) and sx < x1 + ((sy-y1)/(y2-y1))*(x2-x1):
                count += 1
        
        return count%2==1 
*/
bool vector3_is_inside(float* self_vec3, float*** edges, int edges_len)
{
    int tid = get_global_id(0);
    
    int count = 0;
    float sx = self_vec3[0];
    float sy = self_vec3[1];

    for(int i = 0; i < edges_len; i++){
        float** e = edges[i];
        float x1 = e[0][0];
        float y1 = e[0][1];
        float x2 = e[1][0];
        float y2 = e[1][1];
        float temp = (x1 + ((sy-y1)/(y2-y1))*(x2-x1));
        if (((sy < y1) != (sy < y2)) && (sx < temp)){
            count += 1;
        }
    }
    
    return count%2 == 1;
}


/* 
    def vector3_get_2d_point_intersection(vec3_pair_1:[[float]], vec3_pair_2:[[float]]):
        vlst = (
            ((vec3_pair_1[0][0],vec3_pair_1[0][1]),(vec3_pair_1[1][0],vec3_pair_1[1][1])),
            ((vec3_pair_2[0][0],vec3_pair_2[0][1]),(vec3_pair_2[1][0],vec3_pair_2[1][1]))
        )
        
        xdiff = (vlst[0][0][0] - vlst[0][1][0], vlst[1][0][0] - vlst[1][1][0])
        ydiff = (vlst[0][0][1] - vlst[0][1][1], vlst[1][0][1] - vlst[1][1][1])

        div = Vector3.vector3_det(xdiff, ydiff)
        if div == 0: return None  # Linhas não se cruzam

        d = (Vector3.vector3_det(*vlst[0]), Vector3.vector3_det(*vlst[1]))
        x = Vector3.vector3_det(d, xdiff) / div
        y = Vector3.vector3_det(d, ydiff) / div
        
        for i in range(2):
            if x > max(vlst[i][0][0], vlst[i][1][0]) or x < min(vlst[i][0][0], vlst[i][1][0]): return None
            if y > max(vlst[i][0][1], vlst[i][1][1]) or y < min(vlst[i][0][1], vlst[i][1][1]): return None
        
        return Vector3(x, y, 0)  # Retorna as coordenadas do cruzamento
*/
float* vector3_get_2d_point_intersection(float** vec3_pair_1, float** vec3_pair_2){
    float* result;

    float*** vlst;
    vlst[0][0] = vec3_pair_1[0];
    vlst[0][1] = vec3_pair_1[1];
    vlst[1][0] = vec3_pair_2[0];
    vlst[1][1] = vec3_pair_2[1];

    float* xdiff;
    xdiff[0] = vlst[0][0][0] - vlst[0][1][0];
    xdiff[1] = vlst[1][0][0] - vlst[1][1][0];

    float* ydiff;
    ydiff[0] = vlst[0][0][1] - vlst[0][1][1];
    ydiff[1] = vlst[1][0][1] - vlst[1][1][1];

    float div = vector3_det(xdiff, ydiff);
    if (div == 0) return result;

    //d = (Vector3.vector3_det(*vlst[0]), Vector3.vector3_det(*vlst[1]))
    float* d;
    d[0] = vector3_det(vlst[0][0], vlst[0][1]); //REVISAR !!!
    d[1] = vector3_det(vlst[1][0], vlst[1][1]);

    float x = vector3_det(d, xdiff) / div;
    float y = vector3_det(d, ydiff) / div;
    
    for (int i = 0; i < 2; i++){
        if ((x > max(vlst[i][0][0], vlst[i][1][0])) || (x < min(vlst[i][0][0], vlst[i][1][0]))) return result;
        if ((y > max(vlst[i][0][1], vlst[i][1][1])) || (y < min(vlst[i][0][1], vlst[i][1][1]))) return result;
    }

    result[0] = x;
    result[1] = y;

    return result;
}



/* 
    def get_projection_vec3_arrays(transform_len:float, rotation_axis:[float], vec_pair:[[float]]):
        pv1 = vec_pair[0]
        pv1[0] += transform_len * math.sin(rotation_axis[0])
        pv1[1] += transform_len * math.cos(rotation_axis[0])
        
        pv2 = vec_pair[1]
        pv2[0] += transform_len * math.sin(rotation_axis[0])
        pv2[1] += transform_len * math.cos(rotation_axis[0])
        
        return [pv1, pv2]
*/
float** get_projection_vec3_arrays(float transform_len, float* rotation_axis, float** vec_pair){
        float** result;
        float* pv1;
        float* pv2;

        pv1 = vec_pair[0];
        pv1[0] += transform_len * sin(rotation_axis[0]);
        pv1[1] += transform_len * cos(rotation_axis[0]);
        
        pv2 = vec_pair[1];
        pv2[0] += transform_len * sin(rotation_axis[0]);
        pv2[1] += transform_len * cos(rotation_axis[0]);

        result[0] = pv1;
        result[1] = pv2;
        return result;
}


/* 
    def will_collide_2d(pv, vec_pair_1:[[float]], vec_pair_2:[[float]]):
        if Vector3.vector3_get_2d_point_intersection([vec_pair_1[0], pv[0]], vec_pair_2): return  True
        if Vector3.vector3_get_2d_point_intersection([vec_pair_1[1], pv[1]], vec_pair_2): return  True
        if Vector3.vector3_get_2d_point_intersection([pv[0], pv[1]], vec_pair_2): return  True
        
        poly = [vec_pair_1, [vec_pair_1[0], pv[0]], [vec_pair_1[1], pv[1]], [pv[0], pv[1]]]
        inside = Vector3.vector3_is_inside(vec_pair_2[0], poly) or Vector3.vector3_is_inside(vec_pair_2[1], poly)
        
        return inside 
*/
bool  will_collide_2d(float** pv, float** vec_pair_1, float** vec_pair_2){
    float** tmp;

    tmp[0] = vec_pair_1[0];
    tmp[1] = pv[0];
    if (vector3_get_2d_point_intersection(tmp, vec_pair_2)) return true;

    tmp[0] = vec_pair_1[1];
    tmp[1] = pv[1];
    if (vector3_get_2d_point_intersection(tmp, vec_pair_2)) return true;

    tmp[0] = pv[0];
    if (vector3_get_2d_point_intersection(tmp, vec_pair_2)) return true;
    
    float*** poly;
    poly[0] = vec_pair_1;
    poly[1][0] = vec_pair_1[0];
    poly[1][1] = pv[0];
    poly[2][0] = vec_pair_1[1];
    poly[2][1] = pv[1];
    poly[3][0] = pv[0];
    poly[3][1] = pv[1];

    bool inside = (vector3_is_inside(vec_pair_2[0], poly, 4) || vector3_is_inside(vec_pair_2[1], poly, 4));
    
    return inside;
}








/* 
    def will_collide(self, ref_position_from:Vector3, transform_len:float, rotation_axis:Vector3, ref_position_other:Vector3, other_polygon):
        self_vector_list = self.get_vectors(ref_position_from)
        other_vector_list = other_polygon.get_vectors(ref_position_other)
        rot_axis_arr = rotation_axis.get_float_array()
        
        last_v = self_vector_list[0]
        for v in self_vector_list[1:]:
            last_v2 = other_vector_list[0]
            vec1_pair = [last_v.get_float_array(), v.get_float_array()]
            pv = Vector3.get_projection_vec3_arrays(transform_len, rot_axis_arr, vec1_pair)
            
            for v2 in other_vector_list[1:]: 
                if Vector3.will_collide_2d(pv, vec1_pair, [last_v2.get_float_array(), v2.get_float_array()]): return True
                last_v2 = v2
                
            last_v = v
            
        return False
*/

__kernel void will_collide(
    __global float* values, __global bool* ret
    /* __global float* transform_len, __global float* rotation_axis, 
    __global float* ref_position_from, __global float* from_polygon_vec_lst, __global int* from_poly_vec_lst_count,
    __global float* ref_position_other,__global float* other_polygon_vec_lst, __global int* other_poly_vec_lst_count */
    )
{
    int gid = get_global_id(0);
    float mov_objs_count = values[0];
    
    /* for (int i = 0; i < *from_poly_vec_lst_count; i++){
        
    } */

}