# Comparison of Discrepancies in BIM Models

This algorithm involves a multi-step process to detect differences between BIM models and scanned LiDAR pointcloud. The algorithm first read .xyz format ground truth and target scanned .ply data, then applies point cloud alignment.

After alignment, the algorithm identifies outliers in the ground-truth point cloud relative to the BIM model's point cloud. These outliers represent discrepancies or deviations, highlighting areas where the BIM model does not match the actual built environment. 


## Environment Setup
 The algorithm has been validated on Python 3.10.16. with .obj and .ply data inputs, in theory it also works with .xyz format.
 
 ```bash
  
  cd bim_pcd_compare
  pip install -r requirements.txt
```

## Usage
(Optional) If you facing errors, You may use ```cloudcompare``` to downsample the .xyz pointcloud and save as .ply for a faster and easier process.

Place your revit .obj models and scanned point clouds under same folder path (e.g. ./data/aaa) directory,
please also remember to add sufix (Wall_ and Beam_Column_) to allow the program determine structure type.

After data preperation, you may need to change the hyperparameters including```data_folder_path```.
The ```abnormal_thres``` parameter can be adjusted to refine the sensitivity of outlier detection.
```bash
python main.py
```

The program will output ```abnormal.ply```, ```xxx__normal.ply``` and ```xxx_bim_pcd.ply```.





## Under development
- Noise pruning
- Model rough clustering
- Object detection


## Authors
- [@Michael SIN](https://www.github.com/Michael-Sin)
