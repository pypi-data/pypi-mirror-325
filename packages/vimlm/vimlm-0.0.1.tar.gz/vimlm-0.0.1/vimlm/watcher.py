import asyncio
import subprocess
import json
import os
from watchfiles import awatch
from nanollama32 import Chat

DEBUG = False
NUM_TOKEN = 1000
DIRECTORY = os.path.expanduser("~/watched_dir")  
OUT_FILE = "response.md"
LOG_FILE = "log.json"
FILES = ["context", "yank", "user", "tree"]  

out_path = os.path.join(DIRECTORY, OUT_FILE)
log_path = os.path.join(DIRECTORY, LOG_FILE)
os.makedirs(DIRECTORY, exist_ok=True)
chat = Chat(variant='uncn_llama_32_3b_it')

with open(out_path, "w", encoding="utf-8") as f:
    f.write('LLM is ready')

async def monitor_directory():
    async for changes in awatch(DIRECTORY):
        found_files = {os.path.basename(f) for _, f in changes}
        if FILES[-1] in found_files and set(FILES).issubset(set(os.listdir(DIRECTORY))):
            await process_files()

async def process_files():
    data = {}
    for file in FILES:
        path = os.path.join(DIRECTORY, file)
        with open(path, "r", encoding="utf-8") as f:
            data[file] = f.read().strip()
        os.remove(path)  
    data['ext'] = data['tree'].split('.')[-1]
    if len(data['yank']) > 0:
        str_template = "**{tree}**\n```{ext}\n{context}\n```\n\n```{ext}\n{yank}\n```\n\n{user}" if '\n' in data['yank'] else "**{tree}**\n```{ext}\n{context}\n```\n\n`{yank}` {user}"
    else:
        str_template = "**{tree}**\n```{ext}\n{context}\n\n```\n\n{user}"
    prompt = str_template.format(**data)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write('')
    response = chat(prompt, max_new=NUM_TOKEN, verbose=DEBUG, stream=out_path)[0][:-10].strip()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(response)
    chat.reset()
    if DEBUG:
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as log_f:
                logs = json.load(log_f)
        else:
            logs = []
        logs.append({'prompt':prompt, 'respone':response})
        with open(log_path, "w", encoding="utf-8") as log_f:
            json.dump(logs, log_f, indent=2)

asyncio.run(monitor_directory())

