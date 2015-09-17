from textwrap import dedent
import os
import sys
from os.path import join, isdir
from shutil import copy2


def mod2name(mod):
    name = mod.split("/")[-1]
    if "-" in name:
        parts = name.split("-")
        name = parts[0] + "".join([part.title() for part in parts[1:]])
    return name


def fixit(content):
    content = dedent(content)
    final = []
    modules = []
    exporting = False
    exporters = []

    pre = " " * 8

    for line in content.splitlines():
        if exporting:
            exporters.append(pre + line)
        else:
            if line.startswith("import "):
                parts = line.split()
                assert len(parts) in [2, 4], "sytnax error"
                mod = parts[1]
                name = mod2name(mod)
                if len(parts) == 4:
                    assert parts[2] == "as", "syntax error"
                    name = parts[3]
                modules.append((name, mod))
            elif line.startswith("export"):
                exporting = True
                exporters.append(line.split(None, 1)[1])
            else:
                final.append(pre + line)

    return (
        dedent(
            """
                define(
                    [%s],
                    function(%s){
                        %s
                        return %s
                    }
                )
            """
        ) % (
            ", ".join('"%s"' % m[1] for m in modules),
            ", ".join('%s' % m[0] for m in modules),
            ("\n".join(final)).strip(),
            ("\n".join(exporters)).strip()
        )
    ).strip() + "\n"


def fix_file(src, dst):
    if src == "-":
        src = sys.stdin.read()
    else:
        src = open(src, "rt").read()

    content = fixit(src)

    if dst == "-":
        sys.stdout.write(content)
    else:
        dstf = open(dst, "w+")
        dstf.write(content)
        dstf.close()


def fix_dir(src, dst):
    if not isdir(dst):
        os.makedirs(dst)
    for root, dirs, files in os.walk(src):
        for fname in files:
            ffname = join(root, fname)
            dfname = join(dst, root[len(src)+1:], fname)
            if fname.endswith(".js"):
                fix_file(ffname, dfname)
            else:
                copy2(ffname, dfname)
        for dname in dirs:
            dfname = join(dst, root[len(src)+1:], dname)
            if not isdir(dfname):
                os.makedirs()
