from textwrap import dedent


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

    return dedent(
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
        "\n".join(final),
        "\n".join(exporters)
    )


def fix_file(src, dst):
    pass


def fix_dir(src, dst):
    pass
