from collections.abc import Iterable
import os
from pathlib import Path
from subprocess import check_output
from typing import Annotated

from pydantic import Field
from typing_extensions import Unpack, override

from ..__base__ import CmdKw, Config, Line, Location, Producer, Substitution


class ExecConfig(Config):
    work_dir: Annotated[Path, Field(default_factory=Path)]
    env_vars: Annotated[dict[str, str], Field(default_factory=dict)]


class ExecCommand(Producer, name='exec'):
    conf: ExecConfig

    @override
    def __init__(self, args: str, *, conf: ExecConfig, **kw: Unpack[CmdKw]) -> None:
        super().__init__(args, conf=conf, **kw)
        commands = args.strip()
        if not commands:
            raise self.exc_invalid_args()
        self.commands = commands

    @override
    def produce(self, sub: Substitution) -> Iterable[Line]:
        try:
            result = check_output(
                args=['sh', '-c', self.commands],
                env=dict(os.environ) | self.conf.env_vars,
                text=True,
                cwd=self.conf.work_dir,
            )
        except Exception as exc:
            raise self.exc_runtime_error(self.commands) from exc

        for i, text in enumerate(result.splitlines()):
            line = Line(text=text, loc=Location('stdout', lineno=i))
            yield line
