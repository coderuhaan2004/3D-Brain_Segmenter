import os
import numpy as np
import nibabel as nib
import argparse

def save_mgz(mgz_dir, output_dir):
    # Iterate through the directory to find the MGZ file
    for file in os.listdir(mgz_dir):
        if file.endswith(".mgz"):
            mgz_path = os.path.join(mgz_dir, file)
            
            # Load MGZ file
            try:
                mgz_img = nib.load(mgz_path)
                mgz_array = mgz_img.get_fdata().astype(np.int32)  # Convert to integer labels

                # Save as NIfTI image
                nii_filename = f"{os.path.splitext(file)[0]}.nii.gz"
                nib.save(mgz_img, os.path.join(output_dir, nii_filename))
                print(f"Converted {file} to {nii_filename}")
            
            except Exception as e:
                print(f"Failed to convert {file}: {e}")
        else:
            print(f"Skipped {file} (not an MGZ file)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert original MGZ brain image to NIfTI format")
    parser.add_argument("mgz_dir", type=str, help="Path to directory containing MGZ file(s)")
    parser.add_argument("output_dir", type=str, help="Output directory for NIfTI file(s)")
    args = parser.parse_args()

    # Ensure output directory exists
    os.makedirs(args.output_dir, exist_ok=True)

    save_mgz(args.mgz_dir, args.output_dir)