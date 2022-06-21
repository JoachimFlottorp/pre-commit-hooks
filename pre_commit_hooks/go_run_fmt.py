from __future__ import annotations

from typing import Sequence

import subprocess
import argparse

def auto(args: argparse.Namespace) -> str:
    return args.auto is True and "-w" or ""  

def format(write: str) -> int:
    proc = subprocess.run(["gofmt", "-l", write, "."], capture_output=True)
    stdout = proc.stdout.decode('utf-8')
    if stdout != '':
        if write == "":
            split = len(stdout.split('\n')) - 1
            print(f"{split} files need to be formatted: \n{stdout}")
            return 1
        else:
            print(f"Wrote go fmt changes to\t\n{stdout}")
    return 0

def main(_args: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Runs go fmt a built int golang formatter")
    parser.add_argument("-a", "--auto", action="store_true", help="Automatically write go fmt changes", default=False)
    args = parser.parse_args(_args)
    
    return format(auto(args))
