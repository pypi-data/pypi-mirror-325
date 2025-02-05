import json
import asyncio
from tqdm import tqdm
from openai import AsyncOpenAI
import argparse
from pathlib import Path
import aiofiles
import base64
import random

client = AsyncOpenAI(
    api_key="sk-proj-16vgjrpilasc",
    base_url="https://open-tutorials-k8ju0zoi229m.gear-c1.openbayes.net/v1",
)

# 设置最大并发请求数
MAX_CONCURRENT_REQUESTS = 4

prompt = """以下是这个截图的 ocr 的结果，请你结合 ocr 结果描述图片的内容。

{ocr}

最后回答以下问题：

1. 描述截图的内容，重点描述截图的布局、程序以及其他视觉元素，如果所展示的文字内容过多，则尽量简要描述相关内容
2. 为这个截图内容分级：PG | PG-13 | R | X
3. 这个屏幕的用户在做什么

请按照 JSON 格式返回数据，格式如下：

{{ "description": "string", "rating": "PG|PG-13|R|X", "behavior": "string" }}

不要包含除了 JSON 之外的其他内容，也不要包含任何注释"""

model = "qwen2-vl-72b"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


async def summarize_text(semaphore, data):
    async with semaphore:
        try:
            base64_image = encode_image(data["image"])
            ocr_result = " ".join([item["rec_txt"] for item in data["ocr"]])
            ocr_result = ocr_result[:1024]

            response = await asyncio.wait_for(
                client.chat.completions.create(
                    model=model,  # Use the extracted model variable here
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful assistant that summarizes and analyzes image descriptions.",
                        },
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "image_url",
                                    "image_url": {"url": f"data:image/webp;base64,{base64_image}"},
                                },
                                {
                                    "type": "text",
                                    "text": prompt.format(ocr=ocr_result),
                                },
                            ],
                        },
                    ],
                    stream=False,
                    max_tokens=1024,
                    temperature=0.1,
                    top_p=0.8,
                    extra_body={'repetition_penalty': 1.2}
                ),
                timeout=60  # 1 minute timeout
            )
            summary = response.choices[0].message.content.strip()
            data["sum"] = summary
            data["ocr"] = ocr_result
            return data
        except asyncio.TimeoutError:
            print(f"Timeout processing item {data['id']}")
            return None
        except Exception as e:
            print(f"Error processing item {data['id']}: {str(e)}")
            return None


async def summarize_dataset(input_file, output_file, limit=None):
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

    # Load existing summaries
    existing_summaries = set()
    if Path(output_file).exists():
        with open(output_file, "r") as outfile:
            for line in outfile:
                existing_summaries.add(json.loads(line)["id"])

    with open(input_file, "r") as infile:
        data = [json.loads(line) for line in infile]

    if limit:
        random.seed(42)
        data = random.sample(data, limit)

    # Filter out already processed items
    data_to_process = [item for item in data if item["id"] not in existing_summaries]

    processed_count = 0
    skipped_count = len(data) - len(data_to_process)

    async def process_and_write(item):
        nonlocal processed_count
        result = await summarize_text(semaphore, item)
        if result:
            async with aiofiles.open(output_file, "a") as outfile:
                await outfile.write(json.dumps(result, ensure_ascii=False) + "\n")
            processed_count += 1

    tasks = [process_and_write(item) for item in data_to_process]

    for task in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Summarizing"):
        await task

    print(
        f"Processed {processed_count} new items. Skipped {skipped_count} existing items."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Summarize dataset with optional limit."
    )
    parser.add_argument("--input", default="dataset.jsonl", help="Input JSONL file")
    parser.add_argument(
        "--output", default="dataset.updated.jsonl", help="Output JSONL file"
    )
    parser.add_argument(
        "--limit", type=int, help="Limit the number of records to process"
    )
    args = parser.parse_args()

    asyncio.run(summarize_dataset(args.input, args.output, args.limit))
