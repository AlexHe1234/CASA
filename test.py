import numpy as np
import trimesh


path = '/Users/alexhe/Downloads/snow_leopard_male/frame_000001.obj' 
mesh = trimesh.load(path)

# data = np.load('/Users/alexhe/Downloads/snow_leopard_male/info/0001.npz', allow_pickle=True)
data = np.load('/Users/alexhe/Downloads/snow_leopard_male/skeleton/skeleton_all_frames.npy', allow_pickle=True).item()

breakpoint()
