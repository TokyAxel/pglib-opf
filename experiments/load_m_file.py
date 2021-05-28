from oct2py import octave as oct
oct.eval("cd .")
oct.eval("../pglib_opf_case3_lmbd.m")
oct.eval("save -v7 pglib_opf_case3_lmbd.mat")

from scipy.io import loadmat
D = loadmat("pglib_opf_case3_lmbd.mat")
print(D.keys())
