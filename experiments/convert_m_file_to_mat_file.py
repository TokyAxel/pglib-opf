from oct2py import octave as oct
oct.eval("cd ../")
oct.eval("pglib_opf_case3_lmbd")
oct.eval("save -v7 experiments/pglib_opf_case3_lmbd.mat")

#ptr = oct.pull('bus')

res = oct.feval("pglib_opf_case3_lmbd")
print(res)

from scipy.io import loadmat
D = loadmat("pglib_opf_case3_lmbd.mat")
print(D)
