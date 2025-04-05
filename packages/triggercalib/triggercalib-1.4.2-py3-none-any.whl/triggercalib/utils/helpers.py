###############################################################################
# (c) Copyright 2024-2025 CERN for the benefit of the LHCb Collaboration      #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################

from array import array
from ctypes import c_double
from typing import Annotated, Dict, List

import numpy as np
import ROOT as R
import uproot as up

from triggercalib.utils import core, typing

has_zfit = core.zfit_installed()
if has_zfit:
    import zfit


def bins_from_taxis(axis, as_array=False):
    """Extract bin edges from a ROOT TAxis object

    Args:
        axis: ROOT TAxis object to extract bins from
        as_array: Whether to return bins as a ROOT array

    Returns:
        list or array: List of bin edges or ROOT array of bin edges
    """
    bins = [axis.GetBinLowEdge(0)] + [
        axis.GetBinUpEdge(i) for i in range(1, axis.GetNbins() + 1)
    ]

    if as_array:
        return array("d", bins)
    return bins


def tgraph_to_th(graph, name="", title=""):
    """Convert a ROOT TGraph(2D)AsymmErrors to a TH1(2)D

    Args:
        graph: ROOT TGraph(2D)AsymmErrors to convert
        name: Optional name for output histogram
        title: Optional title for output histogram

    Returns:
        TH1D or TH2D: Histogram containing graph points with symmetric errors
    """
    if not name:
        name = graph.GetName()

    if not title:
        title = graph.GetTitle()

    x = c_double(0)
    y = c_double(0)

    xbins = bins_from_taxis(graph.GetXaxis(), as_array=True)

    if isinstance(graph, R.TGraphAsymmErrors):
        hist = R.TH1D(name, title, len(xbins) - 1, xbins)
        for point in range(graph.GetN()):
            graph.GetPoint(point, x, y)
            _bin = hist.FindBin(x)
            hist.SetBinContent(_bin, y)
            hist.SetBinError(_bin, graph.GetErrorY(point))

    elif isinstance(graph, R.TGraph2DAsymmErrors):
        z = c_double(0)

        ybins = bins_from_taxis(graph.GetYaxis(), as_array=True)

        hist = R.TH2D(
            name,
            title,
            len(xbins) - 1,
            xbins,
            len(ybins) - 1,
            ybins,
        )
        for point in range(graph.GetN()):
            graph.GetPoint(point, x, y, z)
            _bin = hist.FindBin(x, y)
            hist.SetBinContent(_bin, z)
            hist.SetBinError(_bin, graph.GetErrorZ(point))
    else:
        raise TypeError(f"Object '{name}' of unrecognised type '{type(graph)}'")

    return hist


def tgraph_to_np(tgraph, xscale=1, yscale=1):
    # TODO: write docstring

    graph = up.from_pyroot(tgraph)
    xvals, yvals = graph.values()
    xlow_errs, ylow_errs = graph.errors("low")
    xhigh_errs, yhigh_errs = graph.errors("high")

    return (
        xvals * xscale,
        yvals * yscale,
        (xlow_errs * xscale, xhigh_errs * xscale),
        (ylow_errs * yscale, yhigh_errs * yscale),
    )


def th_to_np(th, xscale=1, yscale=1):
    # TODO: write docstring

    histogram = up.from_pyroot(th)
    yvals, edges = histogram.to_numpy()
    xerrs = np.diff(edges)
    xvals = edges[:-1] + xerrs
    yerrs = histogram.errors()

    return xvals * xscale, yvals * yscale, xerrs * xscale, yerrs * yscale


def get_backend(data=None, observable=None, pdf=None):
    # TODO: write docstring

    roofit_objects = []
    zfit_objects = []

    if data is None and observable is None and pdf is None:
        return None

    if data is not None:
        if isinstance(data, R.RooAbsData):
            roofit_objects.append(data)
        elif has_zfit and isinstance(data, zfit.Data):
            zfit_objects.append(data)

    if observable is not None:
        if isinstance(observable, R.RooAbsReal):
            roofit_objects.append(observable)
        elif has_zfit and isinstance(observable, zfit.Space):
            zfit_objects.append(observable)

    if pdf is not None:
        if isinstance(pdf, R.RooAbsPdf):
            roofit_objects.append(pdf)
        elif has_zfit and isinstance(pdf, zfit.pdf.BasePDF):
            zfit_objects.append(pdf)

    if len(roofit_objects) > 0 and len(zfit_objects) > 0:
        raise ValueError(
            f"Unsupported combination of fitting objects. These must be either both RooFit objects or both zFit objects. RooFit objects: {roofit_objects}, zFit objects: {zfit_objects}"
        )

    if len(roofit_objects) > 0:
        return "roofit"
    elif len(zfit_objects) > 0:
        return "zfit"

    raise ValueError(
        f"Unsupported combination of fitting objects. These must be either both RooFit objects or both zFit objects. RooFit objects: {roofit_objects}, zFit objects: {zfit_objects}"
    )


def construct_variable(
    name,
    backend,
    value: float = None,
    limits: Annotated[List[float], 2] = None,
    title: str = None,
):
    # TODO: write docstring

    if title is None:
        title = name

    if backend == "roofit":
        if limits:
            if value:
                return R.RooRealVar(name, title, value, *limits)
            return R.RooRealVar(name, title, *limits)
        elif value:
            return R.RooRealVar(name, title, value)
        return R.RooRealVar(name, title, -np.inf, np.inf)
    elif has_zfit and backend == "zfit":
        # TODO: <- Inform user that value is ignored when creating a zfit Space
        if limits is None:
            limits = (-np.inf, np.inf)
        return zfit.Space(name, limits=limits)

    raise ValueError(
        f"Backend '{backend}' not recognised. Variable '{name}' could not be constructed."
    )


def create_dataset(
    data: Dict[str, np.ndarray],
    observable: typing.observable,
    weight="",
):
    # TODO: write docstring

    observables = observable if isinstance(observable, List) else [observable]

    backends = [get_backend(observable=observable) for observable in observables]
    if len(set(backends)) == 1:
        backend = backends[0]
    else:
        raise ValueError(
            f"Unsupported combination of observables. These must be either all ROOT RooAbsReal or all zFit Spaces. Observables: {observables}"
        )

    if weight and not any(get_variable_name(obs) for obs in observables):
        observables.append(construct_variable(weight, backend))

    if backend == "roofit":
        return R.RooDataSet.from_numpy(data, observables, weight_name=weight)

    elif has_zfit and backend == "zfit":
        np_dataset = np.array(
            [
                branch
                for branch_name, branch in data.items()
                if branch_name in [get_variable_name(obs) for obs in observables]
            ]
        ).T
        return zfit.Data.from_numpy(
            obs=zfit.dimension.combine_spaces(*observables),
            array=np_dataset,
            weights=data[weight] if weight else None,
        )


def fit_result_to_string(fit_result):
    # TODO: write docstring
    _width = 48

    result_string = "=" * _width + "\n"
    if isinstance(fit_result, R.RooFitResult):
        result_string += f"Fit performed with RooFit from ROOT {R.__version__}\n"
        result_string += "\nInitial parameters:\n"
        for var in fit_result.floatParsInit():
            result_string += f"{var.GetName()}: {var.getVal()} +/- {var.getError()}\n"
        result_string += "\nFinal parameters:\n"
        for var in fit_result.floatParsFinal():
            result_string += f"{var.GetName()}: {var.getVal()} +/- {var.getError()}\n"

        if len(fit_result.constPars()) > 0:
            result_string += "\nConstant parameters:\n"
            for var in fit_result.constPars():
                result_string += f"{var.GetName()}: {var.getVal()}\n"
        result_string += f"\nCovariance quality: {fit_result.covQual()}\n"
        result_string += f"Fit status: {fit_result.status()}\n"
        result_string += f"Minimum value: {fit_result.minNll()}\n"
        result_string += "=" * _width + "\n"

        return result_string

    elif has_zfit and isinstance(fit_result, zfit.minimizers.fitresult.FitResult):
        result_string += f"Fit performed with zfit {zfit.__version__}"
        result_string += "\nFinal parameters:\n"
        for param, param_info in fit_result.params.items():
            result_string += f"{param.name}: {param_info['value']} +/- {param_info['hesse']['error']}\n"
        result_string += f"\nValid: {fit_result.valid}\n"
        result_string += f"Converged: {fit_result.converged}\n"
        result_string += f"Fit status: {fit_result.status}\n"
        result_string += f"Minimum value: {fit_result.fmin}\n"
        result_string += "=" * _width + "\n"

        return result_string

    raise TypeError(
        f"Unrecognised type '{type(fit_result)}' for 'fit_result'. 'fit_result' must be of type 'ROOT.RooFitResult' or 'zfit.minimizers.fitresult.FitResult'."
    )


def write_fit_result(fit_result, path, verbose=False):
    # TODO: write docstring

    result_string = fit_result_to_string(fit_result)
    if verbose:
        print(result_string)

    with open(path, "w") as result_file:
        result_file.write(result_string)

    return


def get_variable_name(observable: typing.observable):
    # TODO: write docstring

    if isinstance(observable, R.RooAbsReal):
        return observable.GetName()
    elif has_zfit and isinstance(observable, zfit.Space):
        return observable.obs[0]
    raise NotImplementedError(
        f"Could not determine name for observable of type '{type(observable)}'"
    )
