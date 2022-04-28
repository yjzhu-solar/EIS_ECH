import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
rcParams["figure.figsize"] = (10,8)
#plt.style.use("science")
import eispac
from glob import glob
import sunpy

if __name__ == "__main__":
    data_filenames = glob("../src/level1/*.data.h5")
    data_filenames = sorted(data_filenames)

    for ii, filename in enumerate(data_filenames):
        data_cube_0 = eispac.read_cube(filename,0)
        data_cube_1 = eispac.read_cube(filename,1)
        data_cube_2 = eispac.read_cube(filename,2)
        data_cube_3 = eispac.read_cube(filename,3)

        # fe_12_195_tmplt = eispac.read_template("./fit_template/fe_12_195_119.1c.template.h5")
        # fe_10_184_tmplt = eispac.read_template("./fit_template/fe_10_184_536.1c.template.h5")
        # fe_10_257_tmplt = eispac.read_template("./fit_template/fe_10_257_262.4c.template.h5")
        # mg_7_276_tmplt = eispac.read_template("./fit_template/mg_07_276_153.1c.template.h5")
        # mg_7_280_tmplt = eispac.read_template("./fit_template/mg_07_280_737.1c.template.h5")
        # si_10_258_tmplt = eispac.read_template("./fit_template/si_10_258_375.1c.template.h5")
        # si_10_261_tmplt = eispac.read_template("./fit_template/si_10_261_058.1c.template.h5")
        # fe_8_185_tmplt = eispac.read_template("./fit_template/fe_08_185_213.1c.template.h5")
        # fe_8_186_tmplt = eispac.read_template("./fit_template/fe_08_186_601.1c.template.h5")
        he_2_256_tmplt = eispac.read_template("./fit_template/he_02_256_317.2c.template.h5")
        fe_9_197_tmplt = eispac.read_template("./fit_template/fe_09_197_862.1c.template.h5")
        o_6_184_tmplt = eispac.read_template("./fit_template/o__06_184_117.1c.template.h5")
        fe_11_188_tmplt = eispac.read_template("./fit_template/fe_11_188_216.2c.template.h5")
        fe_14_270_tmplt = eispac.read_template("./fit_template/fe_14_270_519.2c.template.h5")
        fe_15_284_tmplt = eispac.read_template("./fit_template/fe_15_284_160.2c.template.h5")
        fe_13_202_tmplt = eispac.read_template("./fit_template/fe_13_202_044.1c.template.h5")

        # fe_12_195_fit_res = eispac.fit_spectra(data_cube_1, fe_12_195_tmplt, ncpu="max")
        # fe_10_184_fit_res = eispac.fit_spectra(data_cube_0, fe_10_184_tmplt, ncpu="max")
        # fe_10_257_fit_res = eispac.fit_spectra(data_cube_2, fe_10_257_tmplt, ncpu="max")
        # mg_7_276_fit_res = eispac.fit_spectra(data_cube_3, mg_7_276_tmplt, ncpu="max")
        # mg_7_280_fit_res = eispac.fit_spectra(data_cube_3, mg_7_280_tmplt, ncpu="max")
        # si_10_258_fit_res = eispac.fit_spectra(data_cube_2, si_10_258_tmplt, ncpu="max")
        # si_10_261_fit_res = eispac.fit_spectra(data_cube_2, si_10_261_tmplt, ncpu="max")
        # fe_8_185_fit_res = eispac.fit_spectra(data_cube_0, fe_8_185_tmplt, ncpu="max")
        # fe_8_186_fit_res = eispac.fit_spectra(data_cube_0, fe_8_186_tmplt, ncpu="max")
        he_2_256_fit_res = eispac.fit_spectra(data_cube_2, he_2_256_tmplt, ncpu="max")
        fe_9_197_fit_res = eispac.fit_spectra(data_cube_1, fe_9_197_tmplt, ncpu="max")
        o_6_184_fit_res = eispac.fit_spectra(data_cube_0, o_6_184_tmplt, ncpu="max")
        fe_11_188_fit_res = eispac.fit_spectra(data_cube_0, fe_11_188_tmplt, ncpu="max")
        fe_14_270_fit_res = eispac.fit_spectra(data_cube_3, fe_14_270_tmplt, ncpu="max")
        fe_15_284_fit_res = eispac.fit_spectra(data_cube_3, fe_15_284_tmplt, ncpu="max")
        fe_13_202_fit_res = eispac.fit_spectra(data_cube_1, fe_13_202_tmplt, ncpu="max")






        # for fit_res in (fe_12_195_fit_res, fe_10_184_fit_res, fe_10_257_fit_res,
        #                 mg_7_276_fit_res, mg_7_280_fit_res, si_10_258_fit_res, 
        #                 si_10_261_fit_res,fe_8_185_fit_res,fe_8_186_fit_res,
        #                 he_2_256_fit_res,fe_9_197_fit_res,o_6_184_fit_res,
        #                 fe_11_188_fit_res,fe_14_270_fit_res,fe_15_284_fit_res):
        for fit_res in (he_2_256_fit_res,fe_9_197_fit_res,o_6_184_fit_res,
                        fe_11_188_fit_res,fe_14_270_fit_res,fe_15_284_fit_res,
                        fe_13_202_fit_res):
            eispac.save_fit(fit_res, save_dir = "../save/eis_fit/")




    