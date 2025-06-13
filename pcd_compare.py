import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def pcd_loader(gt_file_path, target_file_path):
    gt_pcd = o3d.io.read_point_cloud(gt_file_path)
    tg_pcd = o3d.io.read_point_cloud(target_file_path)
    return gt_pcd, tg_pcd


def o3d_visualization(data_list):
    # Visualize on open3d
    o3d.visualization.draw_geometries(data_list)


def abnormal_place_clustering(pts):
    # Do clustering for abnormal points
    num_points = points.shape[0]
    labels = np.random.randint(0, 2, size=num_points)


    with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
        labels = np.array(pts.cluster_dbscan(eps=1000, min_points=500, print_progress=True))
    max_label = labels.max()
    colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
    colors[labels < 0] = 0
    pts.colors = o3d.utility.Vector3dVector(colors[:, :3])
    print(f"point cloud has {max_label + 1} clusters")
    return pts


def bim_comparison(out_folder_path, normal_file_path, gt_file_path, target_file_path, abnormal_thres):
    # Dataloader
    source, target = pcd_loader(gt_file_path, target_file_path)

    # Calculate distance of each points in the 2 pointclouds
    distances = target.compute_point_cloud_distance(source)
    gt_vis = source.paint_uniform_color([0.2, 0.3, 0.4])
    distances = np.asarray(distances)

    # Seperate abnormal points and normal points
    abnormal_indices = np.where(distances > abnormal_thres)[0]
    abnormal_points = target.select_by_index(abnormal_indices)
    abnormal_points.paint_uniform_color([0.7, 0.1, 0.1])
    normal_indices = np.where(distances <= abnormal_thres)[0]
    normal_points = target.select_by_index(normal_indices)
    normal_points.paint_uniform_color([0, 0.7, 0])

    o3d.io.write_point_cloud(out_folder_path , abnormal_points)
    o3d.io.write_point_cloud(normal_file_path , normal_points)



    # # Visualization on open3d
    # data_list = []              # Data in this list will use for visualization
    # data_list.append(gt_vis)
    # #data_list.append(normal_points)


    # # Use DBSCAN for abnormal points clustering
    # # clustered_abnormal_points = abnormal_place_clustering(abnormal_points)
    # # data_list.append(clustered_abnormal_points)


    # data_list.append(abnormal_points)
    # o3d_visualization(data_list)


