from pathlib import Path
from typing import Final

import typer
from beni import bfile, bpath, btask
from beni.bcolor import printGreen, printMagenta, printYellow
from beni.bfunc import syncCall

app: Final = btask.newSubApp('code 工具')


@app.command()
@syncCall
async def tidy_tasks(
    tasks_path: Path = typer.Argument(Path.cwd(), help="tasks 路径"),
):
    '整理 task 项目中的 tasks/__init__.py'

    initFile = tasks_path / '__init__.py'
    btask.assertTrue(initFile.is_file(), '文件不存在', initFile)
    files = bpath.listFile(tasks_path)
    files = [x for x in files if not x.name.startswith('_')]
    contents = [f'from . import {x.stem}' for x in files]
    contents.insert(0, '# type: ignore')
    contents.append('')
    content = '\n'.join(contents)
    oldContent = await bfile.readText(initFile)
    if oldContent != content:
        await bfile.writeText(
            initFile,
            content,
        )
        printYellow(initFile)
        printMagenta(content)
    printGreen('OK')


@app.command()
@syncCall
async def tidy_modules(
    modules_path: Path = typer.Argument(Path.cwd(), help="modules_path 路径"),
):
    '整理 fastapi 项目中的 modules/__init__.py'

    importContents: list[str] = []
    managerContents: list[str] = []

    xxdict: dict[str, set[Path]] = {}
    for file in sorted(modules_path.glob('**/*Manager.py')):
        if file.parent == modules_path:
            subName = '.'
        elif file.parent.parent == modules_path:
            subName = f'.{file.parent.stem}'
        else:
            continue
        xxdict.setdefault(subName, set()).add(file)
    for subName in sorted(xxdict.keys()):
        files = sorted(xxdict[subName])
        importContents.append(f'from {subName} import {", ".join([x.stem for x in files])}')
    managerContents.extend([f'    {x.stem},' for x in sorted([y for x in xxdict.values() for y in x])])

    managerContents = [x for x in managerContents if x]
    contents = [
        '\n'.join(importContents),
        'managers = [\n' + '\n'.join(managerContents) + '\n]',
    ]
    content = '\n\n'.join(contents) + '\n'
    file = modules_path / '__init__.py'
    printYellow(str(file))
    printMagenta(content)
    await bfile.writeText(file, content)
    printGreen('OK')


@app.command()
@syncCall
async def gen_init_py(
    workspace_path: Path = typer.Argument(Path.cwd(), help='workspace 路径'),
):
    '递归生成 __init__.py 文件'

    async def makeInitFiles(p: Path):
        if p.name == '__pycache__':
            return
        if p.name.startswith('.'):
            return
        if workspace_path != p:
            initFile = p / '__init__.py'
            if not initFile.exists():
                printYellow(initFile)
                await bfile.writeText(initFile, '')
        for x in bpath.listDir(p):
            await makeInitFiles(x)

    await makeInitFiles(workspace_path)
    printGreen('OK')
