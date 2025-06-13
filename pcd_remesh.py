import pymeshlab
from tqdm import tqdm
import numpy as np
import open3d as o3d

def remesh(obj_path, out_folder_path, obj_type):
    print("Remeshing " + obj_path +"\n")
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(obj_path)
    ms.apply_filter('meshing_merge_close_vertices')
    ms.apply_filter('meshing_remove_null_faces')
    ms.apply_filter('meshing_remove_unreferenced_vertices')
    ms.apply_filter('generate_sampling_poisson_disk', samplenum=3000000)

    # Save mesh 
    #print("Completed remeshing, saving mesh in .obj and pcd in .ply\n")
    ms.save_current_mesh(out_folder_path + "/" + obj_type + "_bim_pcd.ply")
    #ms.save_current_mesh(out_folder_path + "/" + obj_type + "_remeshed_bim.obj")


    # mesh = ms.current_mesh()
    # vertices = np.array(mesh.vertex_matrix())   # Nx3 numpy array of vertices
    # faces = np.array(mesh.face_matrix())        # Mx3 numpy array of face indices
    # o3d_mesh = o3d.geometry.TriangleMesh()
    # o3d_mesh.vertices = o3d.utility.Vector3dVector(vertices)
    # o3d_mesh.triangles = o3d.utility.Vector3iVector(faces)

    
    # o3d_mesh.compute_triangle_normals()    # Optional: compute normals for visualization
    # #o3d_mesh.compute_vertex_normals()

    # #o3d_mesh.triangle_normals = o3d.utility.Vector3dVector([])

    # remesh_name = out_folder_path + "/" + obj_type + "_remeshed_bim.obj"
    # o3d.io.write_triangle_mesh(remesh_name, o3d_mesh)

    # Visualize
    #o3d.visualization.draw_geometries([o3d_mesh])

