# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_newpresto', [dirname(__file__)])
        except ImportError:
            import _newpresto
            return _newpresto
        if fp is not None:
            try:
                _mod = imp.load_module('_newpresto', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _newpresto = swig_import_helper()
    del swig_import_helper
else:
    import _newpresto
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class fcomplex(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, fcomplex, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, fcomplex, name)
    __repr__ = _swig_repr
    __swig_setmethods__["r"] = _newpresto.fcomplex_r_set
    __swig_getmethods__["r"] = _newpresto.fcomplex_r_get
    if _newclass:r = _swig_property(_newpresto.fcomplex_r_get, _newpresto.fcomplex_r_set)
    __swig_setmethods__["i"] = _newpresto.fcomplex_i_set
    __swig_getmethods__["i"] = _newpresto.fcomplex_i_get
    if _newclass:i = _swig_property(_newpresto.fcomplex_i_get, _newpresto.fcomplex_i_set)
    def __init__(self): 
        this = _newpresto.new_fcomplex()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _newpresto.delete_fcomplex
    __del__ = lambda self : None;
fcomplex_swigregister = _newpresto.fcomplex_swigregister
fcomplex_swigregister(fcomplex)

SQRT2 = _newpresto.SQRT2
PI = _newpresto.PI
TWOPI = _newpresto.TWOPI
DEGTORAD = _newpresto.DEGTORAD
RADTODEG = _newpresto.RADTODEG
PIBYTWO = _newpresto.PIBYTWO
SOL = _newpresto.SOL
SECPERJULYR = _newpresto.SECPERJULYR
SECPERDAY = _newpresto.SECPERDAY
ARCSEC2RAD = _newpresto.ARCSEC2RAD
SEC2RAD = _newpresto.SEC2RAD
LOWACC = _newpresto.LOWACC
HIGHACC = _newpresto.HIGHACC
INTERBIN = _newpresto.INTERBIN
INTERPOLATE = _newpresto.INTERPOLATE
NO_CHECK_ALIASED = _newpresto.NO_CHECK_ALIASED
CHECK_ALIASED = _newpresto.CHECK_ALIASED
CONV = _newpresto.CONV
CORR = _newpresto.CORR
INPLACE_CONV = _newpresto.INPLACE_CONV
INPLACE_CORR = _newpresto.INPLACE_CORR
FFTDK = _newpresto.FFTDK
FFTD = _newpresto.FFTD
FFTK = _newpresto.FFTK
NOFFTS = _newpresto.NOFFTS
RAW = _newpresto.RAW
PREPPED = _newpresto.PREPPED
FFT = _newpresto.FFT
SAME = _newpresto.SAME

def read_wisdom():
  return _newpresto.read_wisdom()
read_wisdom = _newpresto.read_wisdom

def good_factor(*args):
  return _newpresto.good_factor(*args)
good_factor = _newpresto.good_factor

def fftwcall(*args):
  return _newpresto.fftwcall(*args)
fftwcall = _newpresto.fftwcall

def tablesixstepfft(*args):
  return _newpresto.tablesixstepfft(*args)
tablesixstepfft = _newpresto.tablesixstepfft

def realfft(*args):
  return _newpresto.realfft(*args)
realfft = _newpresto.realfft
class infodata(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, infodata, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, infodata, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ra_s"] = _newpresto.infodata_ra_s_set
    __swig_getmethods__["ra_s"] = _newpresto.infodata_ra_s_get
    if _newclass:ra_s = _swig_property(_newpresto.infodata_ra_s_get, _newpresto.infodata_ra_s_set)
    __swig_setmethods__["dec_s"] = _newpresto.infodata_dec_s_set
    __swig_getmethods__["dec_s"] = _newpresto.infodata_dec_s_get
    if _newclass:dec_s = _swig_property(_newpresto.infodata_dec_s_get, _newpresto.infodata_dec_s_set)
    __swig_setmethods__["N"] = _newpresto.infodata_N_set
    __swig_getmethods__["N"] = _newpresto.infodata_N_get
    if _newclass:N = _swig_property(_newpresto.infodata_N_get, _newpresto.infodata_N_set)
    __swig_setmethods__["dt"] = _newpresto.infodata_dt_set
    __swig_getmethods__["dt"] = _newpresto.infodata_dt_get
    if _newclass:dt = _swig_property(_newpresto.infodata_dt_get, _newpresto.infodata_dt_set)
    __swig_setmethods__["fov"] = _newpresto.infodata_fov_set
    __swig_getmethods__["fov"] = _newpresto.infodata_fov_get
    if _newclass:fov = _swig_property(_newpresto.infodata_fov_get, _newpresto.infodata_fov_set)
    __swig_setmethods__["mjd_f"] = _newpresto.infodata_mjd_f_set
    __swig_getmethods__["mjd_f"] = _newpresto.infodata_mjd_f_get
    if _newclass:mjd_f = _swig_property(_newpresto.infodata_mjd_f_get, _newpresto.infodata_mjd_f_set)
    __swig_setmethods__["dm"] = _newpresto.infodata_dm_set
    __swig_getmethods__["dm"] = _newpresto.infodata_dm_get
    if _newclass:dm = _swig_property(_newpresto.infodata_dm_get, _newpresto.infodata_dm_set)
    __swig_setmethods__["freq"] = _newpresto.infodata_freq_set
    __swig_getmethods__["freq"] = _newpresto.infodata_freq_get
    if _newclass:freq = _swig_property(_newpresto.infodata_freq_get, _newpresto.infodata_freq_set)
    __swig_setmethods__["freqband"] = _newpresto.infodata_freqband_set
    __swig_getmethods__["freqband"] = _newpresto.infodata_freqband_get
    if _newclass:freqband = _swig_property(_newpresto.infodata_freqband_get, _newpresto.infodata_freqband_set)
    __swig_setmethods__["chan_wid"] = _newpresto.infodata_chan_wid_set
    __swig_getmethods__["chan_wid"] = _newpresto.infodata_chan_wid_get
    if _newclass:chan_wid = _swig_property(_newpresto.infodata_chan_wid_get, _newpresto.infodata_chan_wid_set)
    __swig_setmethods__["wavelen"] = _newpresto.infodata_wavelen_set
    __swig_getmethods__["wavelen"] = _newpresto.infodata_wavelen_get
    if _newclass:wavelen = _swig_property(_newpresto.infodata_wavelen_get, _newpresto.infodata_wavelen_set)
    __swig_setmethods__["waveband"] = _newpresto.infodata_waveband_set
    __swig_getmethods__["waveband"] = _newpresto.infodata_waveband_get
    if _newclass:waveband = _swig_property(_newpresto.infodata_waveband_get, _newpresto.infodata_waveband_set)
    __swig_setmethods__["energy"] = _newpresto.infodata_energy_set
    __swig_getmethods__["energy"] = _newpresto.infodata_energy_get
    if _newclass:energy = _swig_property(_newpresto.infodata_energy_get, _newpresto.infodata_energy_set)
    __swig_setmethods__["energyband"] = _newpresto.infodata_energyband_set
    __swig_getmethods__["energyband"] = _newpresto.infodata_energyband_get
    if _newclass:energyband = _swig_property(_newpresto.infodata_energyband_get, _newpresto.infodata_energyband_set)
    __swig_setmethods__["num_chan"] = _newpresto.infodata_num_chan_set
    __swig_getmethods__["num_chan"] = _newpresto.infodata_num_chan_get
    if _newclass:num_chan = _swig_property(_newpresto.infodata_num_chan_get, _newpresto.infodata_num_chan_set)
    __swig_setmethods__["mjd_i"] = _newpresto.infodata_mjd_i_set
    __swig_getmethods__["mjd_i"] = _newpresto.infodata_mjd_i_get
    if _newclass:mjd_i = _swig_property(_newpresto.infodata_mjd_i_get, _newpresto.infodata_mjd_i_set)
    __swig_setmethods__["ra_h"] = _newpresto.infodata_ra_h_set
    __swig_getmethods__["ra_h"] = _newpresto.infodata_ra_h_get
    if _newclass:ra_h = _swig_property(_newpresto.infodata_ra_h_get, _newpresto.infodata_ra_h_set)
    __swig_setmethods__["ra_m"] = _newpresto.infodata_ra_m_set
    __swig_getmethods__["ra_m"] = _newpresto.infodata_ra_m_get
    if _newclass:ra_m = _swig_property(_newpresto.infodata_ra_m_get, _newpresto.infodata_ra_m_set)
    __swig_setmethods__["dec_d"] = _newpresto.infodata_dec_d_set
    __swig_getmethods__["dec_d"] = _newpresto.infodata_dec_d_get
    if _newclass:dec_d = _swig_property(_newpresto.infodata_dec_d_get, _newpresto.infodata_dec_d_set)
    __swig_setmethods__["dec_m"] = _newpresto.infodata_dec_m_set
    __swig_getmethods__["dec_m"] = _newpresto.infodata_dec_m_get
    if _newclass:dec_m = _swig_property(_newpresto.infodata_dec_m_get, _newpresto.infodata_dec_m_set)
    __swig_setmethods__["bary"] = _newpresto.infodata_bary_set
    __swig_getmethods__["bary"] = _newpresto.infodata_bary_get
    if _newclass:bary = _swig_property(_newpresto.infodata_bary_get, _newpresto.infodata_bary_set)
    __swig_setmethods__["numonoff"] = _newpresto.infodata_numonoff_set
    __swig_getmethods__["numonoff"] = _newpresto.infodata_numonoff_get
    if _newclass:numonoff = _swig_property(_newpresto.infodata_numonoff_get, _newpresto.infodata_numonoff_set)
    __swig_setmethods__["notes"] = _newpresto.infodata_notes_set
    __swig_getmethods__["notes"] = _newpresto.infodata_notes_get
    if _newclass:notes = _swig_property(_newpresto.infodata_notes_get, _newpresto.infodata_notes_set)
    __swig_setmethods__["name"] = _newpresto.infodata_name_set
    __swig_getmethods__["name"] = _newpresto.infodata_name_get
    if _newclass:name = _swig_property(_newpresto.infodata_name_get, _newpresto.infodata_name_set)
    __swig_setmethods__["object"] = _newpresto.infodata_object_set
    __swig_getmethods__["object"] = _newpresto.infodata_object_get
    if _newclass:object = _swig_property(_newpresto.infodata_object_get, _newpresto.infodata_object_set)
    __swig_setmethods__["instrument"] = _newpresto.infodata_instrument_set
    __swig_getmethods__["instrument"] = _newpresto.infodata_instrument_get
    if _newclass:instrument = _swig_property(_newpresto.infodata_instrument_get, _newpresto.infodata_instrument_set)
    __swig_setmethods__["observer"] = _newpresto.infodata_observer_set
    __swig_getmethods__["observer"] = _newpresto.infodata_observer_get
    if _newclass:observer = _swig_property(_newpresto.infodata_observer_get, _newpresto.infodata_observer_set)
    __swig_setmethods__["analyzer"] = _newpresto.infodata_analyzer_set
    __swig_getmethods__["analyzer"] = _newpresto.infodata_analyzer_get
    if _newclass:analyzer = _swig_property(_newpresto.infodata_analyzer_get, _newpresto.infodata_analyzer_set)
    __swig_setmethods__["telescope"] = _newpresto.infodata_telescope_set
    __swig_getmethods__["telescope"] = _newpresto.infodata_telescope_get
    if _newclass:telescope = _swig_property(_newpresto.infodata_telescope_get, _newpresto.infodata_telescope_set)
    __swig_setmethods__["band"] = _newpresto.infodata_band_set
    __swig_getmethods__["band"] = _newpresto.infodata_band_get
    if _newclass:band = _swig_property(_newpresto.infodata_band_get, _newpresto.infodata_band_set)
    __swig_setmethods__["filt"] = _newpresto.infodata_filt_set
    __swig_getmethods__["filt"] = _newpresto.infodata_filt_get
    if _newclass:filt = _swig_property(_newpresto.infodata_filt_get, _newpresto.infodata_filt_set)
    def __init__(self): 
        this = _newpresto.new_infodata()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _newpresto.delete_infodata
    __del__ = lambda self : None;
infodata_swigregister = _newpresto.infodata_swigregister
infodata_swigregister(infodata)


def readinf(*args):
  return _newpresto.readinf(*args)
readinf = _newpresto.readinf

def writeinf(*args):
  return _newpresto.writeinf(*args)
writeinf = _newpresto.writeinf
class orbitparams(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, orbitparams, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, orbitparams, name)
    __repr__ = _swig_repr
    __swig_setmethods__["p"] = _newpresto.orbitparams_p_set
    __swig_getmethods__["p"] = _newpresto.orbitparams_p_get
    if _newclass:p = _swig_property(_newpresto.orbitparams_p_get, _newpresto.orbitparams_p_set)
    __swig_setmethods__["e"] = _newpresto.orbitparams_e_set
    __swig_getmethods__["e"] = _newpresto.orbitparams_e_get
    if _newclass:e = _swig_property(_newpresto.orbitparams_e_get, _newpresto.orbitparams_e_set)
    __swig_setmethods__["x"] = _newpresto.orbitparams_x_set
    __swig_getmethods__["x"] = _newpresto.orbitparams_x_get
    if _newclass:x = _swig_property(_newpresto.orbitparams_x_get, _newpresto.orbitparams_x_set)
    __swig_setmethods__["w"] = _newpresto.orbitparams_w_set
    __swig_getmethods__["w"] = _newpresto.orbitparams_w_get
    if _newclass:w = _swig_property(_newpresto.orbitparams_w_get, _newpresto.orbitparams_w_set)
    __swig_setmethods__["t"] = _newpresto.orbitparams_t_set
    __swig_getmethods__["t"] = _newpresto.orbitparams_t_get
    if _newclass:t = _swig_property(_newpresto.orbitparams_t_get, _newpresto.orbitparams_t_set)
    __swig_setmethods__["pd"] = _newpresto.orbitparams_pd_set
    __swig_getmethods__["pd"] = _newpresto.orbitparams_pd_get
    if _newclass:pd = _swig_property(_newpresto.orbitparams_pd_get, _newpresto.orbitparams_pd_set)
    __swig_setmethods__["wd"] = _newpresto.orbitparams_wd_set
    __swig_getmethods__["wd"] = _newpresto.orbitparams_wd_get
    if _newclass:wd = _swig_property(_newpresto.orbitparams_wd_get, _newpresto.orbitparams_wd_set)
    def __init__(self): 
        this = _newpresto.new_orbitparams()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _newpresto.delete_orbitparams
    __del__ = lambda self : None;
orbitparams_swigregister = _newpresto.orbitparams_swigregister
orbitparams_swigregister(orbitparams)

class psrparams(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, psrparams, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, psrparams, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jname"] = _newpresto.psrparams_jname_set
    __swig_getmethods__["jname"] = _newpresto.psrparams_jname_get
    if _newclass:jname = _swig_property(_newpresto.psrparams_jname_get, _newpresto.psrparams_jname_set)
    __swig_setmethods__["bname"] = _newpresto.psrparams_bname_set
    __swig_getmethods__["bname"] = _newpresto.psrparams_bname_get
    if _newclass:bname = _swig_property(_newpresto.psrparams_bname_get, _newpresto.psrparams_bname_set)
    __swig_setmethods__["alias"] = _newpresto.psrparams_alias_set
    __swig_getmethods__["alias"] = _newpresto.psrparams_alias_get
    if _newclass:alias = _swig_property(_newpresto.psrparams_alias_get, _newpresto.psrparams_alias_set)
    __swig_setmethods__["ra2000"] = _newpresto.psrparams_ra2000_set
    __swig_getmethods__["ra2000"] = _newpresto.psrparams_ra2000_get
    if _newclass:ra2000 = _swig_property(_newpresto.psrparams_ra2000_get, _newpresto.psrparams_ra2000_set)
    __swig_setmethods__["dec2000"] = _newpresto.psrparams_dec2000_set
    __swig_getmethods__["dec2000"] = _newpresto.psrparams_dec2000_get
    if _newclass:dec2000 = _swig_property(_newpresto.psrparams_dec2000_get, _newpresto.psrparams_dec2000_set)
    __swig_setmethods__["dm"] = _newpresto.psrparams_dm_set
    __swig_getmethods__["dm"] = _newpresto.psrparams_dm_get
    if _newclass:dm = _swig_property(_newpresto.psrparams_dm_get, _newpresto.psrparams_dm_set)
    __swig_setmethods__["timepoch"] = _newpresto.psrparams_timepoch_set
    __swig_getmethods__["timepoch"] = _newpresto.psrparams_timepoch_get
    if _newclass:timepoch = _swig_property(_newpresto.psrparams_timepoch_get, _newpresto.psrparams_timepoch_set)
    __swig_setmethods__["p"] = _newpresto.psrparams_p_set
    __swig_getmethods__["p"] = _newpresto.psrparams_p_get
    if _newclass:p = _swig_property(_newpresto.psrparams_p_get, _newpresto.psrparams_p_set)
    __swig_setmethods__["pd"] = _newpresto.psrparams_pd_set
    __swig_getmethods__["pd"] = _newpresto.psrparams_pd_get
    if _newclass:pd = _swig_property(_newpresto.psrparams_pd_get, _newpresto.psrparams_pd_set)
    __swig_setmethods__["pdd"] = _newpresto.psrparams_pdd_set
    __swig_getmethods__["pdd"] = _newpresto.psrparams_pdd_get
    if _newclass:pdd = _swig_property(_newpresto.psrparams_pdd_get, _newpresto.psrparams_pdd_set)
    __swig_setmethods__["f"] = _newpresto.psrparams_f_set
    __swig_getmethods__["f"] = _newpresto.psrparams_f_get
    if _newclass:f = _swig_property(_newpresto.psrparams_f_get, _newpresto.psrparams_f_set)
    __swig_setmethods__["fd"] = _newpresto.psrparams_fd_set
    __swig_getmethods__["fd"] = _newpresto.psrparams_fd_get
    if _newclass:fd = _swig_property(_newpresto.psrparams_fd_get, _newpresto.psrparams_fd_set)
    __swig_setmethods__["fdd"] = _newpresto.psrparams_fdd_set
    __swig_getmethods__["fdd"] = _newpresto.psrparams_fdd_get
    if _newclass:fdd = _swig_property(_newpresto.psrparams_fdd_get, _newpresto.psrparams_fdd_set)
    __swig_setmethods__["orb"] = _newpresto.psrparams_orb_set
    __swig_getmethods__["orb"] = _newpresto.psrparams_orb_get
    if _newclass:orb = _swig_property(_newpresto.psrparams_orb_get, _newpresto.psrparams_orb_set)
    def __init__(self): 
        this = _newpresto.new_psrparams()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _newpresto.delete_psrparams
    __del__ = lambda self : None;
psrparams_swigregister = _newpresto.psrparams_swigregister
psrparams_swigregister(psrparams)


def get_psr_at_epoch(*args):
  return _newpresto.get_psr_at_epoch(*args)
get_psr_at_epoch = _newpresto.get_psr_at_epoch

def get_psr_from_parfile(*args):
  return _newpresto.get_psr_from_parfile(*args)
get_psr_from_parfile = _newpresto.get_psr_from_parfile

def mjd_to_datestr(*args):
  return _newpresto.mjd_to_datestr(*args)
mjd_to_datestr = _newpresto.mjd_to_datestr

def fresnl(*args):
  return _newpresto.fresnl(*args)
fresnl = _newpresto.fresnl
class rderivs(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rderivs, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rderivs, name)
    __repr__ = _swig_repr
    __swig_setmethods__["pow"] = _newpresto.rderivs_pow_set
    __swig_getmethods__["pow"] = _newpresto.rderivs_pow_get
    if _newclass:pow = _swig_property(_newpresto.rderivs_pow_get, _newpresto.rderivs_pow_set)
    __swig_setmethods__["phs"] = _newpresto.rderivs_phs_set
    __swig_getmethods__["phs"] = _newpresto.rderivs_phs_get
    if _newclass:phs = _swig_property(_newpresto.rderivs_phs_get, _newpresto.rderivs_phs_set)
    __swig_setmethods__["dpow"] = _newpresto.rderivs_dpow_set
    __swig_getmethods__["dpow"] = _newpresto.rderivs_dpow_get
    if _newclass:dpow = _swig_property(_newpresto.rderivs_dpow_get, _newpresto.rderivs_dpow_set)
    __swig_setmethods__["dphs"] = _newpresto.rderivs_dphs_set
    __swig_getmethods__["dphs"] = _newpresto.rderivs_dphs_get
    if _newclass:dphs = _swig_property(_newpresto.rderivs_dphs_get, _newpresto.rderivs_dphs_set)
    __swig_setmethods__["d2pow"] = _newpresto.rderivs_d2pow_set
    __swig_getmethods__["d2pow"] = _newpresto.rderivs_d2pow_get
    if _newclass:d2pow = _swig_property(_newpresto.rderivs_d2pow_get, _newpresto.rderivs_d2pow_set)
    __swig_setmethods__["d2phs"] = _newpresto.rderivs_d2phs_set
    __swig_getmethods__["d2phs"] = _newpresto.rderivs_d2phs_get
    if _newclass:d2phs = _swig_property(_newpresto.rderivs_d2phs_get, _newpresto.rderivs_d2phs_set)
    __swig_setmethods__["locpow"] = _newpresto.rderivs_locpow_set
    __swig_getmethods__["locpow"] = _newpresto.rderivs_locpow_get
    if _newclass:locpow = _swig_property(_newpresto.rderivs_locpow_get, _newpresto.rderivs_locpow_set)
    def __init__(self): 
        this = _newpresto.new_rderivs()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _newpresto.delete_rderivs
    __del__ = lambda self : None;
rderivs_swigregister = _newpresto.rderivs_swigregister
rderivs_swigregister(rderivs)

class fourierprops(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, fourierprops, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, fourierprops, name)
    __repr__ = _swig_repr
    __swig_setmethods__["r"] = _newpresto.fourierprops_r_set
    __swig_getmethods__["r"] = _newpresto.fourierprops_r_get
    if _newclass:r = _swig_property(_newpresto.fourierprops_r_get, _newpresto.fourierprops_r_set)
    __swig_setmethods__["rerr"] = _newpresto.fourierprops_rerr_set
    __swig_getmethods__["rerr"] = _newpresto.fourierprops_rerr_get
    if _newclass:rerr = _swig_property(_newpresto.fourierprops_rerr_get, _newpresto.fourierprops_rerr_set)
    __swig_setmethods__["z"] = _newpresto.fourierprops_z_set
    __swig_getmethods__["z"] = _newpresto.fourierprops_z_get
    if _newclass:z = _swig_property(_newpresto.fourierprops_z_get, _newpresto.fourierprops_z_set)
    __swig_setmethods__["zerr"] = _newpresto.fourierprops_zerr_set
    __swig_getmethods__["zerr"] = _newpresto.fourierprops_zerr_get
    if _newclass:zerr = _swig_property(_newpresto.fourierprops_zerr_get, _newpresto.fourierprops_zerr_set)
    __swig_setmethods__["w"] = _newpresto.fourierprops_w_set
    __swig_getmethods__["w"] = _newpresto.fourierprops_w_get
    if _newclass:w = _swig_property(_newpresto.fourierprops_w_get, _newpresto.fourierprops_w_set)
    __swig_setmethods__["werr"] = _newpresto.fourierprops_werr_set
    __swig_getmethods__["werr"] = _newpresto.fourierprops_werr_get
    if _newclass:werr = _swig_property(_newpresto.fourierprops_werr_get, _newpresto.fourierprops_werr_set)
    __swig_setmethods__["pow"] = _newpresto.fourierprops_pow_set
    __swig_getmethods__["pow"] = _newpresto.fourierprops_pow_get
    if _newclass:pow = _swig_property(_newpresto.fourierprops_pow_get, _newpresto.fourierprops_pow_set)
    __swig_setmethods__["powerr"] = _newpresto.fourierprops_powerr_set
    __swig_getmethods__["powerr"] = _newpresto.fourierprops_powerr_get
    if _newclass:powerr = _swig_property(_newpresto.fourierprops_powerr_get, _newpresto.fourierprops_powerr_set)
    __swig_setmethods__["sig"] = _newpresto.fourierprops_sig_set
    __swig_getmethods__["sig"] = _newpresto.fourierprops_sig_get
    if _newclass:sig = _swig_property(_newpresto.fourierprops_sig_get, _newpresto.fourierprops_sig_set)
    __swig_setmethods__["rawpow"] = _newpresto.fourierprops_rawpow_set
    __swig_getmethods__["rawpow"] = _newpresto.fourierprops_rawpow_get
    if _newclass:rawpow = _swig_property(_newpresto.fourierprops_rawpow_get, _newpresto.fourierprops_rawpow_set)
    __swig_setmethods__["phs"] = _newpresto.fourierprops_phs_set
    __swig_getmethods__["phs"] = _newpresto.fourierprops_phs_get
    if _newclass:phs = _swig_property(_newpresto.fourierprops_phs_get, _newpresto.fourierprops_phs_set)
    __swig_setmethods__["phserr"] = _newpresto.fourierprops_phserr_set
    __swig_getmethods__["phserr"] = _newpresto.fourierprops_phserr_get
    if _newclass:phserr = _swig_property(_newpresto.fourierprops_phserr_get, _newpresto.fourierprops_phserr_set)
    __swig_setmethods__["cen"] = _newpresto.fourierprops_cen_set
    __swig_getmethods__["cen"] = _newpresto.fourierprops_cen_get
    if _newclass:cen = _swig_property(_newpresto.fourierprops_cen_get, _newpresto.fourierprops_cen_set)
    __swig_setmethods__["cenerr"] = _newpresto.fourierprops_cenerr_set
    __swig_getmethods__["cenerr"] = _newpresto.fourierprops_cenerr_get
    if _newclass:cenerr = _swig_property(_newpresto.fourierprops_cenerr_get, _newpresto.fourierprops_cenerr_set)
    __swig_setmethods__["pur"] = _newpresto.fourierprops_pur_set
    __swig_getmethods__["pur"] = _newpresto.fourierprops_pur_get
    if _newclass:pur = _swig_property(_newpresto.fourierprops_pur_get, _newpresto.fourierprops_pur_set)
    __swig_setmethods__["purerr"] = _newpresto.fourierprops_purerr_set
    __swig_getmethods__["purerr"] = _newpresto.fourierprops_purerr_get
    if _newclass:purerr = _swig_property(_newpresto.fourierprops_purerr_get, _newpresto.fourierprops_purerr_set)
    __swig_setmethods__["locpow"] = _newpresto.fourierprops_locpow_set
    __swig_getmethods__["locpow"] = _newpresto.fourierprops_locpow_get
    if _newclass:locpow = _swig_property(_newpresto.fourierprops_locpow_get, _newpresto.fourierprops_locpow_set)
    def __init__(self): 
        this = _newpresto.new_fourierprops()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _newpresto.delete_fourierprops
    __del__ = lambda self : None;
fourierprops_swigregister = _newpresto.fourierprops_swigregister
fourierprops_swigregister(fourierprops)

class foldstats(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, foldstats, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, foldstats, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numdata"] = _newpresto.foldstats_numdata_set
    __swig_getmethods__["numdata"] = _newpresto.foldstats_numdata_get
    if _newclass:numdata = _swig_property(_newpresto.foldstats_numdata_get, _newpresto.foldstats_numdata_set)
    __swig_setmethods__["data_avg"] = _newpresto.foldstats_data_avg_set
    __swig_getmethods__["data_avg"] = _newpresto.foldstats_data_avg_get
    if _newclass:data_avg = _swig_property(_newpresto.foldstats_data_avg_get, _newpresto.foldstats_data_avg_set)
    __swig_setmethods__["data_var"] = _newpresto.foldstats_data_var_set
    __swig_getmethods__["data_var"] = _newpresto.foldstats_data_var_get
    if _newclass:data_var = _swig_property(_newpresto.foldstats_data_var_get, _newpresto.foldstats_data_var_set)
    __swig_setmethods__["numprof"] = _newpresto.foldstats_numprof_set
    __swig_getmethods__["numprof"] = _newpresto.foldstats_numprof_get
    if _newclass:numprof = _swig_property(_newpresto.foldstats_numprof_get, _newpresto.foldstats_numprof_set)
    __swig_setmethods__["prof_avg"] = _newpresto.foldstats_prof_avg_set
    __swig_getmethods__["prof_avg"] = _newpresto.foldstats_prof_avg_get
    if _newclass:prof_avg = _swig_property(_newpresto.foldstats_prof_avg_get, _newpresto.foldstats_prof_avg_set)
    __swig_setmethods__["prof_var"] = _newpresto.foldstats_prof_var_set
    __swig_getmethods__["prof_var"] = _newpresto.foldstats_prof_var_get
    if _newclass:prof_var = _swig_property(_newpresto.foldstats_prof_var_get, _newpresto.foldstats_prof_var_set)
    __swig_setmethods__["redchi"] = _newpresto.foldstats_redchi_set
    __swig_getmethods__["redchi"] = _newpresto.foldstats_redchi_get
    if _newclass:redchi = _swig_property(_newpresto.foldstats_redchi_get, _newpresto.foldstats_redchi_set)
    def __init__(self): 
        this = _newpresto.new_foldstats()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _newpresto.delete_foldstats
    __del__ = lambda self : None;
foldstats_swigregister = _newpresto.foldstats_swigregister
foldstats_swigregister(foldstats)


def gen_fvect(*args):
  return _newpresto.gen_fvect(*args)
gen_fvect = _newpresto.gen_fvect

def gen_cvect(*args):
  return _newpresto.gen_cvect(*args)
gen_cvect = _newpresto.gen_cvect

def power_arr(*args):
  return _newpresto.power_arr(*args)
power_arr = _newpresto.power_arr

def phase_arr(*args):
  return _newpresto.phase_arr(*args)
phase_arr = _newpresto.phase_arr

def frotate(*args):
  return _newpresto.frotate(*args)
frotate = _newpresto.frotate

def drotate(*args):
  return _newpresto.drotate(*args)
drotate = _newpresto.drotate

def keplers_eqn(*args):
  return _newpresto.keplers_eqn(*args)
keplers_eqn = _newpresto.keplers_eqn

def E_to_phib(*args):
  return _newpresto.E_to_phib(*args)
E_to_phib = _newpresto.E_to_phib

def E_to_v(*args):
  return _newpresto.E_to_v(*args)
E_to_v = _newpresto.E_to_v

def E_to_p(*args):
  return _newpresto.E_to_p(*args)
E_to_p = _newpresto.E_to_p

def E_to_z(*args):
  return _newpresto.E_to_z(*args)
E_to_z = _newpresto.E_to_z

def E_to_phib_BT(*args):
  return _newpresto.E_to_phib_BT(*args)
E_to_phib_BT = _newpresto.E_to_phib_BT

def dorbint(*args):
  return _newpresto.dorbint(*args)
dorbint = _newpresto.dorbint

def binary_velocity(*args):
  return _newpresto.binary_velocity(*args)
binary_velocity = _newpresto.binary_velocity

def r_resp_halfwidth(*args):
  return _newpresto.r_resp_halfwidth(*args)
r_resp_halfwidth = _newpresto.r_resp_halfwidth

def z_resp_halfwidth(*args):
  return _newpresto.z_resp_halfwidth(*args)
z_resp_halfwidth = _newpresto.z_resp_halfwidth

def w_resp_halfwidth(*args):
  return _newpresto.w_resp_halfwidth(*args)
w_resp_halfwidth = _newpresto.w_resp_halfwidth

def bin_resp_halfwidth(*args):
  return _newpresto.bin_resp_halfwidth(*args)
bin_resp_halfwidth = _newpresto.bin_resp_halfwidth

def gen_r_response(*args):
  return _newpresto.gen_r_response(*args)
gen_r_response = _newpresto.gen_r_response

def gen_z_response(*args):
  return _newpresto.gen_z_response(*args)
gen_z_response = _newpresto.gen_z_response

def gen_w_response(*args):
  return _newpresto.gen_w_response(*args)
gen_w_response = _newpresto.gen_w_response

def gen_bin_response(*args):
  return _newpresto.gen_bin_response(*args)
gen_bin_response = _newpresto.gen_bin_response

def get_localpower(*args):
  return _newpresto.get_localpower(*args)
get_localpower = _newpresto.get_localpower

def get_localpower3d(*args):
  return _newpresto.get_localpower3d(*args)
get_localpower3d = _newpresto.get_localpower3d

def get_derivs3d(*args):
  return _newpresto.get_derivs3d(*args)
get_derivs3d = _newpresto.get_derivs3d

def calc_props(*args):
  return _newpresto.calc_props(*args)
calc_props = _newpresto.calc_props

def calc_binprops(*args):
  return _newpresto.calc_binprops(*args)
calc_binprops = _newpresto.calc_binprops

def calc_rzwerrs(*args):
  return _newpresto.calc_rzwerrs(*args)
calc_rzwerrs = _newpresto.calc_rzwerrs

def extended_equiv_gaussian_sigma(*args):
  return _newpresto.extended_equiv_gaussian_sigma(*args)
extended_equiv_gaussian_sigma = _newpresto.extended_equiv_gaussian_sigma

def log_asymtotic_incomplete_gamma(*args):
  return _newpresto.log_asymtotic_incomplete_gamma(*args)
log_asymtotic_incomplete_gamma = _newpresto.log_asymtotic_incomplete_gamma

def log_asymtotic_gamma(*args):
  return _newpresto.log_asymtotic_gamma(*args)
log_asymtotic_gamma = _newpresto.log_asymtotic_gamma

def equivalent_gaussian_sigma(*args):
  return _newpresto.equivalent_gaussian_sigma(*args)
equivalent_gaussian_sigma = _newpresto.equivalent_gaussian_sigma

def chi2_logp(*args):
  return _newpresto.chi2_logp(*args)
chi2_logp = _newpresto.chi2_logp

def chi2_sigma(*args):
  return _newpresto.chi2_sigma(*args)
chi2_sigma = _newpresto.chi2_sigma

def candidate_sigma(*args):
  return _newpresto.candidate_sigma(*args)
candidate_sigma = _newpresto.candidate_sigma

def power_for_sigma(*args):
  return _newpresto.power_for_sigma(*args)
power_for_sigma = _newpresto.power_for_sigma

def switch_f_and_p(*args):
  return _newpresto.switch_f_and_p(*args)
switch_f_and_p = _newpresto.switch_f_and_p

def chisqr(*args):
  return _newpresto.chisqr(*args)
chisqr = _newpresto.chisqr

def print_candidate(*args):
  return _newpresto.print_candidate(*args)
print_candidate = _newpresto.print_candidate

def print_bin_candidate(*args):
  return _newpresto.print_bin_candidate(*args)
print_bin_candidate = _newpresto.print_bin_candidate

def read_rzw_cand(*args):
  return _newpresto.read_rzw_cand(*args)
read_rzw_cand = _newpresto.read_rzw_cand

def get_rzw_cand(*args):
  return _newpresto.get_rzw_cand(*args)
get_rzw_cand = _newpresto.get_rzw_cand

def read_bin_cand(*args):
  return _newpresto.read_bin_cand(*args)
read_bin_cand = _newpresto.read_bin_cand

def get_bin_cand(*args):
  return _newpresto.get_bin_cand(*args)
get_bin_cand = _newpresto.get_bin_cand

def dms2rad(*args):
  return _newpresto.dms2rad(*args)
dms2rad = _newpresto.dms2rad

def hms2rad(*args):
  return _newpresto.hms2rad(*args)
hms2rad = _newpresto.hms2rad

def hours2hms(*args):
  return _newpresto.hours2hms(*args)
hours2hms = _newpresto.hours2hms

def deg2dms(*args):
  return _newpresto.deg2dms(*args)
deg2dms = _newpresto.deg2dms

def sphere_ang_diff(*args):
  return _newpresto.sphere_ang_diff(*args)
sphere_ang_diff = _newpresto.sphere_ang_diff
# This file is compatible with both classic and new-style classes.


