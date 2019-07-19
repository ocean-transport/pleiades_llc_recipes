# quick tests that the pleaides datasets are readable with llcreader
# copied from https://github.com/xgcm/xmitgcm/blob/master/xmitgcm/test/test_llcreader.py

import pytest
from xmitgcm import llcreader

EXPECTED_VARS = ['Eta', 'KPPhbl', 'oceFWflx', 'oceQnet', 'oceQsw', 'oceSflux',
            'oceTAUX', 'oceTAUY', 'PhiBot', 'Salt', 'SIarea', 'SIheff',
            'SIhsalt', 'SIhsnow', 'SIuice', 'SIvice', 'Theta', 'U', 'V', 'W']


@pytest.fixture(scope='module', params=[2160, 4320])
def ecco_portal_model(request):
    if request.param==2160:
        return llcreader.PleiadesLLC2160Model()
    else:
        return llcreader.PleiadesLLC4320Model()

def test_ecco_portal_faces(ecco_portal_model):
    # just get three timesteps
    iter_stop = ecco_portal_model.iter_start + 2 * ecco_portal_model.iter_step + 1
    ds_faces = ecco_portal_model.get_dataset(iter_stop=iter_stop)
    nx = ecco_portal_model.nx
    assert ds_faces.dims == {'face': 13, 'i': nx, 'i_g': nx, 'j': nx,
                              'j_g': nx, 'k': 90, 'k_u': 90, 'k_l': 90,
                              'k_p1': 90, 'time': 3}
    assert set(EXPECTED_VARS) == set(ds_faces.data_vars)

def test_ecco_portal_load(ecco_portal_model):
    # an expensive test because it actually loads data
    iter_stop = ecco_portal_model.iter_start + 2 * ecco_portal_model.iter_step + 1
    ds_faces = ecco_portal_model.get_dataset(varnames=['Eta'], iter_stop=iter_stop)
    # a lookup table
    expected = {2160: -1.3054643869400024, 4320: -1.262018084526062}
    assert ds_faces.Eta[0, 0, -1, -1].values.item() == expected[ecco_portal_model.nx]

def test_ecco_portal_latlon(ecco_portal_model):
    iter_stop = ecco_portal_model.iter_start + 2 * ecco_portal_model.iter_step + 1
    ds_ll = ecco_portal_model.get_dataset(iter_stop=iter_stop, type='latlon')
    nx = ecco_portal_model.nx
    assert ds_ll.dims == {'i': 4*nx, 'k_u': 90, 'k_l': 90, 'time': 3,
                             'k': 90, 'j_g': 3*nx, 'i_g': 4*nx, 'k_p1': 90,
                             'j': 3*nx, 'face': 13}
    assert set(EXPECTED_VARS) == set(ds_ll.data_vars)

