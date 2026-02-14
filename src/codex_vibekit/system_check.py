from __future__ import annotations

import platform
import shutil
import sys


def run_check() -> int:
    uv_path = shutil.which("uv")
    git_path = shutil.which("git")

    print("codex-vibekit check")
    print(f"- Python: {platform.python_version()} ({sys.executable})")
    print(f"- uv: {'OK' if uv_path else 'MISSING'}" + (f" ({uv_path})" if uv_path else ""))
    print(
        f"- git: {'OK' if git_path else 'MISSING'}" + (f" ({git_path})" if git_path else "")
    )
    if sys.version_info < (3, 11):
        print("- note: Python 3.11+ is recommended.")
    if not uv_path:
        print("- install uv: https://docs.astral.sh/uv/")
    return 0

