import torch
# Create the empty dictionary for storing data
data_store = {}

# Manually populate the dictionary with the keys and corresponding tensors
data_store[('NonHarmonicFourierActivation', 5, 'Identity')] = {'coefficients':torch.tensor(
                        [
                            [
                                [
                                    5.4164e00,
                                    -5.7772e-01,
                                    -4.0032e00,
                                    -5.4021e-03,
                                    -3.8050e-03,
                                    -5.2792e-01,
                                    -9.1534e-03,
                                    -7.0159e-03,
                                    -6.7936e-02,
                                    -1.7951e-01,
                                    -2.5187e-02,
                                ],
                                [
                                    -1.5605e-01,
                                    1.0163e01,
                                    1.6775e00,
                                    6.6595e-02,
                                    1.8576e-01,
                                    2.2065e-02,
                                    -2.1711e-03,
                                    2.0581e-03,
                                    -3.7545e-03,
                                    -2.1703e-03,
                                    6.7910e-04,
                                ],
                            ]
                        ]
                    ),'frequencies':torch.tensor(
                        [
                            [
                                [
                                    0.0051,
                                    0.0679,
                                    -0.0784,
                                    0.0347,
                                    -0.0646,
                                    -0.0910,
                                    -0.2753,
                                    0.2788,
                                    -0.1303,
                                    -0.0829,
                                    0.1319,
                                ],
                                [
                                    -0.0392,
                                    0.0714,
                                    -0.0765,
                                    -0.1355,
                                    0.0859,
                                    -0.0879,
                                    -0.1975,
                                    0.2282,
                                    -0.1254,
                                    -0.0807,
                                    0.1309,
                                ],
                            ]
                        ],
                    )} 
data_store[('NonHarmonicFourierActivation', 5, 'SiLU')] = {'coefficients':,'frequencies':} 
# Add more entries manually like the above...
