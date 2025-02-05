from pathlib import Path
from typing import Iterable

import pandas as pd
from click import command

from .lists import get_list_path
from ..core.arg import (CMD_LISTPOS,
                        arg_input_path,
                        opt_complement,
                        opt_max_fmut_pos,
                        opt_force,
                        opt_max_procs)
from ..core.run import run_func
from ..core.seq import FIELD_REF, POS_NAME
from ..core.task import as_list_of_tuples, dispatch
from ..core.write import need_write
from ..core.table import MUTAT_REL, PositionTable
from ..graph.table import load_pos_tables


def find_pos(table: PositionTable,
             max_fmut_pos: float,
             complement: bool):
    # Initially select all unmasked positions.
    region = table.region.copy()
    positions = region.unmasked_int
    # Apply each filter.
    region.add_mask(
        "max_fmut_pos",
        positions[table.fetch_ratio(rel=MUTAT_REL,
                                    exclude_masked=True,
                                    squeeze=True)
                  > max_fmut_pos],
        complement=complement
    )
    return region.unmasked_int


def list_pos(table: PositionTable, force: bool, **kwargs):
    """ List positions meeting specific criteria from the table. """
    list_file = get_list_path(table)
    if need_write(list_file, force):
        positions = pd.MultiIndex.from_product(
            [[table.ref], find_pos(table, **kwargs)],
            names=[FIELD_REF, POS_NAME]
        )
        positions.to_frame(index=False).to_csv(list_file, index=False)
    return list_file


@run_func(CMD_LISTPOS)
def run(input_path: Iterable[str | Path], *,
        max_fmut_pos,
        complement: bool,
        force: bool,
        max_procs: int) -> list[Path]:
    """ List positions meeting specific criteria from each table. """
    # Find the positional table files.
    tables = load_pos_tables(input_path)
    # List positions for each table.
    return dispatch(list_pos,
                    max_procs,
                    pass_n_procs=False,
                    args=as_list_of_tuples(tables),
                    kwargs=dict(max_fmut_pos=max_fmut_pos,
                                complement=complement,
                                force=force))


params = [
    # Input files
    arg_input_path,
    # Selection
    opt_max_fmut_pos,
    opt_complement,
    # Effort
    opt_force,
    # Parallelization
    opt_max_procs,
]


@command(CMD_LISTPOS, params=params)
def cli(*args, **kwargs):
    """ List positions meeting specific criteria. """
    return run(*args, **kwargs)
