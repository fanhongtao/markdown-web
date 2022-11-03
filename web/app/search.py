from dataclasses import dataclass
from operator import attrgetter
from pathlib import Path
from typing import List

@dataclass
class Result:
    filename: str
    filename_count: int
    content_count: int
    lines: List[str]


def search_files(root: Path, searchTerms: List[str]) -> List[Result]:
    results = _search(root, root, searchTerms)
    results = sorted(results, key=attrgetter('filename_count', 'content_count'), reverse=True)
    return results


def _search(dir: Path, root: Path, searchTerms: List[str]) -> List[Result]:
    results = []
    for entry in dir.iterdir():
        if entry.is_dir() and entry.name != ".git":
            results += _search(entry, root, searchTerms)
        else:
            filename_count = _match_filename(entry, searchTerms)
            if entry.suffix in ['.md', '.txt']:
                content_count, lines = _match_content(entry, searchTerms)
            else:
                content_count, lines = 0, []
            if filename_count != 0 or content_count != 0:
                results.append(Result(entry.relative_to(root), filename_count, content_count, lines))
    return results


def _match_filename(file: Path, searchTerms: List[str]) -> int:
    return _match_str(file.name, searchTerms)


def _match_content(file: Path, searchTerms: List[str]):
    count = 0
    lines = []
    content = file.read_text()
    for line in content.splitlines():
        num = _match_str(line, searchTerms)
        if num > 0:
            count += num
            lines.append(line)
    return count, lines


def _match_str(src: str, searchTerms: List[str]) -> int:
    count = 0
    src = src.lower()
    for item in searchTerms:
        item = item.lower()
        idx = 0
        while True:
            idx = src.find(item, idx)
            if idx == -1:
                break
            else:
                count += 1
                idx += 1
    return count
