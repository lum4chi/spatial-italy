import leafmap

from spatial_italy.map import plot_municipalities_map


def test_plot_municipalities_map():
    m = plot_municipalities_map()
    assert isinstance(m, leafmap.foliumap.Map)
