"""Dump odcs-template.xlsx as text, one file per sheet plus the named ranges, so layout changes show up as a readable diff.

Usage:
    python dump_template.py            # rewrite template-dump/
    python dump_template.py --check    # exit 1 when template-dump/ is stale
"""

import re
import sys
import zipfile
from pathlib import Path

import openpyxl

ROOT = Path(__file__).parent
TEMPLATE = ROOT / "odcs-template.xlsx"
OUT = ROOT / "template-dump"


def dump(workbook, path=TEMPLATE) -> dict[str, str]:
    files = {}
    # validations and conditional formats with a direct reference to another sheet are stored as
    # x14 extensions; openpyxl-based consumers drop them, so they must not exist (use names instead)
    extensions = []
    with zipfile.ZipFile(path) as archive:
        for name in sorted(archive.namelist()):
            if name.startswith("xl/worksheets/sheet"):
                xml = archive.read(name).decode()
                for tag in re.findall(r"<x14:(dataValidation|conditionalFormatting)\b", xml):
                    extensions.append(f"{name}\t{tag}")
    files["unsupported-extensions.txt"] = "\n".join(extensions) + "\n"
    names = []
    for name, defined in sorted(workbook.defined_names.items()):
        names.append(f"{name}\t{defined.attr_text}")
    for sheet in workbook.worksheets:
        for name in sorted(sheet.defined_names):
            names.append(f"{name}\t{sheet.defined_names[name].attr_text}\t(scope: {sheet.title})")
    files["named-ranges.txt"] = "\n".join(names) + "\n"

    for sheet in workbook.worksheets:
        lines = [f"sheet\t{sheet.title}\tstate={sheet.sheet_state}"]
        for merged in sorted(str(r) for r in sheet.merged_cells.ranges):
            lines.append(f"merged\t{merged}")
        for validation in sheet.data_validations.dataValidation:
            if validation.type:
                lines.append(f"validation\t{validation.sqref}\t{validation.type}\t{validation.formula1}")
        for cf in sheet.conditional_formatting:
            for rule in cf.rules:
                lines.append(f"conditional\t{cf.sqref}\t{rule.type}\t{';'.join(rule.formula or [])}")
        for row in sheet.iter_rows():
            for cell in row:
                if cell.value is None:
                    continue
                value = str(cell.value).replace("\\", "\\\\").replace("\n", "\\n").replace("\t", "\\t")
                lines.append(f"{cell.coordinate}\t{value}")
        files[sheet.title.replace("<", "").replace(">", "").replace(" ", "_") + ".txt"] = "\n".join(lines) + "\n"
    return files


def main() -> int:
    files = dump(openpyxl.load_workbook(TEMPLATE))
    if "--check" in sys.argv:
        stale = [name for name, text in files.items() if not (OUT / name).exists() or (OUT / name).read_text() != text]
        stale += [p.name for p in OUT.glob("*.txt") if p.name not in files]
        if stale:
            print("template-dump/ is stale for: " + ", ".join(sorted(stale)) + "\nRun: python dump_template.py")
            return 1
        print("template-dump/ is up to date")
        return 0
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.txt"):
        old.unlink()
    for name, text in files.items():
        (OUT / name).write_text(text)
    print(f"Wrote {len(files)} files to {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
