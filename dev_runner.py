# A file that automatically restarts any changes to the code
import asyncio
import subprocess

from watchfiles import arun_process

def start_bot():
    # Запуск основного скрипта
    # python -m main
    subprocess.run(['python', '-m', 'main'])

async def main():
    await arun_process(
        'app',
        'config',
        'dev_runner.py',
        'main.py',
        target=start_bot
    )

if __name__ == '__main__':
    asyncio.run(main())
