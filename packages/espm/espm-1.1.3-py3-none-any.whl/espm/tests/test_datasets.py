from espm.datasets.eds_spim import get_metadata
import numpy as np
from espm.datasets.base import generate_dataset, generate_spim_sample, sample_to_EDSespm, generate_spim
from espm.models import EDXS
from espm.models.generate_EDXS_phases import generate_brem_params, generate_random_phases, unique_elts
import os
import hyperspy.api as hs
import shutil
from espm.conf import DATASETS_PATH
from pathlib import Path
from exspy.utils.eds import take_off_angle
import espm.weights.generate_weights as wts
from espm.weights.generate_weights import generate_weights
from espm.models.EDXS_function import elts_list_from_dict_list
from espm.models.generate_EDXS_phases import generate_modular_phases
from espm.estimators import SmoothNMF

elts_dicts = [{"Fe" : 0.54860348,
               "Pt" : 0.38286879,
               "Mo" : 0.03166235,
               "O" : 0.03686538},
               {"Ca" : 0.54860348,
                "Si" : 0.38286879,
                "O" : 0.15166235},
                {"Cu" : 0.34,
                 "Mo" : 0.12,
                 "Au" : 0.54}]

brstlg_pars = [{"b0" : 5e-3,
                  "b1" : 3e-2},
                 {"b0" : 7e-3,
                    "b1" : 5e-2},
                    {"b0" : 3e-3,
                    "b1" : 5e-2}]

scales = [0.05, 0.05, 0.05]

model_params = {"e_offset" : 0.2,
                "e_size" : 1900,
                "e_scale" : 0.01,
                "width_slope" : 0.01,
                "width_intercept" : 0.065,
                "db_name" : "200keV_xrays.json",
                "E0" : 200,
                "params_dict" : {
                    "Abs" : {
                        "thickness" : 100.0e-7,
                        "toa" : 35,
                        "density" : 5
                    },
                    "Det" : "SDD_efficiency.txt"
                }}  

misc_params = {"N" : 400,
                "densities" : [1.3,1.6,1.9],
                "data_folder" : "test_gen_data",
                "seed" : 42,
                "shape_2d" : (100,120),
                "model" : "EDXS"}

elements = elts_list_from_dict_list(elts_dicts)

def test_generate():

    # Generate the phases
    model = EDXS(**model_params)
    model.generate_g_matr(g_type = "bremsstrahlung", elements=elements, elements_dict = {})
    phases1 = generate_modular_phases(elts_dicts = elts_dicts, brstlg_pars =  brstlg_pars, scales = scales, model_params = model_params)
    G = model.G
    n_phases = len(elts_dicts)
    maps = generate_weights(weight_type='sphere', shape_2d= misc_params["shape_2d"], n_phases=n_phases, seed=misc_params["seed"], radius = 15)
    densities = np.array(misc_params["densities"])
    spim_sample = generate_spim_sample(phases1,maps,model_params=model_params, misc_params=misc_params)
    spim = spim_sample["X"]
    cont_spim = spim_sample["Xdot"]
    Xdot = misc_params["N"]* maps @ np.diag(densities)@ phases1
    W = np.abs(np.linalg.lstsq(G,spim.sum(axis = (0,1)),rcond = None)[0])
    
    assert phases1.shape == (3, 1900)
    assert maps.shape == (100,120,3)
    assert spim.shape == (100,120,1900)
    np.testing.assert_allclose(np.sum(phases1, axis=1), np.ones([3]))
    np.testing.assert_allclose( Xdot, cont_spim)
    np.testing.assert_allclose( Xdot.sum(axis=(0,1)), G@W, rtol = 0.1 )

    if os.path.exists("test.hspy"):
        os.remove("test.hspy")
    filename = "test.hspy"
    hspy_spim = sample_to_EDSespm(spim_sample,elements=elements)
    hspy_spim.save(filename)
    si = hs.load(filename)
    assert si.metadata.Signal.signal_type == "EDS_espm_Simulated"
    si.build_G(problem_type = "bremsstrahlung")
    G = si.G
    phases, maps = si.phases, si.maps_2d
    # weights = weights.reshape((100,120,n_phases))
    X = si.data
    W = np.linalg.lstsq(G,X.sum(axis = (0,1)),rcond = None)[0]
    
    assert phases.shape == (1900, 3)
    assert maps.shape == (100,120,3)
    assert si.data.shape == (100,120,1900)
    np.testing.assert_allclose( Xdot, maps @ phases.T)
    np.testing.assert_allclose( Xdot.sum(axis=(0,1)), G@W, rtol = 0.2 )

    os.remove(filename)

    if os.path.exists(str(DATASETS_PATH / Path(misc_params["data_folder"]))):
        shutil.rmtree(str(DATASETS_PATH / Path(misc_params["data_folder"])))
    
    generate_dataset(base_seed=misc_params['seed'],
                    sample_number=2,
                    model_params = model_params,
                    misc_params = misc_params,
                    phases = phases1,
                    weights = maps,
                    elements = elements)
    gen_folder = DATASETS_PATH / Path(misc_params["data_folder"])
    gen_si = hs.load(gen_folder / Path("sample_0.hspy"))
    
    np.testing.assert_allclose(X,gen_si.data)

    shutil.rmtree(str(gen_folder))
    
def test_generate_spim():
     
    k = 3
    ell = 7
    shape_2d = [4,5]
    pd = 0.3
    seed = 0

    phases = np.random.rand(k, ell)
    weights = np.random.rand(*shape_2d, k)
    densities = 1 - pd + 2*pd*np.random.rand(k)

    # Ns = np.linspace(10, 200, 30)
    # vals = []
    # vals2 = []

    # for N in Ns:
    #     Xdot = generate_spim(phases, weights, densities, N, seed=seed,continuous = True)/N
    #     X = generate_spim(phases, weights, densities, N, seed=seed,continuous = False)/N
    #     X2 = np.random.poisson(N * Xdot) / N

    #     vals.append(np.mean(np.abs(X - Xdot)))
    #     vals2.append(np.mean(np.abs(X2 - Xdot)))
        
    # plt.plot(Ns, vals)
    # plt.plot(Ns, vals2)
    N = 10000
    X3 = np.zeros([*shape_2d, ell])
    for k, w in enumerate(densities):
        # generating the spectroscopic events
        for i in range(shape_2d[0]):
            for j in range(shape_2d[1]):
                # Draw a local_N based on the local density
                local_N = np.random.poisson(N * w * weights[i, j, k])
                # draw local_N events from the ideal spectrum
                counts = np.random.choice(
                    ell, local_N, p=phases[k]/np.sum(phases[k])
                )
                # Generate the spectrum based on the drawn events
                hist = np.bincount(counts, minlength=ell)
                X3[i, j] += hist

    
    Xdot = generate_spim(phases, weights, densities, N, seed=seed,continuous = True)/N
    X = generate_spim(phases, weights, densities, N, seed=seed,continuous = False)/N
    # X2 = np.random.poisson(N * Xdot) / N

    X3 /= N
    assert ( np.mean(np.abs(X - Xdot)) < 0.005)
    assert ( np.mean(np.abs(X3 - Xdot)) < 0.005)
    assert ( np.mean(np.abs(X - X3)) < 0.006)



def test_generate_random_weights():
    shape_2d = [28, 36]
    n_phases = 5
    
    w = wts.random_weights(shape_2d=shape_2d, n_phases=n_phases)
    
    assert(w.shape == (*shape_2d, n_phases))
    np.testing.assert_array_less(-1e-30, w)
    np.testing.assert_array_almost_equal(np.sum(w, axis=2), 1)

def test_generate_laplacian_weights():
    shape_2d = [28, 36]
    n_phases = 5
    
    w = wts.laplacian_weights(shape_2d=shape_2d, n_phases=n_phases)
    
    assert(w.shape == (*shape_2d, n_phases))
    np.testing.assert_array_less(-1e-30, w)
    np.testing.assert_array_almost_equal(np.sum(w, axis=2), 1)
    
def test_generate_two_sphere():
    shape_2d = [80, 80]
    n_phases = 3
    radius = 2
    
    w = wts.spheres_weights(shape_2d=shape_2d, n_phases=n_phases, radius= radius)
    
    assert(w.shape == (80, 80, 3))
    np.testing.assert_array_less(-1e-30, w)
    np.testing.assert_array_almost_equal(np.sum(w, axis=2), 1)

def test_generate_gaussian_ripple() : 
    shape_2d = [100,40]
    width = 10
    
    w = wts.gaussian_ripple_weights(shape_2d, width = width)

    assert(w.shape == (100,40,2))
    np.testing.assert_array_less(-1e-30,w)
    np.testing.assert_array_almost_equal(np.sum(w,axis = 2), 1)

# def test_gen_EDXS () : 
    
#     b_dict = generate_brem_params(42)
#     assert b_dict["b0"] <= 1.0 
#     assert b_dict["b1"] <= 1.0

#     phases, dicts = generate_random_phases(n_phases=3,seed = 42)
#     np.testing.assert_array_less(-1e-30, phases)
#     model = EDXS(**DEFAULT_SYNTHETIC_DATA_DICT["model_parameters"])
#     model.generate_phases(dicts)
#     np.testing.assert_almost_equal(model.phases,phases)

#     unique_list = unique_elts(dicts)
#     assert len(unique_list) == len(set(unique_list))

def test_decomposition () :
    if os.path.exists(str(DATASETS_PATH / Path(misc_params["data_folder"]))):
        shutil.rmtree(str(DATASETS_PATH / Path(misc_params["data_folder"])))

    phases1 = generate_modular_phases(elts_dicts = elts_dicts, brstlg_pars =  brstlg_pars, scales = scales, model_params = model_params)
    maps = generate_weights(weight_type='sphere', shape_2d= misc_params["shape_2d"], n_phases=len(elts_dicts), seed=misc_params["seed"], radius = 15)
    generate_dataset(base_seed=misc_params['seed'],
                    sample_number=2,
                    model_params = model_params,
                    misc_params = misc_params,
                    phases = phases1,
                    weights = maps,
                    elements = elements)

    gen_folder = DATASETS_PATH / Path(misc_params["data_folder"])
    gen_si = hs.load(gen_folder / Path("sample_0.hspy"))
    gen_si.change_dtype("float64")
    gen_si.build_G()
    est = SmoothNMF(n_components=3, G = gen_si.model, tol = 1e-7, hspy_comp = True)
    gen_si.decomposition(algorithm = est)
    assert gen_si.metadata.Signal.signal_type == "EDS_espm_Simulated"
    np.testing.assert_allclose((est.G_@est.W_@est.H_).sum(axis = 1), gen_si.X.sum(axis = 1), rtol = 0.5)
    indices = gen_si.model.NMF_simplex()
    np.testing.assert_allclose(est.W_[indices,:].sum(axis = 0), np.ones(3), rtol = 0.1)

    shutil.rmtree(str(gen_folder))

def test_spim () : 

    if os.path.exists(str(DATASETS_PATH / Path(misc_params["data_folder"]))):
        shutil.rmtree(str(DATASETS_PATH / Path(misc_params["data_folder"])))
    phases1 = generate_modular_phases(elts_dicts = elts_dicts, brstlg_pars =  brstlg_pars, scales = scales, model_params = model_params)
    maps = generate_weights(weight_type='sphere', shape_2d= misc_params["shape_2d"], n_phases=len(elts_dicts), seed=misc_params["seed"], radius = 15)
    generate_dataset(base_seed=misc_params['seed'],
                    sample_number=2,
                    model_params = model_params,
                    misc_params = misc_params,
                    phases = phases1,
                    weights = maps,
                    elements = elements)
    gen_folder = DATASETS_PATH / Path(misc_params["data_folder"])
    gen_si = hs.load(gen_folder / Path("sample_0.hspy"))

    assert gen_si.metadata.Signal.signal_type == "EDS_espm_Simulated"

    mod_pars = get_metadata(gen_si)
    # mod_pars["params_dict"]["Abs"]["atomic_fraction"] = False

    assert model_params == mod_pars

    shape = gen_si.shape_2d
    gen_si = hs.load(gen_folder / Path("sample_0.hspy"))
    gen_si.build_G(problem_type = "identity")
    assert shape == (100,120)
    assert gen_si.G is None
    
    gen_si = hs.load(gen_folder / Path("sample_0.hspy"))
    gen_si.build_G(problem_type = "no_brstlg",elements_dict = {}, ignored_elements = [])
    assert gen_si.G.shape == (1900, 8)
    
    gen_si = hs.load(gen_folder / Path("sample_0.hspy"))
    gen_si.build_G(problem_type = "bremsstrahlung",elements_dict = {}, ignored_elements = [])
    assert gen_si.G.shape == (1900, 10)
    
    Xflat = gen_si.X
    assert Xflat.shape == (1900, 120*100)

    gen_si = hs.load(gen_folder / Path("sample_0.hspy"))
    gen_si.build_G(problem_type = "bremsstrahlung",elements_dict = {"26" : 3.0}, ignored_elements = [])
    assert gen_si.G.shape == (1900, 11)

    gen_si = hs.load(gen_folder / Path("sample_0.hspy"))
    gen_si.build_G(problem_type = "no_brstlg",elements_dict = {"26" : 3.0}, ignored_elements = [])
    assert gen_si.G.shape == (1900, 9)

    gen_si = hs.load(gen_folder / Path("sample_0.hspy"))
    gen_si.build_G(problem_type = "bremsstrahlung",elements_dict = {"26" : 3.0}, ignored_elements = ['Cu'])
    assert gen_si.G.shape == (1900, 22)

    detector_dict = {
        "detection" : {
            "thickness" : 45,
            "elements_dict" : {
                "Si" : 3,
                "Se" : 4
            }
        },
        "layer1" : {
            "thickness" : 34,
            "elements_dict" : {
                "Ge" : 1,
                "O" : 3
            }
        }
    }

    gen_si.set_microscope_parameters(beam_energy = 100, azimuth_angle = 2.0, elevation_angle = 3.0, tilt_stage = 4.0 )
    gen_si.set_elements(elements = ["Si"])
    gen_si.metadata.Acquisition_instrument.TEM.Stage.tilt_beta = 0.0

    gen_si.set_analysis_parameters(thickness = 500e-7, density = 4, detector_type = detector_dict, width_slope = 0.3, width_intercept = 65.0, xray_db = "100keV_xrays.json")

    assert gen_si.metadata.Sample.thickness == 500e-7
    assert gen_si.metadata.Sample.density == 4
    assert gen_si.metadata.Sample.elements == ["Si"]
    assert gen_si.metadata.xray_db == "100keV_xrays.json"
    assert gen_si.metadata.Acquisition_instrument.TEM.Stage.tilt_alpha == 4.0
    assert gen_si.metadata.Acquisition_instrument.TEM.beam_energy == 100
    assert gen_si.metadata.Acquisition_instrument.TEM.Detector.EDS.take_off_angle == take_off_angle(4.0,2.0,3.0)
    assert gen_si.metadata.Acquisition_instrument.TEM.Detector.EDS.type.as_dictionary() == detector_dict
    assert gen_si.metadata.Acquisition_instrument.TEM.Detector.EDS.width_slope == 0.3
    assert gen_si.metadata.Acquisition_instrument.TEM.Detector.EDS.width_intercept == 65.0

    shutil.rmtree(str(gen_folder))


def test_carto_fixed_W() :

    def create_data()  : 
        a = np.random.rand(50,70,100)
        s = hs.signals.Signal1D(a)
        s.axes_manager[-1].offset = 0.2
        s.axes_manager[-1].scale = 0.1
        s.set_signal_type("EDS_espm")
        s.add_elements(elements = ["Si","O","Fe","Ca"])
        s.set_microscope_parameters(beam_energy = 100, azimuth_angle = 2.0, elevation_angle = 3.0, tilt_stage = 4.0 )
        s.metadata.Acquisition_instrument.TEM.Stage.tilt_beta = 0.0
        s.set_analysis_parameters(thickness = 500e-7, density = 4, detector_type = 'SDD_efficiency.txt', width_slope = 0.3, width_intercept = 65.0, xray_db = "100keV_xrays.json")
        return s
     
    s = create_data()
    s.build_G(problem_type = "bremsstrahlung",ignored_elements = [])
    fw1 = s.carto_fixed_W(brstlg_comps = 2)
    tw1_1 = np.diag(-1* np.ones(4))
    tw1_2 = np.zeros((2,4))
    tw1_prime = np.vstack((tw1_1,tw1_2))
    tw1_3 = np.zeros((4,2))
    tw1_4 = -1*np.ones((2,2))
    tw1_second = np.vstack((tw1_3,tw1_4))
    tw1 = np.hstack((tw1_prime,tw1_second))

    assert(fw1.shape == (6,6))
    np.testing.assert_array_equal(fw1,tw1)

    s = create_data()
    s.build_G(problem_type = "no_brstlg", ignored_elements = [])
    fw2 = s.carto_fixed_W()
    tw2 = np.diag(-1* np.ones(4))

    assert(fw2.shape == (4,4))
    np.testing.assert_array_equal(fw2,tw2)

    s = create_data()
    s.build_G(problem_type = "no_brstlg", elements_dict = {"26" : 3.0}, ignored_elements = [])
    fw3 = s.carto_fixed_W()
    tw3 = np.diag(-1* np.ones(5))

    assert(fw3.shape == (5,5))
    np.testing.assert_array_equal(fw3,tw3)

def test_set_fixed_W() : 
    def create_data()  : 
        a = np.random.rand(50,70,100)
        s = hs.signals.Signal1D(a)
        s.axes_manager[-1].offset = 0.2
        s.axes_manager[-1].scale = 0.1
        s.set_signal_type("EDS_espm")
        s.add_elements(elements = ["Si","O","Fe","Ca"])
        s.set_microscope_parameters(beam_energy = 100, azimuth_angle = 2.0, elevation_angle = 3.0, tilt_stage = 4.0 )
        s.metadata.Acquisition_instrument.TEM.Stage.tilt_beta = 0.0
        s.set_analysis_parameters(thickness = 500e-7, density = 4, detector_type = 'SDD_efficiency.txt', width_slope = 0.3, width_intercept = 65.0, xray_db = "100keV_xrays.json")
        return s
    
    s = create_data()
    s.build_G(problem_type = "bremsstrahlung", ignored_elements = [])
    fw1 = s.set_fixed_W({'p0' : {"Si" : 0.0, 'O' : 0.5, 'b1' : 10.0},'p1' : {}, 'p2' : {'O' : 0.4, 'Fe' : 0.6, 'b0' : 3.0} })
    tw1 = (np.array([[-1.0, -1.0, 0.5, 0.0, -1.0, 10.0],
                [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0],
                [-1.0, 0.6, 0.4, -1.0, 3.0, -1.0]])).T
    assert(fw1.shape == (6,3))
    np.testing.assert_array_equal(fw1,tw1)

    s = create_data()
    s.build_G(problem_type = "no_brstlg", elements_dict = {"Fe" : 3.0}, ignored_elements = [])
    fw2 = s.set_fixed_W({'p0' : {"Si" : 0.0, 'O' : 0.5},'p1' : {}, 'p2' : {'O' : 0.4, 'Fe' : 0.6} })
    tw2 = (np.array([[-1.0, -1.0, -1.0, 0.5,0.0],
                [-1.0, -1.0, -1.0, -1.0, -1.0],
                [-1.0, -1.0, 0.6, 0.4, -1.0]])).T
    
    assert(fw2.shape == (5,3))
    np.testing.assert_array_equal(fw2,tw2)
        
    s = create_data()
    s.build_G(problem_type = "bremsstrahlung", ignored_elements = ['Cu'])
    fw3 = s.set_fixed_W({'p0' : {"Si" : 0.0, 'O' : 0.5, 'b1' : 10.0},'p1' : {}, 'p2' : {'O' : 0.4, 'Fe' : 0.6, 'b0' : 3.0} })
    tw3 = (np.array([[-1.0,-1.0, 0.5, 0.0, -1.0, -1.0, -1.0, -1.0,-1.0, -1.0,-1.0, -1.0,-1.0, -1.0,-1.0, -1.0, 10.0],
                [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0,-1.0, -1.0,-1.0, -1.0,-1.0, -1.0,-1.0, -1.0,-1.0, -1.0, -1.0],
                [-1.0, 0.6, 0.4, -1.0, -1.0, -1.0, -1.0, -1.0,-1.0, -1.0,-1.0, -1.0,-1.0, -1.0,-1.0, 3.0, -1.0]])).T
    assert(fw1.shape == (6,3))
    np.testing.assert_array_equal(fw3,tw3)

def test_estimate_best_binning () : 
    pass
    # TODO : Implement this test


