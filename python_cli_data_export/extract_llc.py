from __future__ import annotations

import click
import json
from xmitgcm import llcreader
from os.path import abspath, expanduser, expandvars
from os import PathLike
from typing import List, Union

MODEL_LLC2160 = 'llc2160'
MODEL_LLC4320 = 'llc4320'


def _expand_path(path: str) -> str:
    """
    :path: A path on the filesystem.
    :return: An expanded path
    """
    # expanduser -> expands "~" i.e., user's home directory
    # expandvars -> expands environment variables like $HOME
    # abspath -> expands a relative path to an absolute path
    return abspath(expanduser(expandvars(path)))


def extract_llc(model_name: Union(MODEL_LLC2160, MODEL_LLC4320),
                varnames: List[str],
                klevel: List[int],
                iter: List[int],
                path: str | PathLike,
                facen: List[int],
                istart: int,
                iend: int,
                jstart: int,
                jend: int,
                fdepth: bool,
                verbose: bool):
    if model_name == MODEL_LLC2160:
        model = llcreader.PleiadesLLC2160Model()
    elif model_name == MODEL_LLC4320:
        model = llcreader.PleiadesLLC4320Model()
    else:
        raise ValueError(f"Invalid model {model_name}")

    if fdepth:
        ds = model.get_dataset(varnames=varnames, iters=iter,
                               k_levels=klevel, read_grid=False)
    else:
        ds = model.get_dataset(varnames=varnames, iters=iter, read_grid=False)

    if verbose:
        print(ds)

    print(path)
    ds_sel = ds.sel(face=facen)
    ds_isel = ds_sel.isel(i=slice(istart, iend),
                          i_g=slice(istart, iend),
                          j=slice(jstart, jend),
                          j_g=slice(jstart, jend))
    ds_isel.to_netcdf(path)


@click.command()
@click.option('--model_name', default=MODEL_LLC4320, help='Model type')
@click.option('--variables', default='["Eta"]', help='Variable to open. Has to be a pair for 2D vectors.')
@click.option('--klevel', default='[0]', help='Vertical level num')
@click.option('--iter', default='[92160]', help='Iteration number')
@click.option('--out_dir', default='./', help='Output Dir')
@click.option('--facen', default='[1]', help='Face')
@click.option('--istart', default='1080', help='Start of i indices to cut out')
@click.option('--iend', default='3240', help='End of i indices to cut out')
@click.option('--jstart', default='0', help='Start of j indices to cut out')
@click.option('--jend', default='2160', help='End of j indices to cut out')
@click.option('--fdepth', default='n', help='Output view of xarray.')
@click.option('--verbose', default='n', help='Output view of xarray')
def main(model_name, variables, klevel, iter, out_dir, facen, istart, iend, jstart, jend, fdepth, verbose):
    """ Program to read some llc data and output netcdf file.
    Take all inputs as strings, or lists as '["var1","var2"]' """
    varnames = json.loads(variables)
    klevel = json.loads(klevel)
    iter = json.loads(iter)  # need to look at model.iter_* to figure these out
    istart = json.loads(istart)
    iend = json.loads(iend)
    jstart = json.loads(jstart)
    jend = json.loads(jend)
    facen = json.loads(facen)
    is_fdepth = True if fdepth.lower() == "y" else False
    is_verbose = True if verbose.lower() == "y" else False

    # Construct a filename based on arguments
    var_names = '-'.join(vars for vars in varnames)
    k_names = '-'.join(str(klev) for klev in klevel)
    fname = f'{model_name}_'+var_names+'_k'+k_names+f'_iter_{iter[0]}.nc'
    expanded_path = _expand_path(out_dir+fname)

    extract_llc(model_name=model_name,
                varnames=varnames,
                klevel=klevel,
                iter=iter,
                path=expanded_path,
                facen=facen,
                istart=istart,
                iend=iend,
                jstart=jstart,
                jend=jend,
                fdepth=is_fdepth,
                verbose=is_verbose)


if __name__ == '__main__':
    main()
