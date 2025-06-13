from pcd_remesh import remesh
from pcd_compare import bim_comparison
from dataloader import load_data_folder

# Hyperparameters
data_folder_path = "data/demo_1"
abnormal_thres = 500                                            # Sensitivity for abnormal points detection
obj_type_list = []


# Load all files under designated folder
obj_list, target_file_path, out_folder_path = load_data_folder(data_folder_path)


# Remesh all .obj files and save under ./output folder
for obj_name in obj_list:
    if "Beam_Column" in obj_name or "beam_column" in obj_name:  # Check .obj property
        obj_type = "Beam_Column"
    elif obj_name[:4]=="Wall" or "wall" in obj_name:
        obj_type = "Wall"
    else:
        obj_type = "Unknown"
    obj_path = data_folder_path + "/" + obj_name
    remesh(obj_path, out_folder_path, obj_type)                 # Remesh BIM .obj model and save as .ply
    obj_type_list.append(obj_type)


# Compare BIM pointcloud and LiDAR pointcloud
if len(obj_type_list)>= 2:
    reuse_flag = False
    for obj_type in obj_type_list:
        print("Comparing with: " + obj_type + " obj.")
        gt_file_path = out_folder_path + "/" + obj_type + "_bim_pcd.ply"
        abnormal_file_path = out_folder_path + "/abnormal.ply"
        normal_file_path = out_folder_path + "/" + obj_type + "_normal.ply"

        if reuse_flag == False:
            bim_comparison(abnormal_file_path, normal_file_path, gt_file_path, target_file_path, abnormal_thres)
            reuse_flag =True
        else:
            bim_comparison(abnormal_file_path, normal_file_path, gt_file_path, abnormal_file_path, abnormal_thres)

else:
    print("Comparing with: " + obj_type_list[0] + " obj.")
    gt_file_path = out_folder_path + "/" + obj_type_list[0] + "_bim_pcd.ply"
    abnormal_file_path = out_folder_path + "/abnormal.ply"
    normal_file_path = out_folder_path + "/" + obj_type_list[0] + "_normal.ply"
    bim_comparison(abnormal_file_path, normal_file_path, gt_file_path, target_file_path, abnormal_thres)

print("------------Finished------------")