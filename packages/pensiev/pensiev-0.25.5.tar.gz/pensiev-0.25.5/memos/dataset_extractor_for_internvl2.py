"""
准备 image path 和 ocr 数据，用于后续提供给 internvl2 生成更符合需求的 caption
"""

import json
import argparse
from sqlalchemy.orm import sessionmaker
from memos.models import EntityModel, EntityMetadataModel
from memos.config import get_database_path
from sqlalchemy import create_engine
from tqdm import tqdm
from pathlib import Path
import argilla as rg
from PIL import Image
import io


def prepare_huggingface_dataset(output_file, batch_size=100, record_count=10000, libraries=None):
    """Prepare a Hugging Face dataset and save it as JSONL."""
    db_path = get_database_path()
    engine = create_engine(f"sqlite:///{db_path}")
    Session = sessionmaker(bind=engine)

    def simplify_ocr_data(ocr_data):
        simplified_data = []
        for item in ocr_data:
            # 提取左上角和右下角的坐标
            dt_boxes = [item["dt_boxes"][0], item["dt_boxes"][2]]
            # 保留 rec_txt 字段，剔除 score
            simplified_data.append({
                "dt_boxes": dt_boxes,
                "rec_txt": item["rec_txt"]
            })
        return simplified_data

    with Session() as session, open(output_file, "w", encoding="utf-8") as f:
        query = session.query(EntityModel)
        
        # 如果指定了 libraries，添加过滤条件
        if libraries:
            query = query.filter(EntityModel.library_id.in_(libraries))
        
        total = query.count()

        progress_bar = tqdm(
            total=min(total, record_count), desc="Processing entities", unit="entity"
        )
        inserted_records = 0

        for offset in range(0, total, batch_size):
            batch = query.limit(batch_size).offset(offset).all()

            for entity in batch:
                # Skip entities with "low_info" tag
                if any(tag.name == "low_info" for tag in entity.tags):
                    progress_bar.update(1)
                    continue

                metadata = {entry.key: entry.value for entry in entity.metadata_entries}

                ocr = metadata.get("ocr_result")
                if not ocr or not Path(entity.filepath).exists():
                    progress_bar.update(1)
                    continue

                # Load JSON from string
                ocr_data = json.loads(ocr)

                # Simplify OCR result
                simplified_ocr = simplify_ocr_data(ocr_data)

                record = {
                    "id": entity.id,
                    "image": entity.filepath,
                    "ocr": simplified_ocr,
                }

                # Dump to JSON string
                json_record = json.dumps(record, ensure_ascii=False)
                f.write(json_record + "\n")
                progress_bar.update(1)
                inserted_records += 1

                if inserted_records >= record_count:
                    break
            if inserted_records >= record_count:
                break

        progress_bar.close()

    print(f"Dataset saved to {output_file}")


def init_argilla_dataset(client, dataset_name="image_captioning"):
    workspace_name = "argilla"

    workspace = client.workspaces(workspace_name)

    if workspace is None:
        workspace = rg.Workspace(name=workspace_name, client=client)
        workspace.create()
        print(f"Workspace created: {workspace_name}")

    dataset = client.datasets(name=dataset_name)

    if dataset is not None:
        return dataset

    settings = rg.Settings(
        fields=[
            rg.ImageField(name="image"), 
            rg.TextField(name="filepath")
        ],
        questions=[
            rg.TextQuestion(
                name="text",
                title="Description of the image",
                required=True,
                use_markdown=True,
            )
        ],
    )

    dataset = rg.Dataset(
        name=dataset_name, workspace=workspace_name, settings=settings, client=client
    )

    dataset.create()
    print(f"Dataset created: {dataset_name}")

    return dataset


def upload_to_argilla(input_file, batch_size=10, dataset_name="image_captioning"):
    """Upload a JSONL dataset to Argilla."""

    client = rg.Argilla(api_url="http://localhost:6900", api_key="argilla.apikey")

    dataset = init_argilla_dataset(client, dataset_name)

    records = []
    total_records = sum(1 for _ in open(input_file, "r"))

    with open(input_file, "r", encoding="utf-8") as f:
        progress_bar = tqdm(
            total=total_records, desc="Uploading to Argilla", unit="record"
        )

        for line in f:
            record_data = json.loads(line)
            image = Image.open(record_data["image"]).convert("RGB")
            image.thumbnail((1280, 1280))

            rg_record = rg.Record(
                id=str(record_data["id"]),
                fields={
                    "image": image,
                    "filepath": record_data["image"],
                },
                suggestions=[
                    rg.Suggestion(
                        "text", record_data["answer"], score=1.0, agent="internvl2"
                    )
                ],
            )
            records.append(rg_record)

            if len(records) >= batch_size:
                dataset.records.log(records)
                progress_bar.update(batch_size)
                records = []

        if records:
            dataset.records.log(records)
            progress_bar.update(len(records))

        progress_bar.close()

    print(f"Dataset uploaded to Argilla: {dataset_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepare and upload dataset")
    parser.add_argument("--output_file", default="dataset.jsonl", help="Output file path")
    parser.add_argument("--size", type=int, default=10000, help="Number of records to extract")
    parser.add_argument("--libraries", nargs="+", type=int, help="List of library IDs to filter entities")
    args = parser.parse_args()

    prepare_huggingface_dataset(args.output_file, record_count=args.size, libraries=args.libraries)
    print(f"Dataset saved to {args.output_file}")
    # Uncomment the following line if you want to upload to Argilla
    # upload_to_argilla(args.output_file)
