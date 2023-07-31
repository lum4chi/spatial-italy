import pytest
import geopandas as gpd


@pytest.fixture
def confini_amministrativi_comuni_sample():
    return gpd.GeoDataFrame.from_features(
        {
            "type": "FeatureCollection",
            "features": [
                {
                    "id": "430",
                    "type": "Feature",
                    "properties": {
                        "COD_RIP": 2,
                        "COD_REG": 4,
                        "COD_PROV": 21,
                        "COD_CM": 0,
                        "COD_UTS": 21,
                        "PRO_COM": 21110,
                        "PRO_COM_T": "021110",
                        "COMUNE": "Vandoies",
                        "COMUNE_A": "Vintl",
                        "CC_UTS": 0,
                        "Shape_Leng": 60124.5951433,
                    },
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [708188.5301000001, 5203226.8192],
                                [708362.4009999996, 5188786.8344],
                                [711254.585, 5186030.8365],
                                [705157.9670000002, 5187876.336200001],
                                [698950.1639, 5200366.3248],
                                [708188.5301000001, 5203226.8192],
                            ]
                        ],
                    },
                },
                {
                    "id": "1949",
                    "type": "Feature",
                    "properties": {
                        "COD_RIP": 1,
                        "COD_REG": 3,
                        "COD_PROV": 15,
                        "COD_CM": 215,
                        "COD_UTS": 215,
                        "PRO_COM": 15146,
                        "PRO_COM_T": "015146",
                        "COMUNE": "Milano",
                        "COMUNE_A": None,
                        "CC_UTS": 1,
                        "Shape_Leng": 79382.9940082,
                    },
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [513714.53839999996, 5042508.055600001],
                                [521709.6897, 5039152.573000001],
                                [515069.93039999995, 5025972.139799999],
                                [503349.39190000016, 5034467.8478999995],
                                [513714.53839999996, 5042508.055600001],
                            ]
                        ],
                    },
                },
                {
                    "id": "2072",
                    "type": "Feature",
                    "properties": {
                        "COD_RIP": 1,
                        "COD_REG": 3,
                        "COD_PROV": 16,
                        "COD_CM": 0,
                        "COD_UTS": 16,
                        "PRO_COM": 16065,
                        "PRO_COM_T": "016065",
                        "COMUNE": "Castro",
                        "COMUNE_A": None,
                        "CC_UTS": 0,
                        "Shape_Leng": 7589.85709697,
                    },
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [582769.2432000004, 5072848.3155000005],
                                [583865.2367000002, 5072551.318299999],
                                [582687.2434999999, 5071088.328299999],
                                [581770.2525000004, 5073429.3125],
                                [582769.2432000004, 5072848.3155000005],
                            ]
                        ],
                    },
                },
                {
                    "id": "4796",
                    "type": "Feature",
                    "properties": {
                        "COD_RIP": 3,
                        "COD_REG": 12,
                        "COD_PROV": 58,
                        "COD_CM": 258,
                        "COD_UTS": 258,
                        "PRO_COM": 58091,
                        "PRO_COM_T": "058091",
                        "COMUNE": "Roma",
                        "COMUNE_A": None,
                        "CC_UTS": 1,
                        "Shape_Leng": 279799.733172,
                    },
                    "geometry": {
                        "type": "MultiPolygon",
                        "coordinates": [
                            [
                                [
                                    [770434.4868999999, 4625676.636399999],
                                    [770419.8887, 4625622.495999999],
                                    [770417.0312000001, 4625623.130999999],
                                    [770434.4868999999, 4625676.636399999],
                                ]
                            ],
                            [
                                [
                                    [770196.8558, 4625730.3774],
                                    [770169.1600000001, 4625633.085100001],
                                    [770166.6149000004, 4625634.415899999],
                                    [770196.8558, 4625730.3774],
                                ]
                            ],
                            [
                                [
                                    [769745.5120000001, 4625758.6107],
                                    [769759.6623999998, 4625751.8684],
                                    [769728.4067000002, 4625761.857000001],
                                    [769745.5120000001, 4625758.6107],
                                ]
                            ],
                            [
                                [
                                    [770434.4868999999, 4625676.636399999],
                                    [776488.7397999996, 4666724.043],
                                    [794705.1940000001, 4664510.135399999],
                                    [819987.6591999996, 4642905.863700001],
                                    [797657.4439000003, 4636011.439200001],
                                    [799588.5493999999, 4621634.9628],
                                    [770434.4868999999, 4625676.636399999],
                                ],
                                [
                                    [786799.1048999997, 4645117.684800001],
                                    [786193.7819999997, 4645157.9935],
                                    [785912.8291999996, 4644669.944499999],
                                    [786722.4793999996, 4644501.0393],
                                    [786799.1048999997, 4645117.684800001],
                                ],
                            ],
                            [
                                [
                                    [773307.9467000002, 4670723.6862],
                                    [775830.2657000003, 4668785.8828],
                                    [775716.1940000001, 4667685.2969],
                                    [771325.5010000002, 4667473.772500001],
                                    [773307.9467000002, 4670723.6862],
                                ]
                            ],
                        ],
                    },
                },
                {
                    "id": "5181",
                    "type": "Feature",
                    "properties": {
                        "COD_RIP": 4,
                        "COD_REG": 15,
                        "COD_PROV": 63,
                        "COD_CM": 263,
                        "COD_UTS": 263,
                        "PRO_COM": 63049,
                        "PRO_COM_T": "063049",
                        "COMUNE": "Napoli",
                        "COMUNE_A": None,
                        "CC_UTS": 1,
                        "Shape_Leng": 66700.0022767,
                    },
                    "geometry": {
                        "type": "MultiPolygon",
                        "coordinates": [
                            [
                                [
                                    [937674.6979999999, 4528649.4350000005],
                                    [937737.1826999998, 4528638.746200001],
                                    [937680.6588000003, 4528544.385],
                                    [937648.1924999999, 4528572.110099999],
                                    [937674.6979999999, 4528649.4350000005],
                                ]
                            ],
                            [
                                [
                                    [935240.1772999996, 4530273.402899999],
                                    [935231.5509000001, 4530258.4321],
                                    [935217.7845999999, 4530254.7497000005],
                                    [935228.5581, 4530272.5889],
                                    [935240.1772999996, 4530273.402899999],
                                ]
                            ],
                            [
                                [
                                    [940380.6917000003, 4532519.6328],
                                    [940418.9422000004, 4532560.490499999],
                                    [940437.8265000004, 4532577.728499999],
                                    [940441.2684000004, 4532573.5513],
                                    [940380.6917000003, 4532519.6328],
                                ]
                            ],
                            [
                                [
                                    [940301.3647999996, 4532619.0503],
                                    [940307.8958999999, 4532622.5503],
                                    [940311.1458, 4532621.5503],
                                    [940307.0210999995, 4532618.5503],
                                    [940301.3647999996, 4532619.0503],
                                ]
                            ],
                            [
                                [
                                    [940395.9238999998, 4532715.822000001],
                                    [940393.9011000004, 4532712.8159],
                                    [940337.0283000004, 4532772.420399999],
                                    [940391.2791999998, 4532720.215],
                                    [940395.9238999998, 4532715.822000001],
                                ]
                            ],
                            [
                                [
                                    [947183.5400999999, 4533631.709000001],
                                    [947181.4552999996, 4533629.791999999],
                                    [947164.0420000004, 4533642.2656],
                                    [947167.3294000002, 4533644.3388],
                                    [947183.5400999999, 4533631.709000001],
                                ]
                            ],
                            [
                                [
                                    [940301.3647999996, 4532619.0503],
                                    [933028.7697000001, 4535460.389799999],
                                    [941216.9914999995, 4542341.819399999],
                                    [951318.2132000001, 4536759.5474],
                                    [948698.6782, 4532567.238],
                                    [944676.7476000004, 4534922.011399999],
                                    [943876.7627999997, 4534868.011299999],
                                    [940301.3647999996, 4532619.0503],
                                ]
                            ],
                        ],
                    },
                },
                {
                    "id": "6169",
                    "type": "Feature",
                    "properties": {
                        "COD_RIP": 4,
                        "COD_REG": 16,
                        "COD_PROV": 75,
                        "COD_CM": 0,
                        "COD_UTS": 75,
                        "PRO_COM": 75096,
                        "PRO_COM_T": "075096",
                        "COMUNE": "Castro",
                        "COMUNE_A": None,
                        "CC_UTS": 0,
                        "Shape_Leng": 11264.356382,
                    },
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [1305204.4375999998, 4473425.272],
                                [1305704.1769000003, 4470662.5451],
                                [1304499.9353, 4469789.8058],
                                [1302795.2028, 4470853.8003],
                                [1305204.4375999998, 4473425.272],
                            ]
                        ],
                    },
                },
            ],
            "crs": {
                "type": "name",
                "properties": {"name": "urn:ogc:def:crs:EPSG::32632"},
            },
        }
    )
