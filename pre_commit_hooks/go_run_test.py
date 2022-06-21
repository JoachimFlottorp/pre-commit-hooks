from __future__ import annotations

import subprocess
from dataclasses import dataclass, field

@dataclass
class Result:
    okay: bool
    reason: str = field(default="")

def was_fail(src: bytes) -> Result:
    split = src.split(b'\n')
    for line in split:
        if b'FAIL' in line:
            return Result(False, line.decode('utf-8'))

    return Result(True)

def test() -> bool:
    proc = subprocess.run(["go", "test", "./...", "-count=1"], capture_output=True)
    stdout = proc.stdout
    stderr = proc.stderr
    if stdout is not None:
        result = was_fail(stdout)
        if result.okay is False:
            print(result.reason)
            return result.okay

    if stderr is not None:
        result = was_fail(stderr)
        if result.okay is False:
            print(result.reason)
            return result.okay

    return True

def main() -> int:
    return 0 if test() == True else 1

if __name__ == "__main__":
    main()