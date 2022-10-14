from xmitgcm import llcreader
model = llcreader.PleiadesLLC2160Model()

# $ python -m export_llc --model "llc4320" --variable "THETA" --klevel 0 --timestep 90293 --output-dir /nobackup/dbalwada/llc_export

#model = 'llc2160'
variable = ['Eta']
klevel = [0]
iter = [92160] # need to look at model.iter_* to figure these out

output_dir = './'

ds = model.get_dataset(varnames=variable, iters=iter, k_levels=klevel, type='latlon', read_grid=False)

print(ds)
