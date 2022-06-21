from __future__ import annotations

from typing import Sequence 
import subprocess

def was_fail(src: bytes) -> bool:
    split = src.split(b'\n')
    for line in split:
        if b'FAIL' in line:
            return True
        
    return False

def test() -> bool:
    # Expects to be in the project directory.

    proc = subprocess.run(["go", "test", "./...", "-count=1"], capture_output=True)
    stdout = proc.stdout
    stderr = proc.stderr
    if stdout is not None:
        if was_fail(stdout) is True:
            print(stdout.decode('utf-8'))
            return False
        
    if stderr is not None:
        if was_fail(stderr) is True:
            print(stderr.decode('utf-8'))
            return False

    return True
    
def main(args: Sequence[str] | None = None) -> int:
    '''
        Runs every test in the directory.
    '''
    return 0 if test() == True else 1
