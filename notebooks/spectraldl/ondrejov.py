def plot_spectrum(hdulist, axes):
    data = hdulist[1].data
    waves = data.field('spectral')
    fluxes = data.field('flux')

    return axes.plot(waves, fluxes)

def get_waves(hdulist):
    return hdulist[1].data.field('spectral')

def get_fluxes(hdulist):
    return hdulist[1].data.field('flux')

def get_spectrum(hdulist):
    return get_waves(hdulist), get_fluxes(hdulist)

def get_object_name(hdulist):
    return hdulist[1].header['OBJECT']
