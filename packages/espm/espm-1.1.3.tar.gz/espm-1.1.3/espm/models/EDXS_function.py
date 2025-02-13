r"""
EDXS functions
--------------

The :mod:`espm.models.EDXS_function` module implements misceallenous functions required for the :mod: `espm.models.edxs`.
This module include bremsstrahlung modelling, database reading and dicts and list manipulation functions.

"""

import numpy as np
from scipy.special import erfc
from espm.models.absorption_edxs import det_efficiency_from_curve,det_efficiency,absorption_correction
from espm.models import edxs as e
from collections import Counter
from espm.conf import SYMBOLS_PERIODIC_TABLE
import json

from espm.utils import number_to_symbol_list
    
def gaussian(x, mu, sigma):
    r"""
    Calculate the gaussian function according to the following formula:

    .. math::

        f(x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{(x-\mu)^2}{2 \sigma^2}}

    Parameters
    ----------
    x : np.array 1D
        Energy scale.
    mu : float
        Mean of the gaussian.
    sigma : float
        Standard deviation of the gaussian.
    
    Returns
    -------
    gaussian : np.array 1D
        Gaussian distribution on x, with mean mu and standard deviation sigma.
    """
    return (
        1
        / (sigma * np.sqrt(2 * np.pi))
        * np.exp(-np.power(x - mu, 2) / (2 * np.power(sigma, 2)))
    )

def read_lines_db (elt,db_dict) :
    r"""
    Read the energy and cross section of each line of a chemical element for explicit databases.
    
    Parameters
    ----------
    elt : 
        :string: Atomic number.
    db_dict : 
        :dict: Dictionnary extracted from the json database containing the emission lines and their energies.
    
    Returns
    -------
    energies : 
        :list float: List of energies associated to each emission line of the given element
    cross-sections : 
        :list float: List of emission cross-sections of each line of the given element
    """
    energies = []
    cs = []
    for line in db_dict[str(elt)] : 
        energies.append(db_dict[str(elt)][line]["energy"])
        cs.append(db_dict[str(elt)][line]["cs"])
    return energies, cs

def read_compact_db (elt,db_dict) :
    r"""
    Read the energy and cross section of each line of a chemical element for compact databases.
    
    Parameters
    ----------
    elt : 
        :string: Atomic number.
    db_dict : 
        :dict: Dictionnary extracted from the json database containing the emission lines and their energies.
    
    Returns
    -------
    energies : 
        :list float: List of energies associated to each emission line of the given element
    cross-sections : 
        :list float: List of emission cross-sections of each line of the given element
    """
    energies = db_dict[str(elt)]["energies"]
    cs = db_dict[str(elt)]["cs"] 
    return energies, cs

def chapman_bremsstrahlung(x, b0, b1, b2):
    r"""
    Calculate the bremsstrahlung as parametrized by chapman et al. 
    
    Parameters
    ----------
    x : 
        :np.array 1D: Energy scale.
    b0 : 
        :float: First parameter, corresponding to the inverse of the energy.
    b1 : 
        :float: Second parameter, corresponding to the energy.
    b2 : 
        :float: Third parameter, corresponding to the square of the energy.
    
    Returns
    -------
    bremsstrahlung : 
        :np.array 1D: Bremsstrahlung model

    Notes
    -----
    For details see :cite:p:`chapman1984understanding`
    """
    return b0 / x + b1 + b2 * x
    
def lifshin_bremsstrahlung(x, b0, b1, E0 = 200):
    r"""
    Calculate the custom parametrized bremsstrahlung inspired by the model of L.Lifshin.

    The model is designed to have the same definition set as the original model of L.Lifshin with :math:`b_0 > 0` and :math:`b_1 > 0`.

    The model is defined as follows:

    .. math::

        f(\varepsilon) = b_0 \frac{\varepsilon_0 - \varepsilon}{\varepsilon_0 \varepsilon} \left(1 - \frac{\varepsilon_0 - \varepsilon}{\varepsilon_0}\right) + b_1 \frac{\left( \varepsilon_0 - \varepsilon \right) ^2}{\varepsilon_0^2 \varepsilon}

    where :math:`\varepsilon_0` is the energy of the incident beam, :math:`\varepsilon` is the energy of the emitted photon and :math:`b_0` and :math:`b_1` are the parameters of the model.    
    
    Parameters
    ----------
    x : 
        :np.array 1D: Energy scale.
    b0 : 
        :float: First parameter.
    b1 : 
        :float: Second parameter.
    E0 : 
        :float: Energy of the incident beam in keV.
    
    Returns
    -------
    bremsstrahlung : 
        :np.array 1D: Bremsstrahlung model
        
    Notes
    -----
    For details see L.Lifshin, Ottawa, Proc.9.Ann.Conf.Microbeam Analysis Soc. 53. (1974)
    """
    lbb0 = lifshin_bremsstrahlung_b0(x,b0,E0)
    lbb1 = lifshin_bremsstrahlung_b1(x,b1,E0)
    return lbb0 + lbb1

def lifshin_bremsstrahlung_b0(x, b0, E0 = 200):
    r"""
    Calculate the first part of our bremsstrahlung model.
    """
    assert np.inf not in 1/x, "You have 0.0 in your energy scale. Retry with a cropped energy scale"
    # return b0*((E0 - x)/x - np.power(E0 - x, 2)/(E0*x))
    return b0*(E0 -x)/(E0*x)*(1 - (E0 - x)/E0)

def lifshin_bremsstrahlung_b1(x, b1, E0 = 200):
    r"""
    Calculate the second part of our bremsstrahlung model.
    """
    assert np.inf not in 1/x, "You have 0.0 in your energy scale. Retry with a cropped energy scale"
    return b1*np.power((E0 - x),2)/(E0*E0*x)

def shelf(x, height, length):
    r"""
    Calculate the shelf contribution of the EDXS Silicon Drift Detector (SDD) detector.

    Parameters
    ----------
    x : 
        :np.array 1D: Energy scale.
    height : 
        :float: Height in intensity of shelf contribution of the detector.
    length : 
        :float: Length in energy of shelf contribution of the detector.
    
    Returns
    -------
    shelf : 
        :np.array 1D: SDD shelf model.
        
    Notes
    -----
    For details see :cite:p:`scholze2009modelling`
    """
    return height * erfc(x - length)

def continuum_xrays(x,params_dict={},b0= 0, b1 = 0, E0 = 200,*,elements_dict = {"Si" : 1.0} ):
    r"""
    Computes the continuum X-rays, i.e. the bremsstrahlung multiplied by the absorption and the detection efficiency.

    Parameters
    ----------
    x : 
        :np.array 1D: Energy scale.
    params_dict : 
        :dict: Dictionnary containing the absorption and detection parameters.
    b0 : 
        :float: First parameter.
    b1 : 
        :float: Second parameter.
    E0 : 
        :float: Energy of the incident beam in keV.
    elements_dict : 
        :dict: Composition of the studied sample. It is required for absorption calculation.
    
    Returns
    -------
    continuum_xrays : 
        :np.array 1D: Continuum X-rays model.

    Notes
    -----
    * When an empty dict is provided. The continuum X-rays are set to 0. This is useful to perform calculations without the bremsstrahlung for example.
    * For an example structure of the params_dict parameter, check the DEFAULT_EDXS_PARAMS espm.conf.
    * For a custom detection efficiency, check the spectrum fit notebook.
    """
    if len(params_dict) == 0 : 
        return 0*x
    
    B = lifshin_bremsstrahlung(
            x,
            b0 = b0,
            b1 = b1,
            E0 = E0
        )

    A = absorption_correction(x,**params_dict["Abs"],elements_dict=elements_dict)

    if type(params_dict["Det"]) == str : 
        D = det_efficiency_from_curve(x,params_dict["Det"])
    else : 
        D = det_efficiency(x,params_dict["Det"])

    return B * A * D 

def G_bremsstrahlung(x,E0,params_dict,*,elements_dict = {}):
    r"""
    Computes the two-parts continuum X-rays for the G matrix. The two parts of the bremsstrahlung are constructed separately so that its parameters can fitted to data.
    Absorption and detection are multiplied to each part. 

    Parameters
    ----------
    x : 
        :np.array 1D: Energy scale.
    params_dict : 
        :dict: Dictionnary containing the absorption and detection parameters.
    elements_dict : 
        :dict: Composition of the studied sample. It is required for absorption calculation.
    
    Returns
    -------
    continuum_xrays : 
        :np.array 2D: Two parts continuum X-rays model with shape (energy scale size, 2).
    """
    A = absorption_correction(x,**params_dict["Abs"],elements_dict= elements_dict)
    
    if type(params_dict["Det"]) == str : 
        D = det_efficiency_from_curve(x,params_dict["Det"])
    else : 
        D = det_efficiency(x,params_dict["Det"])

    B0 = A*D*lifshin_bremsstrahlung_b0(
            x,
            b0 = 1,
            E0 = E0
        )

    B1 = A*D*lifshin_bremsstrahlung_b1(
        x,
        b1=1,
        E0 = E0
    )

    B = np.vstack((B0,B1)).T
    
    return B

# @number_to_symbol_list    
# def elts_dict_from_W (part_W,*,elements = []) : 
#     r"""
#     Create a dictionnary of the elemental concentration from a fitted W. It useful to recompute absorption during the our custom NMF calculations.

#     Parameters
#     ----------
#     part_W : 
#         :np.array 2D: W matrix output from the NMF calculation. It only makes sense when the NMF decomposition if performed with G.
#     elements : 
#         :list: List of elements as atomic number or symbol.

#     Returns
#     -------
#     elements_dictionnary : 
#         :dict: Dictionnary containing the concentration associated to each chemical element of the problem.
    
#     Examples
#     --------
#     >>> import numpy as np
#     >>> from espm.models.EDXS_function import elts_dict_from_W
#     >>> W = np.ones((4,3))
#     >>> elts = ["Si","Ca","O","C"]
#     >>> elts_dict_from_W(W,elements = elts)
#         {"Si" : 0.25, "Ca" : 0.25, "O" : 0.25, "C" : 0.25}

#     Notes
#     -----
#     This function should maybe move to another part of espm.
#     """
#     mask_zeros = np.sum(part_W,axis=0) != 0
#     norm_P = np.mean(part_W[:,mask_zeros] / part_W[:,mask_zeros].sum(axis = 0),axis=1)
#     elements_dict = {}
#     #with open(SYMBOLS_PERIODIC_TABLE,"r") as f : 
#     #    SPT = json.load(f)["table"]
#     for i,elt in enumerate(elements) :
#         elements_dict[elt] = norm_P[i] # * SPT[elt]["atomic_mass"]
#     factor =  sum(elements_dict.values())
#     return {key:elements_dict[key]/factor for key in elements_dict}

def elts_dict_from_dict_list (dict_list) : 
    r"""
    Create a single dictionnary of the elemental concentration from a list of dictionnary containing chemical compositions. The new dictionnary corresponds to the average chemical composition of the list.

    Parameters
    ----------
    dict_list : 
        :list [dict]: list of chemical composition dictionnary

    Returns
    -------
    elements_dictionnary : 
        :dict: Dictionnary containing the concentration associated to each chemical elements contained in the input.

    Examples
    --------
    >>> import numpy as np
    >>> from espm.models.EDXS_function import elts_dict_from_dict_list
    >>> dicts = [{"Si" : 1.0},{"Ca" : 1.0},{"O" : 1.0},{"C" : 1.0}]
    >>> elts_dict_from_dict_list(dicts)
        {"Si" : 0.25, "Ca" : 0.25, "O" : 0.25, "C" : 0.25}

    Notes
    -----
    This function should maybe move to another part of espm.
    """
    unique_elts_dict = sum((Counter(x) for x in dict_list),Counter())
    sum_elts = sum(unique_elts_dict.values())
    for e in unique_elts_dict : 
        unique_elts_dict[e] /= sum_elts
    return unique_elts_dict

def elts_list_from_dict_list (dict_list) :
    r"""
    Create a list of elements from a list of dictionnary containing chemical compositions. The list contains all the elements contained in the input.

    Parameters
    ----------
    dict_list :
        :list [dict]: list of chemical composition dictionnary

    Returns
    -------
    elements_list :
        :list: List of elements as atomic number or symbol.

    Examples
    --------
    >>> import numpy as np
    >>> from espm.models.EDXS_function import elts_list_from_dict_list
    >>> dicts = [{"Si" : 1.0, "C" : 0.5, "O" : 0.5},{"Ca" : 1.0, "K" : 2.0},{"O" : 1.0, "Si" : 0.5},{"C" : 1.0}] 
    >>> elts_list_from_dict_list(dicts)
        ["Si","Ca","O","C","K"]
    """ 
    unique_elts_dict = sum((Counter(x) for x in dict_list),Counter())
    return list(unique_elts_dict.keys())



