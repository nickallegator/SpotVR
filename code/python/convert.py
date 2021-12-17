# https://stackoverflow.com/questions/51350493/convertion-of-ply-format-to-pcd-format

import open3d as o3d
file= input("Enter File Name:")
pcd = o3d.io.read_point_cloud(file)
o3d.io.write_point_cloud("UnityProject/Capstone/Assets/file.ply", pcd)
