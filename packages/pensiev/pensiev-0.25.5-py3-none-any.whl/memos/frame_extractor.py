import cv2
from PIL import Image
from pathlib import Path
import argparse


def extract_video_frame(video_path: Path, frame_number: int) -> Image.Image:
    cap = cv2.VideoCapture(str(video_path))
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return None

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return Image.fromarray(frame_rgb)


def test_extract_video_frame(video_path: Path, frame_number: int):
    # 确保测试视频文件存在
    if not video_path.is_file():
        print(f"Error: Video file not found at {video_path}")
        return

    # 尝试提取指定帧
    frame_image = extract_video_frame(video_path, frame_number)

    if frame_image is None:
        print(f"Error: Failed to extract frame {frame_number} from video")
    else:
        print(f"Successfully extracted frame {frame_number} from video")
        print(f"Frame dimensions: {frame_image.size}")

        # 保存提取的帧为图像文件
        output_path = video_path.with_name(f"extracted_frame_{frame_number}.png")
        frame_image.save(output_path)
        print(f"Extracted frame saved to: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract a frame from a video file.")
    parser.add_argument("video_path", type=str, help="Path to the video file")
    parser.add_argument(
        "frame_number", type=int, help="Frame number to extract (0-based index)"
    )

    args = parser.parse_args()

    video_path = Path(args.video_path)
    frame_number = args.frame_number

    test_extract_video_frame(video_path, frame_number)
