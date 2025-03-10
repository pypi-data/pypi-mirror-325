from pathlib import Path
from typing import Final

import typer
from beni import bcolor, binput, bpath, btask
from beni.bfunc import syncCall

from ..common.func import useResources
from .venv import add as venvAdd

app: Final = btask.app


@app.command('project')
@syncCall
async def _(
    path: Path = typer.Option(Path.cwd(), '--path', help='workspace 路径'),
):
    '生成新项目'

    # 检查目标路径是否合法
    if path.exists():
        if not path.is_dir():
            bcolor.printRed('目标路径不是一个目录', path)
            return
        elif list(bpath.get(path).glob('*')):
            bcolor.printRed('目标路径不是空目录', path)
            return

    bcolor.printYellow(path)
    await binput.confirm('即将在此路径生成新项目，是否继续？')
    venvAdd(['benimang'], path)
    with useResources('project') as sourceProjectPath:
        bpath.copyOverwrite(sourceProjectPath, path)
