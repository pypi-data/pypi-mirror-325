# Fold Layer

The Fold Layer is a novel neural network layer designed to transform high-dimensional data with efficient learning and reduced complexity. Inspired by principles of geometric folding, this model employs a custom nonlinearity to reshape data through learned hyperplanes, allowing for non-linear transformations that improve prediction speed and convergence.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Research & Development](#research--development)
- [Contributing](#contributing)
- [License](#license)
- [Workflow](#workflow)

## Overview

The Fold Layer architecture introduces a data transformation process similar to folding in origami, where input data is sequentially mapped across high-dimensional hyperplanes. This process enables:
- A reduced need for large, high-parameter layers in standard architectures.
- Accelerated prediction through **hyperplane-based data folding**.
- Simplified optimization, using fewer trainable parameters to capture complex data patterns.

## Features
- **Custom Nonlinearity**: Each layer learns a set of hyperplanes to reshape the data dynamically, reducing training time.
- **Optimized Performance**: Through reduced parameterization, fold layers achieve lower latency at run time.
- **Configurable Optimizers**: Support for various optimizers to best match the model's fold-based architecture.
- **Improved Memory Efficiency**: Fewer parameters make Fold Layers more memory and parameter efficient.
- **Interpretability**: Fold operations provide a more intuitive and interpretable alternative to traditional deep learning models.

## Architecture
The fold layers are inspired by origami and the Fold and Cut Theorem to emulate a ReLU function but add the capability to fold data into more separable forms in fewer steps. They modify the data by finding the projection of the data onto a hyperplane and then adding the projection to the data twice in N-dimensional space to 'fold' the data. This process is repeated for each fold layer in the model. The fold layer is defined by the following equation:

$$
L_p(\mathbf{x}, \mathbf{n}_p) = \mathbf{x} - 2 \left( \mathbb{1}_{\{\mathbf{n}_p \cdot \mathbf{x} > \mathbf{n}_p \cdot \mathbf{n}_p\}} 
\right) \left(1 - \frac{\mathbf{x} \cdot \mathbf{n}_p}{\lVert \mathbf{n}_p \rVert} \right) \mathbf{n}_p
$$


## Installation

You can install this package from ```PyPi``` with

```bash
pip install FoldLayer
```

or 

```bash
python -m pip install --upgrade FoldLayer
```


## Usage

This section is under development. Please check back soon for usage instructions.

```python
import fold_layer
```


## Research and Development
The Fold Layer is under active research, focusing on:
- Experimenting with different fold depth and width configurations.
- Testing efficiency gains in prediction for natural language processing, computer vision, and other domains.
- Identifying optimizers that best support fold-layer dynamics.
- Experimenting with folds in higher dimensions.
- Developing a fold version of convolutional neural networks.

## Contributing
Contributions to improve the Fold Layer, fix bugs, or add features are welcome! Please open an issue or submit a pull request.

Current Contributors:

Dallin Stewart - dallinpstewart@gmail.com

[![LinkedIn][linkedin-icon]][linkedin-url1] [![GitHub][github-icon]][github-url1] [![Email][email-icon]][email-url1]

Sam Layton

[![LinkedIn][linkedin-icon]][linkedin-url2] [![GitHub][github-icon]][github-url2] [![Email][email-icon]][email-url2]

Jeddy Bennett - jeddybennett01@gmail.com

[![LinkedIn][linkedin-icon]][linkedin-url3] [![GitHub][github-icon]][github-url3] [![Email][email-icon]][email-url3]

Nathaniel Driggs

[![LinkedIn][linkedin-icon]][linkedin-url4] [![GitHub][github-icon]][github-url4] [![Email][email-icon]][email-url4]


## License
This project is licensed under the MIT License. See the LICENSE file for details.




[linkedIn-icon]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedIn-url1]: https://www.linkedin.com/in/dallinstewart/
[linkedIn-url2]: https://www.linkedin.com/in/
[linkedIn-url3]: https://www.linkedin.com/in/jeddy-bennett/
[linkedIn-url4]: https://www.linkedin.com/in/


[github-icon]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[github-url1]: https://github.com/binDebug3
[github-url2]: https://github.com/
[github-url3]: https://github.com/jeddybennett
[github-url4]: https://github.com/

[Email-icon]: https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white
[Email-url1]: mailto:dallinpstewart@gmail.com
[Email-url2]: mailto:dallinpstewart@gmail.com
[Email-url3]: mailto:jeddybennett01@gmail.com
[Email-url4]: mailto:dallinpstewart@gmail.com
