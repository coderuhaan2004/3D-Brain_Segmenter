import os
import numpy as np
import nibabel as nib
import json
import argparse

def highlight_label(mgz_path, lut_path ,output_dir):
    #dictionary for the grayscale values of the subparts of the brain
    subparts ={}
    # Load MGZ file
    mgz_img = nib.load(mgz_path)
    mgz_array = mgz_img.get_fdata().astype(np.int32)  # Convert to integer labels
    print("Unique Labels:", np.unique(mgz_array))

    # Load LUT (Look-Up Table)
    with open(lut_path, "r") as f:
        lut = json.load(f)

    # Initialize output grayscale image
    # For each voxel, take its label-id and assign the grayscale intensity value to the voxel

    x_dim, y_dim, z_dim = mgz_array.shape
    highlighted_array = np.zeros((x_dim, y_dim, z_dim), dtype=np.uint8)  # Initialize with zeros

    print("Iterating over the MGZ array to assign grayscale values...")
    for i in range(x_dim):
        for j in range(y_dim):
            for k in range(z_dim):
                label_id = mgz_array[i, j, k]
                if str(label_id) in lut:
                    color_rgb = np.array(lut[str(label_id)][0][:3], dtype=np.uint8)
                    # Convert RGB to grayscale intensity
                    grayscale_value = int(0.2989 * color_rgb[0] + 0.5870 * color_rgb[1] + 0.1140 * color_rgb[2])
                    subparts[lut[str(label_id)][1]] = grayscale_value # Store the grayscale value for the subpart with name of the subpart
                    highlighted_array[i,j,k] = grayscale_value  # Assign grayscale intensity
                else:
                    highlighted_array[i,j,k] = 0

    # Convert to NIfTI format
    highlighted_nifti = nib.Nifti1Image(highlighted_array, affine=mgz_img.affine, header=mgz_img.header)

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save the new highlighted NIfTI file
    output_file = os.path.join(output_dir, f"highlighted_brain_gray.nii.gz")
    nib.save(highlighted_nifti, output_file)
    print(f"Saved grayscale highlighted NIFTI image as {output_file}")
    print(f"Subparts and their grayscale values:")
    for subpart, value in subparts.items():
        print(f"{subpart}: {value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Highlight a label in a brain MGZ image and save as NIfTI")
    parser.add_argument("mgz_path", type=str, help="Path to the MGZ file")
    parser.add_argument("lut_path", type=str, help="Path to the LUT JSON file")
    parser.add_argument("output_dir", type=str, help="Output directory for the NIfTI file")

    args = parser.parse_args()

    highlight_label(args.mgz_path, args.lut_path, args.output_dir)