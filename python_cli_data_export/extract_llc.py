import click
import json
from xmitgcm import llcreader

@click.command()
@click.option('--model_name', default='llc4320', help='Model type')
@click.option('--variables', default='["Eta"]', help='Variable to open. Has to be a pair for 2D vectors.')
@click.option('--klevel', default='[0]', help='Vertical level num')
@click.option('--iter', default='[92160]', help='Iteration number')
@click.option('--out_dir', default='./', help='Output Dir')
def extract_llc(model_name, variables, klevel, iter, out_dir):

	if model_name=='llc2160':
		model = llcreader.PleiadesLLC2160Model()
	elif model_name=='llc4320':
		model = llcreader.PleiadesLLC4320Model()

	variable = json.loads(variables)
	klevel = json.loads(klevel)
	iter = json.loads(iter) # need to look at model.iter_* to figure these out


	ds = model.get_dataset(varnames=variable, iters=iter, k_levels=klevel, type='latlon', read_grid=False)

	print(ds)

	var_names = '-'.join(vars  for vars in variable)
	k_names = '-'.join(str(klev) for klev in klevel)
	fname=f'{model_name}_'+var_names+'_k'+k_names+f'_iter_{iter[0]}.nc'
	ds.to_netcdf(out_dir+fname)

if __name__ == '__main__':
    extract_llc()

