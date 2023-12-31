import leafmap

from spatial_italy.map import (
    create_italy_map,
    add_municipality_populations_layer,
    add_seismic_zones_layer,
)
from .fixtures.confini import confini_amministrativi_comuni_sample


def test_create_italy_map():
    m = create_italy_map()
    assert isinstance(m, leafmap.foliumap.Map)
    assert m.location == [42.8333, 12.8333]


def test_add_municipality_populations_layer(
    mocker, confini_amministrativi_comuni_sample
):
    mocker.patch(
        "spatial_italy.data.request_confini_amministrativi_comuni",
        return_value=confini_amministrativi_comuni_sample,
    )
    m = create_italy_map()
    n_children_pre = len(m._children)
    add_municipality_populations_layer(m)
    n_children_post = len(m._children)
    assert n_children_pre < n_children_post


def test_add_seismic_zones_layer():
    m = create_italy_map()
    n_children_pre = len(m._children)
    add_seismic_zones_layer(m)
    n_children_post = len(m._children)
    assert n_children_pre < n_children_post
