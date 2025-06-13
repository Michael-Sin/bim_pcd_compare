import os

def load_data_folder(data_folder_path):
    # Load revit .obj and lidar .xyz files
    obj_list = []
    for f in os.listdir(data_folder_path):
        if f[-4:] == ".obj":                                            # Model file made from revit (.obj)
            obj_list.append(f)
        elif f[-4:] == ".xyz" or f[-4:] == ".las" or f[-4:] == ".ply":  # LiDAR scanned file (.xyz/.las/.ply)
            target_pcd_name = f
    target_file_path = data_folder_path + "/" + target_pcd_name
    print("Found total "+str(len(obj_list))+" .obj files.")

    # Create output folder
    out_folder_path = "output/" + data_folder_path.replace("/", "_")
    os.makedirs(out_folder_path, exist_ok=True)
    return obj_list, target_file_path, out_folder_path
