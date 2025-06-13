import open3d as o3d
mesh= o3d.io.read_triangle_mesh("data/HRWX_DDS_F3_A_A_partial.obj")
mesh.compute_vertex_normals()
mesh.paint_uniform_color([0.3,0.8,0.3])
pcd = o3d.io.read_point_cloud("data/test_tg.ply")
o3d.visualization.draw_geometries([mesh,pcd])