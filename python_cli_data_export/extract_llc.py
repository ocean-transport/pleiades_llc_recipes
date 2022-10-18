import click
import json
from xmitgcm import llcreader

@click.command()
@click.option('--model_name', default='llc4320', help='Model type')
@click.option('--variables', default='["Eta"]', help='Variable to open. Has to be a pair for 2D vectors.')
@click.option('--klevel', default='[0]', help='Vertical level num')
@click.option('--iter', default='[92160]', help='Iteration number')
@click.option('--out_dir', default='./', help='Output Dir')
@click.option('--facen', default='[1]', help='Face')
@click.option('--istart', default='1080', help='Start of i indices to cut out')
@click.option('--iend', default='3240', help='End of i indices to cut out')
@click.option('--jstart', default='0', help='Start of j indices to cut out')
@click.option('--jend', default='2160', help='End of j indices to cut out')
@click.option('--verbose', default='n', help='Output view of xarray') 
def extract_llc(model_name, variables, klevel, iter, out_dir, facen, istart, iend, jstart, jend, verbose):
	""" Program to read some llc data and output netcdf file.
Take all inputs as strings, or lists as '["var1","var2"]' """
	if model_name=='llc2160':
		model = llcreader.PleiadesLLC2160Model()
	elif model_name=='llc4320':
		model = llcreader.PleiadesLLC4320Model()

	variable = json.loads(variables)
	klevel = json.loads(klevel)
	iter = json.loads(iter) # need to look at model.iter_* to figure these out

	ds = model.get_dataset(varnames=variable, iters=iter, k_levels=klevel, read_grid=False)

	if verbose=='y':
		print(ds)

	var_names = '-'.join(vars  for vars in variable)
	k_names = '-'.join(str(klev) for klev in klevel)
	fname=f'{model_name}_'+var_names+'_k'+k_names+f'_iter_{iter[0]}.nc'
	print(fname)
	facen=json.loads(facen)
	istart=json.loads(istart)
	iend=json.loads(iend)
	jstart=json.loads(jstart)
	jend=json.loads(jend)
	ds.sel(face=facen).isel(i=slice(istart,iend),j=slice(jstart,jend)).to_netcdf(out_dir+fname)

if __name__ == '__main__':
    extract_llc()

