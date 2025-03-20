import os
import numpy as np
import nibabel as nib
import json
import argparse

def highlight_label(mgz_path, lut_path, output_dir, label_id):
    # Load MGZ file
    mgz_img = nib.load(mgz_path)
    mgz_array = mgz_img.get_fdata().astype(np.int32)  # Convert to integer labels
    print("Unique Labels:", np.unique(mgz_array))

    # Load LUT (Look-Up Table)
    with open(lut_path, "r") as f:
        lut = json.load(f)

    # Initialize output grayscale image
    highlighted_array = np.zeros_like(mgz_array, dtype=np.uint8)

    if str(label_id) in lut:
        color_rgb = np.array(lut[str(label_id)][0][:3], dtype=np.uint8)  # Extract RGB color

        # Convert RGB to grayscale intensity
        grayscale_value = int(0.2989 * color_rgb[0] + 0.5870 * color_rgb[1] + 0.1140 * color_rgb[2])

        # Binary mask for the selected label
        mask = (mgz_array == label_id)

        # Assign grayscale intensity for the highlighted region
        highlighted_array[mask] = grayscale_value  # Highlighted label
        highlighted_array[~mask] = 100  # Mid-gray for other regions

        # Convert to NIfTI format
        highlighted_nifti = nib.Nifti1Image(highlighted_array, affine=mgz_img.affine, header=mgz_img.header)

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Save the new highlighted NIfTI file
        output_file = os.path.join(output_dir, f"highlighted_brain_gray{label_id}.nii.gz")
        nib.save(highlighted_nifti, output_file)
        print(f"Saved grayscale highlighted NIFTI image as {output_file}")
    else:
        print("Label ID not found in LUT.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Highlight a label in a brain MGZ image and save as NIfTI")
    parser.add_argument("mgz_path", type=str, help="Path to the MGZ file")
    parser.add_argument("lut_path", type=str, help="Path to the LUT JSON file")
    parser.add_argument("output_dir", type=str, help="Output directory for the NIfTI file")
    parser.add_argument("label_id", type=int, help="Label ID to highlight")

    args = parser.parse_args()

    highlight_label(args.mgz_path, args.lut_path, args.output_dir, args.label_id)