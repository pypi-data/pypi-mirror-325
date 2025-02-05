import json
import asyncio
from tqdm import tqdm
from openai import AsyncOpenAI
import argparse
from pathlib import Path
import aiofiles

client = AsyncOpenAI(
    api_key="sk-proj-16vgjrpilasc",
    base_url="https://aisensiy-43v6wj9s940a.gear-c1.openbayes.net/v1",
)

# 设置最大并发请求数
MAX_CONCURRENT_REQUESTS = 32

prompt = """Please read the following screenshot description and provide a BRIEF SUMMARY focusing on the main layout and key visual elements. Infer what the user might be doing.

If the screenshot shows a desktop idle or lock screen state, please JUST RETURN INFORMATION TELL THE USER IS INACTIVE, DO NOT GIVE ME MORE EXPLAINATION. Here are some hints to describe when a screenshot shows a desktop idle or lock screen state:

# ... (rest of the prompt remains unchanged) ...

<content>
{content}
</content>
"""


async def summarize_text(semaphore, data):
    async with semaphore:
        try:
            response = await client.chat.completions.create(
                model="llama-3.1-70b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that summarizes and analyzes image descriptions.",
                    },
                    {"role": "user", "content": prompt.format(content=data["answer"])},
                ],
                max_tokens=512,
                temperature=0.3,
            )
            summary = response.choices[0].message.content.strip()
            data["sum"] = summary
            return data
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
        data = data[:limit]

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
