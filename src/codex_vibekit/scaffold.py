from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
import shutil


@dataclass
class InitResult:
    created: list[Path] = field(default_factory=list)
    conflicts: list[tuple[Path, Path]] = field(default_factory=list)
    skipped: list[Path] = field(default_factory=list)

    def summary(self) -> str:
        lines: list[str] = []
        lines.append("codex-vibekit init summary")
        lines.append(f"- created: {len(self.created)}")
        lines.append(f"- conflicts (*.vibekit-new): {len(self.conflicts)}")
        lines.append(f"- skipped: {len(self.skipped)}")
        if self.conflicts:
            lines.append("")
            lines.append("conflicts:")
            for existing, vibekit_new in self.conflicts[:20]:
                lines.append(f"- {existing} -> {vibekit_new}")
            if len(self.conflicts) > 20:
                lines.append(f"- ... ({len(self.conflicts) - 20} more)")
        return "\n".join(lines)


def _scaffold_root() -> Path:
    return Path(__file__).resolve().parent / "assets" / "scaffold"


def _copy_tree_no_overwrite(src_root: Path, dst_root: Path) -> InitResult:
    created: list[Path] = []
    conflicts: list[tuple[Path, Path]] = []
    skipped: list[Path] = []

    for src_path in sorted(src_root.rglob("*")):
        rel = src_path.relative_to(src_root)
        dst_path = dst_root / rel

        if src_path.is_dir():
            dst_path.mkdir(parents=True, exist_ok=True)
            continue

        dst_path.parent.mkdir(parents=True, exist_ok=True)

        if dst_path.exists():
            try:
                if dst_path.is_file() and dst_path.read_bytes() == src_path.read_bytes():
                    skipped.append(dst_path)
                    continue
            except OSError:
                pass

            vibekit_new = dst_path.with_name(dst_path.name + ".vibekit-new")
            if vibekit_new.exists():
                skipped.append(dst_path)
                continue
            shutil.copy2(src_path, vibekit_new)
            conflicts.append((dst_path, vibekit_new))
            continue

        shutil.copy2(src_path, dst_path)
        created.append(dst_path)

    return InitResult(created=created, conflicts=conflicts, skipped=skipped)


def _ensure_required_dirs(dst_root: Path) -> None:
    required = [
        dst_root / "docs" / "templates",
        dst_root / "docs" / "decisions",
        dst_root / "docs" / "specs",
        dst_root / "docs" / "design",
        dst_root / "docs" / "contracts",
        dst_root / "docs" / "plans",
        dst_root / "logs" / "work",
        dst_root / "skills" / "orchestrator",
        dst_root / "skills" / "planner",
        dst_root / "skills" / "builder",
        dst_root / "skills" / "critic",
        dst_root / "skills" / "techniques" / "brainstorming",
    ]
    for path in required:
        path.mkdir(parents=True, exist_ok=True)


def _ensure_todays_worklog(dst_root: Path, result: InitResult) -> None:
    logs_dir = dst_root / "logs" / "work"
    logs_dir.mkdir(parents=True, exist_ok=True)
    filename = f"WORKLOG-{date.today().isoformat()}.md"
    worklog_path = logs_dir / filename
    if worklog_path.exists():
        return
    worklog_path.write_text(
        f"# Work Log ({date.today().isoformat()})\n\n",
        encoding="utf-8",
    )
    result.created.append(worklog_path)


def init_scaffold(path: str | Path) -> InitResult:
    dst_root = Path(path).expanduser().resolve()
    dst_root.mkdir(parents=True, exist_ok=True)

    src_root = _scaffold_root()
    if not src_root.exists():
        raise RuntimeError(f"scaffold assets not found at {src_root}")

    result = _copy_tree_no_overwrite(src_root=src_root, dst_root=dst_root)
    _ensure_required_dirs(dst_root)
    _ensure_todays_worklog(dst_root, result)
    return result
