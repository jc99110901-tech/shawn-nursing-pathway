#!/usr/bin/env python3

import argparse
import hashlib
import json
import shutil
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "shawn-nursing-pathway"
DIST_NAMES = (
    "shawn-nursing-pathway-lite.md",
    "shawn-nursing-pathway-full.md",
    "shawn-nursing-pathway-workbuddy.zip",
    "manifest.json",
)
RAW_BASE = (
    "https://raw.githubusercontent.com/jc99110901-tech/"
    "shawn-nursing-pathway/main/dist"
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").rstrip() + "\n"


def markdown_source(path: Path) -> str:
    relative = path.relative_to(ROOT)
    return f"\n\n---\n\n## Source: `{relative}`\n\n{read_text(path)}"


def release_metadata() -> dict:
    return json.loads(read_text(ROOT / "release.json"))


def render_lite(metadata: dict) -> str:
    header = f"""# Shawn Nursing Pathway Lite

Version: {metadata["version"]}
Release date: {metadata["release_date"]}
Canonical source: https://github.com/jc99110901-tech/shawn-nursing-pathway

This is the low-friction, Chinese-first, single-file distribution. Upload it to
an AI chat or use it as the system/role instruction. It does not provide any
admission, employment, visa, licensure, or immigration guarantee.

---

"""
    return header + read_text(ROOT / "universal" / "quick-start-cn.md")


def render_full(metadata: dict) -> str:
    header = f"""# Shawn Nursing Pathway Full Knowledge Pack

Version: {metadata["version"]}
Release date: {metadata["release_date"]}
Canonical source: https://github.com/jc99110901-tech/shawn-nursing-pathway

This is the single-file knowledge-base distribution. Use the Lite file as the
system/role instruction when the platform separates prompts from knowledge.
Detailed references below are public screening material, not current official
policy. Time-sensitive facts must still be checked against current official
sources at answer time.
"""
    paths = [ROOT / "universal" / "quick-start-cn.md", SKILL_ROOT / "SKILL.md"]
    paths.extend(sorted((SKILL_ROOT / "references").glob("*.md")))
    return header + "".join(markdown_source(path) for path in paths)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def build_workbuddy_zip(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for source in sorted(SKILL_ROOT.rglob("*")):
            if not source.is_file() or source.name in {".DS_Store"}:
                continue
            relative = source.relative_to(SKILL_ROOT).as_posix()
            info = zipfile.ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_source() -> None:
    skill = read_text(SKILL_ROOT / "SKILL.md")
    if not skill.startswith("---\n"):
        raise SystemExit("SKILL.md frontmatter is missing")
    frontmatter = skill.split("---", 2)[1]
    keys = [
        line.split(":", 1)[0].strip()
        for line in frontmatter.splitlines()
        if ":" in line
    ]
    if keys != ["name", "description"]:
        raise SystemExit(f"Unexpected SKILL.md frontmatter keys: {keys}")


def build(target: Path) -> None:
    validate_source()
    metadata = release_metadata()
    target.mkdir(parents=True, exist_ok=True)

    lite = target / DIST_NAMES[0]
    full = target / DIST_NAMES[1]
    workbuddy = target / DIST_NAMES[2]
    manifest = target / DIST_NAMES[3]

    write_text(lite, render_lite(metadata))
    write_text(full, render_full(metadata))
    build_workbuddy_zip(workbuddy)

    files = {}
    for path in (lite, full, workbuddy):
        files[path.name] = {
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "url": f"{RAW_BASE}/{path.name}",
        }

    output = {
        "name": "shawn-nursing-pathway",
        "version": metadata["version"],
        "release_date": metadata["release_date"],
        "canonical_repository": (
            "https://github.com/jc99110901-tech/shawn-nursing-pathway"
        ),
        "files": files,
    }
    write_text(manifest, json.dumps(output, ensure_ascii=False, indent=2) + "\n")


def check() -> int:
    with tempfile.TemporaryDirectory() as directory:
        expected = Path(directory)
        build(expected)
        mismatches = []
        for name in DIST_NAMES:
            current = ROOT / "dist" / name
            generated = expected / name
            if not current.exists() or current.read_bytes() != generated.read_bytes():
                mismatches.append(name)
        if mismatches:
            print("Distribution files are stale:", ", ".join(mismatches))
            return 1
    print("Distribution files are current.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify committed distribution files match the current source.",
    )
    args = parser.parse_args()
    if args.check:
        return check()

    dist = ROOT / "dist"
    if dist.exists():
        shutil.rmtree(dist)
    build(dist)
    print(f"Built distribution files in {dist}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
