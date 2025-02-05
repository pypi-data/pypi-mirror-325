import json
import os
import shutil
from tqdm import tqdm
from PIL import Image
import io
from concurrent.futures import ThreadPoolExecutor, as_completed


def compress_and_convert_image(image_path, output_path, max_size_mb=2):
    with Image.open(image_path) as img:
        if (
            image_path.lower().endswith(".png")
            and os.path.getsize(image_path) > max_size_mb * 1024 * 1024
        ):
            # 将 PNG 转换为 JPG 并压缩
            img = img.convert("RGB")
            output_path = output_path.rsplit(".", 1)[0] + ".jpg"
            img.save(output_path, "JPEG", quality=85)
        else:
            # 直接复制原图
            img.save(output_path)
    return output_path


def process_image(data, shots_dir):
    image_path = data.get("image")
    if image_path and os.path.exists(image_path):
        image_name = os.path.basename(image_path)
        new_image_path = os.path.join(shots_dir, image_name)
        if new_image_path == image_path:
            return None
        try:
            new_image_path = compress_and_convert_image(image_path, new_image_path)
            data["image"] = os.path.relpath(new_image_path, shots_dir)
            return data, os.path.basename(new_image_path)
        except Exception as e:
            print(f"Error processing image {image_path}: {e}")
    elif not image_path:
        return data, None
    return None


def update_image_paths(input_file, output_file, shots_dir, max_workers=8):
    if not os.path.exists(shots_dir):
        os.makedirs(shots_dir)

    updated_data = []
    seen_images = set()

    with open(input_file, "r") as infile:
        data_list = [json.loads(line) for line in infile]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(process_image, data, shots_dir) for data in data_list
        ]

        for future in tqdm(
            as_completed(futures), total=len(futures), desc="Processing images"
        ):
            result = future.result()
            if result:
                data, image_name = result
                if image_name and image_name not in seen_images:
                    seen_images.add(image_name)
                    updated_data.append(data)
                elif not image_name:
                    updated_data.append(data)

    with open(output_file, "w") as outfile:
        for item in tqdm(updated_data, desc="Writing updated data", unit="item"):
            json.dump(item, outfile, ensure_ascii=False)
            outfile.write("\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Update image paths in the dataset.")
    parser.add_argument(
        "--input_file",
        type=str,
        default="dataset.updated.jsonl",
        help="Path to the input JSONL file.",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default="dataset.updated.formatted.jsonl",
        help="Path to the output JSONL file.",
    )
    parser.add_argument(
        "--shots_dir",
        type=str,
        default="shots",
        help="Directory to save processed images.",
    )
    parser.add_argument(
        "--max_workers", type=int, default=8, help="Maximum number of worker threads."
    )

    args = parser.parse_args()

    update_image_paths(
        args.input_file, args.output_file, args.shots_dir, args.max_workers
    )
