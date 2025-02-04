"""PartCompoundAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from PIL.Image import Image

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7704

_PART_COMPOUND_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "PartCompoundAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7349,
        _7350,
        _7351,
        _7353,
        _7355,
        _7356,
        _7357,
        _7359,
        _7360,
        _7362,
        _7363,
        _7364,
        _7365,
        _7367,
        _7368,
        _7369,
        _7370,
        _7372,
        _7374,
        _7375,
        _7377,
        _7378,
        _7380,
        _7381,
        _7383,
        _7385,
        _7386,
        _7388,
        _7390,
        _7391,
        _7392,
        _7394,
        _7396,
        _7398,
        _7399,
        _7400,
        _7401,
        _7402,
        _7404,
        _7405,
        _7406,
        _7407,
        _7409,
        _7410,
        _7411,
        _7413,
        _7415,
        _7417,
        _7418,
        _7420,
        _7421,
        _7423,
        _7424,
        _7425,
        _7426,
        _7427,
        _7428,
        _7429,
        _7430,
        _7431,
        _7433,
        _7435,
        _7436,
        _7437,
        _7438,
        _7439,
        _7440,
        _7442,
        _7443,
        _7445,
        _7446,
        _7447,
        _7449,
        _7450,
        _7452,
        _7453,
        _7455,
        _7456,
        _7458,
        _7459,
        _7461,
        _7462,
        _7463,
        _7464,
        _7465,
        _7466,
        _7467,
        _7468,
        _7470,
        _7471,
        _7472,
        _7473,
        _7474,
        _7476,
        _7477,
        _7479,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7080,
        _7081,
        _7082,
        _7084,
        _7086,
        _7087,
        _7088,
        _7090,
        _7091,
        _7093,
        _7094,
        _7095,
        _7096,
        _7098,
        _7099,
        _7100,
        _7101,
        _7103,
        _7105,
        _7106,
        _7108,
        _7109,
        _7111,
        _7112,
        _7114,
        _7116,
        _7117,
        _7119,
        _7121,
        _7122,
        _7123,
        _7125,
        _7127,
        _7129,
        _7130,
        _7131,
        _7132,
        _7133,
        _7135,
        _7136,
        _7137,
        _7138,
        _7140,
        _7141,
        _7142,
        _7144,
        _7146,
        _7148,
        _7149,
        _7151,
        _7152,
        _7154,
        _7155,
        _7156,
        _7157,
        _7158,
        _7159,
        _7160,
        _7161,
        _7162,
        _7164,
        _7166,
        _7167,
        _7168,
        _7169,
        _7170,
        _7171,
        _7173,
        _7174,
        _7176,
        _7177,
        _7178,
        _7180,
        _7181,
        _7183,
        _7184,
        _7186,
        _7187,
        _7189,
        _7190,
        _7192,
        _7193,
        _7194,
        _7195,
        _7196,
        _7197,
        _7198,
        _7199,
        _7201,
        _7202,
        _7203,
        _7204,
        _7205,
        _7207,
        _7208,
        _7210,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6812,
        _6813,
        _6814,
        _6816,
        _6818,
        _6819,
        _6820,
        _6822,
        _6823,
        _6825,
        _6826,
        _6827,
        _6828,
        _6830,
        _6831,
        _6832,
        _6833,
        _6835,
        _6837,
        _6838,
        _6840,
        _6841,
        _6843,
        _6844,
        _6846,
        _6848,
        _6849,
        _6851,
        _6853,
        _6854,
        _6855,
        _6857,
        _6859,
        _6861,
        _6862,
        _6863,
        _6864,
        _6865,
        _6867,
        _6868,
        _6869,
        _6870,
        _6872,
        _6873,
        _6874,
        _6876,
        _6878,
        _6880,
        _6881,
        _6883,
        _6884,
        _6886,
        _6887,
        _6888,
        _6889,
        _6890,
        _6891,
        _6892,
        _6893,
        _6894,
        _6896,
        _6898,
        _6899,
        _6900,
        _6901,
        _6902,
        _6903,
        _6905,
        _6906,
        _6908,
        _6909,
        _6910,
        _6912,
        _6913,
        _6915,
        _6916,
        _6918,
        _6919,
        _6921,
        _6922,
        _6924,
        _6925,
        _6926,
        _6927,
        _6928,
        _6929,
        _6930,
        _6931,
        _6933,
        _6934,
        _6935,
        _6936,
        _6937,
        _6939,
        _6940,
        _6942,
    )
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6541,
        _6542,
        _6543,
        _6545,
        _6547,
        _6548,
        _6549,
        _6551,
        _6552,
        _6554,
        _6555,
        _6556,
        _6557,
        _6559,
        _6560,
        _6561,
        _6562,
        _6564,
        _6566,
        _6567,
        _6569,
        _6570,
        _6572,
        _6573,
        _6575,
        _6577,
        _6578,
        _6580,
        _6582,
        _6583,
        _6584,
        _6586,
        _6588,
        _6590,
        _6591,
        _6592,
        _6593,
        _6594,
        _6596,
        _6597,
        _6598,
        _6599,
        _6601,
        _6602,
        _6603,
        _6605,
        _6607,
        _6609,
        _6610,
        _6612,
        _6613,
        _6615,
        _6616,
        _6617,
        _6618,
        _6619,
        _6620,
        _6621,
        _6622,
        _6623,
        _6625,
        _6627,
        _6628,
        _6629,
        _6630,
        _6631,
        _6632,
        _6634,
        _6635,
        _6637,
        _6638,
        _6639,
        _6641,
        _6642,
        _6644,
        _6645,
        _6647,
        _6648,
        _6650,
        _6651,
        _6653,
        _6654,
        _6655,
        _6656,
        _6657,
        _6658,
        _6659,
        _6660,
        _6662,
        _6663,
        _6664,
        _6665,
        _6666,
        _6668,
        _6669,
        _6671,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
        _6004,
        _6005,
        _6006,
        _6008,
        _6010,
        _6011,
        _6012,
        _6014,
        _6015,
        _6017,
        _6018,
        _6019,
        _6020,
        _6022,
        _6023,
        _6024,
        _6025,
        _6027,
        _6029,
        _6030,
        _6032,
        _6033,
        _6035,
        _6036,
        _6038,
        _6040,
        _6041,
        _6043,
        _6045,
        _6046,
        _6047,
        _6049,
        _6051,
        _6053,
        _6054,
        _6055,
        _6056,
        _6057,
        _6059,
        _6060,
        _6061,
        _6062,
        _6064,
        _6065,
        _6066,
        _6068,
        _6070,
        _6072,
        _6073,
        _6075,
        _6076,
        _6078,
        _6079,
        _6080,
        _6081,
        _6082,
        _6083,
        _6084,
        _6085,
        _6086,
        _6088,
        _6090,
        _6091,
        _6092,
        _6093,
        _6094,
        _6095,
        _6097,
        _6098,
        _6100,
        _6101,
        _6102,
        _6104,
        _6105,
        _6107,
        _6108,
        _6110,
        _6111,
        _6113,
        _6114,
        _6116,
        _6117,
        _6118,
        _6119,
        _6120,
        _6121,
        _6122,
        _6123,
        _6125,
        _6126,
        _6127,
        _6128,
        _6129,
        _6131,
        _6132,
        _6134,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6268,
        _6269,
        _6270,
        _6272,
        _6274,
        _6275,
        _6276,
        _6278,
        _6279,
        _6281,
        _6282,
        _6283,
        _6284,
        _6286,
        _6287,
        _6288,
        _6289,
        _6291,
        _6293,
        _6294,
        _6296,
        _6297,
        _6299,
        _6300,
        _6302,
        _6304,
        _6305,
        _6307,
        _6309,
        _6310,
        _6311,
        _6313,
        _6315,
        _6317,
        _6318,
        _6319,
        _6320,
        _6321,
        _6323,
        _6324,
        _6325,
        _6326,
        _6328,
        _6329,
        _6330,
        _6332,
        _6334,
        _6336,
        _6337,
        _6339,
        _6340,
        _6342,
        _6343,
        _6344,
        _6345,
        _6346,
        _6347,
        _6348,
        _6349,
        _6350,
        _6352,
        _6354,
        _6355,
        _6356,
        _6357,
        _6358,
        _6359,
        _6361,
        _6362,
        _6364,
        _6365,
        _6366,
        _6368,
        _6369,
        _6371,
        _6372,
        _6374,
        _6375,
        _6377,
        _6378,
        _6380,
        _6381,
        _6382,
        _6383,
        _6384,
        _6385,
        _6386,
        _6387,
        _6389,
        _6390,
        _6391,
        _6392,
        _6393,
        _6395,
        _6396,
        _6398,
    )
    from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
        _5649,
        _5650,
        _5651,
        _5653,
        _5655,
        _5656,
        _5657,
        _5659,
        _5660,
        _5662,
        _5663,
        _5664,
        _5665,
        _5667,
        _5668,
        _5669,
        _5670,
        _5672,
        _5674,
        _5675,
        _5677,
        _5678,
        _5680,
        _5681,
        _5683,
        _5685,
        _5686,
        _5688,
        _5690,
        _5691,
        _5692,
        _5694,
        _5696,
        _5698,
        _5699,
        _5700,
        _5701,
        _5702,
        _5704,
        _5705,
        _5706,
        _5707,
        _5709,
        _5710,
        _5711,
        _5713,
        _5715,
        _5717,
        _5718,
        _5720,
        _5721,
        _5723,
        _5724,
        _5725,
        _5726,
        _5727,
        _5728,
        _5729,
        _5730,
        _5731,
        _5733,
        _5735,
        _5736,
        _5737,
        _5738,
        _5739,
        _5740,
        _5742,
        _5743,
        _5745,
        _5746,
        _5747,
        _5749,
        _5750,
        _5752,
        _5753,
        _5755,
        _5756,
        _5758,
        _5759,
        _5761,
        _5762,
        _5763,
        _5764,
        _5765,
        _5766,
        _5767,
        _5768,
        _5770,
        _5771,
        _5772,
        _5773,
        _5774,
        _5776,
        _5777,
        _5779,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
        _4833,
        _4834,
        _4835,
        _4837,
        _4839,
        _4840,
        _4841,
        _4843,
        _4844,
        _4846,
        _4847,
        _4848,
        _4849,
        _4851,
        _4852,
        _4853,
        _4854,
        _4856,
        _4858,
        _4859,
        _4861,
        _4862,
        _4864,
        _4865,
        _4867,
        _4869,
        _4870,
        _4872,
        _4874,
        _4875,
        _4876,
        _4878,
        _4880,
        _4882,
        _4883,
        _4884,
        _4885,
        _4886,
        _4888,
        _4889,
        _4890,
        _4891,
        _4893,
        _4894,
        _4895,
        _4897,
        _4899,
        _4901,
        _4902,
        _4904,
        _4905,
        _4907,
        _4908,
        _4909,
        _4910,
        _4911,
        _4912,
        _4913,
        _4914,
        _4915,
        _4917,
        _4919,
        _4920,
        _4921,
        _4922,
        _4923,
        _4924,
        _4926,
        _4927,
        _4929,
        _4930,
        _4931,
        _4933,
        _4934,
        _4936,
        _4937,
        _4939,
        _4940,
        _4942,
        _4943,
        _4945,
        _4946,
        _4947,
        _4948,
        _4949,
        _4950,
        _4951,
        _4952,
        _4954,
        _4955,
        _4956,
        _4957,
        _4958,
        _4960,
        _4961,
        _4963,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5360,
        _5361,
        _5362,
        _5364,
        _5366,
        _5367,
        _5368,
        _5370,
        _5371,
        _5373,
        _5374,
        _5375,
        _5376,
        _5378,
        _5379,
        _5380,
        _5381,
        _5383,
        _5385,
        _5386,
        _5388,
        _5389,
        _5391,
        _5392,
        _5394,
        _5396,
        _5397,
        _5399,
        _5401,
        _5402,
        _5403,
        _5405,
        _5407,
        _5409,
        _5410,
        _5411,
        _5412,
        _5413,
        _5415,
        _5416,
        _5417,
        _5418,
        _5420,
        _5421,
        _5422,
        _5424,
        _5426,
        _5428,
        _5429,
        _5431,
        _5432,
        _5434,
        _5435,
        _5436,
        _5437,
        _5438,
        _5439,
        _5440,
        _5441,
        _5442,
        _5444,
        _5446,
        _5447,
        _5448,
        _5449,
        _5450,
        _5451,
        _5453,
        _5454,
        _5456,
        _5457,
        _5458,
        _5460,
        _5461,
        _5463,
        _5464,
        _5466,
        _5467,
        _5469,
        _5470,
        _5472,
        _5473,
        _5474,
        _5475,
        _5476,
        _5477,
        _5478,
        _5479,
        _5481,
        _5482,
        _5483,
        _5484,
        _5485,
        _5487,
        _5488,
        _5490,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5097,
        _5098,
        _5099,
        _5101,
        _5103,
        _5104,
        _5105,
        _5107,
        _5108,
        _5110,
        _5111,
        _5112,
        _5113,
        _5115,
        _5116,
        _5117,
        _5118,
        _5120,
        _5122,
        _5123,
        _5125,
        _5126,
        _5128,
        _5129,
        _5131,
        _5133,
        _5134,
        _5136,
        _5138,
        _5139,
        _5140,
        _5142,
        _5144,
        _5146,
        _5147,
        _5148,
        _5149,
        _5150,
        _5152,
        _5153,
        _5154,
        _5155,
        _5157,
        _5158,
        _5159,
        _5161,
        _5163,
        _5165,
        _5166,
        _5168,
        _5169,
        _5171,
        _5172,
        _5173,
        _5174,
        _5175,
        _5176,
        _5177,
        _5178,
        _5179,
        _5181,
        _5183,
        _5184,
        _5185,
        _5186,
        _5187,
        _5188,
        _5190,
        _5191,
        _5193,
        _5194,
        _5195,
        _5197,
        _5198,
        _5200,
        _5201,
        _5203,
        _5204,
        _5206,
        _5207,
        _5209,
        _5210,
        _5211,
        _5212,
        _5213,
        _5214,
        _5215,
        _5216,
        _5218,
        _5219,
        _5220,
        _5221,
        _5222,
        _5224,
        _5225,
        _5227,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4544,
        _4545,
        _4546,
        _4548,
        _4550,
        _4551,
        _4552,
        _4554,
        _4555,
        _4557,
        _4558,
        _4559,
        _4560,
        _4562,
        _4563,
        _4564,
        _4565,
        _4567,
        _4569,
        _4570,
        _4572,
        _4573,
        _4575,
        _4576,
        _4578,
        _4580,
        _4581,
        _4583,
        _4585,
        _4586,
        _4587,
        _4589,
        _4591,
        _4593,
        _4594,
        _4595,
        _4596,
        _4597,
        _4599,
        _4600,
        _4601,
        _4602,
        _4604,
        _4605,
        _4606,
        _4608,
        _4610,
        _4612,
        _4613,
        _4615,
        _4616,
        _4618,
        _4619,
        _4620,
        _4621,
        _4622,
        _4623,
        _4624,
        _4625,
        _4626,
        _4628,
        _4630,
        _4631,
        _4632,
        _4633,
        _4634,
        _4635,
        _4637,
        _4638,
        _4640,
        _4641,
        _4642,
        _4644,
        _4645,
        _4647,
        _4648,
        _4650,
        _4651,
        _4653,
        _4654,
        _4656,
        _4657,
        _4658,
        _4659,
        _4660,
        _4661,
        _4662,
        _4663,
        _4665,
        _4666,
        _4667,
        _4668,
        _4669,
        _4671,
        _4672,
        _4674,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
        _4264,
        _4265,
        _4266,
        _4268,
        _4270,
        _4271,
        _4272,
        _4274,
        _4275,
        _4277,
        _4278,
        _4279,
        _4280,
        _4282,
        _4283,
        _4284,
        _4285,
        _4287,
        _4289,
        _4290,
        _4292,
        _4293,
        _4295,
        _4296,
        _4298,
        _4300,
        _4301,
        _4303,
        _4305,
        _4306,
        _4307,
        _4309,
        _4311,
        _4313,
        _4314,
        _4315,
        _4316,
        _4317,
        _4319,
        _4320,
        _4321,
        _4322,
        _4324,
        _4325,
        _4326,
        _4328,
        _4330,
        _4332,
        _4333,
        _4335,
        _4336,
        _4338,
        _4339,
        _4340,
        _4341,
        _4342,
        _4343,
        _4344,
        _4345,
        _4346,
        _4348,
        _4350,
        _4351,
        _4352,
        _4353,
        _4354,
        _4355,
        _4357,
        _4358,
        _4360,
        _4361,
        _4362,
        _4364,
        _4365,
        _4367,
        _4368,
        _4370,
        _4371,
        _4373,
        _4374,
        _4376,
        _4377,
        _4378,
        _4379,
        _4380,
        _4381,
        _4382,
        _4383,
        _4385,
        _4386,
        _4387,
        _4388,
        _4389,
        _4391,
        _4392,
        _4394,
    )
    from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
        _3990,
        _3991,
        _3992,
        _3994,
        _3996,
        _3997,
        _3998,
        _4000,
        _4001,
        _4003,
        _4004,
        _4005,
        _4006,
        _4008,
        _4009,
        _4010,
        _4011,
        _4013,
        _4015,
        _4016,
        _4018,
        _4019,
        _4021,
        _4022,
        _4024,
        _4026,
        _4027,
        _4029,
        _4031,
        _4032,
        _4033,
        _4035,
        _4037,
        _4039,
        _4040,
        _4041,
        _4042,
        _4043,
        _4045,
        _4046,
        _4047,
        _4048,
        _4050,
        _4051,
        _4052,
        _4054,
        _4056,
        _4058,
        _4059,
        _4061,
        _4062,
        _4064,
        _4065,
        _4066,
        _4067,
        _4068,
        _4069,
        _4070,
        _4071,
        _4072,
        _4074,
        _4076,
        _4077,
        _4078,
        _4079,
        _4080,
        _4081,
        _4083,
        _4084,
        _4086,
        _4087,
        _4088,
        _4090,
        _4091,
        _4093,
        _4094,
        _4096,
        _4097,
        _4099,
        _4100,
        _4102,
        _4103,
        _4104,
        _4105,
        _4106,
        _4107,
        _4108,
        _4109,
        _4111,
        _4112,
        _4113,
        _4114,
        _4115,
        _4117,
        _4118,
        _4120,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3197,
        _3198,
        _3199,
        _3201,
        _3203,
        _3204,
        _3205,
        _3207,
        _3208,
        _3210,
        _3211,
        _3212,
        _3213,
        _3215,
        _3216,
        _3217,
        _3218,
        _3220,
        _3222,
        _3223,
        _3225,
        _3226,
        _3228,
        _3229,
        _3231,
        _3233,
        _3234,
        _3236,
        _3238,
        _3239,
        _3240,
        _3242,
        _3244,
        _3246,
        _3247,
        _3248,
        _3249,
        _3250,
        _3252,
        _3253,
        _3254,
        _3255,
        _3257,
        _3258,
        _3259,
        _3261,
        _3263,
        _3265,
        _3266,
        _3268,
        _3269,
        _3271,
        _3272,
        _3273,
        _3274,
        _3275,
        _3276,
        _3277,
        _3278,
        _3279,
        _3281,
        _3283,
        _3284,
        _3285,
        _3286,
        _3287,
        _3288,
        _3290,
        _3291,
        _3293,
        _3294,
        _3295,
        _3297,
        _3298,
        _3300,
        _3301,
        _3303,
        _3304,
        _3306,
        _3307,
        _3309,
        _3310,
        _3311,
        _3312,
        _3313,
        _3314,
        _3315,
        _3316,
        _3318,
        _3319,
        _3320,
        _3321,
        _3322,
        _3324,
        _3325,
        _3327,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3723,
        _3724,
        _3725,
        _3727,
        _3729,
        _3730,
        _3731,
        _3733,
        _3734,
        _3736,
        _3737,
        _3738,
        _3739,
        _3741,
        _3742,
        _3743,
        _3744,
        _3746,
        _3748,
        _3749,
        _3751,
        _3752,
        _3754,
        _3755,
        _3757,
        _3759,
        _3760,
        _3762,
        _3764,
        _3765,
        _3766,
        _3768,
        _3770,
        _3772,
        _3773,
        _3774,
        _3775,
        _3776,
        _3778,
        _3779,
        _3780,
        _3781,
        _3783,
        _3784,
        _3785,
        _3787,
        _3789,
        _3791,
        _3792,
        _3794,
        _3795,
        _3797,
        _3798,
        _3799,
        _3800,
        _3801,
        _3802,
        _3803,
        _3804,
        _3805,
        _3807,
        _3809,
        _3810,
        _3811,
        _3812,
        _3813,
        _3814,
        _3816,
        _3817,
        _3819,
        _3820,
        _3821,
        _3823,
        _3824,
        _3826,
        _3827,
        _3829,
        _3830,
        _3832,
        _3833,
        _3835,
        _3836,
        _3837,
        _3838,
        _3839,
        _3840,
        _3841,
        _3842,
        _3844,
        _3845,
        _3846,
        _3847,
        _3848,
        _3850,
        _3851,
        _3853,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3460,
        _3461,
        _3462,
        _3464,
        _3466,
        _3467,
        _3468,
        _3470,
        _3471,
        _3473,
        _3474,
        _3475,
        _3476,
        _3478,
        _3479,
        _3480,
        _3481,
        _3483,
        _3485,
        _3486,
        _3488,
        _3489,
        _3491,
        _3492,
        _3494,
        _3496,
        _3497,
        _3499,
        _3501,
        _3502,
        _3503,
        _3505,
        _3507,
        _3509,
        _3510,
        _3511,
        _3512,
        _3513,
        _3515,
        _3516,
        _3517,
        _3518,
        _3520,
        _3521,
        _3522,
        _3524,
        _3526,
        _3528,
        _3529,
        _3531,
        _3532,
        _3534,
        _3535,
        _3536,
        _3537,
        _3538,
        _3539,
        _3540,
        _3541,
        _3542,
        _3544,
        _3546,
        _3547,
        _3548,
        _3549,
        _3550,
        _3551,
        _3553,
        _3554,
        _3556,
        _3557,
        _3558,
        _3560,
        _3561,
        _3563,
        _3564,
        _3566,
        _3567,
        _3569,
        _3570,
        _3572,
        _3573,
        _3574,
        _3575,
        _3576,
        _3577,
        _3578,
        _3579,
        _3581,
        _3582,
        _3583,
        _3584,
        _3585,
        _3587,
        _3588,
        _3590,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
        _2928,
        _2929,
        _2930,
        _2932,
        _2934,
        _2935,
        _2936,
        _2938,
        _2939,
        _2941,
        _2942,
        _2943,
        _2944,
        _2946,
        _2947,
        _2948,
        _2949,
        _2951,
        _2953,
        _2954,
        _2956,
        _2957,
        _2959,
        _2960,
        _2962,
        _2964,
        _2965,
        _2967,
        _2969,
        _2970,
        _2971,
        _2973,
        _2975,
        _2977,
        _2978,
        _2979,
        _2981,
        _2982,
        _2984,
        _2985,
        _2986,
        _2987,
        _2989,
        _2990,
        _2991,
        _2993,
        _2995,
        _2997,
        _2998,
        _3000,
        _3001,
        _3003,
        _3004,
        _3005,
        _3006,
        _3007,
        _3008,
        _3009,
        _3010,
        _3011,
        _3013,
        _3015,
        _3016,
        _3017,
        _3018,
        _3019,
        _3020,
        _3022,
        _3023,
        _3025,
        _3026,
        _3028,
        _3030,
        _3031,
        _3033,
        _3034,
        _3036,
        _3037,
        _3039,
        _3040,
        _3042,
        _3043,
        _3044,
        _3045,
        _3046,
        _3047,
        _3048,
        _3049,
        _3051,
        _3052,
        _3053,
        _3054,
        _3055,
        _3057,
        _3058,
        _3060,
    )

    Self = TypeVar("Self", bound="PartCompoundAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="PartCompoundAnalysis._Cast_PartCompoundAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartCompoundAnalysis:
    """Special nested class for casting PartCompoundAnalysis to subclasses."""

    __parent__: "PartCompoundAnalysis"

    @property
    def design_entity_compound_analysis(
        self: "CastSelf",
    ) -> "_7704.DesignEntityCompoundAnalysis":
        return self.__parent__._cast(_7704.DesignEntityCompoundAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2726.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2726

        return self.__parent__._cast(_2726.DesignEntityAnalysis)

    @property
    def abstract_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2928.AbstractAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2928,
        )

        return self.__parent__._cast(_2928.AbstractAssemblyCompoundSystemDeflection)

    @property
    def abstract_shaft_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2929.AbstractShaftCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2929,
        )

        return self.__parent__._cast(_2929.AbstractShaftCompoundSystemDeflection)

    @property
    def abstract_shaft_or_housing_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2930.AbstractShaftOrHousingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2930,
        )

        return self.__parent__._cast(
            _2930.AbstractShaftOrHousingCompoundSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2932.AGMAGleasonConicalGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2932,
        )

        return self.__parent__._cast(
            _2932.AGMAGleasonConicalGearCompoundSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2934.AGMAGleasonConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2934,
        )

        return self.__parent__._cast(
            _2934.AGMAGleasonConicalGearSetCompoundSystemDeflection
        )

    @property
    def assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2935.AssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2935,
        )

        return self.__parent__._cast(_2935.AssemblyCompoundSystemDeflection)

    @property
    def bearing_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2936.BearingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2936,
        )

        return self.__parent__._cast(_2936.BearingCompoundSystemDeflection)

    @property
    def belt_drive_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2938.BeltDriveCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2938,
        )

        return self.__parent__._cast(_2938.BeltDriveCompoundSystemDeflection)

    @property
    def bevel_differential_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2939.BevelDifferentialGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2939,
        )

        return self.__parent__._cast(
            _2939.BevelDifferentialGearCompoundSystemDeflection
        )

    @property
    def bevel_differential_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2941.BevelDifferentialGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2941,
        )

        return self.__parent__._cast(
            _2941.BevelDifferentialGearSetCompoundSystemDeflection
        )

    @property
    def bevel_differential_planet_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2942.BevelDifferentialPlanetGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2942,
        )

        return self.__parent__._cast(
            _2942.BevelDifferentialPlanetGearCompoundSystemDeflection
        )

    @property
    def bevel_differential_sun_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2943.BevelDifferentialSunGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2943,
        )

        return self.__parent__._cast(
            _2943.BevelDifferentialSunGearCompoundSystemDeflection
        )

    @property
    def bevel_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2944.BevelGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2944,
        )

        return self.__parent__._cast(_2944.BevelGearCompoundSystemDeflection)

    @property
    def bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2946.BevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2946,
        )

        return self.__parent__._cast(_2946.BevelGearSetCompoundSystemDeflection)

    @property
    def bolt_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2947.BoltCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2947,
        )

        return self.__parent__._cast(_2947.BoltCompoundSystemDeflection)

    @property
    def bolted_joint_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2948.BoltedJointCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2948,
        )

        return self.__parent__._cast(_2948.BoltedJointCompoundSystemDeflection)

    @property
    def clutch_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2949.ClutchCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2949,
        )

        return self.__parent__._cast(_2949.ClutchCompoundSystemDeflection)

    @property
    def clutch_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2951.ClutchHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2951,
        )

        return self.__parent__._cast(_2951.ClutchHalfCompoundSystemDeflection)

    @property
    def component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2953.ComponentCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2953,
        )

        return self.__parent__._cast(_2953.ComponentCompoundSystemDeflection)

    @property
    def concept_coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2954.ConceptCouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2954,
        )

        return self.__parent__._cast(_2954.ConceptCouplingCompoundSystemDeflection)

    @property
    def concept_coupling_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2956.ConceptCouplingHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2956,
        )

        return self.__parent__._cast(_2956.ConceptCouplingHalfCompoundSystemDeflection)

    @property
    def concept_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2957.ConceptGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2957,
        )

        return self.__parent__._cast(_2957.ConceptGearCompoundSystemDeflection)

    @property
    def concept_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2959.ConceptGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2959,
        )

        return self.__parent__._cast(_2959.ConceptGearSetCompoundSystemDeflection)

    @property
    def conical_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2960.ConicalGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2960,
        )

        return self.__parent__._cast(_2960.ConicalGearCompoundSystemDeflection)

    @property
    def conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2962.ConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2962,
        )

        return self.__parent__._cast(_2962.ConicalGearSetCompoundSystemDeflection)

    @property
    def connector_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2964.ConnectorCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2964,
        )

        return self.__parent__._cast(_2964.ConnectorCompoundSystemDeflection)

    @property
    def coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2965.CouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2965,
        )

        return self.__parent__._cast(_2965.CouplingCompoundSystemDeflection)

    @property
    def coupling_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2967.CouplingHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2967,
        )

        return self.__parent__._cast(_2967.CouplingHalfCompoundSystemDeflection)

    @property
    def cvt_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2969.CVTCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2969,
        )

        return self.__parent__._cast(_2969.CVTCompoundSystemDeflection)

    @property
    def cvt_pulley_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2970.CVTPulleyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2970,
        )

        return self.__parent__._cast(_2970.CVTPulleyCompoundSystemDeflection)

    @property
    def cycloidal_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2971.CycloidalAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2971,
        )

        return self.__parent__._cast(_2971.CycloidalAssemblyCompoundSystemDeflection)

    @property
    def cycloidal_disc_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2973.CycloidalDiscCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2973,
        )

        return self.__parent__._cast(_2973.CycloidalDiscCompoundSystemDeflection)

    @property
    def cylindrical_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2975.CylindricalGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2975,
        )

        return self.__parent__._cast(_2975.CylindricalGearCompoundSystemDeflection)

    @property
    def cylindrical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2977.CylindricalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2977,
        )

        return self.__parent__._cast(_2977.CylindricalGearSetCompoundSystemDeflection)

    @property
    def cylindrical_planet_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2978.CylindricalPlanetGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2978,
        )

        return self.__parent__._cast(
            _2978.CylindricalPlanetGearCompoundSystemDeflection
        )

    @property
    def datum_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2979.DatumCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2979,
        )

        return self.__parent__._cast(_2979.DatumCompoundSystemDeflection)

    @property
    def external_cad_model_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2981.ExternalCADModelCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2981,
        )

        return self.__parent__._cast(_2981.ExternalCADModelCompoundSystemDeflection)

    @property
    def face_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2982.FaceGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2982,
        )

        return self.__parent__._cast(_2982.FaceGearCompoundSystemDeflection)

    @property
    def face_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2984.FaceGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2984,
        )

        return self.__parent__._cast(_2984.FaceGearSetCompoundSystemDeflection)

    @property
    def fe_part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2985.FEPartCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2985,
        )

        return self.__parent__._cast(_2985.FEPartCompoundSystemDeflection)

    @property
    def flexible_pin_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2986.FlexiblePinAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2986,
        )

        return self.__parent__._cast(_2986.FlexiblePinAssemblyCompoundSystemDeflection)

    @property
    def gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2987.GearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2987,
        )

        return self.__parent__._cast(_2987.GearCompoundSystemDeflection)

    @property
    def gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2989.GearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2989,
        )

        return self.__parent__._cast(_2989.GearSetCompoundSystemDeflection)

    @property
    def guide_dxf_model_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2990.GuideDxfModelCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2990,
        )

        return self.__parent__._cast(_2990.GuideDxfModelCompoundSystemDeflection)

    @property
    def hypoid_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2991.HypoidGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2991,
        )

        return self.__parent__._cast(_2991.HypoidGearCompoundSystemDeflection)

    @property
    def hypoid_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2993.HypoidGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2993,
        )

        return self.__parent__._cast(_2993.HypoidGearSetCompoundSystemDeflection)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2995.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2995,
        )

        return self.__parent__._cast(
            _2995.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2997.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2997,
        )

        return self.__parent__._cast(
            _2997.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2998.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2998,
        )

        return self.__parent__._cast(
            _2998.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3000.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3000,
        )

        return self.__parent__._cast(
            _3000.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3001.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3001,
        )

        return self.__parent__._cast(
            _3001.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3003.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3003,
        )

        return self.__parent__._cast(
            _3003.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
        )

    @property
    def mass_disc_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3004.MassDiscCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3004,
        )

        return self.__parent__._cast(_3004.MassDiscCompoundSystemDeflection)

    @property
    def measurement_component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3005.MeasurementComponentCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3005,
        )

        return self.__parent__._cast(_3005.MeasurementComponentCompoundSystemDeflection)

    @property
    def microphone_array_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3006.MicrophoneArrayCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3006,
        )

        return self.__parent__._cast(_3006.MicrophoneArrayCompoundSystemDeflection)

    @property
    def microphone_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3007.MicrophoneCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3007,
        )

        return self.__parent__._cast(_3007.MicrophoneCompoundSystemDeflection)

    @property
    def mountable_component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3008.MountableComponentCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3008,
        )

        return self.__parent__._cast(_3008.MountableComponentCompoundSystemDeflection)

    @property
    def oil_seal_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3009.OilSealCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3009,
        )

        return self.__parent__._cast(_3009.OilSealCompoundSystemDeflection)

    @property
    def part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3010.PartCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3010,
        )

        return self.__parent__._cast(_3010.PartCompoundSystemDeflection)

    @property
    def part_to_part_shear_coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3011.PartToPartShearCouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3011,
        )

        return self.__parent__._cast(
            _3011.PartToPartShearCouplingCompoundSystemDeflection
        )

    @property
    def part_to_part_shear_coupling_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3013.PartToPartShearCouplingHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3013,
        )

        return self.__parent__._cast(
            _3013.PartToPartShearCouplingHalfCompoundSystemDeflection
        )

    @property
    def planetary_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3015.PlanetaryGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3015,
        )

        return self.__parent__._cast(_3015.PlanetaryGearSetCompoundSystemDeflection)

    @property
    def planet_carrier_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3016.PlanetCarrierCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3016,
        )

        return self.__parent__._cast(_3016.PlanetCarrierCompoundSystemDeflection)

    @property
    def point_load_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3017.PointLoadCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3017,
        )

        return self.__parent__._cast(_3017.PointLoadCompoundSystemDeflection)

    @property
    def power_load_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3018.PowerLoadCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3018,
        )

        return self.__parent__._cast(_3018.PowerLoadCompoundSystemDeflection)

    @property
    def pulley_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3019.PulleyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3019,
        )

        return self.__parent__._cast(_3019.PulleyCompoundSystemDeflection)

    @property
    def ring_pins_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3020.RingPinsCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3020,
        )

        return self.__parent__._cast(_3020.RingPinsCompoundSystemDeflection)

    @property
    def rolling_ring_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3022.RollingRingAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3022,
        )

        return self.__parent__._cast(_3022.RollingRingAssemblyCompoundSystemDeflection)

    @property
    def rolling_ring_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3023.RollingRingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3023,
        )

        return self.__parent__._cast(_3023.RollingRingCompoundSystemDeflection)

    @property
    def root_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3025.RootAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3025,
        )

        return self.__parent__._cast(_3025.RootAssemblyCompoundSystemDeflection)

    @property
    def shaft_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3026.ShaftCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3026,
        )

        return self.__parent__._cast(_3026.ShaftCompoundSystemDeflection)

    @property
    def shaft_hub_connection_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3028.ShaftHubConnectionCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3028,
        )

        return self.__parent__._cast(_3028.ShaftHubConnectionCompoundSystemDeflection)

    @property
    def specialised_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3030.SpecialisedAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3030,
        )

        return self.__parent__._cast(_3030.SpecialisedAssemblyCompoundSystemDeflection)

    @property
    def spiral_bevel_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3031.SpiralBevelGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3031,
        )

        return self.__parent__._cast(_3031.SpiralBevelGearCompoundSystemDeflection)

    @property
    def spiral_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3033.SpiralBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3033,
        )

        return self.__parent__._cast(_3033.SpiralBevelGearSetCompoundSystemDeflection)

    @property
    def spring_damper_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3034.SpringDamperCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3034,
        )

        return self.__parent__._cast(_3034.SpringDamperCompoundSystemDeflection)

    @property
    def spring_damper_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3036.SpringDamperHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3036,
        )

        return self.__parent__._cast(_3036.SpringDamperHalfCompoundSystemDeflection)

    @property
    def straight_bevel_diff_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3037.StraightBevelDiffGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3037,
        )

        return self.__parent__._cast(
            _3037.StraightBevelDiffGearCompoundSystemDeflection
        )

    @property
    def straight_bevel_diff_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3039.StraightBevelDiffGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3039,
        )

        return self.__parent__._cast(
            _3039.StraightBevelDiffGearSetCompoundSystemDeflection
        )

    @property
    def straight_bevel_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3040.StraightBevelGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3040,
        )

        return self.__parent__._cast(_3040.StraightBevelGearCompoundSystemDeflection)

    @property
    def straight_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3042.StraightBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3042,
        )

        return self.__parent__._cast(_3042.StraightBevelGearSetCompoundSystemDeflection)

    @property
    def straight_bevel_planet_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3043.StraightBevelPlanetGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3043,
        )

        return self.__parent__._cast(
            _3043.StraightBevelPlanetGearCompoundSystemDeflection
        )

    @property
    def straight_bevel_sun_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3044.StraightBevelSunGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3044,
        )

        return self.__parent__._cast(_3044.StraightBevelSunGearCompoundSystemDeflection)

    @property
    def synchroniser_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3045.SynchroniserCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3045,
        )

        return self.__parent__._cast(_3045.SynchroniserCompoundSystemDeflection)

    @property
    def synchroniser_half_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3046.SynchroniserHalfCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3046,
        )

        return self.__parent__._cast(_3046.SynchroniserHalfCompoundSystemDeflection)

    @property
    def synchroniser_part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3047.SynchroniserPartCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3047,
        )

        return self.__parent__._cast(_3047.SynchroniserPartCompoundSystemDeflection)

    @property
    def synchroniser_sleeve_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3048.SynchroniserSleeveCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3048,
        )

        return self.__parent__._cast(_3048.SynchroniserSleeveCompoundSystemDeflection)

    @property
    def torque_converter_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3049.TorqueConverterCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3049,
        )

        return self.__parent__._cast(_3049.TorqueConverterCompoundSystemDeflection)

    @property
    def torque_converter_pump_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3051.TorqueConverterPumpCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3051,
        )

        return self.__parent__._cast(_3051.TorqueConverterPumpCompoundSystemDeflection)

    @property
    def torque_converter_turbine_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3052.TorqueConverterTurbineCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3052,
        )

        return self.__parent__._cast(
            _3052.TorqueConverterTurbineCompoundSystemDeflection
        )

    @property
    def unbalanced_mass_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3053.UnbalancedMassCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3053,
        )

        return self.__parent__._cast(_3053.UnbalancedMassCompoundSystemDeflection)

    @property
    def virtual_component_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3054.VirtualComponentCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3054,
        )

        return self.__parent__._cast(_3054.VirtualComponentCompoundSystemDeflection)

    @property
    def worm_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3055.WormGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3055,
        )

        return self.__parent__._cast(_3055.WormGearCompoundSystemDeflection)

    @property
    def worm_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3057.WormGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3057,
        )

        return self.__parent__._cast(_3057.WormGearSetCompoundSystemDeflection)

    @property
    def zerol_bevel_gear_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3058.ZerolBevelGearCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3058,
        )

        return self.__parent__._cast(_3058.ZerolBevelGearCompoundSystemDeflection)

    @property
    def zerol_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3060.ZerolBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3060,
        )

        return self.__parent__._cast(_3060.ZerolBevelGearSetCompoundSystemDeflection)

    @property
    def abstract_assembly_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3197.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3197,
        )

        return self.__parent__._cast(
            _3197.AbstractAssemblyCompoundSteadyStateSynchronousResponse
        )

    @property
    def abstract_shaft_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3198.AbstractShaftCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3198,
        )

        return self.__parent__._cast(
            _3198.AbstractShaftCompoundSteadyStateSynchronousResponse
        )

    @property
    def abstract_shaft_or_housing_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3199.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3199,
        )

        return self.__parent__._cast(
            _3199.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
        )

    @property
    def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3201.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3201,
        )

        return self.__parent__._cast(
            _3201.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3203.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3203,
        )

        return self.__parent__._cast(
            _3203.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def assembly_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3204.AssemblyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3204,
        )

        return self.__parent__._cast(
            _3204.AssemblyCompoundSteadyStateSynchronousResponse
        )

    @property
    def bearing_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3205.BearingCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3205,
        )

        return self.__parent__._cast(
            _3205.BearingCompoundSteadyStateSynchronousResponse
        )

    @property
    def belt_drive_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3207.BeltDriveCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3207,
        )

        return self.__parent__._cast(
            _3207.BeltDriveCompoundSteadyStateSynchronousResponse
        )

    @property
    def bevel_differential_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3208.BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3208,
        )

        return self.__parent__._cast(
            _3208.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def bevel_differential_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3210.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3210,
        )

        return self.__parent__._cast(
            _3210.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3211.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3211,
        )

        return self.__parent__._cast(
            _3211.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3212.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3212,
        )

        return self.__parent__._cast(
            _3212.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def bevel_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3213.BevelGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3213,
        )

        return self.__parent__._cast(
            _3213.BevelGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def bevel_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3215.BevelGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3215,
        )

        return self.__parent__._cast(
            _3215.BevelGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def bolt_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3216.BoltCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3216,
        )

        return self.__parent__._cast(_3216.BoltCompoundSteadyStateSynchronousResponse)

    @property
    def bolted_joint_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3217.BoltedJointCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3217,
        )

        return self.__parent__._cast(
            _3217.BoltedJointCompoundSteadyStateSynchronousResponse
        )

    @property
    def clutch_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3218.ClutchCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3218,
        )

        return self.__parent__._cast(_3218.ClutchCompoundSteadyStateSynchronousResponse)

    @property
    def clutch_half_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3220.ClutchHalfCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3220,
        )

        return self.__parent__._cast(
            _3220.ClutchHalfCompoundSteadyStateSynchronousResponse
        )

    @property
    def component_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3222.ComponentCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3222,
        )

        return self.__parent__._cast(
            _3222.ComponentCompoundSteadyStateSynchronousResponse
        )

    @property
    def concept_coupling_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3223.ConceptCouplingCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3223,
        )

        return self.__parent__._cast(
            _3223.ConceptCouplingCompoundSteadyStateSynchronousResponse
        )

    @property
    def concept_coupling_half_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3225.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3225,
        )

        return self.__parent__._cast(
            _3225.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse
        )

    @property
    def concept_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3226.ConceptGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3226,
        )

        return self.__parent__._cast(
            _3226.ConceptGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def concept_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3228.ConceptGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3228,
        )

        return self.__parent__._cast(
            _3228.ConceptGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def conical_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3229.ConicalGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3229,
        )

        return self.__parent__._cast(
            _3229.ConicalGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def conical_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3231.ConicalGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3231,
        )

        return self.__parent__._cast(
            _3231.ConicalGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def connector_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3233.ConnectorCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3233,
        )

        return self.__parent__._cast(
            _3233.ConnectorCompoundSteadyStateSynchronousResponse
        )

    @property
    def coupling_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3234.CouplingCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3234,
        )

        return self.__parent__._cast(
            _3234.CouplingCompoundSteadyStateSynchronousResponse
        )

    @property
    def coupling_half_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3236.CouplingHalfCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3236,
        )

        return self.__parent__._cast(
            _3236.CouplingHalfCompoundSteadyStateSynchronousResponse
        )

    @property
    def cvt_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3238.CVTCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3238,
        )

        return self.__parent__._cast(_3238.CVTCompoundSteadyStateSynchronousResponse)

    @property
    def cvt_pulley_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3239.CVTPulleyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3239,
        )

        return self.__parent__._cast(
            _3239.CVTPulleyCompoundSteadyStateSynchronousResponse
        )

    @property
    def cycloidal_assembly_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3240.CycloidalAssemblyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3240,
        )

        return self.__parent__._cast(
            _3240.CycloidalAssemblyCompoundSteadyStateSynchronousResponse
        )

    @property
    def cycloidal_disc_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3242.CycloidalDiscCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3242,
        )

        return self.__parent__._cast(
            _3242.CycloidalDiscCompoundSteadyStateSynchronousResponse
        )

    @property
    def cylindrical_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3244.CylindricalGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3244,
        )

        return self.__parent__._cast(
            _3244.CylindricalGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def cylindrical_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3246.CylindricalGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3246,
        )

        return self.__parent__._cast(
            _3246.CylindricalGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def cylindrical_planet_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3247.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3247,
        )

        return self.__parent__._cast(
            _3247.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def datum_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3248.DatumCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3248,
        )

        return self.__parent__._cast(_3248.DatumCompoundSteadyStateSynchronousResponse)

    @property
    def external_cad_model_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3249.ExternalCADModelCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3249,
        )

        return self.__parent__._cast(
            _3249.ExternalCADModelCompoundSteadyStateSynchronousResponse
        )

    @property
    def face_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3250.FaceGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3250,
        )

        return self.__parent__._cast(
            _3250.FaceGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def face_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3252.FaceGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3252,
        )

        return self.__parent__._cast(
            _3252.FaceGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def fe_part_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3253.FEPartCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3253,
        )

        return self.__parent__._cast(_3253.FEPartCompoundSteadyStateSynchronousResponse)

    @property
    def flexible_pin_assembly_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3254.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3254,
        )

        return self.__parent__._cast(
            _3254.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse
        )

    @property
    def gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3255.GearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3255,
        )

        return self.__parent__._cast(_3255.GearCompoundSteadyStateSynchronousResponse)

    @property
    def gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3257.GearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3257,
        )

        return self.__parent__._cast(
            _3257.GearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def guide_dxf_model_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3258.GuideDxfModelCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3258,
        )

        return self.__parent__._cast(
            _3258.GuideDxfModelCompoundSteadyStateSynchronousResponse
        )

    @property
    def hypoid_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3259.HypoidGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3259,
        )

        return self.__parent__._cast(
            _3259.HypoidGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def hypoid_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3261.HypoidGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3261,
        )

        return self.__parent__._cast(
            _3261.HypoidGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3263.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3263,
        )

        return self.__parent__._cast(
            _3263.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3265.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3265,
        )

        return self.__parent__._cast(
            _3265.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> (
        "_3266.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3266,
        )

        return self.__parent__._cast(
            _3266.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3268.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3268,
        )

        return self.__parent__._cast(
            _3268.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3269.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3269,
        )

        return self.__parent__._cast(
            _3269.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3271.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3271,
        )

        return self.__parent__._cast(
            _3271.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def mass_disc_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3272.MassDiscCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3272,
        )

        return self.__parent__._cast(
            _3272.MassDiscCompoundSteadyStateSynchronousResponse
        )

    @property
    def measurement_component_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3273.MeasurementComponentCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3273,
        )

        return self.__parent__._cast(
            _3273.MeasurementComponentCompoundSteadyStateSynchronousResponse
        )

    @property
    def microphone_array_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3274.MicrophoneArrayCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3274,
        )

        return self.__parent__._cast(
            _3274.MicrophoneArrayCompoundSteadyStateSynchronousResponse
        )

    @property
    def microphone_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3275.MicrophoneCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3275,
        )

        return self.__parent__._cast(
            _3275.MicrophoneCompoundSteadyStateSynchronousResponse
        )

    @property
    def mountable_component_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3276.MountableComponentCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3276,
        )

        return self.__parent__._cast(
            _3276.MountableComponentCompoundSteadyStateSynchronousResponse
        )

    @property
    def oil_seal_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3277.OilSealCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3277,
        )

        return self.__parent__._cast(
            _3277.OilSealCompoundSteadyStateSynchronousResponse
        )

    @property
    def part_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3278.PartCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3278,
        )

        return self.__parent__._cast(_3278.PartCompoundSteadyStateSynchronousResponse)

    @property
    def part_to_part_shear_coupling_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3279.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3279,
        )

        return self.__parent__._cast(
            _3279.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse
        )

    @property
    def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3281.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3281,
        )

        return self.__parent__._cast(
            _3281.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse
        )

    @property
    def planetary_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3283.PlanetaryGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3283,
        )

        return self.__parent__._cast(
            _3283.PlanetaryGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def planet_carrier_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3284.PlanetCarrierCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3284,
        )

        return self.__parent__._cast(
            _3284.PlanetCarrierCompoundSteadyStateSynchronousResponse
        )

    @property
    def point_load_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3285.PointLoadCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3285,
        )

        return self.__parent__._cast(
            _3285.PointLoadCompoundSteadyStateSynchronousResponse
        )

    @property
    def power_load_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3286.PowerLoadCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3286,
        )

        return self.__parent__._cast(
            _3286.PowerLoadCompoundSteadyStateSynchronousResponse
        )

    @property
    def pulley_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3287.PulleyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3287,
        )

        return self.__parent__._cast(_3287.PulleyCompoundSteadyStateSynchronousResponse)

    @property
    def ring_pins_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3288.RingPinsCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3288,
        )

        return self.__parent__._cast(
            _3288.RingPinsCompoundSteadyStateSynchronousResponse
        )

    @property
    def rolling_ring_assembly_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3290.RollingRingAssemblyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3290,
        )

        return self.__parent__._cast(
            _3290.RollingRingAssemblyCompoundSteadyStateSynchronousResponse
        )

    @property
    def rolling_ring_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3291.RollingRingCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3291,
        )

        return self.__parent__._cast(
            _3291.RollingRingCompoundSteadyStateSynchronousResponse
        )

    @property
    def root_assembly_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3293.RootAssemblyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3293,
        )

        return self.__parent__._cast(
            _3293.RootAssemblyCompoundSteadyStateSynchronousResponse
        )

    @property
    def shaft_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3294.ShaftCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3294,
        )

        return self.__parent__._cast(_3294.ShaftCompoundSteadyStateSynchronousResponse)

    @property
    def shaft_hub_connection_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3295.ShaftHubConnectionCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3295,
        )

        return self.__parent__._cast(
            _3295.ShaftHubConnectionCompoundSteadyStateSynchronousResponse
        )

    @property
    def specialised_assembly_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3297.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3297,
        )

        return self.__parent__._cast(
            _3297.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
        )

    @property
    def spiral_bevel_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3298.SpiralBevelGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3298,
        )

        return self.__parent__._cast(
            _3298.SpiralBevelGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3300.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3300,
        )

        return self.__parent__._cast(
            _3300.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def spring_damper_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3301.SpringDamperCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3301,
        )

        return self.__parent__._cast(
            _3301.SpringDamperCompoundSteadyStateSynchronousResponse
        )

    @property
    def spring_damper_half_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3303.SpringDamperHalfCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3303,
        )

        return self.__parent__._cast(
            _3303.SpringDamperHalfCompoundSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3304.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3304,
        )

        return self.__parent__._cast(
            _3304.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3306.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3306,
        )

        return self.__parent__._cast(
            _3306.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3307.StraightBevelGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3307,
        )

        return self.__parent__._cast(
            _3307.StraightBevelGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3309.StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3309,
        )

        return self.__parent__._cast(
            _3309.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_planet_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3310.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3310,
        )

        return self.__parent__._cast(
            _3310.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3311.StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3311,
        )

        return self.__parent__._cast(
            _3311.StraightBevelSunGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def synchroniser_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3312.SynchroniserCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3312,
        )

        return self.__parent__._cast(
            _3312.SynchroniserCompoundSteadyStateSynchronousResponse
        )

    @property
    def synchroniser_half_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3313.SynchroniserHalfCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3313,
        )

        return self.__parent__._cast(
            _3313.SynchroniserHalfCompoundSteadyStateSynchronousResponse
        )

    @property
    def synchroniser_part_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3314.SynchroniserPartCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3314,
        )

        return self.__parent__._cast(
            _3314.SynchroniserPartCompoundSteadyStateSynchronousResponse
        )

    @property
    def synchroniser_sleeve_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3315.SynchroniserSleeveCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3315,
        )

        return self.__parent__._cast(
            _3315.SynchroniserSleeveCompoundSteadyStateSynchronousResponse
        )

    @property
    def torque_converter_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3316.TorqueConverterCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3316,
        )

        return self.__parent__._cast(
            _3316.TorqueConverterCompoundSteadyStateSynchronousResponse
        )

    @property
    def torque_converter_pump_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3318.TorqueConverterPumpCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3318,
        )

        return self.__parent__._cast(
            _3318.TorqueConverterPumpCompoundSteadyStateSynchronousResponse
        )

    @property
    def torque_converter_turbine_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3319.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3319,
        )

        return self.__parent__._cast(
            _3319.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse
        )

    @property
    def unbalanced_mass_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3320.UnbalancedMassCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3320,
        )

        return self.__parent__._cast(
            _3320.UnbalancedMassCompoundSteadyStateSynchronousResponse
        )

    @property
    def virtual_component_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3321.VirtualComponentCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3321,
        )

        return self.__parent__._cast(
            _3321.VirtualComponentCompoundSteadyStateSynchronousResponse
        )

    @property
    def worm_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3322.WormGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3322,
        )

        return self.__parent__._cast(
            _3322.WormGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def worm_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3324.WormGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3324,
        )

        return self.__parent__._cast(
            _3324.WormGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def zerol_bevel_gear_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3325.ZerolBevelGearCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3325,
        )

        return self.__parent__._cast(
            _3325.ZerolBevelGearCompoundSteadyStateSynchronousResponse
        )

    @property
    def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3327.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3327,
        )

        return self.__parent__._cast(
            _3327.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
        )

    @property
    def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3460.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3460,
        )

        return self.__parent__._cast(
            _3460.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def abstract_shaft_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3461.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3461,
        )

        return self.__parent__._cast(
            _3461.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def abstract_shaft_or_housing_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3462.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3462,
        )

        return self.__parent__._cast(
            _3462.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3464.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3464,
        )

        return self.__parent__._cast(
            _3464.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> (
        "_3466.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3466,
        )

        return self.__parent__._cast(
            _3466.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def assembly_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3467.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3467,
        )

        return self.__parent__._cast(
            _3467.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bearing_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3468.BearingCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3468,
        )

        return self.__parent__._cast(
            _3468.BearingCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def belt_drive_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3470.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3470,
        )

        return self.__parent__._cast(
            _3470.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3471.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3471,
        )

        return self.__parent__._cast(
            _3471.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3473.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3473,
        )

        return self.__parent__._cast(
            _3473.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3474.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3474,
        )

        return self.__parent__._cast(
            _3474.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3475.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3475,
        )

        return self.__parent__._cast(
            _3475.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3476.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3476,
        )

        return self.__parent__._cast(
            _3476.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3478.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3478,
        )

        return self.__parent__._cast(
            _3478.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bolt_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3479.BoltCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3479,
        )

        return self.__parent__._cast(
            _3479.BoltCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bolted_joint_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3480.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3480,
        )

        return self.__parent__._cast(
            _3480.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def clutch_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3481.ClutchCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3481,
        )

        return self.__parent__._cast(
            _3481.ClutchCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3483.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3483,
        )

        return self.__parent__._cast(
            _3483.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def component_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3485.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3485,
        )

        return self.__parent__._cast(
            _3485.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def concept_coupling_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3486.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3486,
        )

        return self.__parent__._cast(
            _3486.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3488.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3488,
        )

        return self.__parent__._cast(
            _3488.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def concept_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3489.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3489,
        )

        return self.__parent__._cast(
            _3489.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def concept_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3491.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3491,
        )

        return self.__parent__._cast(
            _3491.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3492.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3492,
        )

        return self.__parent__._cast(
            _3492.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3494.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3494,
        )

        return self.__parent__._cast(
            _3494.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def connector_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3496.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3496,
        )

        return self.__parent__._cast(
            _3496.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def coupling_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3497.CouplingCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3497,
        )

        return self.__parent__._cast(
            _3497.CouplingCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3499.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3499,
        )

        return self.__parent__._cast(
            _3499.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cvt_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3501.CVTCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3501,
        )

        return self.__parent__._cast(
            _3501.CVTCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3502.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3502,
        )

        return self.__parent__._cast(
            _3502.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cycloidal_assembly_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3503.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3503,
        )

        return self.__parent__._cast(
            _3503.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cycloidal_disc_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3505.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3505,
        )

        return self.__parent__._cast(
            _3505.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3507.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3507,
        )

        return self.__parent__._cast(
            _3507.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cylindrical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3509.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3509,
        )

        return self.__parent__._cast(
            _3509.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3510.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3510,
        )

        return self.__parent__._cast(
            _3510.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def datum_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3511.DatumCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3511,
        )

        return self.__parent__._cast(
            _3511.DatumCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def external_cad_model_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3512.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3512,
        )

        return self.__parent__._cast(
            _3512.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def face_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3513.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3513,
        )

        return self.__parent__._cast(
            _3513.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def face_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3515.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3515,
        )

        return self.__parent__._cast(
            _3515.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def fe_part_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3516.FEPartCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3516,
        )

        return self.__parent__._cast(
            _3516.FEPartCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def flexible_pin_assembly_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3517.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3517,
        )

        return self.__parent__._cast(
            _3517.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3518.GearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3518,
        )

        return self.__parent__._cast(
            _3518.GearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3520.GearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3520,
        )

        return self.__parent__._cast(
            _3520.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def guide_dxf_model_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3521.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3521,
        )

        return self.__parent__._cast(
            _3521.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3522.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3522,
        )

        return self.__parent__._cast(
            _3522.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3524.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3524,
        )

        return self.__parent__._cast(
            _3524.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3526.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3526,
        )

        return self.__parent__._cast(
            _3526.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3528.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3528,
        )

        return self.__parent__._cast(
            _3528.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3529.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3529,
        )

        return self.__parent__._cast(
            _3529.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3531.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3531,
        )

        return self.__parent__._cast(
            _3531.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3532.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3532,
        )

        return self.__parent__._cast(
            _3532.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3534.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3534,
        )

        return self.__parent__._cast(
            _3534.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def mass_disc_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3535.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3535,
        )

        return self.__parent__._cast(
            _3535.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def measurement_component_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3536.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3536,
        )

        return self.__parent__._cast(
            _3536.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def microphone_array_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3537.MicrophoneArrayCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3537,
        )

        return self.__parent__._cast(
            _3537.MicrophoneArrayCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def microphone_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3538.MicrophoneCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3538,
        )

        return self.__parent__._cast(
            _3538.MicrophoneCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3539.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3539,
        )

        return self.__parent__._cast(
            _3539.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def oil_seal_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3540.OilSealCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3540,
        )

        return self.__parent__._cast(
            _3540.OilSealCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def part_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3541.PartCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3541,
        )

        return self.__parent__._cast(
            _3541.PartCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def part_to_part_shear_coupling_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3542.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3542,
        )

        return self.__parent__._cast(
            _3542.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3544.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3544,
        )

        return self.__parent__._cast(
            _3544.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def planetary_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3546.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3546,
        )

        return self.__parent__._cast(
            _3546.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def planet_carrier_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3547.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3547,
        )

        return self.__parent__._cast(
            _3547.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def point_load_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3548.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3548,
        )

        return self.__parent__._cast(
            _3548.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def power_load_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3549.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3549,
        )

        return self.__parent__._cast(
            _3549.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def pulley_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3550.PulleyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3550,
        )

        return self.__parent__._cast(
            _3550.PulleyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def ring_pins_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3551.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3551,
        )

        return self.__parent__._cast(
            _3551.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def rolling_ring_assembly_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3553.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3553,
        )

        return self.__parent__._cast(
            _3553.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3554.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3554,
        )

        return self.__parent__._cast(
            _3554.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def root_assembly_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3556.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3556,
        )

        return self.__parent__._cast(
            _3556.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def shaft_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3557.ShaftCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3557,
        )

        return self.__parent__._cast(
            _3557.ShaftCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def shaft_hub_connection_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3558.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3558,
        )

        return self.__parent__._cast(
            _3558.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3560.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3560,
        )

        return self.__parent__._cast(
            _3560.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3561.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3561,
        )

        return self.__parent__._cast(
            _3561.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3563.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3563,
        )

        return self.__parent__._cast(
            _3563.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def spring_damper_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3564.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3564,
        )

        return self.__parent__._cast(
            _3564.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3566.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3566,
        )

        return self.__parent__._cast(
            _3566.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3567.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3567,
        )

        return self.__parent__._cast(
            _3567.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3569.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3569,
        )

        return self.__parent__._cast(
            _3569.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3570.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3570,
        )

        return self.__parent__._cast(
            _3570.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3572.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3572,
        )

        return self.__parent__._cast(
            _3572.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3573.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3573,
        )

        return self.__parent__._cast(
            _3573.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3574.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3574,
        )

        return self.__parent__._cast(
            _3574.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3575.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3575,
        )

        return self.__parent__._cast(
            _3575.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3576.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3576,
        )

        return self.__parent__._cast(
            _3576.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3577.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3577,
        )

        return self.__parent__._cast(
            _3577.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3578.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3578,
        )

        return self.__parent__._cast(
            _3578.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def torque_converter_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3579.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3579,
        )

        return self.__parent__._cast(
            _3579.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3581.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3581,
        )

        return self.__parent__._cast(
            _3581.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3582.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3582,
        )

        return self.__parent__._cast(
            _3582.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def unbalanced_mass_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3583.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3583,
        )

        return self.__parent__._cast(
            _3583.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3584.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3584,
        )

        return self.__parent__._cast(
            _3584.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def worm_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3585.WormGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3585,
        )

        return self.__parent__._cast(
            _3585.WormGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def worm_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3587.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3587,
        )

        return self.__parent__._cast(
            _3587.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3588.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3588,
        )

        return self.__parent__._cast(
            _3588.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def zerol_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3590.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
            _3590,
        )

        return self.__parent__._cast(
            _3590.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3723.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3723,
        )

        return self.__parent__._cast(
            _3723.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3724.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3724,
        )

        return self.__parent__._cast(
            _3724.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3725.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3725,
        )

        return self.__parent__._cast(
            _3725.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3727.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3727,
        )

        return self.__parent__._cast(
            _3727.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_3729.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3729,
        )

        return self.__parent__._cast(
            _3729.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3730.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3730,
        )

        return self.__parent__._cast(
            _3730.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bearing_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3731.BearingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3731,
        )

        return self.__parent__._cast(
            _3731.BearingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def belt_drive_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3733.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3733,
        )

        return self.__parent__._cast(
            _3733.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3734.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3734,
        )

        return self.__parent__._cast(
            _3734.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3736.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3736,
        )

        return self.__parent__._cast(
            _3736.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3737.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3737,
        )

        return self.__parent__._cast(
            _3737.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3738.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3738,
        )

        return self.__parent__._cast(
            _3738.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3739.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3739,
        )

        return self.__parent__._cast(
            _3739.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3741.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3741,
        )

        return self.__parent__._cast(
            _3741.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bolt_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3742.BoltCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3742,
        )

        return self.__parent__._cast(
            _3742.BoltCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bolted_joint_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3743.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3743,
        )

        return self.__parent__._cast(
            _3743.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def clutch_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3744.ClutchCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3744,
        )

        return self.__parent__._cast(
            _3744.ClutchCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3746.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3746,
        )

        return self.__parent__._cast(
            _3746.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3748.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3748,
        )

        return self.__parent__._cast(
            _3748.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_coupling_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3749.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3749,
        )

        return self.__parent__._cast(
            _3749.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3751.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3751,
        )

        return self.__parent__._cast(
            _3751.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3752.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3752,
        )

        return self.__parent__._cast(
            _3752.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3754.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3754,
        )

        return self.__parent__._cast(
            _3754.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3755.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3755,
        )

        return self.__parent__._cast(
            _3755.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3757.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3757,
        )

        return self.__parent__._cast(
            _3757.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def connector_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3759.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3759,
        )

        return self.__parent__._cast(
            _3759.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def coupling_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3760.CouplingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3760,
        )

        return self.__parent__._cast(
            _3760.CouplingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3762.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3762,
        )

        return self.__parent__._cast(
            _3762.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cvt_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3764.CVTCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3764,
        )

        return self.__parent__._cast(
            _3764.CVTCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3765.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3765,
        )

        return self.__parent__._cast(
            _3765.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cycloidal_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3766.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3766,
        )

        return self.__parent__._cast(
            _3766.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3768.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3768,
        )

        return self.__parent__._cast(
            _3768.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3770.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3770,
        )

        return self.__parent__._cast(
            _3770.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cylindrical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3772.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3772,
        )

        return self.__parent__._cast(
            _3772.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3773.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3773,
        )

        return self.__parent__._cast(
            _3773.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def datum_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3774.DatumCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3774,
        )

        return self.__parent__._cast(
            _3774.DatumCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def external_cad_model_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3775.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3775,
        )

        return self.__parent__._cast(
            _3775.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def face_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3776.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3776,
        )

        return self.__parent__._cast(
            _3776.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def face_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3778.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3778,
        )

        return self.__parent__._cast(
            _3778.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def fe_part_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3779.FEPartCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3779,
        )

        return self.__parent__._cast(
            _3779.FEPartCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def flexible_pin_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3780.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3780,
        )

        return self.__parent__._cast(
            _3780.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3781.GearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3781,
        )

        return self.__parent__._cast(
            _3781.GearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3783.GearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3783,
        )

        return self.__parent__._cast(
            _3783.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def guide_dxf_model_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3784.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3784,
        )

        return self.__parent__._cast(
            _3784.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3785.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3785,
        )

        return self.__parent__._cast(
            _3785.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3787.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3787,
        )

        return self.__parent__._cast(
            _3787.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3789.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3789,
        )

        return self.__parent__._cast(
            _3789.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3791.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3791,
        )

        return self.__parent__._cast(
            _3791.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3792.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3792,
        )

        return self.__parent__._cast(
            _3792.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3794.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3794,
        )

        return self.__parent__._cast(
            _3794.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3795.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3795,
        )

        return self.__parent__._cast(
            _3795.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3797.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3797,
        )

        return self.__parent__._cast(
            _3797.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def mass_disc_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3798.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3798,
        )

        return self.__parent__._cast(
            _3798.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def measurement_component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3799.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3799,
        )

        return self.__parent__._cast(
            _3799.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def microphone_array_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3800.MicrophoneArrayCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3800,
        )

        return self.__parent__._cast(
            _3800.MicrophoneArrayCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def microphone_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3801.MicrophoneCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3801,
        )

        return self.__parent__._cast(
            _3801.MicrophoneCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3802.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3802,
        )

        return self.__parent__._cast(
            _3802.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def oil_seal_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3803.OilSealCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3803,
        )

        return self.__parent__._cast(
            _3803.OilSealCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3804.PartCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3804,
        )

        return self.__parent__._cast(
            _3804.PartCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3805.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3805,
        )

        return self.__parent__._cast(
            _3805.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3807.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3807,
        )

        return self.__parent__._cast(
            _3807.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def planetary_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3809.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3809,
        )

        return self.__parent__._cast(
            _3809.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def planet_carrier_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3810.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3810,
        )

        return self.__parent__._cast(
            _3810.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def point_load_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3811.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3811,
        )

        return self.__parent__._cast(
            _3811.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def power_load_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3812.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3812,
        )

        return self.__parent__._cast(
            _3812.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def pulley_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3813.PulleyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3813,
        )

        return self.__parent__._cast(
            _3813.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def ring_pins_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3814.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3814,
        )

        return self.__parent__._cast(
            _3814.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def rolling_ring_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3816.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3816,
        )

        return self.__parent__._cast(
            _3816.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3817.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3817,
        )

        return self.__parent__._cast(
            _3817.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def root_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3819.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3819,
        )

        return self.__parent__._cast(
            _3819.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def shaft_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3820.ShaftCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3820,
        )

        return self.__parent__._cast(
            _3820.ShaftCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3821.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3821,
        )

        return self.__parent__._cast(
            _3821.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3823.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3823,
        )

        return self.__parent__._cast(
            _3823.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3824.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3824,
        )

        return self.__parent__._cast(
            _3824.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3826.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3826,
        )

        return self.__parent__._cast(
            _3826.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spring_damper_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3827.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3827,
        )

        return self.__parent__._cast(
            _3827.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3829.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3829,
        )

        return self.__parent__._cast(
            _3829.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3830.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3830,
        )

        return self.__parent__._cast(
            _3830.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3832.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3832,
        )

        return self.__parent__._cast(
            _3832.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3833.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3833,
        )

        return self.__parent__._cast(
            _3833.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3835.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3835,
        )

        return self.__parent__._cast(
            _3835.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3836.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3836,
        )

        return self.__parent__._cast(
            _3836.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3837.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3837,
        )

        return self.__parent__._cast(
            _3837.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3838.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3838,
        )

        return self.__parent__._cast(
            _3838.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3839.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3839,
        )

        return self.__parent__._cast(
            _3839.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3840.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3840,
        )

        return self.__parent__._cast(
            _3840.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3841.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3841,
        )

        return self.__parent__._cast(
            _3841.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3842.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3842,
        )

        return self.__parent__._cast(
            _3842.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3844.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3844,
        )

        return self.__parent__._cast(
            _3844.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3845.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3845,
        )

        return self.__parent__._cast(
            _3845.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3846.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3846,
        )

        return self.__parent__._cast(
            _3846.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def virtual_component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3847.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3847,
        )

        return self.__parent__._cast(
            _3847.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def worm_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3848.WormGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3848,
        )

        return self.__parent__._cast(
            _3848.WormGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def worm_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3850.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3850,
        )

        return self.__parent__._cast(
            _3850.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3851.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3851,
        )

        return self.__parent__._cast(
            _3851.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3853.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3853,
        )

        return self.__parent__._cast(
            _3853.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def abstract_assembly_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_3990.AbstractAssemblyCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _3990,
        )

        return self.__parent__._cast(_3990.AbstractAssemblyCompoundStabilityAnalysis)

    @property
    def abstract_shaft_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_3991.AbstractShaftCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _3991,
        )

        return self.__parent__._cast(_3991.AbstractShaftCompoundStabilityAnalysis)

    @property
    def abstract_shaft_or_housing_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_3992.AbstractShaftOrHousingCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _3992,
        )

        return self.__parent__._cast(
            _3992.AbstractShaftOrHousingCompoundStabilityAnalysis
        )

    @property
    def agma_gleason_conical_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_3994.AGMAGleasonConicalGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _3994,
        )

        return self.__parent__._cast(
            _3994.AGMAGleasonConicalGearCompoundStabilityAnalysis
        )

    @property
    def agma_gleason_conical_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_3996.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _3996,
        )

        return self.__parent__._cast(
            _3996.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
        )

    @property
    def assembly_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_3997.AssemblyCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _3997,
        )

        return self.__parent__._cast(_3997.AssemblyCompoundStabilityAnalysis)

    @property
    def bearing_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_3998.BearingCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _3998,
        )

        return self.__parent__._cast(_3998.BearingCompoundStabilityAnalysis)

    @property
    def belt_drive_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4000.BeltDriveCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4000,
        )

        return self.__parent__._cast(_4000.BeltDriveCompoundStabilityAnalysis)

    @property
    def bevel_differential_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4001.BevelDifferentialGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4001,
        )

        return self.__parent__._cast(
            _4001.BevelDifferentialGearCompoundStabilityAnalysis
        )

    @property
    def bevel_differential_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4003.BevelDifferentialGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4003,
        )

        return self.__parent__._cast(
            _4003.BevelDifferentialGearSetCompoundStabilityAnalysis
        )

    @property
    def bevel_differential_planet_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4004.BevelDifferentialPlanetGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4004,
        )

        return self.__parent__._cast(
            _4004.BevelDifferentialPlanetGearCompoundStabilityAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4005.BevelDifferentialSunGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4005,
        )

        return self.__parent__._cast(
            _4005.BevelDifferentialSunGearCompoundStabilityAnalysis
        )

    @property
    def bevel_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4006.BevelGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4006,
        )

        return self.__parent__._cast(_4006.BevelGearCompoundStabilityAnalysis)

    @property
    def bevel_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4008.BevelGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4008,
        )

        return self.__parent__._cast(_4008.BevelGearSetCompoundStabilityAnalysis)

    @property
    def bolt_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4009.BoltCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4009,
        )

        return self.__parent__._cast(_4009.BoltCompoundStabilityAnalysis)

    @property
    def bolted_joint_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4010.BoltedJointCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4010,
        )

        return self.__parent__._cast(_4010.BoltedJointCompoundStabilityAnalysis)

    @property
    def clutch_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4011.ClutchCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4011,
        )

        return self.__parent__._cast(_4011.ClutchCompoundStabilityAnalysis)

    @property
    def clutch_half_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4013.ClutchHalfCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4013,
        )

        return self.__parent__._cast(_4013.ClutchHalfCompoundStabilityAnalysis)

    @property
    def component_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4015.ComponentCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4015,
        )

        return self.__parent__._cast(_4015.ComponentCompoundStabilityAnalysis)

    @property
    def concept_coupling_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4016.ConceptCouplingCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4016,
        )

        return self.__parent__._cast(_4016.ConceptCouplingCompoundStabilityAnalysis)

    @property
    def concept_coupling_half_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4018.ConceptCouplingHalfCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4018,
        )

        return self.__parent__._cast(_4018.ConceptCouplingHalfCompoundStabilityAnalysis)

    @property
    def concept_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4019.ConceptGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4019,
        )

        return self.__parent__._cast(_4019.ConceptGearCompoundStabilityAnalysis)

    @property
    def concept_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4021.ConceptGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4021,
        )

        return self.__parent__._cast(_4021.ConceptGearSetCompoundStabilityAnalysis)

    @property
    def conical_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4022.ConicalGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4022,
        )

        return self.__parent__._cast(_4022.ConicalGearCompoundStabilityAnalysis)

    @property
    def conical_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4024.ConicalGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4024,
        )

        return self.__parent__._cast(_4024.ConicalGearSetCompoundStabilityAnalysis)

    @property
    def connector_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4026.ConnectorCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4026,
        )

        return self.__parent__._cast(_4026.ConnectorCompoundStabilityAnalysis)

    @property
    def coupling_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4027.CouplingCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4027,
        )

        return self.__parent__._cast(_4027.CouplingCompoundStabilityAnalysis)

    @property
    def coupling_half_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4029.CouplingHalfCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4029,
        )

        return self.__parent__._cast(_4029.CouplingHalfCompoundStabilityAnalysis)

    @property
    def cvt_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4031.CVTCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4031,
        )

        return self.__parent__._cast(_4031.CVTCompoundStabilityAnalysis)

    @property
    def cvt_pulley_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4032.CVTPulleyCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4032,
        )

        return self.__parent__._cast(_4032.CVTPulleyCompoundStabilityAnalysis)

    @property
    def cycloidal_assembly_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4033.CycloidalAssemblyCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4033,
        )

        return self.__parent__._cast(_4033.CycloidalAssemblyCompoundStabilityAnalysis)

    @property
    def cycloidal_disc_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4035.CycloidalDiscCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4035,
        )

        return self.__parent__._cast(_4035.CycloidalDiscCompoundStabilityAnalysis)

    @property
    def cylindrical_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4037.CylindricalGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4037,
        )

        return self.__parent__._cast(_4037.CylindricalGearCompoundStabilityAnalysis)

    @property
    def cylindrical_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4039.CylindricalGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4039,
        )

        return self.__parent__._cast(_4039.CylindricalGearSetCompoundStabilityAnalysis)

    @property
    def cylindrical_planet_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4040.CylindricalPlanetGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4040,
        )

        return self.__parent__._cast(
            _4040.CylindricalPlanetGearCompoundStabilityAnalysis
        )

    @property
    def datum_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4041.DatumCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4041,
        )

        return self.__parent__._cast(_4041.DatumCompoundStabilityAnalysis)

    @property
    def external_cad_model_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4042.ExternalCADModelCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4042,
        )

        return self.__parent__._cast(_4042.ExternalCADModelCompoundStabilityAnalysis)

    @property
    def face_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4043.FaceGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4043,
        )

        return self.__parent__._cast(_4043.FaceGearCompoundStabilityAnalysis)

    @property
    def face_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4045.FaceGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4045,
        )

        return self.__parent__._cast(_4045.FaceGearSetCompoundStabilityAnalysis)

    @property
    def fe_part_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4046.FEPartCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4046,
        )

        return self.__parent__._cast(_4046.FEPartCompoundStabilityAnalysis)

    @property
    def flexible_pin_assembly_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4047.FlexiblePinAssemblyCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4047,
        )

        return self.__parent__._cast(_4047.FlexiblePinAssemblyCompoundStabilityAnalysis)

    @property
    def gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4048.GearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4048,
        )

        return self.__parent__._cast(_4048.GearCompoundStabilityAnalysis)

    @property
    def gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4050.GearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4050,
        )

        return self.__parent__._cast(_4050.GearSetCompoundStabilityAnalysis)

    @property
    def guide_dxf_model_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4051.GuideDxfModelCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4051,
        )

        return self.__parent__._cast(_4051.GuideDxfModelCompoundStabilityAnalysis)

    @property
    def hypoid_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4052.HypoidGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4052,
        )

        return self.__parent__._cast(_4052.HypoidGearCompoundStabilityAnalysis)

    @property
    def hypoid_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4054.HypoidGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4054,
        )

        return self.__parent__._cast(_4054.HypoidGearSetCompoundStabilityAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4056.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4056,
        )

        return self.__parent__._cast(
            _4056.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4058.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4058,
        )

        return self.__parent__._cast(
            _4058.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4059.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4059,
        )

        return self.__parent__._cast(
            _4059.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4061.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4061,
        )

        return self.__parent__._cast(
            _4061.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4062.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4062,
        )

        return self.__parent__._cast(
            _4062.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4064.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4064,
        )

        return self.__parent__._cast(
            _4064.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
        )

    @property
    def mass_disc_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4065.MassDiscCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4065,
        )

        return self.__parent__._cast(_4065.MassDiscCompoundStabilityAnalysis)

    @property
    def measurement_component_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4066.MeasurementComponentCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4066,
        )

        return self.__parent__._cast(
            _4066.MeasurementComponentCompoundStabilityAnalysis
        )

    @property
    def microphone_array_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4067.MicrophoneArrayCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4067,
        )

        return self.__parent__._cast(_4067.MicrophoneArrayCompoundStabilityAnalysis)

    @property
    def microphone_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4068.MicrophoneCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4068,
        )

        return self.__parent__._cast(_4068.MicrophoneCompoundStabilityAnalysis)

    @property
    def mountable_component_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4069.MountableComponentCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4069,
        )

        return self.__parent__._cast(_4069.MountableComponentCompoundStabilityAnalysis)

    @property
    def oil_seal_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4070.OilSealCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4070,
        )

        return self.__parent__._cast(_4070.OilSealCompoundStabilityAnalysis)

    @property
    def part_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4071.PartCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4071,
        )

        return self.__parent__._cast(_4071.PartCompoundStabilityAnalysis)

    @property
    def part_to_part_shear_coupling_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4072.PartToPartShearCouplingCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4072,
        )

        return self.__parent__._cast(
            _4072.PartToPartShearCouplingCompoundStabilityAnalysis
        )

    @property
    def part_to_part_shear_coupling_half_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4074.PartToPartShearCouplingHalfCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4074,
        )

        return self.__parent__._cast(
            _4074.PartToPartShearCouplingHalfCompoundStabilityAnalysis
        )

    @property
    def planetary_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4076.PlanetaryGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4076,
        )

        return self.__parent__._cast(_4076.PlanetaryGearSetCompoundStabilityAnalysis)

    @property
    def planet_carrier_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4077.PlanetCarrierCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4077,
        )

        return self.__parent__._cast(_4077.PlanetCarrierCompoundStabilityAnalysis)

    @property
    def point_load_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4078.PointLoadCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4078,
        )

        return self.__parent__._cast(_4078.PointLoadCompoundStabilityAnalysis)

    @property
    def power_load_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4079.PowerLoadCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4079,
        )

        return self.__parent__._cast(_4079.PowerLoadCompoundStabilityAnalysis)

    @property
    def pulley_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4080.PulleyCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4080,
        )

        return self.__parent__._cast(_4080.PulleyCompoundStabilityAnalysis)

    @property
    def ring_pins_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4081.RingPinsCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4081,
        )

        return self.__parent__._cast(_4081.RingPinsCompoundStabilityAnalysis)

    @property
    def rolling_ring_assembly_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4083.RollingRingAssemblyCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4083,
        )

        return self.__parent__._cast(_4083.RollingRingAssemblyCompoundStabilityAnalysis)

    @property
    def rolling_ring_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4084.RollingRingCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4084,
        )

        return self.__parent__._cast(_4084.RollingRingCompoundStabilityAnalysis)

    @property
    def root_assembly_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4086.RootAssemblyCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4086,
        )

        return self.__parent__._cast(_4086.RootAssemblyCompoundStabilityAnalysis)

    @property
    def shaft_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4087.ShaftCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4087,
        )

        return self.__parent__._cast(_4087.ShaftCompoundStabilityAnalysis)

    @property
    def shaft_hub_connection_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4088.ShaftHubConnectionCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4088,
        )

        return self.__parent__._cast(_4088.ShaftHubConnectionCompoundStabilityAnalysis)

    @property
    def specialised_assembly_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4090.SpecialisedAssemblyCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4090,
        )

        return self.__parent__._cast(_4090.SpecialisedAssemblyCompoundStabilityAnalysis)

    @property
    def spiral_bevel_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4091.SpiralBevelGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4091,
        )

        return self.__parent__._cast(_4091.SpiralBevelGearCompoundStabilityAnalysis)

    @property
    def spiral_bevel_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4093.SpiralBevelGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4093,
        )

        return self.__parent__._cast(_4093.SpiralBevelGearSetCompoundStabilityAnalysis)

    @property
    def spring_damper_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4094.SpringDamperCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4094,
        )

        return self.__parent__._cast(_4094.SpringDamperCompoundStabilityAnalysis)

    @property
    def spring_damper_half_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4096.SpringDamperHalfCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4096,
        )

        return self.__parent__._cast(_4096.SpringDamperHalfCompoundStabilityAnalysis)

    @property
    def straight_bevel_diff_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4097.StraightBevelDiffGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4097,
        )

        return self.__parent__._cast(
            _4097.StraightBevelDiffGearCompoundStabilityAnalysis
        )

    @property
    def straight_bevel_diff_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4099.StraightBevelDiffGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4099,
        )

        return self.__parent__._cast(
            _4099.StraightBevelDiffGearSetCompoundStabilityAnalysis
        )

    @property
    def straight_bevel_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4100.StraightBevelGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4100,
        )

        return self.__parent__._cast(_4100.StraightBevelGearCompoundStabilityAnalysis)

    @property
    def straight_bevel_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4102.StraightBevelGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4102,
        )

        return self.__parent__._cast(
            _4102.StraightBevelGearSetCompoundStabilityAnalysis
        )

    @property
    def straight_bevel_planet_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4103.StraightBevelPlanetGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4103,
        )

        return self.__parent__._cast(
            _4103.StraightBevelPlanetGearCompoundStabilityAnalysis
        )

    @property
    def straight_bevel_sun_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4104.StraightBevelSunGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4104,
        )

        return self.__parent__._cast(
            _4104.StraightBevelSunGearCompoundStabilityAnalysis
        )

    @property
    def synchroniser_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4105.SynchroniserCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4105,
        )

        return self.__parent__._cast(_4105.SynchroniserCompoundStabilityAnalysis)

    @property
    def synchroniser_half_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4106.SynchroniserHalfCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4106,
        )

        return self.__parent__._cast(_4106.SynchroniserHalfCompoundStabilityAnalysis)

    @property
    def synchroniser_part_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4107.SynchroniserPartCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4107,
        )

        return self.__parent__._cast(_4107.SynchroniserPartCompoundStabilityAnalysis)

    @property
    def synchroniser_sleeve_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4108.SynchroniserSleeveCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4108,
        )

        return self.__parent__._cast(_4108.SynchroniserSleeveCompoundStabilityAnalysis)

    @property
    def torque_converter_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4109.TorqueConverterCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4109,
        )

        return self.__parent__._cast(_4109.TorqueConverterCompoundStabilityAnalysis)

    @property
    def torque_converter_pump_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4111.TorqueConverterPumpCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4111,
        )

        return self.__parent__._cast(_4111.TorqueConverterPumpCompoundStabilityAnalysis)

    @property
    def torque_converter_turbine_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4112.TorqueConverterTurbineCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4112,
        )

        return self.__parent__._cast(
            _4112.TorqueConverterTurbineCompoundStabilityAnalysis
        )

    @property
    def unbalanced_mass_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4113.UnbalancedMassCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4113,
        )

        return self.__parent__._cast(_4113.UnbalancedMassCompoundStabilityAnalysis)

    @property
    def virtual_component_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4114.VirtualComponentCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4114,
        )

        return self.__parent__._cast(_4114.VirtualComponentCompoundStabilityAnalysis)

    @property
    def worm_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4115.WormGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4115,
        )

        return self.__parent__._cast(_4115.WormGearCompoundStabilityAnalysis)

    @property
    def worm_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4117.WormGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4117,
        )

        return self.__parent__._cast(_4117.WormGearSetCompoundStabilityAnalysis)

    @property
    def zerol_bevel_gear_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4118.ZerolBevelGearCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4118,
        )

        return self.__parent__._cast(_4118.ZerolBevelGearCompoundStabilityAnalysis)

    @property
    def zerol_bevel_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4120.ZerolBevelGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4120,
        )

        return self.__parent__._cast(_4120.ZerolBevelGearSetCompoundStabilityAnalysis)

    @property
    def abstract_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4264.AbstractAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4264,
        )

        return self.__parent__._cast(_4264.AbstractAssemblyCompoundPowerFlow)

    @property
    def abstract_shaft_compound_power_flow(
        self: "CastSelf",
    ) -> "_4265.AbstractShaftCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4265,
        )

        return self.__parent__._cast(_4265.AbstractShaftCompoundPowerFlow)

    @property
    def abstract_shaft_or_housing_compound_power_flow(
        self: "CastSelf",
    ) -> "_4266.AbstractShaftOrHousingCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4266,
        )

        return self.__parent__._cast(_4266.AbstractShaftOrHousingCompoundPowerFlow)

    @property
    def agma_gleason_conical_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4268.AGMAGleasonConicalGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4268,
        )

        return self.__parent__._cast(_4268.AGMAGleasonConicalGearCompoundPowerFlow)

    @property
    def agma_gleason_conical_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4270.AGMAGleasonConicalGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4270,
        )

        return self.__parent__._cast(_4270.AGMAGleasonConicalGearSetCompoundPowerFlow)

    @property
    def assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4271.AssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4271,
        )

        return self.__parent__._cast(_4271.AssemblyCompoundPowerFlow)

    @property
    def bearing_compound_power_flow(
        self: "CastSelf",
    ) -> "_4272.BearingCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4272,
        )

        return self.__parent__._cast(_4272.BearingCompoundPowerFlow)

    @property
    def belt_drive_compound_power_flow(
        self: "CastSelf",
    ) -> "_4274.BeltDriveCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4274,
        )

        return self.__parent__._cast(_4274.BeltDriveCompoundPowerFlow)

    @property
    def bevel_differential_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4275.BevelDifferentialGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4275,
        )

        return self.__parent__._cast(_4275.BevelDifferentialGearCompoundPowerFlow)

    @property
    def bevel_differential_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4277.BevelDifferentialGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4277,
        )

        return self.__parent__._cast(_4277.BevelDifferentialGearSetCompoundPowerFlow)

    @property
    def bevel_differential_planet_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4278.BevelDifferentialPlanetGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4278,
        )

        return self.__parent__._cast(_4278.BevelDifferentialPlanetGearCompoundPowerFlow)

    @property
    def bevel_differential_sun_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4279.BevelDifferentialSunGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4279,
        )

        return self.__parent__._cast(_4279.BevelDifferentialSunGearCompoundPowerFlow)

    @property
    def bevel_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4280.BevelGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4280,
        )

        return self.__parent__._cast(_4280.BevelGearCompoundPowerFlow)

    @property
    def bevel_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4282.BevelGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4282,
        )

        return self.__parent__._cast(_4282.BevelGearSetCompoundPowerFlow)

    @property
    def bolt_compound_power_flow(self: "CastSelf") -> "_4283.BoltCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4283,
        )

        return self.__parent__._cast(_4283.BoltCompoundPowerFlow)

    @property
    def bolted_joint_compound_power_flow(
        self: "CastSelf",
    ) -> "_4284.BoltedJointCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4284,
        )

        return self.__parent__._cast(_4284.BoltedJointCompoundPowerFlow)

    @property
    def clutch_compound_power_flow(self: "CastSelf") -> "_4285.ClutchCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4285,
        )

        return self.__parent__._cast(_4285.ClutchCompoundPowerFlow)

    @property
    def clutch_half_compound_power_flow(
        self: "CastSelf",
    ) -> "_4287.ClutchHalfCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4287,
        )

        return self.__parent__._cast(_4287.ClutchHalfCompoundPowerFlow)

    @property
    def component_compound_power_flow(
        self: "CastSelf",
    ) -> "_4289.ComponentCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4289,
        )

        return self.__parent__._cast(_4289.ComponentCompoundPowerFlow)

    @property
    def concept_coupling_compound_power_flow(
        self: "CastSelf",
    ) -> "_4290.ConceptCouplingCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4290,
        )

        return self.__parent__._cast(_4290.ConceptCouplingCompoundPowerFlow)

    @property
    def concept_coupling_half_compound_power_flow(
        self: "CastSelf",
    ) -> "_4292.ConceptCouplingHalfCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4292,
        )

        return self.__parent__._cast(_4292.ConceptCouplingHalfCompoundPowerFlow)

    @property
    def concept_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4293.ConceptGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4293,
        )

        return self.__parent__._cast(_4293.ConceptGearCompoundPowerFlow)

    @property
    def concept_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4295.ConceptGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4295,
        )

        return self.__parent__._cast(_4295.ConceptGearSetCompoundPowerFlow)

    @property
    def conical_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4296.ConicalGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4296,
        )

        return self.__parent__._cast(_4296.ConicalGearCompoundPowerFlow)

    @property
    def conical_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4298.ConicalGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4298,
        )

        return self.__parent__._cast(_4298.ConicalGearSetCompoundPowerFlow)

    @property
    def connector_compound_power_flow(
        self: "CastSelf",
    ) -> "_4300.ConnectorCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4300,
        )

        return self.__parent__._cast(_4300.ConnectorCompoundPowerFlow)

    @property
    def coupling_compound_power_flow(
        self: "CastSelf",
    ) -> "_4301.CouplingCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4301,
        )

        return self.__parent__._cast(_4301.CouplingCompoundPowerFlow)

    @property
    def coupling_half_compound_power_flow(
        self: "CastSelf",
    ) -> "_4303.CouplingHalfCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4303,
        )

        return self.__parent__._cast(_4303.CouplingHalfCompoundPowerFlow)

    @property
    def cvt_compound_power_flow(self: "CastSelf") -> "_4305.CVTCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4305,
        )

        return self.__parent__._cast(_4305.CVTCompoundPowerFlow)

    @property
    def cvt_pulley_compound_power_flow(
        self: "CastSelf",
    ) -> "_4306.CVTPulleyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4306,
        )

        return self.__parent__._cast(_4306.CVTPulleyCompoundPowerFlow)

    @property
    def cycloidal_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4307.CycloidalAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4307,
        )

        return self.__parent__._cast(_4307.CycloidalAssemblyCompoundPowerFlow)

    @property
    def cycloidal_disc_compound_power_flow(
        self: "CastSelf",
    ) -> "_4309.CycloidalDiscCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4309,
        )

        return self.__parent__._cast(_4309.CycloidalDiscCompoundPowerFlow)

    @property
    def cylindrical_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4311.CylindricalGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4311,
        )

        return self.__parent__._cast(_4311.CylindricalGearCompoundPowerFlow)

    @property
    def cylindrical_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4313.CylindricalGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4313,
        )

        return self.__parent__._cast(_4313.CylindricalGearSetCompoundPowerFlow)

    @property
    def cylindrical_planet_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4314.CylindricalPlanetGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4314,
        )

        return self.__parent__._cast(_4314.CylindricalPlanetGearCompoundPowerFlow)

    @property
    def datum_compound_power_flow(self: "CastSelf") -> "_4315.DatumCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4315,
        )

        return self.__parent__._cast(_4315.DatumCompoundPowerFlow)

    @property
    def external_cad_model_compound_power_flow(
        self: "CastSelf",
    ) -> "_4316.ExternalCADModelCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4316,
        )

        return self.__parent__._cast(_4316.ExternalCADModelCompoundPowerFlow)

    @property
    def face_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4317.FaceGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4317,
        )

        return self.__parent__._cast(_4317.FaceGearCompoundPowerFlow)

    @property
    def face_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4319.FaceGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4319,
        )

        return self.__parent__._cast(_4319.FaceGearSetCompoundPowerFlow)

    @property
    def fe_part_compound_power_flow(
        self: "CastSelf",
    ) -> "_4320.FEPartCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4320,
        )

        return self.__parent__._cast(_4320.FEPartCompoundPowerFlow)

    @property
    def flexible_pin_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4321.FlexiblePinAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4321,
        )

        return self.__parent__._cast(_4321.FlexiblePinAssemblyCompoundPowerFlow)

    @property
    def gear_compound_power_flow(self: "CastSelf") -> "_4322.GearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4322,
        )

        return self.__parent__._cast(_4322.GearCompoundPowerFlow)

    @property
    def gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4324.GearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4324,
        )

        return self.__parent__._cast(_4324.GearSetCompoundPowerFlow)

    @property
    def guide_dxf_model_compound_power_flow(
        self: "CastSelf",
    ) -> "_4325.GuideDxfModelCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4325,
        )

        return self.__parent__._cast(_4325.GuideDxfModelCompoundPowerFlow)

    @property
    def hypoid_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4326.HypoidGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4326,
        )

        return self.__parent__._cast(_4326.HypoidGearCompoundPowerFlow)

    @property
    def hypoid_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4328.HypoidGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4328,
        )

        return self.__parent__._cast(_4328.HypoidGearSetCompoundPowerFlow)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4330.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4330,
        )

        return self.__parent__._cast(
            _4330.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4332.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4332,
        )

        return self.__parent__._cast(
            _4332.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4333.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4333,
        )

        return self.__parent__._cast(
            _4333.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4335.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4335,
        )

        return self.__parent__._cast(
            _4335.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4336.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4336,
        )

        return self.__parent__._cast(
            _4336.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4338.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4338,
        )

        return self.__parent__._cast(
            _4338.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
        )

    @property
    def mass_disc_compound_power_flow(
        self: "CastSelf",
    ) -> "_4339.MassDiscCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4339,
        )

        return self.__parent__._cast(_4339.MassDiscCompoundPowerFlow)

    @property
    def measurement_component_compound_power_flow(
        self: "CastSelf",
    ) -> "_4340.MeasurementComponentCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4340,
        )

        return self.__parent__._cast(_4340.MeasurementComponentCompoundPowerFlow)

    @property
    def microphone_array_compound_power_flow(
        self: "CastSelf",
    ) -> "_4341.MicrophoneArrayCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4341,
        )

        return self.__parent__._cast(_4341.MicrophoneArrayCompoundPowerFlow)

    @property
    def microphone_compound_power_flow(
        self: "CastSelf",
    ) -> "_4342.MicrophoneCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4342,
        )

        return self.__parent__._cast(_4342.MicrophoneCompoundPowerFlow)

    @property
    def mountable_component_compound_power_flow(
        self: "CastSelf",
    ) -> "_4343.MountableComponentCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4343,
        )

        return self.__parent__._cast(_4343.MountableComponentCompoundPowerFlow)

    @property
    def oil_seal_compound_power_flow(
        self: "CastSelf",
    ) -> "_4344.OilSealCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4344,
        )

        return self.__parent__._cast(_4344.OilSealCompoundPowerFlow)

    @property
    def part_compound_power_flow(self: "CastSelf") -> "_4345.PartCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4345,
        )

        return self.__parent__._cast(_4345.PartCompoundPowerFlow)

    @property
    def part_to_part_shear_coupling_compound_power_flow(
        self: "CastSelf",
    ) -> "_4346.PartToPartShearCouplingCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4346,
        )

        return self.__parent__._cast(_4346.PartToPartShearCouplingCompoundPowerFlow)

    @property
    def part_to_part_shear_coupling_half_compound_power_flow(
        self: "CastSelf",
    ) -> "_4348.PartToPartShearCouplingHalfCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4348,
        )

        return self.__parent__._cast(_4348.PartToPartShearCouplingHalfCompoundPowerFlow)

    @property
    def planetary_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4350.PlanetaryGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4350,
        )

        return self.__parent__._cast(_4350.PlanetaryGearSetCompoundPowerFlow)

    @property
    def planet_carrier_compound_power_flow(
        self: "CastSelf",
    ) -> "_4351.PlanetCarrierCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4351,
        )

        return self.__parent__._cast(_4351.PlanetCarrierCompoundPowerFlow)

    @property
    def point_load_compound_power_flow(
        self: "CastSelf",
    ) -> "_4352.PointLoadCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4352,
        )

        return self.__parent__._cast(_4352.PointLoadCompoundPowerFlow)

    @property
    def power_load_compound_power_flow(
        self: "CastSelf",
    ) -> "_4353.PowerLoadCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4353,
        )

        return self.__parent__._cast(_4353.PowerLoadCompoundPowerFlow)

    @property
    def pulley_compound_power_flow(self: "CastSelf") -> "_4354.PulleyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4354,
        )

        return self.__parent__._cast(_4354.PulleyCompoundPowerFlow)

    @property
    def ring_pins_compound_power_flow(
        self: "CastSelf",
    ) -> "_4355.RingPinsCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4355,
        )

        return self.__parent__._cast(_4355.RingPinsCompoundPowerFlow)

    @property
    def rolling_ring_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4357.RollingRingAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4357,
        )

        return self.__parent__._cast(_4357.RollingRingAssemblyCompoundPowerFlow)

    @property
    def rolling_ring_compound_power_flow(
        self: "CastSelf",
    ) -> "_4358.RollingRingCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4358,
        )

        return self.__parent__._cast(_4358.RollingRingCompoundPowerFlow)

    @property
    def root_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4360.RootAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4360,
        )

        return self.__parent__._cast(_4360.RootAssemblyCompoundPowerFlow)

    @property
    def shaft_compound_power_flow(self: "CastSelf") -> "_4361.ShaftCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4361,
        )

        return self.__parent__._cast(_4361.ShaftCompoundPowerFlow)

    @property
    def shaft_hub_connection_compound_power_flow(
        self: "CastSelf",
    ) -> "_4362.ShaftHubConnectionCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4362,
        )

        return self.__parent__._cast(_4362.ShaftHubConnectionCompoundPowerFlow)

    @property
    def specialised_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4364.SpecialisedAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4364,
        )

        return self.__parent__._cast(_4364.SpecialisedAssemblyCompoundPowerFlow)

    @property
    def spiral_bevel_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4365.SpiralBevelGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4365,
        )

        return self.__parent__._cast(_4365.SpiralBevelGearCompoundPowerFlow)

    @property
    def spiral_bevel_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4367.SpiralBevelGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4367,
        )

        return self.__parent__._cast(_4367.SpiralBevelGearSetCompoundPowerFlow)

    @property
    def spring_damper_compound_power_flow(
        self: "CastSelf",
    ) -> "_4368.SpringDamperCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4368,
        )

        return self.__parent__._cast(_4368.SpringDamperCompoundPowerFlow)

    @property
    def spring_damper_half_compound_power_flow(
        self: "CastSelf",
    ) -> "_4370.SpringDamperHalfCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4370,
        )

        return self.__parent__._cast(_4370.SpringDamperHalfCompoundPowerFlow)

    @property
    def straight_bevel_diff_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4371.StraightBevelDiffGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4371,
        )

        return self.__parent__._cast(_4371.StraightBevelDiffGearCompoundPowerFlow)

    @property
    def straight_bevel_diff_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4373.StraightBevelDiffGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4373,
        )

        return self.__parent__._cast(_4373.StraightBevelDiffGearSetCompoundPowerFlow)

    @property
    def straight_bevel_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4374.StraightBevelGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4374,
        )

        return self.__parent__._cast(_4374.StraightBevelGearCompoundPowerFlow)

    @property
    def straight_bevel_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4376.StraightBevelGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4376,
        )

        return self.__parent__._cast(_4376.StraightBevelGearSetCompoundPowerFlow)

    @property
    def straight_bevel_planet_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4377.StraightBevelPlanetGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4377,
        )

        return self.__parent__._cast(_4377.StraightBevelPlanetGearCompoundPowerFlow)

    @property
    def straight_bevel_sun_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4378.StraightBevelSunGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4378,
        )

        return self.__parent__._cast(_4378.StraightBevelSunGearCompoundPowerFlow)

    @property
    def synchroniser_compound_power_flow(
        self: "CastSelf",
    ) -> "_4379.SynchroniserCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4379,
        )

        return self.__parent__._cast(_4379.SynchroniserCompoundPowerFlow)

    @property
    def synchroniser_half_compound_power_flow(
        self: "CastSelf",
    ) -> "_4380.SynchroniserHalfCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4380,
        )

        return self.__parent__._cast(_4380.SynchroniserHalfCompoundPowerFlow)

    @property
    def synchroniser_part_compound_power_flow(
        self: "CastSelf",
    ) -> "_4381.SynchroniserPartCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4381,
        )

        return self.__parent__._cast(_4381.SynchroniserPartCompoundPowerFlow)

    @property
    def synchroniser_sleeve_compound_power_flow(
        self: "CastSelf",
    ) -> "_4382.SynchroniserSleeveCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4382,
        )

        return self.__parent__._cast(_4382.SynchroniserSleeveCompoundPowerFlow)

    @property
    def torque_converter_compound_power_flow(
        self: "CastSelf",
    ) -> "_4383.TorqueConverterCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4383,
        )

        return self.__parent__._cast(_4383.TorqueConverterCompoundPowerFlow)

    @property
    def torque_converter_pump_compound_power_flow(
        self: "CastSelf",
    ) -> "_4385.TorqueConverterPumpCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4385,
        )

        return self.__parent__._cast(_4385.TorqueConverterPumpCompoundPowerFlow)

    @property
    def torque_converter_turbine_compound_power_flow(
        self: "CastSelf",
    ) -> "_4386.TorqueConverterTurbineCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4386,
        )

        return self.__parent__._cast(_4386.TorqueConverterTurbineCompoundPowerFlow)

    @property
    def unbalanced_mass_compound_power_flow(
        self: "CastSelf",
    ) -> "_4387.UnbalancedMassCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4387,
        )

        return self.__parent__._cast(_4387.UnbalancedMassCompoundPowerFlow)

    @property
    def virtual_component_compound_power_flow(
        self: "CastSelf",
    ) -> "_4388.VirtualComponentCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4388,
        )

        return self.__parent__._cast(_4388.VirtualComponentCompoundPowerFlow)

    @property
    def worm_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4389.WormGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4389,
        )

        return self.__parent__._cast(_4389.WormGearCompoundPowerFlow)

    @property
    def worm_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4391.WormGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4391,
        )

        return self.__parent__._cast(_4391.WormGearSetCompoundPowerFlow)

    @property
    def zerol_bevel_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4392.ZerolBevelGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4392,
        )

        return self.__parent__._cast(_4392.ZerolBevelGearCompoundPowerFlow)

    @property
    def zerol_bevel_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4394.ZerolBevelGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4394,
        )

        return self.__parent__._cast(_4394.ZerolBevelGearSetCompoundPowerFlow)

    @property
    def abstract_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4544.AbstractAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4544,
        )

        return self.__parent__._cast(_4544.AbstractAssemblyCompoundParametricStudyTool)

    @property
    def abstract_shaft_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4545.AbstractShaftCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4545,
        )

        return self.__parent__._cast(_4545.AbstractShaftCompoundParametricStudyTool)

    @property
    def abstract_shaft_or_housing_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4546.AbstractShaftOrHousingCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4546,
        )

        return self.__parent__._cast(
            _4546.AbstractShaftOrHousingCompoundParametricStudyTool
        )

    @property
    def agma_gleason_conical_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4548.AGMAGleasonConicalGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4548,
        )

        return self.__parent__._cast(
            _4548.AGMAGleasonConicalGearCompoundParametricStudyTool
        )

    @property
    def agma_gleason_conical_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4550.AGMAGleasonConicalGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4550,
        )

        return self.__parent__._cast(
            _4550.AGMAGleasonConicalGearSetCompoundParametricStudyTool
        )

    @property
    def assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4551.AssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4551,
        )

        return self.__parent__._cast(_4551.AssemblyCompoundParametricStudyTool)

    @property
    def bearing_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4552.BearingCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4552,
        )

        return self.__parent__._cast(_4552.BearingCompoundParametricStudyTool)

    @property
    def belt_drive_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4554.BeltDriveCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4554,
        )

        return self.__parent__._cast(_4554.BeltDriveCompoundParametricStudyTool)

    @property
    def bevel_differential_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4555.BevelDifferentialGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4555,
        )

        return self.__parent__._cast(
            _4555.BevelDifferentialGearCompoundParametricStudyTool
        )

    @property
    def bevel_differential_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4557.BevelDifferentialGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4557,
        )

        return self.__parent__._cast(
            _4557.BevelDifferentialGearSetCompoundParametricStudyTool
        )

    @property
    def bevel_differential_planet_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4558.BevelDifferentialPlanetGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4558,
        )

        return self.__parent__._cast(
            _4558.BevelDifferentialPlanetGearCompoundParametricStudyTool
        )

    @property
    def bevel_differential_sun_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4559.BevelDifferentialSunGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4559,
        )

        return self.__parent__._cast(
            _4559.BevelDifferentialSunGearCompoundParametricStudyTool
        )

    @property
    def bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4560.BevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4560,
        )

        return self.__parent__._cast(_4560.BevelGearCompoundParametricStudyTool)

    @property
    def bevel_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4562.BevelGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4562,
        )

        return self.__parent__._cast(_4562.BevelGearSetCompoundParametricStudyTool)

    @property
    def bolt_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4563.BoltCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4563,
        )

        return self.__parent__._cast(_4563.BoltCompoundParametricStudyTool)

    @property
    def bolted_joint_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4564.BoltedJointCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4564,
        )

        return self.__parent__._cast(_4564.BoltedJointCompoundParametricStudyTool)

    @property
    def clutch_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4565.ClutchCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4565,
        )

        return self.__parent__._cast(_4565.ClutchCompoundParametricStudyTool)

    @property
    def clutch_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4567.ClutchHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4567,
        )

        return self.__parent__._cast(_4567.ClutchHalfCompoundParametricStudyTool)

    @property
    def component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4569.ComponentCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4569,
        )

        return self.__parent__._cast(_4569.ComponentCompoundParametricStudyTool)

    @property
    def concept_coupling_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4570.ConceptCouplingCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4570,
        )

        return self.__parent__._cast(_4570.ConceptCouplingCompoundParametricStudyTool)

    @property
    def concept_coupling_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4572.ConceptCouplingHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4572,
        )

        return self.__parent__._cast(
            _4572.ConceptCouplingHalfCompoundParametricStudyTool
        )

    @property
    def concept_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4573.ConceptGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4573,
        )

        return self.__parent__._cast(_4573.ConceptGearCompoundParametricStudyTool)

    @property
    def concept_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4575.ConceptGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4575,
        )

        return self.__parent__._cast(_4575.ConceptGearSetCompoundParametricStudyTool)

    @property
    def conical_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4576.ConicalGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4576,
        )

        return self.__parent__._cast(_4576.ConicalGearCompoundParametricStudyTool)

    @property
    def conical_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4578.ConicalGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4578,
        )

        return self.__parent__._cast(_4578.ConicalGearSetCompoundParametricStudyTool)

    @property
    def connector_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4580.ConnectorCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4580,
        )

        return self.__parent__._cast(_4580.ConnectorCompoundParametricStudyTool)

    @property
    def coupling_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4581.CouplingCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4581,
        )

        return self.__parent__._cast(_4581.CouplingCompoundParametricStudyTool)

    @property
    def coupling_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4583.CouplingHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4583,
        )

        return self.__parent__._cast(_4583.CouplingHalfCompoundParametricStudyTool)

    @property
    def cvt_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4585.CVTCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4585,
        )

        return self.__parent__._cast(_4585.CVTCompoundParametricStudyTool)

    @property
    def cvt_pulley_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4586.CVTPulleyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4586,
        )

        return self.__parent__._cast(_4586.CVTPulleyCompoundParametricStudyTool)

    @property
    def cycloidal_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4587.CycloidalAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4587,
        )

        return self.__parent__._cast(_4587.CycloidalAssemblyCompoundParametricStudyTool)

    @property
    def cycloidal_disc_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4589.CycloidalDiscCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4589,
        )

        return self.__parent__._cast(_4589.CycloidalDiscCompoundParametricStudyTool)

    @property
    def cylindrical_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4591.CylindricalGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4591,
        )

        return self.__parent__._cast(_4591.CylindricalGearCompoundParametricStudyTool)

    @property
    def cylindrical_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4593.CylindricalGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4593,
        )

        return self.__parent__._cast(
            _4593.CylindricalGearSetCompoundParametricStudyTool
        )

    @property
    def cylindrical_planet_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4594.CylindricalPlanetGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4594,
        )

        return self.__parent__._cast(
            _4594.CylindricalPlanetGearCompoundParametricStudyTool
        )

    @property
    def datum_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4595.DatumCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4595,
        )

        return self.__parent__._cast(_4595.DatumCompoundParametricStudyTool)

    @property
    def external_cad_model_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4596.ExternalCADModelCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4596,
        )

        return self.__parent__._cast(_4596.ExternalCADModelCompoundParametricStudyTool)

    @property
    def face_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4597.FaceGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4597,
        )

        return self.__parent__._cast(_4597.FaceGearCompoundParametricStudyTool)

    @property
    def face_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4599.FaceGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4599,
        )

        return self.__parent__._cast(_4599.FaceGearSetCompoundParametricStudyTool)

    @property
    def fe_part_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4600.FEPartCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4600,
        )

        return self.__parent__._cast(_4600.FEPartCompoundParametricStudyTool)

    @property
    def flexible_pin_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4601.FlexiblePinAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4601,
        )

        return self.__parent__._cast(
            _4601.FlexiblePinAssemblyCompoundParametricStudyTool
        )

    @property
    def gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4602.GearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4602,
        )

        return self.__parent__._cast(_4602.GearCompoundParametricStudyTool)

    @property
    def gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4604.GearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4604,
        )

        return self.__parent__._cast(_4604.GearSetCompoundParametricStudyTool)

    @property
    def guide_dxf_model_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4605.GuideDxfModelCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4605,
        )

        return self.__parent__._cast(_4605.GuideDxfModelCompoundParametricStudyTool)

    @property
    def hypoid_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4606.HypoidGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4606,
        )

        return self.__parent__._cast(_4606.HypoidGearCompoundParametricStudyTool)

    @property
    def hypoid_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4608.HypoidGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4608,
        )

        return self.__parent__._cast(_4608.HypoidGearSetCompoundParametricStudyTool)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4610.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4610,
        )

        return self.__parent__._cast(
            _4610.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4612.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4612,
        )

        return self.__parent__._cast(
            _4612.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4613.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4613,
        )

        return self.__parent__._cast(
            _4613.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4615.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4615,
        )

        return self.__parent__._cast(
            _4615.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4616.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4616,
        )

        return self.__parent__._cast(
            _4616.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4618.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4618,
        )

        return self.__parent__._cast(
            _4618.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
        )

    @property
    def mass_disc_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4619.MassDiscCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4619,
        )

        return self.__parent__._cast(_4619.MassDiscCompoundParametricStudyTool)

    @property
    def measurement_component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4620.MeasurementComponentCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4620,
        )

        return self.__parent__._cast(
            _4620.MeasurementComponentCompoundParametricStudyTool
        )

    @property
    def microphone_array_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4621.MicrophoneArrayCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4621,
        )

        return self.__parent__._cast(_4621.MicrophoneArrayCompoundParametricStudyTool)

    @property
    def microphone_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4622.MicrophoneCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4622,
        )

        return self.__parent__._cast(_4622.MicrophoneCompoundParametricStudyTool)

    @property
    def mountable_component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4623.MountableComponentCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4623,
        )

        return self.__parent__._cast(
            _4623.MountableComponentCompoundParametricStudyTool
        )

    @property
    def oil_seal_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4624.OilSealCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4624,
        )

        return self.__parent__._cast(_4624.OilSealCompoundParametricStudyTool)

    @property
    def part_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4625.PartCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4625,
        )

        return self.__parent__._cast(_4625.PartCompoundParametricStudyTool)

    @property
    def part_to_part_shear_coupling_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4626.PartToPartShearCouplingCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4626,
        )

        return self.__parent__._cast(
            _4626.PartToPartShearCouplingCompoundParametricStudyTool
        )

    @property
    def part_to_part_shear_coupling_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4628.PartToPartShearCouplingHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4628,
        )

        return self.__parent__._cast(
            _4628.PartToPartShearCouplingHalfCompoundParametricStudyTool
        )

    @property
    def planetary_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4630.PlanetaryGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4630,
        )

        return self.__parent__._cast(_4630.PlanetaryGearSetCompoundParametricStudyTool)

    @property
    def planet_carrier_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4631.PlanetCarrierCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4631,
        )

        return self.__parent__._cast(_4631.PlanetCarrierCompoundParametricStudyTool)

    @property
    def point_load_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4632.PointLoadCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4632,
        )

        return self.__parent__._cast(_4632.PointLoadCompoundParametricStudyTool)

    @property
    def power_load_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4633.PowerLoadCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4633,
        )

        return self.__parent__._cast(_4633.PowerLoadCompoundParametricStudyTool)

    @property
    def pulley_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4634.PulleyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4634,
        )

        return self.__parent__._cast(_4634.PulleyCompoundParametricStudyTool)

    @property
    def ring_pins_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4635.RingPinsCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4635,
        )

        return self.__parent__._cast(_4635.RingPinsCompoundParametricStudyTool)

    @property
    def rolling_ring_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4637.RollingRingAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4637,
        )

        return self.__parent__._cast(
            _4637.RollingRingAssemblyCompoundParametricStudyTool
        )

    @property
    def rolling_ring_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4638.RollingRingCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4638,
        )

        return self.__parent__._cast(_4638.RollingRingCompoundParametricStudyTool)

    @property
    def root_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4640.RootAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4640,
        )

        return self.__parent__._cast(_4640.RootAssemblyCompoundParametricStudyTool)

    @property
    def shaft_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4641.ShaftCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4641,
        )

        return self.__parent__._cast(_4641.ShaftCompoundParametricStudyTool)

    @property
    def shaft_hub_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4642.ShaftHubConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4642,
        )

        return self.__parent__._cast(
            _4642.ShaftHubConnectionCompoundParametricStudyTool
        )

    @property
    def specialised_assembly_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4644.SpecialisedAssemblyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4644,
        )

        return self.__parent__._cast(
            _4644.SpecialisedAssemblyCompoundParametricStudyTool
        )

    @property
    def spiral_bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4645.SpiralBevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4645,
        )

        return self.__parent__._cast(_4645.SpiralBevelGearCompoundParametricStudyTool)

    @property
    def spiral_bevel_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4647.SpiralBevelGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4647,
        )

        return self.__parent__._cast(
            _4647.SpiralBevelGearSetCompoundParametricStudyTool
        )

    @property
    def spring_damper_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4648.SpringDamperCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4648,
        )

        return self.__parent__._cast(_4648.SpringDamperCompoundParametricStudyTool)

    @property
    def spring_damper_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4650.SpringDamperHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4650,
        )

        return self.__parent__._cast(_4650.SpringDamperHalfCompoundParametricStudyTool)

    @property
    def straight_bevel_diff_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4651.StraightBevelDiffGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4651,
        )

        return self.__parent__._cast(
            _4651.StraightBevelDiffGearCompoundParametricStudyTool
        )

    @property
    def straight_bevel_diff_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4653.StraightBevelDiffGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4653,
        )

        return self.__parent__._cast(
            _4653.StraightBevelDiffGearSetCompoundParametricStudyTool
        )

    @property
    def straight_bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4654.StraightBevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4654,
        )

        return self.__parent__._cast(_4654.StraightBevelGearCompoundParametricStudyTool)

    @property
    def straight_bevel_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4656.StraightBevelGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4656,
        )

        return self.__parent__._cast(
            _4656.StraightBevelGearSetCompoundParametricStudyTool
        )

    @property
    def straight_bevel_planet_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4657.StraightBevelPlanetGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4657,
        )

        return self.__parent__._cast(
            _4657.StraightBevelPlanetGearCompoundParametricStudyTool
        )

    @property
    def straight_bevel_sun_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4658.StraightBevelSunGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4658,
        )

        return self.__parent__._cast(
            _4658.StraightBevelSunGearCompoundParametricStudyTool
        )

    @property
    def synchroniser_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4659.SynchroniserCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4659,
        )

        return self.__parent__._cast(_4659.SynchroniserCompoundParametricStudyTool)

    @property
    def synchroniser_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4660.SynchroniserHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4660,
        )

        return self.__parent__._cast(_4660.SynchroniserHalfCompoundParametricStudyTool)

    @property
    def synchroniser_part_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4661.SynchroniserPartCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4661,
        )

        return self.__parent__._cast(_4661.SynchroniserPartCompoundParametricStudyTool)

    @property
    def synchroniser_sleeve_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4662.SynchroniserSleeveCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4662,
        )

        return self.__parent__._cast(
            _4662.SynchroniserSleeveCompoundParametricStudyTool
        )

    @property
    def torque_converter_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4663.TorqueConverterCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4663,
        )

        return self.__parent__._cast(_4663.TorqueConverterCompoundParametricStudyTool)

    @property
    def torque_converter_pump_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4665.TorqueConverterPumpCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4665,
        )

        return self.__parent__._cast(
            _4665.TorqueConverterPumpCompoundParametricStudyTool
        )

    @property
    def torque_converter_turbine_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4666.TorqueConverterTurbineCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4666,
        )

        return self.__parent__._cast(
            _4666.TorqueConverterTurbineCompoundParametricStudyTool
        )

    @property
    def unbalanced_mass_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4667.UnbalancedMassCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4667,
        )

        return self.__parent__._cast(_4667.UnbalancedMassCompoundParametricStudyTool)

    @property
    def virtual_component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4668.VirtualComponentCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4668,
        )

        return self.__parent__._cast(_4668.VirtualComponentCompoundParametricStudyTool)

    @property
    def worm_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4669.WormGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4669,
        )

        return self.__parent__._cast(_4669.WormGearCompoundParametricStudyTool)

    @property
    def worm_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4671.WormGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4671,
        )

        return self.__parent__._cast(_4671.WormGearSetCompoundParametricStudyTool)

    @property
    def zerol_bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4672.ZerolBevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4672,
        )

        return self.__parent__._cast(_4672.ZerolBevelGearCompoundParametricStudyTool)

    @property
    def zerol_bevel_gear_set_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4674.ZerolBevelGearSetCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4674,
        )

        return self.__parent__._cast(_4674.ZerolBevelGearSetCompoundParametricStudyTool)

    @property
    def abstract_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4833.AbstractAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4833,
        )

        return self.__parent__._cast(_4833.AbstractAssemblyCompoundModalAnalysis)

    @property
    def abstract_shaft_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4834.AbstractShaftCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4834,
        )

        return self.__parent__._cast(_4834.AbstractShaftCompoundModalAnalysis)

    @property
    def abstract_shaft_or_housing_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4835.AbstractShaftOrHousingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4835,
        )

        return self.__parent__._cast(_4835.AbstractShaftOrHousingCompoundModalAnalysis)

    @property
    def agma_gleason_conical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4837.AGMAGleasonConicalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4837,
        )

        return self.__parent__._cast(_4837.AGMAGleasonConicalGearCompoundModalAnalysis)

    @property
    def agma_gleason_conical_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4839.AGMAGleasonConicalGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4839,
        )

        return self.__parent__._cast(
            _4839.AGMAGleasonConicalGearSetCompoundModalAnalysis
        )

    @property
    def assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4840.AssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4840,
        )

        return self.__parent__._cast(_4840.AssemblyCompoundModalAnalysis)

    @property
    def bearing_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4841.BearingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4841,
        )

        return self.__parent__._cast(_4841.BearingCompoundModalAnalysis)

    @property
    def belt_drive_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4843.BeltDriveCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4843,
        )

        return self.__parent__._cast(_4843.BeltDriveCompoundModalAnalysis)

    @property
    def bevel_differential_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4844.BevelDifferentialGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4844,
        )

        return self.__parent__._cast(_4844.BevelDifferentialGearCompoundModalAnalysis)

    @property
    def bevel_differential_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4846.BevelDifferentialGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4846,
        )

        return self.__parent__._cast(
            _4846.BevelDifferentialGearSetCompoundModalAnalysis
        )

    @property
    def bevel_differential_planet_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4847.BevelDifferentialPlanetGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4847,
        )

        return self.__parent__._cast(
            _4847.BevelDifferentialPlanetGearCompoundModalAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4848.BevelDifferentialSunGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4848,
        )

        return self.__parent__._cast(
            _4848.BevelDifferentialSunGearCompoundModalAnalysis
        )

    @property
    def bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4849.BevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4849,
        )

        return self.__parent__._cast(_4849.BevelGearCompoundModalAnalysis)

    @property
    def bevel_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4851.BevelGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4851,
        )

        return self.__parent__._cast(_4851.BevelGearSetCompoundModalAnalysis)

    @property
    def bolt_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4852.BoltCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4852,
        )

        return self.__parent__._cast(_4852.BoltCompoundModalAnalysis)

    @property
    def bolted_joint_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4853.BoltedJointCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4853,
        )

        return self.__parent__._cast(_4853.BoltedJointCompoundModalAnalysis)

    @property
    def clutch_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4854.ClutchCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4854,
        )

        return self.__parent__._cast(_4854.ClutchCompoundModalAnalysis)

    @property
    def clutch_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4856.ClutchHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4856,
        )

        return self.__parent__._cast(_4856.ClutchHalfCompoundModalAnalysis)

    @property
    def component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4858.ComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4858,
        )

        return self.__parent__._cast(_4858.ComponentCompoundModalAnalysis)

    @property
    def concept_coupling_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4859.ConceptCouplingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4859,
        )

        return self.__parent__._cast(_4859.ConceptCouplingCompoundModalAnalysis)

    @property
    def concept_coupling_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4861.ConceptCouplingHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4861,
        )

        return self.__parent__._cast(_4861.ConceptCouplingHalfCompoundModalAnalysis)

    @property
    def concept_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4862.ConceptGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4862,
        )

        return self.__parent__._cast(_4862.ConceptGearCompoundModalAnalysis)

    @property
    def concept_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4864.ConceptGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4864,
        )

        return self.__parent__._cast(_4864.ConceptGearSetCompoundModalAnalysis)

    @property
    def conical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4865.ConicalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4865,
        )

        return self.__parent__._cast(_4865.ConicalGearCompoundModalAnalysis)

    @property
    def conical_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4867.ConicalGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4867,
        )

        return self.__parent__._cast(_4867.ConicalGearSetCompoundModalAnalysis)

    @property
    def connector_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4869.ConnectorCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4869,
        )

        return self.__parent__._cast(_4869.ConnectorCompoundModalAnalysis)

    @property
    def coupling_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4870.CouplingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4870,
        )

        return self.__parent__._cast(_4870.CouplingCompoundModalAnalysis)

    @property
    def coupling_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4872.CouplingHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4872,
        )

        return self.__parent__._cast(_4872.CouplingHalfCompoundModalAnalysis)

    @property
    def cvt_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4874.CVTCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4874,
        )

        return self.__parent__._cast(_4874.CVTCompoundModalAnalysis)

    @property
    def cvt_pulley_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4875.CVTPulleyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4875,
        )

        return self.__parent__._cast(_4875.CVTPulleyCompoundModalAnalysis)

    @property
    def cycloidal_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4876.CycloidalAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4876,
        )

        return self.__parent__._cast(_4876.CycloidalAssemblyCompoundModalAnalysis)

    @property
    def cycloidal_disc_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4878.CycloidalDiscCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4878,
        )

        return self.__parent__._cast(_4878.CycloidalDiscCompoundModalAnalysis)

    @property
    def cylindrical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4880.CylindricalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4880,
        )

        return self.__parent__._cast(_4880.CylindricalGearCompoundModalAnalysis)

    @property
    def cylindrical_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4882.CylindricalGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4882,
        )

        return self.__parent__._cast(_4882.CylindricalGearSetCompoundModalAnalysis)

    @property
    def cylindrical_planet_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4883.CylindricalPlanetGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4883,
        )

        return self.__parent__._cast(_4883.CylindricalPlanetGearCompoundModalAnalysis)

    @property
    def datum_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4884.DatumCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4884,
        )

        return self.__parent__._cast(_4884.DatumCompoundModalAnalysis)

    @property
    def external_cad_model_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4885.ExternalCADModelCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4885,
        )

        return self.__parent__._cast(_4885.ExternalCADModelCompoundModalAnalysis)

    @property
    def face_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4886.FaceGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4886,
        )

        return self.__parent__._cast(_4886.FaceGearCompoundModalAnalysis)

    @property
    def face_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4888.FaceGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4888,
        )

        return self.__parent__._cast(_4888.FaceGearSetCompoundModalAnalysis)

    @property
    def fe_part_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4889.FEPartCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4889,
        )

        return self.__parent__._cast(_4889.FEPartCompoundModalAnalysis)

    @property
    def flexible_pin_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4890.FlexiblePinAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4890,
        )

        return self.__parent__._cast(_4890.FlexiblePinAssemblyCompoundModalAnalysis)

    @property
    def gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4891.GearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4891,
        )

        return self.__parent__._cast(_4891.GearCompoundModalAnalysis)

    @property
    def gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4893.GearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4893,
        )

        return self.__parent__._cast(_4893.GearSetCompoundModalAnalysis)

    @property
    def guide_dxf_model_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4894.GuideDxfModelCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4894,
        )

        return self.__parent__._cast(_4894.GuideDxfModelCompoundModalAnalysis)

    @property
    def hypoid_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4895.HypoidGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4895,
        )

        return self.__parent__._cast(_4895.HypoidGearCompoundModalAnalysis)

    @property
    def hypoid_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4897.HypoidGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4897,
        )

        return self.__parent__._cast(_4897.HypoidGearSetCompoundModalAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4899.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4899,
        )

        return self.__parent__._cast(
            _4899.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4901.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4901,
        )

        return self.__parent__._cast(
            _4901.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4902.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4902,
        )

        return self.__parent__._cast(
            _4902.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4904.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4904,
        )

        return self.__parent__._cast(
            _4904.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4905.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4905,
        )

        return self.__parent__._cast(
            _4905.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4907.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4907,
        )

        return self.__parent__._cast(
            _4907.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
        )

    @property
    def mass_disc_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4908.MassDiscCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4908,
        )

        return self.__parent__._cast(_4908.MassDiscCompoundModalAnalysis)

    @property
    def measurement_component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4909.MeasurementComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4909,
        )

        return self.__parent__._cast(_4909.MeasurementComponentCompoundModalAnalysis)

    @property
    def microphone_array_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4910.MicrophoneArrayCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4910,
        )

        return self.__parent__._cast(_4910.MicrophoneArrayCompoundModalAnalysis)

    @property
    def microphone_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4911.MicrophoneCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4911,
        )

        return self.__parent__._cast(_4911.MicrophoneCompoundModalAnalysis)

    @property
    def mountable_component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4912.MountableComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4912,
        )

        return self.__parent__._cast(_4912.MountableComponentCompoundModalAnalysis)

    @property
    def oil_seal_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4913.OilSealCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4913,
        )

        return self.__parent__._cast(_4913.OilSealCompoundModalAnalysis)

    @property
    def part_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4914.PartCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4914,
        )

        return self.__parent__._cast(_4914.PartCompoundModalAnalysis)

    @property
    def part_to_part_shear_coupling_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4915.PartToPartShearCouplingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4915,
        )

        return self.__parent__._cast(_4915.PartToPartShearCouplingCompoundModalAnalysis)

    @property
    def part_to_part_shear_coupling_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4917.PartToPartShearCouplingHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4917,
        )

        return self.__parent__._cast(
            _4917.PartToPartShearCouplingHalfCompoundModalAnalysis
        )

    @property
    def planetary_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4919.PlanetaryGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4919,
        )

        return self.__parent__._cast(_4919.PlanetaryGearSetCompoundModalAnalysis)

    @property
    def planet_carrier_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4920.PlanetCarrierCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4920,
        )

        return self.__parent__._cast(_4920.PlanetCarrierCompoundModalAnalysis)

    @property
    def point_load_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4921.PointLoadCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4921,
        )

        return self.__parent__._cast(_4921.PointLoadCompoundModalAnalysis)

    @property
    def power_load_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4922.PowerLoadCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4922,
        )

        return self.__parent__._cast(_4922.PowerLoadCompoundModalAnalysis)

    @property
    def pulley_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4923.PulleyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4923,
        )

        return self.__parent__._cast(_4923.PulleyCompoundModalAnalysis)

    @property
    def ring_pins_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4924.RingPinsCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4924,
        )

        return self.__parent__._cast(_4924.RingPinsCompoundModalAnalysis)

    @property
    def rolling_ring_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4926.RollingRingAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4926,
        )

        return self.__parent__._cast(_4926.RollingRingAssemblyCompoundModalAnalysis)

    @property
    def rolling_ring_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4927.RollingRingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4927,
        )

        return self.__parent__._cast(_4927.RollingRingCompoundModalAnalysis)

    @property
    def root_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4929.RootAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4929,
        )

        return self.__parent__._cast(_4929.RootAssemblyCompoundModalAnalysis)

    @property
    def shaft_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4930.ShaftCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4930,
        )

        return self.__parent__._cast(_4930.ShaftCompoundModalAnalysis)

    @property
    def shaft_hub_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4931.ShaftHubConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4931,
        )

        return self.__parent__._cast(_4931.ShaftHubConnectionCompoundModalAnalysis)

    @property
    def specialised_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4933.SpecialisedAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4933,
        )

        return self.__parent__._cast(_4933.SpecialisedAssemblyCompoundModalAnalysis)

    @property
    def spiral_bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4934.SpiralBevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4934,
        )

        return self.__parent__._cast(_4934.SpiralBevelGearCompoundModalAnalysis)

    @property
    def spiral_bevel_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4936.SpiralBevelGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4936,
        )

        return self.__parent__._cast(_4936.SpiralBevelGearSetCompoundModalAnalysis)

    @property
    def spring_damper_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4937.SpringDamperCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4937,
        )

        return self.__parent__._cast(_4937.SpringDamperCompoundModalAnalysis)

    @property
    def spring_damper_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4939.SpringDamperHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4939,
        )

        return self.__parent__._cast(_4939.SpringDamperHalfCompoundModalAnalysis)

    @property
    def straight_bevel_diff_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4940.StraightBevelDiffGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4940,
        )

        return self.__parent__._cast(_4940.StraightBevelDiffGearCompoundModalAnalysis)

    @property
    def straight_bevel_diff_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4942.StraightBevelDiffGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4942,
        )

        return self.__parent__._cast(
            _4942.StraightBevelDiffGearSetCompoundModalAnalysis
        )

    @property
    def straight_bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4943.StraightBevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4943,
        )

        return self.__parent__._cast(_4943.StraightBevelGearCompoundModalAnalysis)

    @property
    def straight_bevel_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4945.StraightBevelGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4945,
        )

        return self.__parent__._cast(_4945.StraightBevelGearSetCompoundModalAnalysis)

    @property
    def straight_bevel_planet_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4946.StraightBevelPlanetGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4946,
        )

        return self.__parent__._cast(_4946.StraightBevelPlanetGearCompoundModalAnalysis)

    @property
    def straight_bevel_sun_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4947.StraightBevelSunGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4947,
        )

        return self.__parent__._cast(_4947.StraightBevelSunGearCompoundModalAnalysis)

    @property
    def synchroniser_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4948.SynchroniserCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4948,
        )

        return self.__parent__._cast(_4948.SynchroniserCompoundModalAnalysis)

    @property
    def synchroniser_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4949.SynchroniserHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4949,
        )

        return self.__parent__._cast(_4949.SynchroniserHalfCompoundModalAnalysis)

    @property
    def synchroniser_part_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4950.SynchroniserPartCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4950,
        )

        return self.__parent__._cast(_4950.SynchroniserPartCompoundModalAnalysis)

    @property
    def synchroniser_sleeve_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4951.SynchroniserSleeveCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4951,
        )

        return self.__parent__._cast(_4951.SynchroniserSleeveCompoundModalAnalysis)

    @property
    def torque_converter_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4952.TorqueConverterCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4952,
        )

        return self.__parent__._cast(_4952.TorqueConverterCompoundModalAnalysis)

    @property
    def torque_converter_pump_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4954.TorqueConverterPumpCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4954,
        )

        return self.__parent__._cast(_4954.TorqueConverterPumpCompoundModalAnalysis)

    @property
    def torque_converter_turbine_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4955.TorqueConverterTurbineCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4955,
        )

        return self.__parent__._cast(_4955.TorqueConverterTurbineCompoundModalAnalysis)

    @property
    def unbalanced_mass_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4956.UnbalancedMassCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4956,
        )

        return self.__parent__._cast(_4956.UnbalancedMassCompoundModalAnalysis)

    @property
    def virtual_component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4957.VirtualComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4957,
        )

        return self.__parent__._cast(_4957.VirtualComponentCompoundModalAnalysis)

    @property
    def worm_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4958.WormGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4958,
        )

        return self.__parent__._cast(_4958.WormGearCompoundModalAnalysis)

    @property
    def worm_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4960.WormGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4960,
        )

        return self.__parent__._cast(_4960.WormGearSetCompoundModalAnalysis)

    @property
    def zerol_bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4961.ZerolBevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4961,
        )

        return self.__parent__._cast(_4961.ZerolBevelGearCompoundModalAnalysis)

    @property
    def zerol_bevel_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4963.ZerolBevelGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4963,
        )

        return self.__parent__._cast(_4963.ZerolBevelGearSetCompoundModalAnalysis)

    @property
    def abstract_assembly_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5097.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5097,
        )

        return self.__parent__._cast(
            _5097.AbstractAssemblyCompoundModalAnalysisAtAStiffness
        )

    @property
    def abstract_shaft_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5098.AbstractShaftCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5098,
        )

        return self.__parent__._cast(
            _5098.AbstractShaftCompoundModalAnalysisAtAStiffness
        )

    @property
    def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5099.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5099,
        )

        return self.__parent__._cast(
            _5099.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
        )

    @property
    def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5101.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5101,
        )

        return self.__parent__._cast(
            _5101.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5103.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5103,
        )

        return self.__parent__._cast(
            _5103.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def assembly_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5104.AssemblyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5104,
        )

        return self.__parent__._cast(_5104.AssemblyCompoundModalAnalysisAtAStiffness)

    @property
    def bearing_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5105.BearingCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5105,
        )

        return self.__parent__._cast(_5105.BearingCompoundModalAnalysisAtAStiffness)

    @property
    def belt_drive_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5107.BeltDriveCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5107,
        )

        return self.__parent__._cast(_5107.BeltDriveCompoundModalAnalysisAtAStiffness)

    @property
    def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5108.BevelDifferentialGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5108,
        )

        return self.__parent__._cast(
            _5108.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5110.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5110,
        )

        return self.__parent__._cast(
            _5110.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5111.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5111,
        )

        return self.__parent__._cast(
            _5111.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5112.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5112,
        )

        return self.__parent__._cast(
            _5112.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def bevel_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5113.BevelGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5113,
        )

        return self.__parent__._cast(_5113.BevelGearCompoundModalAnalysisAtAStiffness)

    @property
    def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5115.BevelGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5115,
        )

        return self.__parent__._cast(
            _5115.BevelGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def bolt_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5116.BoltCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5116,
        )

        return self.__parent__._cast(_5116.BoltCompoundModalAnalysisAtAStiffness)

    @property
    def bolted_joint_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5117.BoltedJointCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5117,
        )

        return self.__parent__._cast(_5117.BoltedJointCompoundModalAnalysisAtAStiffness)

    @property
    def clutch_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5118.ClutchCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5118,
        )

        return self.__parent__._cast(_5118.ClutchCompoundModalAnalysisAtAStiffness)

    @property
    def clutch_half_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5120.ClutchHalfCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5120,
        )

        return self.__parent__._cast(_5120.ClutchHalfCompoundModalAnalysisAtAStiffness)

    @property
    def component_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5122.ComponentCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5122,
        )

        return self.__parent__._cast(_5122.ComponentCompoundModalAnalysisAtAStiffness)

    @property
    def concept_coupling_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5123.ConceptCouplingCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5123,
        )

        return self.__parent__._cast(
            _5123.ConceptCouplingCompoundModalAnalysisAtAStiffness
        )

    @property
    def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5125.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5125,
        )

        return self.__parent__._cast(
            _5125.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
        )

    @property
    def concept_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5126.ConceptGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5126,
        )

        return self.__parent__._cast(_5126.ConceptGearCompoundModalAnalysisAtAStiffness)

    @property
    def concept_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5128.ConceptGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5128,
        )

        return self.__parent__._cast(
            _5128.ConceptGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def conical_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5129.ConicalGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5129,
        )

        return self.__parent__._cast(_5129.ConicalGearCompoundModalAnalysisAtAStiffness)

    @property
    def conical_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5131.ConicalGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5131,
        )

        return self.__parent__._cast(
            _5131.ConicalGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def connector_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5133.ConnectorCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5133,
        )

        return self.__parent__._cast(_5133.ConnectorCompoundModalAnalysisAtAStiffness)

    @property
    def coupling_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5134.CouplingCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5134,
        )

        return self.__parent__._cast(_5134.CouplingCompoundModalAnalysisAtAStiffness)

    @property
    def coupling_half_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5136.CouplingHalfCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5136,
        )

        return self.__parent__._cast(
            _5136.CouplingHalfCompoundModalAnalysisAtAStiffness
        )

    @property
    def cvt_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5138.CVTCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5138,
        )

        return self.__parent__._cast(_5138.CVTCompoundModalAnalysisAtAStiffness)

    @property
    def cvt_pulley_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5139.CVTPulleyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5139,
        )

        return self.__parent__._cast(_5139.CVTPulleyCompoundModalAnalysisAtAStiffness)

    @property
    def cycloidal_assembly_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5140.CycloidalAssemblyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5140,
        )

        return self.__parent__._cast(
            _5140.CycloidalAssemblyCompoundModalAnalysisAtAStiffness
        )

    @property
    def cycloidal_disc_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5142.CycloidalDiscCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5142,
        )

        return self.__parent__._cast(
            _5142.CycloidalDiscCompoundModalAnalysisAtAStiffness
        )

    @property
    def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5144.CylindricalGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5144,
        )

        return self.__parent__._cast(
            _5144.CylindricalGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5146.CylindricalGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5146,
        )

        return self.__parent__._cast(
            _5146.CylindricalGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5147.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5147,
        )

        return self.__parent__._cast(
            _5147.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def datum_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5148.DatumCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5148,
        )

        return self.__parent__._cast(_5148.DatumCompoundModalAnalysisAtAStiffness)

    @property
    def external_cad_model_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5149.ExternalCADModelCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5149,
        )

        return self.__parent__._cast(
            _5149.ExternalCADModelCompoundModalAnalysisAtAStiffness
        )

    @property
    def face_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5150.FaceGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5150,
        )

        return self.__parent__._cast(_5150.FaceGearCompoundModalAnalysisAtAStiffness)

    @property
    def face_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5152.FaceGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5152,
        )

        return self.__parent__._cast(_5152.FaceGearSetCompoundModalAnalysisAtAStiffness)

    @property
    def fe_part_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5153.FEPartCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5153,
        )

        return self.__parent__._cast(_5153.FEPartCompoundModalAnalysisAtAStiffness)

    @property
    def flexible_pin_assembly_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5154.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5154,
        )

        return self.__parent__._cast(
            _5154.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
        )

    @property
    def gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5155.GearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5155,
        )

        return self.__parent__._cast(_5155.GearCompoundModalAnalysisAtAStiffness)

    @property
    def gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5157.GearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5157,
        )

        return self.__parent__._cast(_5157.GearSetCompoundModalAnalysisAtAStiffness)

    @property
    def guide_dxf_model_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5158.GuideDxfModelCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5158,
        )

        return self.__parent__._cast(
            _5158.GuideDxfModelCompoundModalAnalysisAtAStiffness
        )

    @property
    def hypoid_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5159.HypoidGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5159,
        )

        return self.__parent__._cast(_5159.HypoidGearCompoundModalAnalysisAtAStiffness)

    @property
    def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5161.HypoidGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5161,
        )

        return self.__parent__._cast(
            _5161.HypoidGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5163.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5163,
        )

        return self.__parent__._cast(
            _5163.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> (
        "_5165.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness"
    ):
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5165,
        )

        return self.__parent__._cast(
            _5165.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5166.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5166,
        )

        return self.__parent__._cast(
            _5166.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5168.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5168,
        )

        return self.__parent__._cast(
            _5168.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> (
        "_5169.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness"
    ):
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5169,
        )

        return self.__parent__._cast(
            _5169.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5171.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5171,
        )

        return self.__parent__._cast(
            _5171.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def mass_disc_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5172.MassDiscCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5172,
        )

        return self.__parent__._cast(_5172.MassDiscCompoundModalAnalysisAtAStiffness)

    @property
    def measurement_component_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5173.MeasurementComponentCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5173,
        )

        return self.__parent__._cast(
            _5173.MeasurementComponentCompoundModalAnalysisAtAStiffness
        )

    @property
    def microphone_array_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5174.MicrophoneArrayCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5174,
        )

        return self.__parent__._cast(
            _5174.MicrophoneArrayCompoundModalAnalysisAtAStiffness
        )

    @property
    def microphone_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5175.MicrophoneCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5175,
        )

        return self.__parent__._cast(_5175.MicrophoneCompoundModalAnalysisAtAStiffness)

    @property
    def mountable_component_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5176.MountableComponentCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5176,
        )

        return self.__parent__._cast(
            _5176.MountableComponentCompoundModalAnalysisAtAStiffness
        )

    @property
    def oil_seal_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5177.OilSealCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5177,
        )

        return self.__parent__._cast(_5177.OilSealCompoundModalAnalysisAtAStiffness)

    @property
    def part_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5178.PartCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5178,
        )

        return self.__parent__._cast(_5178.PartCompoundModalAnalysisAtAStiffness)

    @property
    def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5179.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5179,
        )

        return self.__parent__._cast(
            _5179.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
        )

    @property
    def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5181.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5181,
        )

        return self.__parent__._cast(
            _5181.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
        )

    @property
    def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5183.PlanetaryGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5183,
        )

        return self.__parent__._cast(
            _5183.PlanetaryGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def planet_carrier_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5184.PlanetCarrierCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5184,
        )

        return self.__parent__._cast(
            _5184.PlanetCarrierCompoundModalAnalysisAtAStiffness
        )

    @property
    def point_load_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5185.PointLoadCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5185,
        )

        return self.__parent__._cast(_5185.PointLoadCompoundModalAnalysisAtAStiffness)

    @property
    def power_load_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5186.PowerLoadCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5186,
        )

        return self.__parent__._cast(_5186.PowerLoadCompoundModalAnalysisAtAStiffness)

    @property
    def pulley_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5187.PulleyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5187,
        )

        return self.__parent__._cast(_5187.PulleyCompoundModalAnalysisAtAStiffness)

    @property
    def ring_pins_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5188.RingPinsCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5188,
        )

        return self.__parent__._cast(_5188.RingPinsCompoundModalAnalysisAtAStiffness)

    @property
    def rolling_ring_assembly_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5190.RollingRingAssemblyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5190,
        )

        return self.__parent__._cast(
            _5190.RollingRingAssemblyCompoundModalAnalysisAtAStiffness
        )

    @property
    def rolling_ring_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5191.RollingRingCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5191,
        )

        return self.__parent__._cast(_5191.RollingRingCompoundModalAnalysisAtAStiffness)

    @property
    def root_assembly_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5193.RootAssemblyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5193,
        )

        return self.__parent__._cast(
            _5193.RootAssemblyCompoundModalAnalysisAtAStiffness
        )

    @property
    def shaft_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5194.ShaftCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5194,
        )

        return self.__parent__._cast(_5194.ShaftCompoundModalAnalysisAtAStiffness)

    @property
    def shaft_hub_connection_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5195.ShaftHubConnectionCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5195,
        )

        return self.__parent__._cast(
            _5195.ShaftHubConnectionCompoundModalAnalysisAtAStiffness
        )

    @property
    def specialised_assembly_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5197.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5197,
        )

        return self.__parent__._cast(
            _5197.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
        )

    @property
    def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5198.SpiralBevelGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5198,
        )

        return self.__parent__._cast(
            _5198.SpiralBevelGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5200.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5200,
        )

        return self.__parent__._cast(
            _5200.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def spring_damper_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5201.SpringDamperCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5201,
        )

        return self.__parent__._cast(
            _5201.SpringDamperCompoundModalAnalysisAtAStiffness
        )

    @property
    def spring_damper_half_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5203.SpringDamperHalfCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5203,
        )

        return self.__parent__._cast(
            _5203.SpringDamperHalfCompoundModalAnalysisAtAStiffness
        )

    @property
    def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5204.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5204,
        )

        return self.__parent__._cast(
            _5204.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5206.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5206,
        )

        return self.__parent__._cast(
            _5206.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5207.StraightBevelGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5207,
        )

        return self.__parent__._cast(
            _5207.StraightBevelGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5209.StraightBevelGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5209,
        )

        return self.__parent__._cast(
            _5209.StraightBevelGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5210.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5210,
        )

        return self.__parent__._cast(
            _5210.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5211.StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5211,
        )

        return self.__parent__._cast(
            _5211.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def synchroniser_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5212.SynchroniserCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5212,
        )

        return self.__parent__._cast(
            _5212.SynchroniserCompoundModalAnalysisAtAStiffness
        )

    @property
    def synchroniser_half_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5213.SynchroniserHalfCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5213,
        )

        return self.__parent__._cast(
            _5213.SynchroniserHalfCompoundModalAnalysisAtAStiffness
        )

    @property
    def synchroniser_part_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5214.SynchroniserPartCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5214,
        )

        return self.__parent__._cast(
            _5214.SynchroniserPartCompoundModalAnalysisAtAStiffness
        )

    @property
    def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5215.SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5215,
        )

        return self.__parent__._cast(
            _5215.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
        )

    @property
    def torque_converter_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5216.TorqueConverterCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5216,
        )

        return self.__parent__._cast(
            _5216.TorqueConverterCompoundModalAnalysisAtAStiffness
        )

    @property
    def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5218.TorqueConverterPumpCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5218,
        )

        return self.__parent__._cast(
            _5218.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
        )

    @property
    def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5219.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5219,
        )

        return self.__parent__._cast(
            _5219.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
        )

    @property
    def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5220.UnbalancedMassCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5220,
        )

        return self.__parent__._cast(
            _5220.UnbalancedMassCompoundModalAnalysisAtAStiffness
        )

    @property
    def virtual_component_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5221.VirtualComponentCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5221,
        )

        return self.__parent__._cast(
            _5221.VirtualComponentCompoundModalAnalysisAtAStiffness
        )

    @property
    def worm_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5222.WormGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5222,
        )

        return self.__parent__._cast(_5222.WormGearCompoundModalAnalysisAtAStiffness)

    @property
    def worm_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5224.WormGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5224,
        )

        return self.__parent__._cast(_5224.WormGearSetCompoundModalAnalysisAtAStiffness)

    @property
    def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5225.ZerolBevelGearCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5225,
        )

        return self.__parent__._cast(
            _5225.ZerolBevelGearCompoundModalAnalysisAtAStiffness
        )

    @property
    def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5227.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
            _5227,
        )

        return self.__parent__._cast(
            _5227.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
        )

    @property
    def abstract_assembly_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5360.AbstractAssemblyCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5360,
        )

        return self.__parent__._cast(
            _5360.AbstractAssemblyCompoundModalAnalysisAtASpeed
        )

    @property
    def abstract_shaft_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5361.AbstractShaftCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5361,
        )

        return self.__parent__._cast(_5361.AbstractShaftCompoundModalAnalysisAtASpeed)

    @property
    def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5362.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5362,
        )

        return self.__parent__._cast(
            _5362.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
        )

    @property
    def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5364.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5364,
        )

        return self.__parent__._cast(
            _5364.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
        )

    @property
    def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5366.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5366,
        )

        return self.__parent__._cast(
            _5366.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
        )

    @property
    def assembly_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5367.AssemblyCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5367,
        )

        return self.__parent__._cast(_5367.AssemblyCompoundModalAnalysisAtASpeed)

    @property
    def bearing_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5368.BearingCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5368,
        )

        return self.__parent__._cast(_5368.BearingCompoundModalAnalysisAtASpeed)

    @property
    def belt_drive_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5370.BeltDriveCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5370,
        )

        return self.__parent__._cast(_5370.BeltDriveCompoundModalAnalysisAtASpeed)

    @property
    def bevel_differential_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5371.BevelDifferentialGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5371,
        )

        return self.__parent__._cast(
            _5371.BevelDifferentialGearCompoundModalAnalysisAtASpeed
        )

    @property
    def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5373.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5373,
        )

        return self.__parent__._cast(
            _5373.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
        )

    @property
    def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5374.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5374,
        )

        return self.__parent__._cast(
            _5374.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
        )

    @property
    def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5375.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5375,
        )

        return self.__parent__._cast(
            _5375.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
        )

    @property
    def bevel_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5376.BevelGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5376,
        )

        return self.__parent__._cast(_5376.BevelGearCompoundModalAnalysisAtASpeed)

    @property
    def bevel_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5378.BevelGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5378,
        )

        return self.__parent__._cast(_5378.BevelGearSetCompoundModalAnalysisAtASpeed)

    @property
    def bolt_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5379.BoltCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5379,
        )

        return self.__parent__._cast(_5379.BoltCompoundModalAnalysisAtASpeed)

    @property
    def bolted_joint_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5380.BoltedJointCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5380,
        )

        return self.__parent__._cast(_5380.BoltedJointCompoundModalAnalysisAtASpeed)

    @property
    def clutch_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5381.ClutchCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5381,
        )

        return self.__parent__._cast(_5381.ClutchCompoundModalAnalysisAtASpeed)

    @property
    def clutch_half_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5383.ClutchHalfCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5383,
        )

        return self.__parent__._cast(_5383.ClutchHalfCompoundModalAnalysisAtASpeed)

    @property
    def component_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5385.ComponentCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5385,
        )

        return self.__parent__._cast(_5385.ComponentCompoundModalAnalysisAtASpeed)

    @property
    def concept_coupling_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5386.ConceptCouplingCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5386,
        )

        return self.__parent__._cast(_5386.ConceptCouplingCompoundModalAnalysisAtASpeed)

    @property
    def concept_coupling_half_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5388.ConceptCouplingHalfCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5388,
        )

        return self.__parent__._cast(
            _5388.ConceptCouplingHalfCompoundModalAnalysisAtASpeed
        )

    @property
    def concept_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5389.ConceptGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5389,
        )

        return self.__parent__._cast(_5389.ConceptGearCompoundModalAnalysisAtASpeed)

    @property
    def concept_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5391.ConceptGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5391,
        )

        return self.__parent__._cast(_5391.ConceptGearSetCompoundModalAnalysisAtASpeed)

    @property
    def conical_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5392.ConicalGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5392,
        )

        return self.__parent__._cast(_5392.ConicalGearCompoundModalAnalysisAtASpeed)

    @property
    def conical_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5394.ConicalGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5394,
        )

        return self.__parent__._cast(_5394.ConicalGearSetCompoundModalAnalysisAtASpeed)

    @property
    def connector_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5396.ConnectorCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5396,
        )

        return self.__parent__._cast(_5396.ConnectorCompoundModalAnalysisAtASpeed)

    @property
    def coupling_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5397.CouplingCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5397,
        )

        return self.__parent__._cast(_5397.CouplingCompoundModalAnalysisAtASpeed)

    @property
    def coupling_half_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5399.CouplingHalfCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5399,
        )

        return self.__parent__._cast(_5399.CouplingHalfCompoundModalAnalysisAtASpeed)

    @property
    def cvt_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5401.CVTCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5401,
        )

        return self.__parent__._cast(_5401.CVTCompoundModalAnalysisAtASpeed)

    @property
    def cvt_pulley_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5402.CVTPulleyCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5402,
        )

        return self.__parent__._cast(_5402.CVTPulleyCompoundModalAnalysisAtASpeed)

    @property
    def cycloidal_assembly_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5403.CycloidalAssemblyCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5403,
        )

        return self.__parent__._cast(
            _5403.CycloidalAssemblyCompoundModalAnalysisAtASpeed
        )

    @property
    def cycloidal_disc_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5405.CycloidalDiscCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5405,
        )

        return self.__parent__._cast(_5405.CycloidalDiscCompoundModalAnalysisAtASpeed)

    @property
    def cylindrical_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5407.CylindricalGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5407,
        )

        return self.__parent__._cast(_5407.CylindricalGearCompoundModalAnalysisAtASpeed)

    @property
    def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5409.CylindricalGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5409,
        )

        return self.__parent__._cast(
            _5409.CylindricalGearSetCompoundModalAnalysisAtASpeed
        )

    @property
    def cylindrical_planet_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5410.CylindricalPlanetGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5410,
        )

        return self.__parent__._cast(
            _5410.CylindricalPlanetGearCompoundModalAnalysisAtASpeed
        )

    @property
    def datum_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5411.DatumCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5411,
        )

        return self.__parent__._cast(_5411.DatumCompoundModalAnalysisAtASpeed)

    @property
    def external_cad_model_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5412.ExternalCADModelCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5412,
        )

        return self.__parent__._cast(
            _5412.ExternalCADModelCompoundModalAnalysisAtASpeed
        )

    @property
    def face_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5413.FaceGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5413,
        )

        return self.__parent__._cast(_5413.FaceGearCompoundModalAnalysisAtASpeed)

    @property
    def face_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5415.FaceGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5415,
        )

        return self.__parent__._cast(_5415.FaceGearSetCompoundModalAnalysisAtASpeed)

    @property
    def fe_part_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5416.FEPartCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5416,
        )

        return self.__parent__._cast(_5416.FEPartCompoundModalAnalysisAtASpeed)

    @property
    def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5417.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5417,
        )

        return self.__parent__._cast(
            _5417.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
        )

    @property
    def gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5418.GearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5418,
        )

        return self.__parent__._cast(_5418.GearCompoundModalAnalysisAtASpeed)

    @property
    def gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5420.GearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5420,
        )

        return self.__parent__._cast(_5420.GearSetCompoundModalAnalysisAtASpeed)

    @property
    def guide_dxf_model_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5421.GuideDxfModelCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5421,
        )

        return self.__parent__._cast(_5421.GuideDxfModelCompoundModalAnalysisAtASpeed)

    @property
    def hypoid_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5422.HypoidGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5422,
        )

        return self.__parent__._cast(_5422.HypoidGearCompoundModalAnalysisAtASpeed)

    @property
    def hypoid_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5424.HypoidGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5424,
        )

        return self.__parent__._cast(_5424.HypoidGearSetCompoundModalAnalysisAtASpeed)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5426.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5426,
        )

        return self.__parent__._cast(
            _5426.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5428.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5428,
        )

        return self.__parent__._cast(
            _5428.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5429.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5429,
        )

        return self.__parent__._cast(
            _5429.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5431.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5431,
        )

        return self.__parent__._cast(
            _5431.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5432.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5432,
        )

        return self.__parent__._cast(
            _5432.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_5434.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5434,
        )

        return self.__parent__._cast(
            _5434.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
        )

    @property
    def mass_disc_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5435.MassDiscCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5435,
        )

        return self.__parent__._cast(_5435.MassDiscCompoundModalAnalysisAtASpeed)

    @property
    def measurement_component_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5436.MeasurementComponentCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5436,
        )

        return self.__parent__._cast(
            _5436.MeasurementComponentCompoundModalAnalysisAtASpeed
        )

    @property
    def microphone_array_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5437.MicrophoneArrayCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5437,
        )

        return self.__parent__._cast(_5437.MicrophoneArrayCompoundModalAnalysisAtASpeed)

    @property
    def microphone_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5438.MicrophoneCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5438,
        )

        return self.__parent__._cast(_5438.MicrophoneCompoundModalAnalysisAtASpeed)

    @property
    def mountable_component_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5439.MountableComponentCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5439,
        )

        return self.__parent__._cast(
            _5439.MountableComponentCompoundModalAnalysisAtASpeed
        )

    @property
    def oil_seal_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5440.OilSealCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5440,
        )

        return self.__parent__._cast(_5440.OilSealCompoundModalAnalysisAtASpeed)

    @property
    def part_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5441.PartCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5441,
        )

        return self.__parent__._cast(_5441.PartCompoundModalAnalysisAtASpeed)

    @property
    def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5442.PartToPartShearCouplingCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5442,
        )

        return self.__parent__._cast(
            _5442.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
        )

    @property
    def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5444.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5444,
        )

        return self.__parent__._cast(
            _5444.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
        )

    @property
    def planetary_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5446.PlanetaryGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5446,
        )

        return self.__parent__._cast(
            _5446.PlanetaryGearSetCompoundModalAnalysisAtASpeed
        )

    @property
    def planet_carrier_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5447.PlanetCarrierCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5447,
        )

        return self.__parent__._cast(_5447.PlanetCarrierCompoundModalAnalysisAtASpeed)

    @property
    def point_load_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5448.PointLoadCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5448,
        )

        return self.__parent__._cast(_5448.PointLoadCompoundModalAnalysisAtASpeed)

    @property
    def power_load_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5449.PowerLoadCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5449,
        )

        return self.__parent__._cast(_5449.PowerLoadCompoundModalAnalysisAtASpeed)

    @property
    def pulley_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5450.PulleyCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5450,
        )

        return self.__parent__._cast(_5450.PulleyCompoundModalAnalysisAtASpeed)

    @property
    def ring_pins_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5451.RingPinsCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5451,
        )

        return self.__parent__._cast(_5451.RingPinsCompoundModalAnalysisAtASpeed)

    @property
    def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5453.RollingRingAssemblyCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5453,
        )

        return self.__parent__._cast(
            _5453.RollingRingAssemblyCompoundModalAnalysisAtASpeed
        )

    @property
    def rolling_ring_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5454.RollingRingCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5454,
        )

        return self.__parent__._cast(_5454.RollingRingCompoundModalAnalysisAtASpeed)

    @property
    def root_assembly_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5456.RootAssemblyCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5456,
        )

        return self.__parent__._cast(_5456.RootAssemblyCompoundModalAnalysisAtASpeed)

    @property
    def shaft_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5457.ShaftCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5457,
        )

        return self.__parent__._cast(_5457.ShaftCompoundModalAnalysisAtASpeed)

    @property
    def shaft_hub_connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5458.ShaftHubConnectionCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5458,
        )

        return self.__parent__._cast(
            _5458.ShaftHubConnectionCompoundModalAnalysisAtASpeed
        )

    @property
    def specialised_assembly_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5460.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5460,
        )

        return self.__parent__._cast(
            _5460.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
        )

    @property
    def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5461.SpiralBevelGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5461,
        )

        return self.__parent__._cast(_5461.SpiralBevelGearCompoundModalAnalysisAtASpeed)

    @property
    def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5463.SpiralBevelGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5463,
        )

        return self.__parent__._cast(
            _5463.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
        )

    @property
    def spring_damper_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5464.SpringDamperCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5464,
        )

        return self.__parent__._cast(_5464.SpringDamperCompoundModalAnalysisAtASpeed)

    @property
    def spring_damper_half_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5466.SpringDamperHalfCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5466,
        )

        return self.__parent__._cast(
            _5466.SpringDamperHalfCompoundModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5467.StraightBevelDiffGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5467,
        )

        return self.__parent__._cast(
            _5467.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5469.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5469,
        )

        return self.__parent__._cast(
            _5469.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5470.StraightBevelGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5470,
        )

        return self.__parent__._cast(
            _5470.StraightBevelGearCompoundModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5472.StraightBevelGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5472,
        )

        return self.__parent__._cast(
            _5472.StraightBevelGearSetCompoundModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5473.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5473,
        )

        return self.__parent__._cast(
            _5473.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5474.StraightBevelSunGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5474,
        )

        return self.__parent__._cast(
            _5474.StraightBevelSunGearCompoundModalAnalysisAtASpeed
        )

    @property
    def synchroniser_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5475.SynchroniserCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5475,
        )

        return self.__parent__._cast(_5475.SynchroniserCompoundModalAnalysisAtASpeed)

    @property
    def synchroniser_half_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5476.SynchroniserHalfCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5476,
        )

        return self.__parent__._cast(
            _5476.SynchroniserHalfCompoundModalAnalysisAtASpeed
        )

    @property
    def synchroniser_part_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5477.SynchroniserPartCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5477,
        )

        return self.__parent__._cast(
            _5477.SynchroniserPartCompoundModalAnalysisAtASpeed
        )

    @property
    def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5478.SynchroniserSleeveCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5478,
        )

        return self.__parent__._cast(
            _5478.SynchroniserSleeveCompoundModalAnalysisAtASpeed
        )

    @property
    def torque_converter_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5479.TorqueConverterCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5479,
        )

        return self.__parent__._cast(_5479.TorqueConverterCompoundModalAnalysisAtASpeed)

    @property
    def torque_converter_pump_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5481.TorqueConverterPumpCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5481,
        )

        return self.__parent__._cast(
            _5481.TorqueConverterPumpCompoundModalAnalysisAtASpeed
        )

    @property
    def torque_converter_turbine_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5482.TorqueConverterTurbineCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5482,
        )

        return self.__parent__._cast(
            _5482.TorqueConverterTurbineCompoundModalAnalysisAtASpeed
        )

    @property
    def unbalanced_mass_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5483.UnbalancedMassCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5483,
        )

        return self.__parent__._cast(_5483.UnbalancedMassCompoundModalAnalysisAtASpeed)

    @property
    def virtual_component_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5484.VirtualComponentCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5484,
        )

        return self.__parent__._cast(
            _5484.VirtualComponentCompoundModalAnalysisAtASpeed
        )

    @property
    def worm_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5485.WormGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5485,
        )

        return self.__parent__._cast(_5485.WormGearCompoundModalAnalysisAtASpeed)

    @property
    def worm_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5487.WormGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5487,
        )

        return self.__parent__._cast(_5487.WormGearSetCompoundModalAnalysisAtASpeed)

    @property
    def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5488.ZerolBevelGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5488,
        )

        return self.__parent__._cast(_5488.ZerolBevelGearCompoundModalAnalysisAtASpeed)

    @property
    def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5490.ZerolBevelGearSetCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5490,
        )

        return self.__parent__._cast(
            _5490.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
        )

    @property
    def abstract_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5649.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5649,
        )

        return self.__parent__._cast(
            _5649.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
        )

    @property
    def abstract_shaft_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5650.AbstractShaftCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5650,
        )

        return self.__parent__._cast(
            _5650.AbstractShaftCompoundMultibodyDynamicsAnalysis
        )

    @property
    def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5651.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5651,
        )

        return self.__parent__._cast(
            _5651.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
        )

    @property
    def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5653.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5653,
        )

        return self.__parent__._cast(
            _5653.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5655.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5655,
        )

        return self.__parent__._cast(
            _5655.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5656.AssemblyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5656,
        )

        return self.__parent__._cast(_5656.AssemblyCompoundMultibodyDynamicsAnalysis)

    @property
    def bearing_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5657.BearingCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5657,
        )

        return self.__parent__._cast(_5657.BearingCompoundMultibodyDynamicsAnalysis)

    @property
    def belt_drive_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5659.BeltDriveCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5659,
        )

        return self.__parent__._cast(_5659.BeltDriveCompoundMultibodyDynamicsAnalysis)

    @property
    def bevel_differential_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5660.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5660,
        )

        return self.__parent__._cast(
            _5660.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5662.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5662,
        )

        return self.__parent__._cast(
            _5662.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5663.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5663,
        )

        return self.__parent__._cast(
            _5663.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5664.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5664,
        )

        return self.__parent__._cast(
            _5664.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5665.BevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5665,
        )

        return self.__parent__._cast(_5665.BevelGearCompoundMultibodyDynamicsAnalysis)

    @property
    def bevel_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5667.BevelGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5667,
        )

        return self.__parent__._cast(
            _5667.BevelGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bolt_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5668.BoltCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5668,
        )

        return self.__parent__._cast(_5668.BoltCompoundMultibodyDynamicsAnalysis)

    @property
    def bolted_joint_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5669.BoltedJointCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5669,
        )

        return self.__parent__._cast(_5669.BoltedJointCompoundMultibodyDynamicsAnalysis)

    @property
    def clutch_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5670.ClutchCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5670,
        )

        return self.__parent__._cast(_5670.ClutchCompoundMultibodyDynamicsAnalysis)

    @property
    def clutch_half_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5672.ClutchHalfCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5672,
        )

        return self.__parent__._cast(_5672.ClutchHalfCompoundMultibodyDynamicsAnalysis)

    @property
    def component_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5674.ComponentCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5674,
        )

        return self.__parent__._cast(_5674.ComponentCompoundMultibodyDynamicsAnalysis)

    @property
    def concept_coupling_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5675.ConceptCouplingCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5675,
        )

        return self.__parent__._cast(
            _5675.ConceptCouplingCompoundMultibodyDynamicsAnalysis
        )

    @property
    def concept_coupling_half_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5677.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5677,
        )

        return self.__parent__._cast(
            _5677.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
        )

    @property
    def concept_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5678.ConceptGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5678,
        )

        return self.__parent__._cast(_5678.ConceptGearCompoundMultibodyDynamicsAnalysis)

    @property
    def concept_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5680.ConceptGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5680,
        )

        return self.__parent__._cast(
            _5680.ConceptGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def conical_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5681.ConicalGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5681,
        )

        return self.__parent__._cast(_5681.ConicalGearCompoundMultibodyDynamicsAnalysis)

    @property
    def conical_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5683.ConicalGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5683,
        )

        return self.__parent__._cast(
            _5683.ConicalGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def connector_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5685.ConnectorCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5685,
        )

        return self.__parent__._cast(_5685.ConnectorCompoundMultibodyDynamicsAnalysis)

    @property
    def coupling_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5686.CouplingCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5686,
        )

        return self.__parent__._cast(_5686.CouplingCompoundMultibodyDynamicsAnalysis)

    @property
    def coupling_half_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5688.CouplingHalfCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5688,
        )

        return self.__parent__._cast(
            _5688.CouplingHalfCompoundMultibodyDynamicsAnalysis
        )

    @property
    def cvt_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5690.CVTCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5690,
        )

        return self.__parent__._cast(_5690.CVTCompoundMultibodyDynamicsAnalysis)

    @property
    def cvt_pulley_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5691.CVTPulleyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5691,
        )

        return self.__parent__._cast(_5691.CVTPulleyCompoundMultibodyDynamicsAnalysis)

    @property
    def cycloidal_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5692.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5692,
        )

        return self.__parent__._cast(
            _5692.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
        )

    @property
    def cycloidal_disc_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5694.CycloidalDiscCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5694,
        )

        return self.__parent__._cast(
            _5694.CycloidalDiscCompoundMultibodyDynamicsAnalysis
        )

    @property
    def cylindrical_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5696.CylindricalGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5696,
        )

        return self.__parent__._cast(
            _5696.CylindricalGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def cylindrical_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5698.CylindricalGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5698,
        )

        return self.__parent__._cast(
            _5698.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5699.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5699,
        )

        return self.__parent__._cast(
            _5699.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def datum_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5700.DatumCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5700,
        )

        return self.__parent__._cast(_5700.DatumCompoundMultibodyDynamicsAnalysis)

    @property
    def external_cad_model_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5701.ExternalCADModelCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5701,
        )

        return self.__parent__._cast(
            _5701.ExternalCADModelCompoundMultibodyDynamicsAnalysis
        )

    @property
    def face_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5702.FaceGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5702,
        )

        return self.__parent__._cast(_5702.FaceGearCompoundMultibodyDynamicsAnalysis)

    @property
    def face_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5704.FaceGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5704,
        )

        return self.__parent__._cast(_5704.FaceGearSetCompoundMultibodyDynamicsAnalysis)

    @property
    def fe_part_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5705.FEPartCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5705,
        )

        return self.__parent__._cast(_5705.FEPartCompoundMultibodyDynamicsAnalysis)

    @property
    def flexible_pin_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5706.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5706,
        )

        return self.__parent__._cast(
            _5706.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
        )

    @property
    def gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5707.GearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5707,
        )

        return self.__parent__._cast(_5707.GearCompoundMultibodyDynamicsAnalysis)

    @property
    def gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5709.GearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5709,
        )

        return self.__parent__._cast(_5709.GearSetCompoundMultibodyDynamicsAnalysis)

    @property
    def guide_dxf_model_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5710.GuideDxfModelCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5710,
        )

        return self.__parent__._cast(
            _5710.GuideDxfModelCompoundMultibodyDynamicsAnalysis
        )

    @property
    def hypoid_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5711.HypoidGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5711,
        )

        return self.__parent__._cast(_5711.HypoidGearCompoundMultibodyDynamicsAnalysis)

    @property
    def hypoid_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5713.HypoidGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5713,
        )

        return self.__parent__._cast(
            _5713.HypoidGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5715.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5715,
        )

        return self.__parent__._cast(
            _5715.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> (
        "_5717.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis"
    ):
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5717,
        )

        return self.__parent__._cast(
            _5717.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5718.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5718,
        )

        return self.__parent__._cast(
            _5718.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5720.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5720,
        )

        return self.__parent__._cast(
            _5720.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> (
        "_5721.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis"
    ):
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5721,
        )

        return self.__parent__._cast(
            _5721.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5723.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5723,
        )

        return self.__parent__._cast(
            _5723.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def mass_disc_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5724.MassDiscCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5724,
        )

        return self.__parent__._cast(_5724.MassDiscCompoundMultibodyDynamicsAnalysis)

    @property
    def measurement_component_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5725.MeasurementComponentCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5725,
        )

        return self.__parent__._cast(
            _5725.MeasurementComponentCompoundMultibodyDynamicsAnalysis
        )

    @property
    def microphone_array_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5726.MicrophoneArrayCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5726,
        )

        return self.__parent__._cast(
            _5726.MicrophoneArrayCompoundMultibodyDynamicsAnalysis
        )

    @property
    def microphone_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5727.MicrophoneCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5727,
        )

        return self.__parent__._cast(_5727.MicrophoneCompoundMultibodyDynamicsAnalysis)

    @property
    def mountable_component_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5728.MountableComponentCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5728,
        )

        return self.__parent__._cast(
            _5728.MountableComponentCompoundMultibodyDynamicsAnalysis
        )

    @property
    def oil_seal_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5729.OilSealCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5729,
        )

        return self.__parent__._cast(_5729.OilSealCompoundMultibodyDynamicsAnalysis)

    @property
    def part_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5730.PartCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5730,
        )

        return self.__parent__._cast(_5730.PartCompoundMultibodyDynamicsAnalysis)

    @property
    def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5731.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5731,
        )

        return self.__parent__._cast(
            _5731.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
        )

    @property
    def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5733.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5733,
        )

        return self.__parent__._cast(
            _5733.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
        )

    @property
    def planetary_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5735.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5735,
        )

        return self.__parent__._cast(
            _5735.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def planet_carrier_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5736.PlanetCarrierCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5736,
        )

        return self.__parent__._cast(
            _5736.PlanetCarrierCompoundMultibodyDynamicsAnalysis
        )

    @property
    def point_load_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5737.PointLoadCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5737,
        )

        return self.__parent__._cast(_5737.PointLoadCompoundMultibodyDynamicsAnalysis)

    @property
    def power_load_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5738.PowerLoadCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5738,
        )

        return self.__parent__._cast(_5738.PowerLoadCompoundMultibodyDynamicsAnalysis)

    @property
    def pulley_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5739.PulleyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5739,
        )

        return self.__parent__._cast(_5739.PulleyCompoundMultibodyDynamicsAnalysis)

    @property
    def ring_pins_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5740.RingPinsCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5740,
        )

        return self.__parent__._cast(_5740.RingPinsCompoundMultibodyDynamicsAnalysis)

    @property
    def rolling_ring_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5742.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5742,
        )

        return self.__parent__._cast(
            _5742.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
        )

    @property
    def rolling_ring_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5743.RollingRingCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5743,
        )

        return self.__parent__._cast(_5743.RollingRingCompoundMultibodyDynamicsAnalysis)

    @property
    def root_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5745.RootAssemblyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5745,
        )

        return self.__parent__._cast(
            _5745.RootAssemblyCompoundMultibodyDynamicsAnalysis
        )

    @property
    def shaft_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5746.ShaftCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5746,
        )

        return self.__parent__._cast(_5746.ShaftCompoundMultibodyDynamicsAnalysis)

    @property
    def shaft_hub_connection_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5747.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5747,
        )

        return self.__parent__._cast(
            _5747.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
        )

    @property
    def specialised_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5749.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5749,
        )

        return self.__parent__._cast(
            _5749.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
        )

    @property
    def spiral_bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5750.SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5750,
        )

        return self.__parent__._cast(
            _5750.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5752.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5752,
        )

        return self.__parent__._cast(
            _5752.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def spring_damper_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5753.SpringDamperCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5753,
        )

        return self.__parent__._cast(
            _5753.SpringDamperCompoundMultibodyDynamicsAnalysis
        )

    @property
    def spring_damper_half_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5755.SpringDamperHalfCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5755,
        )

        return self.__parent__._cast(
            _5755.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5756.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5756,
        )

        return self.__parent__._cast(
            _5756.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5758.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5758,
        )

        return self.__parent__._cast(
            _5758.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5759.StraightBevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5759,
        )

        return self.__parent__._cast(
            _5759.StraightBevelGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5761.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5761,
        )

        return self.__parent__._cast(
            _5761.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5762.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5762,
        )

        return self.__parent__._cast(
            _5762.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5763.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5763,
        )

        return self.__parent__._cast(
            _5763.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def synchroniser_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5764.SynchroniserCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5764,
        )

        return self.__parent__._cast(
            _5764.SynchroniserCompoundMultibodyDynamicsAnalysis
        )

    @property
    def synchroniser_half_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5765.SynchroniserHalfCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5765,
        )

        return self.__parent__._cast(
            _5765.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
        )

    @property
    def synchroniser_part_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5766.SynchroniserPartCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5766,
        )

        return self.__parent__._cast(
            _5766.SynchroniserPartCompoundMultibodyDynamicsAnalysis
        )

    @property
    def synchroniser_sleeve_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5767.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5767,
        )

        return self.__parent__._cast(
            _5767.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
        )

    @property
    def torque_converter_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5768.TorqueConverterCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5768,
        )

        return self.__parent__._cast(
            _5768.TorqueConverterCompoundMultibodyDynamicsAnalysis
        )

    @property
    def torque_converter_pump_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5770.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5770,
        )

        return self.__parent__._cast(
            _5770.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
        )

    @property
    def torque_converter_turbine_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5771.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5771,
        )

        return self.__parent__._cast(
            _5771.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
        )

    @property
    def unbalanced_mass_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5772.UnbalancedMassCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5772,
        )

        return self.__parent__._cast(
            _5772.UnbalancedMassCompoundMultibodyDynamicsAnalysis
        )

    @property
    def virtual_component_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5773.VirtualComponentCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5773,
        )

        return self.__parent__._cast(
            _5773.VirtualComponentCompoundMultibodyDynamicsAnalysis
        )

    @property
    def worm_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5774.WormGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5774,
        )

        return self.__parent__._cast(_5774.WormGearCompoundMultibodyDynamicsAnalysis)

    @property
    def worm_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5776.WormGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5776,
        )

        return self.__parent__._cast(_5776.WormGearSetCompoundMultibodyDynamicsAnalysis)

    @property
    def zerol_bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5777.ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5777,
        )

        return self.__parent__._cast(
            _5777.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5779.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5779,
        )

        return self.__parent__._cast(
            _5779.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def abstract_assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6004.AbstractAssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6004,
        )

        return self.__parent__._cast(_6004.AbstractAssemblyCompoundHarmonicAnalysis)

    @property
    def abstract_shaft_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6005.AbstractShaftCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6005,
        )

        return self.__parent__._cast(_6005.AbstractShaftCompoundHarmonicAnalysis)

    @property
    def abstract_shaft_or_housing_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6006.AbstractShaftOrHousingCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6006,
        )

        return self.__parent__._cast(
            _6006.AbstractShaftOrHousingCompoundHarmonicAnalysis
        )

    @property
    def agma_gleason_conical_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6008.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6008,
        )

        return self.__parent__._cast(
            _6008.AGMAGleasonConicalGearCompoundHarmonicAnalysis
        )

    @property
    def agma_gleason_conical_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6010.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6010,
        )

        return self.__parent__._cast(
            _6010.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
        )

    @property
    def assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6011.AssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6011,
        )

        return self.__parent__._cast(_6011.AssemblyCompoundHarmonicAnalysis)

    @property
    def bearing_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6012.BearingCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6012,
        )

        return self.__parent__._cast(_6012.BearingCompoundHarmonicAnalysis)

    @property
    def belt_drive_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6014.BeltDriveCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6014,
        )

        return self.__parent__._cast(_6014.BeltDriveCompoundHarmonicAnalysis)

    @property
    def bevel_differential_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6015.BevelDifferentialGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6015,
        )

        return self.__parent__._cast(
            _6015.BevelDifferentialGearCompoundHarmonicAnalysis
        )

    @property
    def bevel_differential_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6017.BevelDifferentialGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6017,
        )

        return self.__parent__._cast(
            _6017.BevelDifferentialGearSetCompoundHarmonicAnalysis
        )

    @property
    def bevel_differential_planet_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6018.BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6018,
        )

        return self.__parent__._cast(
            _6018.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6019.BevelDifferentialSunGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6019,
        )

        return self.__parent__._cast(
            _6019.BevelDifferentialSunGearCompoundHarmonicAnalysis
        )

    @property
    def bevel_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6020.BevelGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6020,
        )

        return self.__parent__._cast(_6020.BevelGearCompoundHarmonicAnalysis)

    @property
    def bevel_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6022.BevelGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6022,
        )

        return self.__parent__._cast(_6022.BevelGearSetCompoundHarmonicAnalysis)

    @property
    def bolt_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6023.BoltCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6023,
        )

        return self.__parent__._cast(_6023.BoltCompoundHarmonicAnalysis)

    @property
    def bolted_joint_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6024.BoltedJointCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6024,
        )

        return self.__parent__._cast(_6024.BoltedJointCompoundHarmonicAnalysis)

    @property
    def clutch_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6025.ClutchCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6025,
        )

        return self.__parent__._cast(_6025.ClutchCompoundHarmonicAnalysis)

    @property
    def clutch_half_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6027.ClutchHalfCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6027,
        )

        return self.__parent__._cast(_6027.ClutchHalfCompoundHarmonicAnalysis)

    @property
    def component_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6029.ComponentCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6029,
        )

        return self.__parent__._cast(_6029.ComponentCompoundHarmonicAnalysis)

    @property
    def concept_coupling_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6030.ConceptCouplingCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6030,
        )

        return self.__parent__._cast(_6030.ConceptCouplingCompoundHarmonicAnalysis)

    @property
    def concept_coupling_half_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6032.ConceptCouplingHalfCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6032,
        )

        return self.__parent__._cast(_6032.ConceptCouplingHalfCompoundHarmonicAnalysis)

    @property
    def concept_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6033.ConceptGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6033,
        )

        return self.__parent__._cast(_6033.ConceptGearCompoundHarmonicAnalysis)

    @property
    def concept_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6035.ConceptGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6035,
        )

        return self.__parent__._cast(_6035.ConceptGearSetCompoundHarmonicAnalysis)

    @property
    def conical_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6036.ConicalGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6036,
        )

        return self.__parent__._cast(_6036.ConicalGearCompoundHarmonicAnalysis)

    @property
    def conical_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6038.ConicalGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6038,
        )

        return self.__parent__._cast(_6038.ConicalGearSetCompoundHarmonicAnalysis)

    @property
    def connector_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6040.ConnectorCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6040,
        )

        return self.__parent__._cast(_6040.ConnectorCompoundHarmonicAnalysis)

    @property
    def coupling_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6041.CouplingCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6041,
        )

        return self.__parent__._cast(_6041.CouplingCompoundHarmonicAnalysis)

    @property
    def coupling_half_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6043.CouplingHalfCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6043,
        )

        return self.__parent__._cast(_6043.CouplingHalfCompoundHarmonicAnalysis)

    @property
    def cvt_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6045.CVTCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6045,
        )

        return self.__parent__._cast(_6045.CVTCompoundHarmonicAnalysis)

    @property
    def cvt_pulley_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6046.CVTPulleyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6046,
        )

        return self.__parent__._cast(_6046.CVTPulleyCompoundHarmonicAnalysis)

    @property
    def cycloidal_assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6047.CycloidalAssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6047,
        )

        return self.__parent__._cast(_6047.CycloidalAssemblyCompoundHarmonicAnalysis)

    @property
    def cycloidal_disc_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6049.CycloidalDiscCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6049,
        )

        return self.__parent__._cast(_6049.CycloidalDiscCompoundHarmonicAnalysis)

    @property
    def cylindrical_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6051.CylindricalGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6051,
        )

        return self.__parent__._cast(_6051.CylindricalGearCompoundHarmonicAnalysis)

    @property
    def cylindrical_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6053.CylindricalGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6053,
        )

        return self.__parent__._cast(_6053.CylindricalGearSetCompoundHarmonicAnalysis)

    @property
    def cylindrical_planet_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6054.CylindricalPlanetGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6054,
        )

        return self.__parent__._cast(
            _6054.CylindricalPlanetGearCompoundHarmonicAnalysis
        )

    @property
    def datum_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6055.DatumCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6055,
        )

        return self.__parent__._cast(_6055.DatumCompoundHarmonicAnalysis)

    @property
    def external_cad_model_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6056.ExternalCADModelCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6056,
        )

        return self.__parent__._cast(_6056.ExternalCADModelCompoundHarmonicAnalysis)

    @property
    def face_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6057.FaceGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6057,
        )

        return self.__parent__._cast(_6057.FaceGearCompoundHarmonicAnalysis)

    @property
    def face_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6059.FaceGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6059,
        )

        return self.__parent__._cast(_6059.FaceGearSetCompoundHarmonicAnalysis)

    @property
    def fe_part_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6060.FEPartCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6060,
        )

        return self.__parent__._cast(_6060.FEPartCompoundHarmonicAnalysis)

    @property
    def flexible_pin_assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6061.FlexiblePinAssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6061,
        )

        return self.__parent__._cast(_6061.FlexiblePinAssemblyCompoundHarmonicAnalysis)

    @property
    def gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6062.GearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6062,
        )

        return self.__parent__._cast(_6062.GearCompoundHarmonicAnalysis)

    @property
    def gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6064.GearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6064,
        )

        return self.__parent__._cast(_6064.GearSetCompoundHarmonicAnalysis)

    @property
    def guide_dxf_model_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6065.GuideDxfModelCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6065,
        )

        return self.__parent__._cast(_6065.GuideDxfModelCompoundHarmonicAnalysis)

    @property
    def hypoid_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6066.HypoidGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6066,
        )

        return self.__parent__._cast(_6066.HypoidGearCompoundHarmonicAnalysis)

    @property
    def hypoid_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6068.HypoidGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6068,
        )

        return self.__parent__._cast(_6068.HypoidGearSetCompoundHarmonicAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6070.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6070,
        )

        return self.__parent__._cast(
            _6070.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6072.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6072,
        )

        return self.__parent__._cast(
            _6072.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6073.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6073,
        )

        return self.__parent__._cast(
            _6073.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6075.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6075,
        )

        return self.__parent__._cast(
            _6075.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6076.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6076,
        )

        return self.__parent__._cast(
            _6076.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6078.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6078,
        )

        return self.__parent__._cast(
            _6078.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
        )

    @property
    def mass_disc_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6079.MassDiscCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6079,
        )

        return self.__parent__._cast(_6079.MassDiscCompoundHarmonicAnalysis)

    @property
    def measurement_component_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6080.MeasurementComponentCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6080,
        )

        return self.__parent__._cast(_6080.MeasurementComponentCompoundHarmonicAnalysis)

    @property
    def microphone_array_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6081.MicrophoneArrayCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6081,
        )

        return self.__parent__._cast(_6081.MicrophoneArrayCompoundHarmonicAnalysis)

    @property
    def microphone_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6082.MicrophoneCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6082,
        )

        return self.__parent__._cast(_6082.MicrophoneCompoundHarmonicAnalysis)

    @property
    def mountable_component_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6083.MountableComponentCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6083,
        )

        return self.__parent__._cast(_6083.MountableComponentCompoundHarmonicAnalysis)

    @property
    def oil_seal_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6084.OilSealCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6084,
        )

        return self.__parent__._cast(_6084.OilSealCompoundHarmonicAnalysis)

    @property
    def part_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6085.PartCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6085,
        )

        return self.__parent__._cast(_6085.PartCompoundHarmonicAnalysis)

    @property
    def part_to_part_shear_coupling_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6086.PartToPartShearCouplingCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6086,
        )

        return self.__parent__._cast(
            _6086.PartToPartShearCouplingCompoundHarmonicAnalysis
        )

    @property
    def part_to_part_shear_coupling_half_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6088.PartToPartShearCouplingHalfCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6088,
        )

        return self.__parent__._cast(
            _6088.PartToPartShearCouplingHalfCompoundHarmonicAnalysis
        )

    @property
    def planetary_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6090.PlanetaryGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6090,
        )

        return self.__parent__._cast(_6090.PlanetaryGearSetCompoundHarmonicAnalysis)

    @property
    def planet_carrier_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6091.PlanetCarrierCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6091,
        )

        return self.__parent__._cast(_6091.PlanetCarrierCompoundHarmonicAnalysis)

    @property
    def point_load_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6092.PointLoadCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6092,
        )

        return self.__parent__._cast(_6092.PointLoadCompoundHarmonicAnalysis)

    @property
    def power_load_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6093.PowerLoadCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6093,
        )

        return self.__parent__._cast(_6093.PowerLoadCompoundHarmonicAnalysis)

    @property
    def pulley_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6094.PulleyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6094,
        )

        return self.__parent__._cast(_6094.PulleyCompoundHarmonicAnalysis)

    @property
    def ring_pins_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6095.RingPinsCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6095,
        )

        return self.__parent__._cast(_6095.RingPinsCompoundHarmonicAnalysis)

    @property
    def rolling_ring_assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6097.RollingRingAssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6097,
        )

        return self.__parent__._cast(_6097.RollingRingAssemblyCompoundHarmonicAnalysis)

    @property
    def rolling_ring_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6098.RollingRingCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6098,
        )

        return self.__parent__._cast(_6098.RollingRingCompoundHarmonicAnalysis)

    @property
    def root_assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6100.RootAssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6100,
        )

        return self.__parent__._cast(_6100.RootAssemblyCompoundHarmonicAnalysis)

    @property
    def shaft_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6101.ShaftCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6101,
        )

        return self.__parent__._cast(_6101.ShaftCompoundHarmonicAnalysis)

    @property
    def shaft_hub_connection_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6102.ShaftHubConnectionCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6102,
        )

        return self.__parent__._cast(_6102.ShaftHubConnectionCompoundHarmonicAnalysis)

    @property
    def specialised_assembly_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6104.SpecialisedAssemblyCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6104,
        )

        return self.__parent__._cast(_6104.SpecialisedAssemblyCompoundHarmonicAnalysis)

    @property
    def spiral_bevel_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6105.SpiralBevelGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6105,
        )

        return self.__parent__._cast(_6105.SpiralBevelGearCompoundHarmonicAnalysis)

    @property
    def spiral_bevel_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6107.SpiralBevelGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6107,
        )

        return self.__parent__._cast(_6107.SpiralBevelGearSetCompoundHarmonicAnalysis)

    @property
    def spring_damper_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6108.SpringDamperCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6108,
        )

        return self.__parent__._cast(_6108.SpringDamperCompoundHarmonicAnalysis)

    @property
    def spring_damper_half_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6110.SpringDamperHalfCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6110,
        )

        return self.__parent__._cast(_6110.SpringDamperHalfCompoundHarmonicAnalysis)

    @property
    def straight_bevel_diff_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6111.StraightBevelDiffGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6111,
        )

        return self.__parent__._cast(
            _6111.StraightBevelDiffGearCompoundHarmonicAnalysis
        )

    @property
    def straight_bevel_diff_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6113.StraightBevelDiffGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6113,
        )

        return self.__parent__._cast(
            _6113.StraightBevelDiffGearSetCompoundHarmonicAnalysis
        )

    @property
    def straight_bevel_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6114.StraightBevelGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6114,
        )

        return self.__parent__._cast(_6114.StraightBevelGearCompoundHarmonicAnalysis)

    @property
    def straight_bevel_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6116.StraightBevelGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6116,
        )

        return self.__parent__._cast(_6116.StraightBevelGearSetCompoundHarmonicAnalysis)

    @property
    def straight_bevel_planet_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6117.StraightBevelPlanetGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6117,
        )

        return self.__parent__._cast(
            _6117.StraightBevelPlanetGearCompoundHarmonicAnalysis
        )

    @property
    def straight_bevel_sun_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6118.StraightBevelSunGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6118,
        )

        return self.__parent__._cast(_6118.StraightBevelSunGearCompoundHarmonicAnalysis)

    @property
    def synchroniser_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6119.SynchroniserCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6119,
        )

        return self.__parent__._cast(_6119.SynchroniserCompoundHarmonicAnalysis)

    @property
    def synchroniser_half_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6120.SynchroniserHalfCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6120,
        )

        return self.__parent__._cast(_6120.SynchroniserHalfCompoundHarmonicAnalysis)

    @property
    def synchroniser_part_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6121.SynchroniserPartCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6121,
        )

        return self.__parent__._cast(_6121.SynchroniserPartCompoundHarmonicAnalysis)

    @property
    def synchroniser_sleeve_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6122.SynchroniserSleeveCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6122,
        )

        return self.__parent__._cast(_6122.SynchroniserSleeveCompoundHarmonicAnalysis)

    @property
    def torque_converter_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6123.TorqueConverterCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6123,
        )

        return self.__parent__._cast(_6123.TorqueConverterCompoundHarmonicAnalysis)

    @property
    def torque_converter_pump_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6125.TorqueConverterPumpCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6125,
        )

        return self.__parent__._cast(_6125.TorqueConverterPumpCompoundHarmonicAnalysis)

    @property
    def torque_converter_turbine_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6126.TorqueConverterTurbineCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6126,
        )

        return self.__parent__._cast(
            _6126.TorqueConverterTurbineCompoundHarmonicAnalysis
        )

    @property
    def unbalanced_mass_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6127.UnbalancedMassCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6127,
        )

        return self.__parent__._cast(_6127.UnbalancedMassCompoundHarmonicAnalysis)

    @property
    def virtual_component_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6128.VirtualComponentCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6128,
        )

        return self.__parent__._cast(_6128.VirtualComponentCompoundHarmonicAnalysis)

    @property
    def worm_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6129.WormGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6129,
        )

        return self.__parent__._cast(_6129.WormGearCompoundHarmonicAnalysis)

    @property
    def worm_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6131.WormGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6131,
        )

        return self.__parent__._cast(_6131.WormGearSetCompoundHarmonicAnalysis)

    @property
    def zerol_bevel_gear_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6132.ZerolBevelGearCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6132,
        )

        return self.__parent__._cast(_6132.ZerolBevelGearCompoundHarmonicAnalysis)

    @property
    def zerol_bevel_gear_set_compound_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6134.ZerolBevelGearSetCompoundHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses.compound import (
            _6134,
        )

        return self.__parent__._cast(_6134.ZerolBevelGearSetCompoundHarmonicAnalysis)

    @property
    def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6268.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6268,
        )

        return self.__parent__._cast(
            _6268.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def abstract_shaft_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6269.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6269,
        )

        return self.__parent__._cast(
            _6269.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6270.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6270,
        )

        return self.__parent__._cast(
            _6270.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6272.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6272,
        )

        return self.__parent__._cast(
            _6272.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6274.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6274,
        )

        return self.__parent__._cast(
            _6274.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6275.AssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6275,
        )

        return self.__parent__._cast(
            _6275.AssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bearing_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6276.BearingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6276,
        )

        return self.__parent__._cast(
            _6276.BearingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def belt_drive_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6278.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6278,
        )

        return self.__parent__._cast(
            _6278.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6279.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6279,
        )

        return self.__parent__._cast(
            _6279.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6281.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6281,
        )

        return self.__parent__._cast(
            _6281.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6282.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6282,
        )

        return self.__parent__._cast(
            _6282.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6283.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6283,
        )

        return self.__parent__._cast(
            _6283.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6284.BevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6284,
        )

        return self.__parent__._cast(
            _6284.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6286.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6286,
        )

        return self.__parent__._cast(
            _6286.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bolt_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6287.BoltCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6287,
        )

        return self.__parent__._cast(
            _6287.BoltCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bolted_joint_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6288.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6288,
        )

        return self.__parent__._cast(
            _6288.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def clutch_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6289.ClutchCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6289,
        )

        return self.__parent__._cast(
            _6289.ClutchCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def clutch_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6291.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6291,
        )

        return self.__parent__._cast(
            _6291.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def component_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6293.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6293,
        )

        return self.__parent__._cast(
            _6293.ComponentCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def concept_coupling_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6294.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6294,
        )

        return self.__parent__._cast(
            _6294.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6296.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6296,
        )

        return self.__parent__._cast(
            _6296.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def concept_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6297.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6297,
        )

        return self.__parent__._cast(
            _6297.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def concept_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6299.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6299,
        )

        return self.__parent__._cast(
            _6299.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def conical_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6300.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6300,
        )

        return self.__parent__._cast(
            _6300.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6302.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6302,
        )

        return self.__parent__._cast(
            _6302.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def connector_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6304.ConnectorCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6304,
        )

        return self.__parent__._cast(
            _6304.ConnectorCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def coupling_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6305.CouplingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6305,
        )

        return self.__parent__._cast(
            _6305.CouplingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def coupling_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6307.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6307,
        )

        return self.__parent__._cast(
            _6307.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cvt_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6309.CVTCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6309,
        )

        return self.__parent__._cast(
            _6309.CVTCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cvt_pulley_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6310.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6310,
        )

        return self.__parent__._cast(
            _6310.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cycloidal_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6311.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6311,
        )

        return self.__parent__._cast(
            _6311.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6313.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6313,
        )

        return self.__parent__._cast(
            _6313.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6315.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6315,
        )

        return self.__parent__._cast(
            _6315.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6317.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6317,
        )

        return self.__parent__._cast(
            _6317.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6318.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6318,
        )

        return self.__parent__._cast(
            _6318.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def datum_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6319.DatumCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6319,
        )

        return self.__parent__._cast(
            _6319.DatumCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def external_cad_model_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6320.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6320,
        )

        return self.__parent__._cast(
            _6320.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def face_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6321.FaceGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6321,
        )

        return self.__parent__._cast(
            _6321.FaceGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def face_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6323.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6323,
        )

        return self.__parent__._cast(
            _6323.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def fe_part_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6324.FEPartCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6324,
        )

        return self.__parent__._cast(
            _6324.FEPartCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def flexible_pin_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6325.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6325,
        )

        return self.__parent__._cast(
            _6325.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6326.GearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6326,
        )

        return self.__parent__._cast(
            _6326.GearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6328.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6328,
        )

        return self.__parent__._cast(
            _6328.GearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def guide_dxf_model_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6329.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6329,
        )

        return self.__parent__._cast(
            _6329.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def hypoid_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6330.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6330,
        )

        return self.__parent__._cast(
            _6330.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6332.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6332,
        )

        return self.__parent__._cast(
            _6332.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6334.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6334,
        )

        return self.__parent__._cast(
            _6334.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6336.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6336,
        )

        return self.__parent__._cast(
            _6336.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6337.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6337,
        )

        return self.__parent__._cast(
            _6337.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6339.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6339,
        )

        return self.__parent__._cast(
            _6339.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6340.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6340,
        )

        return self.__parent__._cast(
            _6340.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6342.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6342,
        )

        return self.__parent__._cast(
            _6342.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def mass_disc_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6343.MassDiscCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6343,
        )

        return self.__parent__._cast(
            _6343.MassDiscCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def measurement_component_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6344.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6344,
        )

        return self.__parent__._cast(
            _6344.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def microphone_array_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6345.MicrophoneArrayCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6345,
        )

        return self.__parent__._cast(
            _6345.MicrophoneArrayCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def microphone_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6346.MicrophoneCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6346,
        )

        return self.__parent__._cast(
            _6346.MicrophoneCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def mountable_component_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6347.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6347,
        )

        return self.__parent__._cast(
            _6347.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def oil_seal_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6348.OilSealCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6348,
        )

        return self.__parent__._cast(
            _6348.OilSealCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6349.PartCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6349,
        )

        return self.__parent__._cast(
            _6349.PartCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6350.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6350,
        )

        return self.__parent__._cast(
            _6350.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6352.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6352,
        )

        return self.__parent__._cast(
            _6352.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6354.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6354,
        )

        return self.__parent__._cast(
            _6354.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def planet_carrier_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6355.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6355,
        )

        return self.__parent__._cast(
            _6355.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def point_load_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6356.PointLoadCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6356,
        )

        return self.__parent__._cast(
            _6356.PointLoadCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def power_load_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6357.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6357,
        )

        return self.__parent__._cast(
            _6357.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def pulley_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6358.PulleyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6358,
        )

        return self.__parent__._cast(
            _6358.PulleyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def ring_pins_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6359.RingPinsCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6359,
        )

        return self.__parent__._cast(
            _6359.RingPinsCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def rolling_ring_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6361.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6361,
        )

        return self.__parent__._cast(
            _6361.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def rolling_ring_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6362.RollingRingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6362,
        )

        return self.__parent__._cast(
            _6362.RollingRingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def root_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6364.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6364,
        )

        return self.__parent__._cast(
            _6364.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def shaft_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6365.ShaftCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6365,
        )

        return self.__parent__._cast(
            _6365.ShaftCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def shaft_hub_connection_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6366.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6366,
        )

        return self.__parent__._cast(
            _6366.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6368.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6368,
        )

        return self.__parent__._cast(
            _6368.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6369.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6369,
        )

        return self.__parent__._cast(
            _6369.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6371.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6371,
        )

        return self.__parent__._cast(
            _6371.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spring_damper_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6372.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6372,
        )

        return self.__parent__._cast(
            _6372.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spring_damper_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6374.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6374,
        )

        return self.__parent__._cast(
            _6374.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6375.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6375,
        )

        return self.__parent__._cast(
            _6375.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6377.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6377,
        )

        return self.__parent__._cast(
            _6377.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6378.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6378,
        )

        return self.__parent__._cast(
            _6378.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6380.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6380,
        )

        return self.__parent__._cast(
            _6380.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6381.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6381,
        )

        return self.__parent__._cast(
            _6381.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6382.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6382,
        )

        return self.__parent__._cast(
            _6382.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def synchroniser_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6383.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6383,
        )

        return self.__parent__._cast(
            _6383.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def synchroniser_half_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6384.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6384,
        )

        return self.__parent__._cast(
            _6384.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def synchroniser_part_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6385.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6385,
        )

        return self.__parent__._cast(
            _6385.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6386.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6386,
        )

        return self.__parent__._cast(
            _6386.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def torque_converter_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6387.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6387,
        )

        return self.__parent__._cast(
            _6387.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6389.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6389,
        )

        return self.__parent__._cast(
            _6389.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def torque_converter_turbine_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6390.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6390,
        )

        return self.__parent__._cast(
            _6390.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6391.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6391,
        )

        return self.__parent__._cast(
            _6391.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def virtual_component_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6392.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6392,
        )

        return self.__parent__._cast(
            _6392.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def worm_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6393.WormGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6393,
        )

        return self.__parent__._cast(
            _6393.WormGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def worm_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6395.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6395,
        )

        return self.__parent__._cast(
            _6395.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6396.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6396,
        )

        return self.__parent__._cast(
            _6396.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6398.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6398,
        )

        return self.__parent__._cast(
            _6398.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def abstract_assembly_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6541.AbstractAssemblyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6541,
        )

        return self.__parent__._cast(_6541.AbstractAssemblyCompoundDynamicAnalysis)

    @property
    def abstract_shaft_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6542.AbstractShaftCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6542,
        )

        return self.__parent__._cast(_6542.AbstractShaftCompoundDynamicAnalysis)

    @property
    def abstract_shaft_or_housing_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6543.AbstractShaftOrHousingCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6543,
        )

        return self.__parent__._cast(
            _6543.AbstractShaftOrHousingCompoundDynamicAnalysis
        )

    @property
    def agma_gleason_conical_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6545.AGMAGleasonConicalGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6545,
        )

        return self.__parent__._cast(
            _6545.AGMAGleasonConicalGearCompoundDynamicAnalysis
        )

    @property
    def agma_gleason_conical_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6547.AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6547,
        )

        return self.__parent__._cast(
            _6547.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
        )

    @property
    def assembly_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6548.AssemblyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6548,
        )

        return self.__parent__._cast(_6548.AssemblyCompoundDynamicAnalysis)

    @property
    def bearing_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6549.BearingCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6549,
        )

        return self.__parent__._cast(_6549.BearingCompoundDynamicAnalysis)

    @property
    def belt_drive_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6551.BeltDriveCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6551,
        )

        return self.__parent__._cast(_6551.BeltDriveCompoundDynamicAnalysis)

    @property
    def bevel_differential_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6552.BevelDifferentialGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6552,
        )

        return self.__parent__._cast(_6552.BevelDifferentialGearCompoundDynamicAnalysis)

    @property
    def bevel_differential_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6554.BevelDifferentialGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6554,
        )

        return self.__parent__._cast(
            _6554.BevelDifferentialGearSetCompoundDynamicAnalysis
        )

    @property
    def bevel_differential_planet_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6555.BevelDifferentialPlanetGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6555,
        )

        return self.__parent__._cast(
            _6555.BevelDifferentialPlanetGearCompoundDynamicAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6556.BevelDifferentialSunGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6556,
        )

        return self.__parent__._cast(
            _6556.BevelDifferentialSunGearCompoundDynamicAnalysis
        )

    @property
    def bevel_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6557.BevelGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6557,
        )

        return self.__parent__._cast(_6557.BevelGearCompoundDynamicAnalysis)

    @property
    def bevel_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6559.BevelGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6559,
        )

        return self.__parent__._cast(_6559.BevelGearSetCompoundDynamicAnalysis)

    @property
    def bolt_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6560.BoltCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6560,
        )

        return self.__parent__._cast(_6560.BoltCompoundDynamicAnalysis)

    @property
    def bolted_joint_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6561.BoltedJointCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6561,
        )

        return self.__parent__._cast(_6561.BoltedJointCompoundDynamicAnalysis)

    @property
    def clutch_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6562.ClutchCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6562,
        )

        return self.__parent__._cast(_6562.ClutchCompoundDynamicAnalysis)

    @property
    def clutch_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6564.ClutchHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6564,
        )

        return self.__parent__._cast(_6564.ClutchHalfCompoundDynamicAnalysis)

    @property
    def component_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6566.ComponentCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6566,
        )

        return self.__parent__._cast(_6566.ComponentCompoundDynamicAnalysis)

    @property
    def concept_coupling_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6567.ConceptCouplingCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6567,
        )

        return self.__parent__._cast(_6567.ConceptCouplingCompoundDynamicAnalysis)

    @property
    def concept_coupling_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6569.ConceptCouplingHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6569,
        )

        return self.__parent__._cast(_6569.ConceptCouplingHalfCompoundDynamicAnalysis)

    @property
    def concept_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6570.ConceptGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6570,
        )

        return self.__parent__._cast(_6570.ConceptGearCompoundDynamicAnalysis)

    @property
    def concept_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6572.ConceptGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6572,
        )

        return self.__parent__._cast(_6572.ConceptGearSetCompoundDynamicAnalysis)

    @property
    def conical_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6573.ConicalGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6573,
        )

        return self.__parent__._cast(_6573.ConicalGearCompoundDynamicAnalysis)

    @property
    def conical_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6575.ConicalGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6575,
        )

        return self.__parent__._cast(_6575.ConicalGearSetCompoundDynamicAnalysis)

    @property
    def connector_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6577.ConnectorCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6577,
        )

        return self.__parent__._cast(_6577.ConnectorCompoundDynamicAnalysis)

    @property
    def coupling_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6578.CouplingCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6578,
        )

        return self.__parent__._cast(_6578.CouplingCompoundDynamicAnalysis)

    @property
    def coupling_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6580.CouplingHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6580,
        )

        return self.__parent__._cast(_6580.CouplingHalfCompoundDynamicAnalysis)

    @property
    def cvt_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6582.CVTCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6582,
        )

        return self.__parent__._cast(_6582.CVTCompoundDynamicAnalysis)

    @property
    def cvt_pulley_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6583.CVTPulleyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6583,
        )

        return self.__parent__._cast(_6583.CVTPulleyCompoundDynamicAnalysis)

    @property
    def cycloidal_assembly_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6584.CycloidalAssemblyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6584,
        )

        return self.__parent__._cast(_6584.CycloidalAssemblyCompoundDynamicAnalysis)

    @property
    def cycloidal_disc_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6586.CycloidalDiscCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6586,
        )

        return self.__parent__._cast(_6586.CycloidalDiscCompoundDynamicAnalysis)

    @property
    def cylindrical_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6588.CylindricalGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6588,
        )

        return self.__parent__._cast(_6588.CylindricalGearCompoundDynamicAnalysis)

    @property
    def cylindrical_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6590.CylindricalGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6590,
        )

        return self.__parent__._cast(_6590.CylindricalGearSetCompoundDynamicAnalysis)

    @property
    def cylindrical_planet_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6591.CylindricalPlanetGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6591,
        )

        return self.__parent__._cast(_6591.CylindricalPlanetGearCompoundDynamicAnalysis)

    @property
    def datum_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6592.DatumCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6592,
        )

        return self.__parent__._cast(_6592.DatumCompoundDynamicAnalysis)

    @property
    def external_cad_model_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6593.ExternalCADModelCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6593,
        )

        return self.__parent__._cast(_6593.ExternalCADModelCompoundDynamicAnalysis)

    @property
    def face_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6594.FaceGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6594,
        )

        return self.__parent__._cast(_6594.FaceGearCompoundDynamicAnalysis)

    @property
    def face_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6596.FaceGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6596,
        )

        return self.__parent__._cast(_6596.FaceGearSetCompoundDynamicAnalysis)

    @property
    def fe_part_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6597.FEPartCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6597,
        )

        return self.__parent__._cast(_6597.FEPartCompoundDynamicAnalysis)

    @property
    def flexible_pin_assembly_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6598.FlexiblePinAssemblyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6598,
        )

        return self.__parent__._cast(_6598.FlexiblePinAssemblyCompoundDynamicAnalysis)

    @property
    def gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6599.GearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6599,
        )

        return self.__parent__._cast(_6599.GearCompoundDynamicAnalysis)

    @property
    def gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6601.GearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6601,
        )

        return self.__parent__._cast(_6601.GearSetCompoundDynamicAnalysis)

    @property
    def guide_dxf_model_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6602.GuideDxfModelCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6602,
        )

        return self.__parent__._cast(_6602.GuideDxfModelCompoundDynamicAnalysis)

    @property
    def hypoid_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6603.HypoidGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6603,
        )

        return self.__parent__._cast(_6603.HypoidGearCompoundDynamicAnalysis)

    @property
    def hypoid_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6605.HypoidGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6605,
        )

        return self.__parent__._cast(_6605.HypoidGearSetCompoundDynamicAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6607.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6607,
        )

        return self.__parent__._cast(
            _6607.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6609.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6609,
        )

        return self.__parent__._cast(
            _6609.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6610.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6610,
        )

        return self.__parent__._cast(
            _6610.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6612.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6612,
        )

        return self.__parent__._cast(
            _6612.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6613.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6613,
        )

        return self.__parent__._cast(
            _6613.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6615.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6615,
        )

        return self.__parent__._cast(
            _6615.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
        )

    @property
    def mass_disc_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6616.MassDiscCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6616,
        )

        return self.__parent__._cast(_6616.MassDiscCompoundDynamicAnalysis)

    @property
    def measurement_component_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6617.MeasurementComponentCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6617,
        )

        return self.__parent__._cast(_6617.MeasurementComponentCompoundDynamicAnalysis)

    @property
    def microphone_array_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6618.MicrophoneArrayCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6618,
        )

        return self.__parent__._cast(_6618.MicrophoneArrayCompoundDynamicAnalysis)

    @property
    def microphone_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6619.MicrophoneCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6619,
        )

        return self.__parent__._cast(_6619.MicrophoneCompoundDynamicAnalysis)

    @property
    def mountable_component_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6620.MountableComponentCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6620,
        )

        return self.__parent__._cast(_6620.MountableComponentCompoundDynamicAnalysis)

    @property
    def oil_seal_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6621.OilSealCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6621,
        )

        return self.__parent__._cast(_6621.OilSealCompoundDynamicAnalysis)

    @property
    def part_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6622.PartCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6622,
        )

        return self.__parent__._cast(_6622.PartCompoundDynamicAnalysis)

    @property
    def part_to_part_shear_coupling_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6623.PartToPartShearCouplingCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6623,
        )

        return self.__parent__._cast(
            _6623.PartToPartShearCouplingCompoundDynamicAnalysis
        )

    @property
    def part_to_part_shear_coupling_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6625.PartToPartShearCouplingHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6625,
        )

        return self.__parent__._cast(
            _6625.PartToPartShearCouplingHalfCompoundDynamicAnalysis
        )

    @property
    def planetary_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6627.PlanetaryGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6627,
        )

        return self.__parent__._cast(_6627.PlanetaryGearSetCompoundDynamicAnalysis)

    @property
    def planet_carrier_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6628.PlanetCarrierCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6628,
        )

        return self.__parent__._cast(_6628.PlanetCarrierCompoundDynamicAnalysis)

    @property
    def point_load_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6629.PointLoadCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6629,
        )

        return self.__parent__._cast(_6629.PointLoadCompoundDynamicAnalysis)

    @property
    def power_load_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6630.PowerLoadCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6630,
        )

        return self.__parent__._cast(_6630.PowerLoadCompoundDynamicAnalysis)

    @property
    def pulley_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6631.PulleyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6631,
        )

        return self.__parent__._cast(_6631.PulleyCompoundDynamicAnalysis)

    @property
    def ring_pins_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6632.RingPinsCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6632,
        )

        return self.__parent__._cast(_6632.RingPinsCompoundDynamicAnalysis)

    @property
    def rolling_ring_assembly_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6634.RollingRingAssemblyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6634,
        )

        return self.__parent__._cast(_6634.RollingRingAssemblyCompoundDynamicAnalysis)

    @property
    def rolling_ring_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6635.RollingRingCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6635,
        )

        return self.__parent__._cast(_6635.RollingRingCompoundDynamicAnalysis)

    @property
    def root_assembly_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6637.RootAssemblyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6637,
        )

        return self.__parent__._cast(_6637.RootAssemblyCompoundDynamicAnalysis)

    @property
    def shaft_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6638.ShaftCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6638,
        )

        return self.__parent__._cast(_6638.ShaftCompoundDynamicAnalysis)

    @property
    def shaft_hub_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6639.ShaftHubConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6639,
        )

        return self.__parent__._cast(_6639.ShaftHubConnectionCompoundDynamicAnalysis)

    @property
    def specialised_assembly_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6641.SpecialisedAssemblyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6641,
        )

        return self.__parent__._cast(_6641.SpecialisedAssemblyCompoundDynamicAnalysis)

    @property
    def spiral_bevel_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6642.SpiralBevelGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6642,
        )

        return self.__parent__._cast(_6642.SpiralBevelGearCompoundDynamicAnalysis)

    @property
    def spiral_bevel_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6644.SpiralBevelGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6644,
        )

        return self.__parent__._cast(_6644.SpiralBevelGearSetCompoundDynamicAnalysis)

    @property
    def spring_damper_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6645.SpringDamperCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6645,
        )

        return self.__parent__._cast(_6645.SpringDamperCompoundDynamicAnalysis)

    @property
    def spring_damper_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6647.SpringDamperHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6647,
        )

        return self.__parent__._cast(_6647.SpringDamperHalfCompoundDynamicAnalysis)

    @property
    def straight_bevel_diff_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6648.StraightBevelDiffGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6648,
        )

        return self.__parent__._cast(_6648.StraightBevelDiffGearCompoundDynamicAnalysis)

    @property
    def straight_bevel_diff_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6650.StraightBevelDiffGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6650,
        )

        return self.__parent__._cast(
            _6650.StraightBevelDiffGearSetCompoundDynamicAnalysis
        )

    @property
    def straight_bevel_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6651.StraightBevelGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6651,
        )

        return self.__parent__._cast(_6651.StraightBevelGearCompoundDynamicAnalysis)

    @property
    def straight_bevel_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6653.StraightBevelGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6653,
        )

        return self.__parent__._cast(_6653.StraightBevelGearSetCompoundDynamicAnalysis)

    @property
    def straight_bevel_planet_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6654.StraightBevelPlanetGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6654,
        )

        return self.__parent__._cast(
            _6654.StraightBevelPlanetGearCompoundDynamicAnalysis
        )

    @property
    def straight_bevel_sun_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6655.StraightBevelSunGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6655,
        )

        return self.__parent__._cast(_6655.StraightBevelSunGearCompoundDynamicAnalysis)

    @property
    def synchroniser_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6656.SynchroniserCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6656,
        )

        return self.__parent__._cast(_6656.SynchroniserCompoundDynamicAnalysis)

    @property
    def synchroniser_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6657.SynchroniserHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6657,
        )

        return self.__parent__._cast(_6657.SynchroniserHalfCompoundDynamicAnalysis)

    @property
    def synchroniser_part_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6658.SynchroniserPartCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6658,
        )

        return self.__parent__._cast(_6658.SynchroniserPartCompoundDynamicAnalysis)

    @property
    def synchroniser_sleeve_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6659.SynchroniserSleeveCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6659,
        )

        return self.__parent__._cast(_6659.SynchroniserSleeveCompoundDynamicAnalysis)

    @property
    def torque_converter_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6660.TorqueConverterCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6660,
        )

        return self.__parent__._cast(_6660.TorqueConverterCompoundDynamicAnalysis)

    @property
    def torque_converter_pump_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6662.TorqueConverterPumpCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6662,
        )

        return self.__parent__._cast(_6662.TorqueConverterPumpCompoundDynamicAnalysis)

    @property
    def torque_converter_turbine_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6663.TorqueConverterTurbineCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6663,
        )

        return self.__parent__._cast(
            _6663.TorqueConverterTurbineCompoundDynamicAnalysis
        )

    @property
    def unbalanced_mass_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6664.UnbalancedMassCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6664,
        )

        return self.__parent__._cast(_6664.UnbalancedMassCompoundDynamicAnalysis)

    @property
    def virtual_component_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6665.VirtualComponentCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6665,
        )

        return self.__parent__._cast(_6665.VirtualComponentCompoundDynamicAnalysis)

    @property
    def worm_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6666.WormGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6666,
        )

        return self.__parent__._cast(_6666.WormGearCompoundDynamicAnalysis)

    @property
    def worm_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6668.WormGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6668,
        )

        return self.__parent__._cast(_6668.WormGearSetCompoundDynamicAnalysis)

    @property
    def zerol_bevel_gear_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6669.ZerolBevelGearCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6669,
        )

        return self.__parent__._cast(_6669.ZerolBevelGearCompoundDynamicAnalysis)

    @property
    def zerol_bevel_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6671.ZerolBevelGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6671,
        )

        return self.__parent__._cast(_6671.ZerolBevelGearSetCompoundDynamicAnalysis)

    @property
    def abstract_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6812.AbstractAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6812,
        )

        return self.__parent__._cast(
            _6812.AbstractAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def abstract_shaft_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6813.AbstractShaftCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6813,
        )

        return self.__parent__._cast(_6813.AbstractShaftCompoundCriticalSpeedAnalysis)

    @property
    def abstract_shaft_or_housing_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6814.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6814,
        )

        return self.__parent__._cast(
            _6814.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
        )

    @property
    def agma_gleason_conical_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6816.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6816,
        )

        return self.__parent__._cast(
            _6816.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
        )

    @property
    def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6818.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6818,
        )

        return self.__parent__._cast(
            _6818.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6819.AssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6819,
        )

        return self.__parent__._cast(_6819.AssemblyCompoundCriticalSpeedAnalysis)

    @property
    def bearing_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6820.BearingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6820,
        )

        return self.__parent__._cast(_6820.BearingCompoundCriticalSpeedAnalysis)

    @property
    def belt_drive_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6822.BeltDriveCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6822,
        )

        return self.__parent__._cast(_6822.BeltDriveCompoundCriticalSpeedAnalysis)

    @property
    def bevel_differential_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6823.BevelDifferentialGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6823,
        )

        return self.__parent__._cast(
            _6823.BevelDifferentialGearCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_differential_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6825.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6825,
        )

        return self.__parent__._cast(
            _6825.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_differential_planet_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6826.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6826,
        )

        return self.__parent__._cast(
            _6826.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6827.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6827,
        )

        return self.__parent__._cast(
            _6827.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6828.BevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6828,
        )

        return self.__parent__._cast(_6828.BevelGearCompoundCriticalSpeedAnalysis)

    @property
    def bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6830.BevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6830,
        )

        return self.__parent__._cast(_6830.BevelGearSetCompoundCriticalSpeedAnalysis)

    @property
    def bolt_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6831.BoltCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6831,
        )

        return self.__parent__._cast(_6831.BoltCompoundCriticalSpeedAnalysis)

    @property
    def bolted_joint_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6832.BoltedJointCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6832,
        )

        return self.__parent__._cast(_6832.BoltedJointCompoundCriticalSpeedAnalysis)

    @property
    def clutch_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6833.ClutchCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6833,
        )

        return self.__parent__._cast(_6833.ClutchCompoundCriticalSpeedAnalysis)

    @property
    def clutch_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6835.ClutchHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6835,
        )

        return self.__parent__._cast(_6835.ClutchHalfCompoundCriticalSpeedAnalysis)

    @property
    def component_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6837.ComponentCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6837,
        )

        return self.__parent__._cast(_6837.ComponentCompoundCriticalSpeedAnalysis)

    @property
    def concept_coupling_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6838.ConceptCouplingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6838,
        )

        return self.__parent__._cast(_6838.ConceptCouplingCompoundCriticalSpeedAnalysis)

    @property
    def concept_coupling_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6840.ConceptCouplingHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6840,
        )

        return self.__parent__._cast(
            _6840.ConceptCouplingHalfCompoundCriticalSpeedAnalysis
        )

    @property
    def concept_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6841.ConceptGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6841,
        )

        return self.__parent__._cast(_6841.ConceptGearCompoundCriticalSpeedAnalysis)

    @property
    def concept_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6843.ConceptGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6843,
        )

        return self.__parent__._cast(_6843.ConceptGearSetCompoundCriticalSpeedAnalysis)

    @property
    def conical_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6844.ConicalGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6844,
        )

        return self.__parent__._cast(_6844.ConicalGearCompoundCriticalSpeedAnalysis)

    @property
    def conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6846.ConicalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6846,
        )

        return self.__parent__._cast(_6846.ConicalGearSetCompoundCriticalSpeedAnalysis)

    @property
    def connector_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6848.ConnectorCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6848,
        )

        return self.__parent__._cast(_6848.ConnectorCompoundCriticalSpeedAnalysis)

    @property
    def coupling_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6849.CouplingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6849,
        )

        return self.__parent__._cast(_6849.CouplingCompoundCriticalSpeedAnalysis)

    @property
    def coupling_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6851.CouplingHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6851,
        )

        return self.__parent__._cast(_6851.CouplingHalfCompoundCriticalSpeedAnalysis)

    @property
    def cvt_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6853.CVTCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6853,
        )

        return self.__parent__._cast(_6853.CVTCompoundCriticalSpeedAnalysis)

    @property
    def cvt_pulley_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6854.CVTPulleyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6854,
        )

        return self.__parent__._cast(_6854.CVTPulleyCompoundCriticalSpeedAnalysis)

    @property
    def cycloidal_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6855.CycloidalAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6855,
        )

        return self.__parent__._cast(
            _6855.CycloidalAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def cycloidal_disc_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6857.CycloidalDiscCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6857,
        )

        return self.__parent__._cast(_6857.CycloidalDiscCompoundCriticalSpeedAnalysis)

    @property
    def cylindrical_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6859.CylindricalGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6859,
        )

        return self.__parent__._cast(_6859.CylindricalGearCompoundCriticalSpeedAnalysis)

    @property
    def cylindrical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6861.CylindricalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6861,
        )

        return self.__parent__._cast(
            _6861.CylindricalGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def cylindrical_planet_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6862.CylindricalPlanetGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6862,
        )

        return self.__parent__._cast(
            _6862.CylindricalPlanetGearCompoundCriticalSpeedAnalysis
        )

    @property
    def datum_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6863.DatumCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6863,
        )

        return self.__parent__._cast(_6863.DatumCompoundCriticalSpeedAnalysis)

    @property
    def external_cad_model_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6864.ExternalCADModelCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6864,
        )

        return self.__parent__._cast(
            _6864.ExternalCADModelCompoundCriticalSpeedAnalysis
        )

    @property
    def face_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6865.FaceGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6865,
        )

        return self.__parent__._cast(_6865.FaceGearCompoundCriticalSpeedAnalysis)

    @property
    def face_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6867.FaceGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6867,
        )

        return self.__parent__._cast(_6867.FaceGearSetCompoundCriticalSpeedAnalysis)

    @property
    def fe_part_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6868.FEPartCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6868,
        )

        return self.__parent__._cast(_6868.FEPartCompoundCriticalSpeedAnalysis)

    @property
    def flexible_pin_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6869.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6869,
        )

        return self.__parent__._cast(
            _6869.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6870.GearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6870,
        )

        return self.__parent__._cast(_6870.GearCompoundCriticalSpeedAnalysis)

    @property
    def gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6872.GearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6872,
        )

        return self.__parent__._cast(_6872.GearSetCompoundCriticalSpeedAnalysis)

    @property
    def guide_dxf_model_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6873.GuideDxfModelCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6873,
        )

        return self.__parent__._cast(_6873.GuideDxfModelCompoundCriticalSpeedAnalysis)

    @property
    def hypoid_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6874.HypoidGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6874,
        )

        return self.__parent__._cast(_6874.HypoidGearCompoundCriticalSpeedAnalysis)

    @property
    def hypoid_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6876.HypoidGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6876,
        )

        return self.__parent__._cast(_6876.HypoidGearSetCompoundCriticalSpeedAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6878.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6878,
        )

        return self.__parent__._cast(
            _6878.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6880.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6880,
        )

        return self.__parent__._cast(
            _6880.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6881.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6881,
        )

        return self.__parent__._cast(
            _6881.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6883.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6883,
        )

        return self.__parent__._cast(
            _6883.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6884.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6884,
        )

        return self.__parent__._cast(
            _6884.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> (
        "_6886.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis"
    ):
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6886,
        )

        return self.__parent__._cast(
            _6886.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def mass_disc_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6887.MassDiscCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6887,
        )

        return self.__parent__._cast(_6887.MassDiscCompoundCriticalSpeedAnalysis)

    @property
    def measurement_component_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6888.MeasurementComponentCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6888,
        )

        return self.__parent__._cast(
            _6888.MeasurementComponentCompoundCriticalSpeedAnalysis
        )

    @property
    def microphone_array_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6889.MicrophoneArrayCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6889,
        )

        return self.__parent__._cast(_6889.MicrophoneArrayCompoundCriticalSpeedAnalysis)

    @property
    def microphone_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6890.MicrophoneCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6890,
        )

        return self.__parent__._cast(_6890.MicrophoneCompoundCriticalSpeedAnalysis)

    @property
    def mountable_component_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6891.MountableComponentCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6891,
        )

        return self.__parent__._cast(
            _6891.MountableComponentCompoundCriticalSpeedAnalysis
        )

    @property
    def oil_seal_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6892.OilSealCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6892,
        )

        return self.__parent__._cast(_6892.OilSealCompoundCriticalSpeedAnalysis)

    @property
    def part_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6893.PartCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6893,
        )

        return self.__parent__._cast(_6893.PartCompoundCriticalSpeedAnalysis)

    @property
    def part_to_part_shear_coupling_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6894.PartToPartShearCouplingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6894,
        )

        return self.__parent__._cast(
            _6894.PartToPartShearCouplingCompoundCriticalSpeedAnalysis
        )

    @property
    def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6896.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6896,
        )

        return self.__parent__._cast(
            _6896.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
        )

    @property
    def planetary_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6898.PlanetaryGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6898,
        )

        return self.__parent__._cast(
            _6898.PlanetaryGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def planet_carrier_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6899.PlanetCarrierCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6899,
        )

        return self.__parent__._cast(_6899.PlanetCarrierCompoundCriticalSpeedAnalysis)

    @property
    def point_load_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6900.PointLoadCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6900,
        )

        return self.__parent__._cast(_6900.PointLoadCompoundCriticalSpeedAnalysis)

    @property
    def power_load_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6901.PowerLoadCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6901,
        )

        return self.__parent__._cast(_6901.PowerLoadCompoundCriticalSpeedAnalysis)

    @property
    def pulley_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6902.PulleyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6902,
        )

        return self.__parent__._cast(_6902.PulleyCompoundCriticalSpeedAnalysis)

    @property
    def ring_pins_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6903.RingPinsCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6903,
        )

        return self.__parent__._cast(_6903.RingPinsCompoundCriticalSpeedAnalysis)

    @property
    def rolling_ring_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6905.RollingRingAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6905,
        )

        return self.__parent__._cast(
            _6905.RollingRingAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def rolling_ring_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6906.RollingRingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6906,
        )

        return self.__parent__._cast(_6906.RollingRingCompoundCriticalSpeedAnalysis)

    @property
    def root_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6908.RootAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6908,
        )

        return self.__parent__._cast(_6908.RootAssemblyCompoundCriticalSpeedAnalysis)

    @property
    def shaft_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6909.ShaftCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6909,
        )

        return self.__parent__._cast(_6909.ShaftCompoundCriticalSpeedAnalysis)

    @property
    def shaft_hub_connection_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6910.ShaftHubConnectionCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6910,
        )

        return self.__parent__._cast(
            _6910.ShaftHubConnectionCompoundCriticalSpeedAnalysis
        )

    @property
    def specialised_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6912.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6912,
        )

        return self.__parent__._cast(
            _6912.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def spiral_bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6913.SpiralBevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6913,
        )

        return self.__parent__._cast(_6913.SpiralBevelGearCompoundCriticalSpeedAnalysis)

    @property
    def spiral_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6915.SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6915,
        )

        return self.__parent__._cast(
            _6915.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def spring_damper_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6916.SpringDamperCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6916,
        )

        return self.__parent__._cast(_6916.SpringDamperCompoundCriticalSpeedAnalysis)

    @property
    def spring_damper_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6918.SpringDamperHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6918,
        )

        return self.__parent__._cast(
            _6918.SpringDamperHalfCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_diff_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6919.StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6919,
        )

        return self.__parent__._cast(
            _6919.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6921.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6921,
        )

        return self.__parent__._cast(
            _6921.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6922.StraightBevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6922,
        )

        return self.__parent__._cast(
            _6922.StraightBevelGearCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6924.StraightBevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6924,
        )

        return self.__parent__._cast(
            _6924.StraightBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_planet_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6925.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6925,
        )

        return self.__parent__._cast(
            _6925.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_sun_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6926.StraightBevelSunGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6926,
        )

        return self.__parent__._cast(
            _6926.StraightBevelSunGearCompoundCriticalSpeedAnalysis
        )

    @property
    def synchroniser_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6927.SynchroniserCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6927,
        )

        return self.__parent__._cast(_6927.SynchroniserCompoundCriticalSpeedAnalysis)

    @property
    def synchroniser_half_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6928.SynchroniserHalfCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6928,
        )

        return self.__parent__._cast(
            _6928.SynchroniserHalfCompoundCriticalSpeedAnalysis
        )

    @property
    def synchroniser_part_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6929.SynchroniserPartCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6929,
        )

        return self.__parent__._cast(
            _6929.SynchroniserPartCompoundCriticalSpeedAnalysis
        )

    @property
    def synchroniser_sleeve_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6930.SynchroniserSleeveCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6930,
        )

        return self.__parent__._cast(
            _6930.SynchroniserSleeveCompoundCriticalSpeedAnalysis
        )

    @property
    def torque_converter_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6931.TorqueConverterCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6931,
        )

        return self.__parent__._cast(_6931.TorqueConverterCompoundCriticalSpeedAnalysis)

    @property
    def torque_converter_pump_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6933.TorqueConverterPumpCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6933,
        )

        return self.__parent__._cast(
            _6933.TorqueConverterPumpCompoundCriticalSpeedAnalysis
        )

    @property
    def torque_converter_turbine_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6934.TorqueConverterTurbineCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6934,
        )

        return self.__parent__._cast(
            _6934.TorqueConverterTurbineCompoundCriticalSpeedAnalysis
        )

    @property
    def unbalanced_mass_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6935.UnbalancedMassCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6935,
        )

        return self.__parent__._cast(_6935.UnbalancedMassCompoundCriticalSpeedAnalysis)

    @property
    def virtual_component_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6936.VirtualComponentCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6936,
        )

        return self.__parent__._cast(
            _6936.VirtualComponentCompoundCriticalSpeedAnalysis
        )

    @property
    def worm_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6937.WormGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6937,
        )

        return self.__parent__._cast(_6937.WormGearCompoundCriticalSpeedAnalysis)

    @property
    def worm_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6939.WormGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6939,
        )

        return self.__parent__._cast(_6939.WormGearSetCompoundCriticalSpeedAnalysis)

    @property
    def zerol_bevel_gear_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6940.ZerolBevelGearCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6940,
        )

        return self.__parent__._cast(_6940.ZerolBevelGearCompoundCriticalSpeedAnalysis)

    @property
    def zerol_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6942.ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6942,
        )

        return self.__parent__._cast(
            _6942.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7080.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7080,
        )

        return self.__parent__._cast(
            _7080.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def abstract_shaft_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7081.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7081,
        )

        return self.__parent__._cast(
            _7081.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def abstract_shaft_or_housing_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> (
        "_7082.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7082,
        )

        return self.__parent__._cast(
            _7082.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> (
        "_7084.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7084,
        )

        return self.__parent__._cast(
            _7084.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7086.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7086,
        )

        return self.__parent__._cast(
            _7086.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def assembly_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7087.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7087,
        )

        return self.__parent__._cast(
            _7087.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bearing_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7088.BearingCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7088,
        )

        return self.__parent__._cast(
            _7088.BearingCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def belt_drive_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7090.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7090,
        )

        return self.__parent__._cast(
            _7090.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7091.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7091,
        )

        return self.__parent__._cast(
            _7091.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7093.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7093,
        )

        return self.__parent__._cast(
            _7093.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7094.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7094,
        )

        return self.__parent__._cast(
            _7094.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7095.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7095,
        )

        return self.__parent__._cast(
            _7095.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7096.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7096,
        )

        return self.__parent__._cast(
            _7096.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7098.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7098,
        )

        return self.__parent__._cast(
            _7098.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bolt_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7099.BoltCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7099,
        )

        return self.__parent__._cast(
            _7099.BoltCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bolted_joint_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7100.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7100,
        )

        return self.__parent__._cast(
            _7100.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def clutch_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7101.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7101,
        )

        return self.__parent__._cast(
            _7101.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def clutch_half_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7103.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7103,
        )

        return self.__parent__._cast(
            _7103.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def component_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7105.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7105,
        )

        return self.__parent__._cast(
            _7105.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def concept_coupling_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7106.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7106,
        )

        return self.__parent__._cast(
            _7106.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def concept_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7108.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7108,
        )

        return self.__parent__._cast(
            _7108.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def concept_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7109.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7109,
        )

        return self.__parent__._cast(
            _7109.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def concept_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7111.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7111,
        )

        return self.__parent__._cast(
            _7111.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7112.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7112,
        )

        return self.__parent__._cast(
            _7112.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7114.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7114,
        )

        return self.__parent__._cast(
            _7114.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def connector_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7116.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7116,
        )

        return self.__parent__._cast(
            _7116.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def coupling_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7117.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7117,
        )

        return self.__parent__._cast(
            _7117.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7119.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7119,
        )

        return self.__parent__._cast(
            _7119.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cvt_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7121.CVTCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7121,
        )

        return self.__parent__._cast(
            _7121.CVTCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7122.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7122,
        )

        return self.__parent__._cast(
            _7122.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cycloidal_assembly_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7123.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7123,
        )

        return self.__parent__._cast(
            _7123.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cycloidal_disc_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7125.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7125,
        )

        return self.__parent__._cast(
            _7125.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cylindrical_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7127.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7127,
        )

        return self.__parent__._cast(
            _7127.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cylindrical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7129.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7129,
        )

        return self.__parent__._cast(
            _7129.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cylindrical_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7130.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7130,
        )

        return self.__parent__._cast(
            _7130.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def datum_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7131.DatumCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7131,
        )

        return self.__parent__._cast(
            _7131.DatumCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def external_cad_model_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7132.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7132,
        )

        return self.__parent__._cast(
            _7132.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def face_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7133.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7133,
        )

        return self.__parent__._cast(
            _7133.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def face_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7135.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7135,
        )

        return self.__parent__._cast(
            _7135.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def fe_part_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7136.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7136,
        )

        return self.__parent__._cast(
            _7136.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def flexible_pin_assembly_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7137.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7137,
        )

        return self.__parent__._cast(
            _7137.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7138.GearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7138,
        )

        return self.__parent__._cast(
            _7138.GearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7140.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7140,
        )

        return self.__parent__._cast(
            _7140.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def guide_dxf_model_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7141.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7141,
        )

        return self.__parent__._cast(
            _7141.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7142.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7142,
        )

        return self.__parent__._cast(
            _7142.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7144.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7144,
        )

        return self.__parent__._cast(
            _7144.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7146.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7146,
        )

        return self.__parent__._cast(
            _7146.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7148.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7148,
        )

        return self.__parent__._cast(
            _7148.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7149.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7149,
        )

        return self.__parent__._cast(
            _7149.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7151.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7151,
        )

        return self.__parent__._cast(
            _7151.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7152.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7152,
        )

        return self.__parent__._cast(
            _7152.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7154.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7154,
        )

        return self.__parent__._cast(
            _7154.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def mass_disc_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7155.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7155,
        )

        return self.__parent__._cast(
            _7155.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def measurement_component_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7156.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7156,
        )

        return self.__parent__._cast(
            _7156.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def microphone_array_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7157.MicrophoneArrayCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7157,
        )

        return self.__parent__._cast(
            _7157.MicrophoneArrayCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def microphone_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7158.MicrophoneCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7158,
        )

        return self.__parent__._cast(
            _7158.MicrophoneCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7159.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7159,
        )

        return self.__parent__._cast(
            _7159.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def oil_seal_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7160.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7160,
        )

        return self.__parent__._cast(
            _7160.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def part_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7161.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7161,
        )

        return self.__parent__._cast(
            _7161.PartCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def part_to_part_shear_coupling_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> (
        "_7162.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7162,
        )

        return self.__parent__._cast(
            _7162.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def part_to_part_shear_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7164.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7164,
        )

        return self.__parent__._cast(
            _7164.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def planetary_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7166.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7166,
        )

        return self.__parent__._cast(
            _7166.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def planet_carrier_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7167.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7167,
        )

        return self.__parent__._cast(
            _7167.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def point_load_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7168.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7168,
        )

        return self.__parent__._cast(
            _7168.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def power_load_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7169.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7169,
        )

        return self.__parent__._cast(
            _7169.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def pulley_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7170.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7170,
        )

        return self.__parent__._cast(
            _7170.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def ring_pins_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7171.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7171,
        )

        return self.__parent__._cast(
            _7171.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def rolling_ring_assembly_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7173.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7173,
        )

        return self.__parent__._cast(
            _7173.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def rolling_ring_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7174.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7174,
        )

        return self.__parent__._cast(
            _7174.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def root_assembly_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7176.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7176,
        )

        return self.__parent__._cast(
            _7176.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def shaft_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7177.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7177,
        )

        return self.__parent__._cast(
            _7177.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def shaft_hub_connection_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7178.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7178,
        )

        return self.__parent__._cast(
            _7178.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7180.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7180,
        )

        return self.__parent__._cast(
            _7180.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7181.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7181,
        )

        return self.__parent__._cast(
            _7181.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7183.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7183,
        )

        return self.__parent__._cast(
            _7183.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def spring_damper_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7184.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7184,
        )

        return self.__parent__._cast(
            _7184.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def spring_damper_half_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7186.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7186,
        )

        return self.__parent__._cast(
            _7186.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7187.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7187,
        )

        return self.__parent__._cast(
            _7187.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7189.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7189,
        )

        return self.__parent__._cast(
            _7189.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7190.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7190,
        )

        return self.__parent__._cast(
            _7190.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7192.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7192,
        )

        return self.__parent__._cast(
            _7192.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> (
        "_7193.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7193,
        )

        return self.__parent__._cast(
            _7193.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7194.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7194,
        )

        return self.__parent__._cast(
            _7194.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def synchroniser_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7195.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7195,
        )

        return self.__parent__._cast(
            _7195.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def synchroniser_half_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7196.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7196,
        )

        return self.__parent__._cast(
            _7196.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7197.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7197,
        )

        return self.__parent__._cast(
            _7197.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7198.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7198,
        )

        return self.__parent__._cast(
            _7198.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def torque_converter_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7199.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7199,
        )

        return self.__parent__._cast(
            _7199.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def torque_converter_pump_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7201.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7201,
        )

        return self.__parent__._cast(
            _7201.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def torque_converter_turbine_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> (
        "_7202.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7202,
        )

        return self.__parent__._cast(
            _7202.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def unbalanced_mass_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7203.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7203,
        )

        return self.__parent__._cast(
            _7203.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def virtual_component_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7204.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7204,
        )

        return self.__parent__._cast(
            _7204.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def worm_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7205.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7205,
        )

        return self.__parent__._cast(
            _7205.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def worm_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7207.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7207,
        )

        return self.__parent__._cast(
            _7207.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7208.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7208,
        )

        return self.__parent__._cast(
            _7208.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7210.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7210,
        )

        return self.__parent__._cast(
            _7210.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def abstract_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7349.AbstractAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7349,
        )

        return self.__parent__._cast(
            _7349.AbstractAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def abstract_shaft_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7350.AbstractShaftCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7350,
        )

        return self.__parent__._cast(
            _7350.AbstractShaftCompoundAdvancedSystemDeflection
        )

    @property
    def abstract_shaft_or_housing_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7351.AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7351,
        )

        return self.__parent__._cast(
            _7351.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7353.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7353,
        )

        return self.__parent__._cast(
            _7353.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7355.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7355,
        )

        return self.__parent__._cast(
            _7355.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7356.AssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7356,
        )

        return self.__parent__._cast(_7356.AssemblyCompoundAdvancedSystemDeflection)

    @property
    def bearing_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7357.BearingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7357,
        )

        return self.__parent__._cast(_7357.BearingCompoundAdvancedSystemDeflection)

    @property
    def belt_drive_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7359.BeltDriveCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7359,
        )

        return self.__parent__._cast(_7359.BeltDriveCompoundAdvancedSystemDeflection)

    @property
    def bevel_differential_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7360.BevelDifferentialGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7360,
        )

        return self.__parent__._cast(
            _7360.BevelDifferentialGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7362.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7362,
        )

        return self.__parent__._cast(
            _7362.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7363.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7363,
        )

        return self.__parent__._cast(
            _7363.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_sun_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7364.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7364,
        )

        return self.__parent__._cast(
            _7364.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7365.BevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7365,
        )

        return self.__parent__._cast(_7365.BevelGearCompoundAdvancedSystemDeflection)

    @property
    def bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7367.BevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7367,
        )

        return self.__parent__._cast(_7367.BevelGearSetCompoundAdvancedSystemDeflection)

    @property
    def bolt_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7368.BoltCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7368,
        )

        return self.__parent__._cast(_7368.BoltCompoundAdvancedSystemDeflection)

    @property
    def bolted_joint_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7369.BoltedJointCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7369,
        )

        return self.__parent__._cast(_7369.BoltedJointCompoundAdvancedSystemDeflection)

    @property
    def clutch_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7370.ClutchCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7370,
        )

        return self.__parent__._cast(_7370.ClutchCompoundAdvancedSystemDeflection)

    @property
    def clutch_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7372.ClutchHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7372,
        )

        return self.__parent__._cast(_7372.ClutchHalfCompoundAdvancedSystemDeflection)

    @property
    def component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7374.ComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7374,
        )

        return self.__parent__._cast(_7374.ComponentCompoundAdvancedSystemDeflection)

    @property
    def concept_coupling_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7375.ConceptCouplingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7375,
        )

        return self.__parent__._cast(
            _7375.ConceptCouplingCompoundAdvancedSystemDeflection
        )

    @property
    def concept_coupling_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7377.ConceptCouplingHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7377,
        )

        return self.__parent__._cast(
            _7377.ConceptCouplingHalfCompoundAdvancedSystemDeflection
        )

    @property
    def concept_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7378.ConceptGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7378,
        )

        return self.__parent__._cast(_7378.ConceptGearCompoundAdvancedSystemDeflection)

    @property
    def concept_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7380.ConceptGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7380,
        )

        return self.__parent__._cast(
            _7380.ConceptGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def conical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7381.ConicalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7381,
        )

        return self.__parent__._cast(_7381.ConicalGearCompoundAdvancedSystemDeflection)

    @property
    def conical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7383.ConicalGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7383,
        )

        return self.__parent__._cast(
            _7383.ConicalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def connector_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7385.ConnectorCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7385,
        )

        return self.__parent__._cast(_7385.ConnectorCompoundAdvancedSystemDeflection)

    @property
    def coupling_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7386.CouplingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7386,
        )

        return self.__parent__._cast(_7386.CouplingCompoundAdvancedSystemDeflection)

    @property
    def coupling_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7388.CouplingHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7388,
        )

        return self.__parent__._cast(_7388.CouplingHalfCompoundAdvancedSystemDeflection)

    @property
    def cvt_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7390.CVTCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7390,
        )

        return self.__parent__._cast(_7390.CVTCompoundAdvancedSystemDeflection)

    @property
    def cvt_pulley_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7391.CVTPulleyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7391,
        )

        return self.__parent__._cast(_7391.CVTPulleyCompoundAdvancedSystemDeflection)

    @property
    def cycloidal_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7392.CycloidalAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7392,
        )

        return self.__parent__._cast(
            _7392.CycloidalAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def cycloidal_disc_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7394.CycloidalDiscCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7394,
        )

        return self.__parent__._cast(
            _7394.CycloidalDiscCompoundAdvancedSystemDeflection
        )

    @property
    def cylindrical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7396.CylindricalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7396,
        )

        return self.__parent__._cast(
            _7396.CylindricalGearCompoundAdvancedSystemDeflection
        )

    @property
    def cylindrical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7398.CylindricalGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7398,
        )

        return self.__parent__._cast(
            _7398.CylindricalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def cylindrical_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7399.CylindricalPlanetGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7399,
        )

        return self.__parent__._cast(
            _7399.CylindricalPlanetGearCompoundAdvancedSystemDeflection
        )

    @property
    def datum_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7400.DatumCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7400,
        )

        return self.__parent__._cast(_7400.DatumCompoundAdvancedSystemDeflection)

    @property
    def external_cad_model_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7401.ExternalCADModelCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7401,
        )

        return self.__parent__._cast(
            _7401.ExternalCADModelCompoundAdvancedSystemDeflection
        )

    @property
    def face_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7402.FaceGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7402,
        )

        return self.__parent__._cast(_7402.FaceGearCompoundAdvancedSystemDeflection)

    @property
    def face_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7404.FaceGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7404,
        )

        return self.__parent__._cast(_7404.FaceGearSetCompoundAdvancedSystemDeflection)

    @property
    def fe_part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7405.FEPartCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7405,
        )

        return self.__parent__._cast(_7405.FEPartCompoundAdvancedSystemDeflection)

    @property
    def flexible_pin_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7406.FlexiblePinAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7406,
        )

        return self.__parent__._cast(
            _7406.FlexiblePinAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7407.GearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7407,
        )

        return self.__parent__._cast(_7407.GearCompoundAdvancedSystemDeflection)

    @property
    def gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7409.GearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7409,
        )

        return self.__parent__._cast(_7409.GearSetCompoundAdvancedSystemDeflection)

    @property
    def guide_dxf_model_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7410.GuideDxfModelCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7410,
        )

        return self.__parent__._cast(
            _7410.GuideDxfModelCompoundAdvancedSystemDeflection
        )

    @property
    def hypoid_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7411.HypoidGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7411,
        )

        return self.__parent__._cast(_7411.HypoidGearCompoundAdvancedSystemDeflection)

    @property
    def hypoid_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7413.HypoidGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7413,
        )

        return self.__parent__._cast(
            _7413.HypoidGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7415.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7415,
        )

        return self.__parent__._cast(
            _7415.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7417.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7417,
        )

        return self.__parent__._cast(
            _7417.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7418.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7418,
        )

        return self.__parent__._cast(
            _7418.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7420.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7420,
        )

        return self.__parent__._cast(
            _7420.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> (
        "_7421.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7421,
        )

        return self.__parent__._cast(
            _7421.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7423.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7423,
        )

        return self.__parent__._cast(
            _7423.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def mass_disc_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7424.MassDiscCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7424,
        )

        return self.__parent__._cast(_7424.MassDiscCompoundAdvancedSystemDeflection)

    @property
    def measurement_component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7425.MeasurementComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7425,
        )

        return self.__parent__._cast(
            _7425.MeasurementComponentCompoundAdvancedSystemDeflection
        )

    @property
    def microphone_array_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7426.MicrophoneArrayCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7426,
        )

        return self.__parent__._cast(
            _7426.MicrophoneArrayCompoundAdvancedSystemDeflection
        )

    @property
    def microphone_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7427.MicrophoneCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7427,
        )

        return self.__parent__._cast(_7427.MicrophoneCompoundAdvancedSystemDeflection)

    @property
    def mountable_component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7428.MountableComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7428,
        )

        return self.__parent__._cast(
            _7428.MountableComponentCompoundAdvancedSystemDeflection
        )

    @property
    def oil_seal_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7429.OilSealCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7429,
        )

        return self.__parent__._cast(_7429.OilSealCompoundAdvancedSystemDeflection)

    @property
    def part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7430.PartCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7430,
        )

        return self.__parent__._cast(_7430.PartCompoundAdvancedSystemDeflection)

    @property
    def part_to_part_shear_coupling_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7431.PartToPartShearCouplingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7431,
        )

        return self.__parent__._cast(
            _7431.PartToPartShearCouplingCompoundAdvancedSystemDeflection
        )

    @property
    def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7433.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7433,
        )

        return self.__parent__._cast(
            _7433.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
        )

    @property
    def planetary_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7435.PlanetaryGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7435,
        )

        return self.__parent__._cast(
            _7435.PlanetaryGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def planet_carrier_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7436.PlanetCarrierCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7436,
        )

        return self.__parent__._cast(
            _7436.PlanetCarrierCompoundAdvancedSystemDeflection
        )

    @property
    def point_load_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7437.PointLoadCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7437,
        )

        return self.__parent__._cast(_7437.PointLoadCompoundAdvancedSystemDeflection)

    @property
    def power_load_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7438.PowerLoadCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7438,
        )

        return self.__parent__._cast(_7438.PowerLoadCompoundAdvancedSystemDeflection)

    @property
    def pulley_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7439.PulleyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7439,
        )

        return self.__parent__._cast(_7439.PulleyCompoundAdvancedSystemDeflection)

    @property
    def ring_pins_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7440.RingPinsCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7440,
        )

        return self.__parent__._cast(_7440.RingPinsCompoundAdvancedSystemDeflection)

    @property
    def rolling_ring_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7442.RollingRingAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7442,
        )

        return self.__parent__._cast(
            _7442.RollingRingAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def rolling_ring_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7443.RollingRingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7443,
        )

        return self.__parent__._cast(_7443.RollingRingCompoundAdvancedSystemDeflection)

    @property
    def root_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7445.RootAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7445,
        )

        return self.__parent__._cast(_7445.RootAssemblyCompoundAdvancedSystemDeflection)

    @property
    def shaft_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7446.ShaftCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7446,
        )

        return self.__parent__._cast(_7446.ShaftCompoundAdvancedSystemDeflection)

    @property
    def shaft_hub_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7447.ShaftHubConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7447,
        )

        return self.__parent__._cast(
            _7447.ShaftHubConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def specialised_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7449.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7449,
        )

        return self.__parent__._cast(
            _7449.SpecialisedAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def spiral_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7450.SpiralBevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7450,
        )

        return self.__parent__._cast(
            _7450.SpiralBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def spiral_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7452.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7452,
        )

        return self.__parent__._cast(
            _7452.SpiralBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def spring_damper_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7453.SpringDamperCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7453,
        )

        return self.__parent__._cast(_7453.SpringDamperCompoundAdvancedSystemDeflection)

    @property
    def spring_damper_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7455.SpringDamperHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7455,
        )

        return self.__parent__._cast(
            _7455.SpringDamperHalfCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_diff_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7456.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7456,
        )

        return self.__parent__._cast(
            _7456.StraightBevelDiffGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7458.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7458,
        )

        return self.__parent__._cast(
            _7458.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7459.StraightBevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7459,
        )

        return self.__parent__._cast(
            _7459.StraightBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7461.StraightBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7461,
        )

        return self.__parent__._cast(
            _7461.StraightBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7462.StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7462,
        )

        return self.__parent__._cast(
            _7462.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_sun_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7463.StraightBevelSunGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7463,
        )

        return self.__parent__._cast(
            _7463.StraightBevelSunGearCompoundAdvancedSystemDeflection
        )

    @property
    def synchroniser_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7464.SynchroniserCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7464,
        )

        return self.__parent__._cast(_7464.SynchroniserCompoundAdvancedSystemDeflection)

    @property
    def synchroniser_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7465.SynchroniserHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7465,
        )

        return self.__parent__._cast(
            _7465.SynchroniserHalfCompoundAdvancedSystemDeflection
        )

    @property
    def synchroniser_part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7466.SynchroniserPartCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7466,
        )

        return self.__parent__._cast(
            _7466.SynchroniserPartCompoundAdvancedSystemDeflection
        )

    @property
    def synchroniser_sleeve_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7467.SynchroniserSleeveCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7467,
        )

        return self.__parent__._cast(
            _7467.SynchroniserSleeveCompoundAdvancedSystemDeflection
        )

    @property
    def torque_converter_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7468.TorqueConverterCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7468,
        )

        return self.__parent__._cast(
            _7468.TorqueConverterCompoundAdvancedSystemDeflection
        )

    @property
    def torque_converter_pump_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7470.TorqueConverterPumpCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7470,
        )

        return self.__parent__._cast(
            _7470.TorqueConverterPumpCompoundAdvancedSystemDeflection
        )

    @property
    def torque_converter_turbine_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7471.TorqueConverterTurbineCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7471,
        )

        return self.__parent__._cast(
            _7471.TorqueConverterTurbineCompoundAdvancedSystemDeflection
        )

    @property
    def unbalanced_mass_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7472.UnbalancedMassCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7472,
        )

        return self.__parent__._cast(
            _7472.UnbalancedMassCompoundAdvancedSystemDeflection
        )

    @property
    def virtual_component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7473.VirtualComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7473,
        )

        return self.__parent__._cast(
            _7473.VirtualComponentCompoundAdvancedSystemDeflection
        )

    @property
    def worm_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7474.WormGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7474,
        )

        return self.__parent__._cast(_7474.WormGearCompoundAdvancedSystemDeflection)

    @property
    def worm_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7476.WormGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7476,
        )

        return self.__parent__._cast(_7476.WormGearSetCompoundAdvancedSystemDeflection)

    @property
    def zerol_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7477.ZerolBevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7477,
        )

        return self.__parent__._cast(
            _7477.ZerolBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def zerol_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7479.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7479,
        )

        return self.__parent__._cast(
            _7479.ZerolBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def part_compound_analysis(self: "CastSelf") -> "PartCompoundAnalysis":
        return self.__parent__

    def __getattr__(self: "CastSelf", name: str) -> "Any":
        try:
            return self.__getattribute__(name)
        except AttributeError:
            class_name = utility.camel(name)
            raise CastException(
                f'Detected an invalid cast. Cannot cast to type "{class_name}"'
            ) from None


@extended_dataclass(frozen=True, slots=True, weakref_slot=True, eq=False)
class PartCompoundAnalysis(_7704.DesignEntityCompoundAnalysis):
    """PartCompoundAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_COMPOUND_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def two_d_drawing(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "TwoDDrawing")

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_PartCompoundAnalysis":
        """Cast to another type.

        Returns:
            _Cast_PartCompoundAnalysis
        """
        return _Cast_PartCompoundAnalysis(self)
