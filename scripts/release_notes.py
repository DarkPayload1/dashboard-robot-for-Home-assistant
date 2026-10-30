"""Extract one version's release notes from CHANGELOG.md."""
import re
import sys
from pathlib import Path

def release_notes(changelog, version):
    sections = re.split(r"(?m)^# (.+)\n", changelog)
    for index in range(1, len(sections), 2):
        if sections[index].strip().removeprefix("v") == version.removeprefix("v"):
            changes = sections[index + 1].strip()
            if not changes:
                break
            return "## Nyt i denne version\n\n" + changes + "\n\n## Opdatering\n\nOpdatér Dashboard Robot i HACS, genstart Home Assistant og genindlæs dashboardet (Ctrl+Shift+R på computer).\n"
    raise ValueError("Missing changelog entry for " + version)

if __name__ == "__main__":
    print(release_notes(Path("CHANGELOG.md").read_text(encoding="utf-8"), sys.argv[1]), end="")
