import nibabel as nib
import numpy as np

mask_path = 'output.mgz'

mgz_array = nib.load(mask_path).get_fdata().astype(np.int32)  # Convert to integer labels
print("Unique Labels:", np.unique(mgz_array))
