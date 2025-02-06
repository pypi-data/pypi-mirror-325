# Geometric Convolutions

This package implements the GeometricImageNet which allows for writing general functions from geometric images to geometric images. Also, with an easy restriction to group invariant CNN filters, we can write CNNs that are equivariant to those groups for geometric images.

See the paper for more details: https://arxiv.org/abs/2305.12585

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
    1. [Basic Features](#quick-start)
    2. [Learning Scalar Filters](#learning-scalar-filters)
3. [Features](#features)
    1. [GeometricImage](#geometricimage)
    2. [Layer and BatchLayer](#layer-and-batchlayer)
4. [Authors](#authors)
5. [License](#license)

## Installation

- Install using pip: `pip install geometricconvolutions`.
- Alternatively, you can install this repo as an editable install using pip.
  - Clone the repository `git clone https://github.com/WilsonGregory/GeometricConvolutions.git`
  - Navigate to the GeometricConvolutions directory `cd GeometricConvolutions`
  - Locally install the package `pip install -e .` (may have to use pip3 if your system has both python2 and python3 installed)
  - In order to run JAX on a GPU, you will likely need to follow some additional steps detailed in https://github.com/google/jax#installation. You will probably need to know your CUDA version, which can be found with `nvidia-smi` and/or `nvcc --version`.

## Quick Start

### Basic Features
See the script `quick_start.py` for this example in code form.

First our imports. Geometric Convolutions is built in JAX. The majority of the model code resides in geometric.
```
import jax.numpy as jnp
import jax.random as random

import geometricconvolutions.geometric as geom
```

First we construct our image. Suppose you have some data that forms a 3 by 3 vector image, so N=3, D=2, and k=1. Currently only D=2 or D=3 images are valid, and the side lengths must all be equal. The parity is how the image responds when it is reflected. Normal images have parity 0, an image of pseudovectors like angular velocity will have parity 1.
```
key = random.PRNGKey(0)
key, subkey = random.split(key)

N = 3
D = 2
k = 1
parity = 0
data = random.normal(subkey, shape=((N,)*D + (D,)*k))
image = geom.GeometricImage(data, parity=0, D=2)
```

We can visualize this image with the plotting tools in utils. You will need to call matplotlib.pypolot.show() to display.
```
image.plot()
```

Now we can do various operations on this geometric image
```
image2 = geom.GeometricImage.fill(N, parity, D, fill=jnp.array([1,0])) # fill constructor, each pixel is fill

# pixel-wise addition
image + image2

# pixel-wise subtraction
image - image2

# pixel-wise tensor product
image * image2

# scalar multiplication
image * 3
```

We can also apply a group action on the image. First we generate all the operators for dimension D, then we apply one
```
operators = geom.make_all_operators(D)
print("Number of operators:", len(operators))
image.times_group_element(operators[1])
```

Now let us generate all 3 by 3 filters of tensor order k=0,1 and parity=0,1 that are invariant to the operators
```
invariant_filters = geom.get_invariant_filters(
    Ms=[3],
    ks=[0,1],
    parities=[0,1],
    D=D,
    operators=operators,
    scale='one', #all the values of the filter are 1, can also 'normalize' so the norm of the tensor pixel is 1
    return_list=True,
)
print('Number of invariant filters N=3, k=0,1 parity=0,1:', len(invariant_filters))
```

Using these filters, we can perform convolutions on our image. Since the filters are invariant, the convolution
will be equivariant.
```
gg = operators[1] # one operator, a flip over the y-axis
ff_k0 = invariant_filters[1] # one filter, a non-trivial scalar filter
print(
    "Equivariant:",
    jnp.allclose(
        image.times_group_element(gg).convolve_with(ff_k0).data,
        image.convolve_with(ff_k0).times_group_element(gg).data,
        rtol=1e-2,
        atol=1e-2,
    ),
)
```

When convolving with filters that have tensor order > 0, the resulting image have tensor order img.k + filter.k
```
ff_k1 = invariant_filters[5]
print('image k:', image.k)
print('filter k:', ff_k1.k)
convolved_image = image.convolve_with(ff_k1)
print('convolved image k:', convolved_image.k)
```

After convolving, the image has tensor order 1+1=2 pixels. We can transpose the indices of the tensor:
```
convolved_image.transpose((1,0))
```

Since the tensor order is >= 2, we can perform a contraction on those indices which will reduce it to tensor order 0.
```
print('contracted image k:', convolved_image.contract(0,1).k)
```

### Learning Scalar Filters
Now we will have a simple example where we use GeometricConvolutions and JAX to learn scalar filters. See `scalar_example.py` for a python script of the example. First, the imports:
```
import jax.numpy as jnp
from jax import random, vmap
import time
import itertools as it
import math
import optax
from functools import partial

import geometricconvolutions.geometric as geom
import geometricconvolutions.ml as ml
```

Now lets define our images X and what filters we are going to use. Our image will be 2D, 64 x 64 scalar images. Our filters will be 3x3 and they will be the invariant scalar filters only. There are 3 of these, and the first one is the identity.
```
key = random.PRNGKey(time.time_ns())

D = 2
N = 64 #image size
M = 3  #filter image size
num_images = 10

group_actions = geom.make_all_operators(D)
conv_filters = geom.get_unique_invariant_filters(M=M, k=0, parity=0, D=D, operators=group_actions)

key, subkey = random.split(key)
X_images = [geom.GeometricImage(data, 0, D, True) for data in random.normal(subkey, shape=(num_images, N, N))]
```

Now let us define our target function, and then construct our target images Y. The target function will merely be convolving by the filter at index 1, then convolving by the filter at index 2.
```
def target_function(image, conv_filter_a, conv_filter_b):
    return image.convolve_with(conv_filter_a).convolve_with(conv_filter_b)

Y_images = [target_function(image, conv_filters[1], conv_filters[2]) for image in X_images]
```

We now want to define our network and loss function. Machine learning on the GeometricImageNet is done on the BatchLayer object, which is a way of collecting batches of multiple channels of images at possible different tensor orders in a single object. See [Layer and BatchLayer](#layer-and-batchlayer) for more information.

For this toy example, we will make our task straightforward by making our network a linear combination of all the pairs of convolving by one filter from our set of three, then another filter from our set of three with replacement. In this fashion, our target function will be the 5th of 6 images. Our loss is simply the root mean square error loss (RMSE). The ml.train function expects a map_and_loss function that operates on batch layers, and includes the parameters key and train that we won't use for this model.
```
def batch_net(params, layer, conv_filters):
    channel_convolve = vmap(geom.convolve, in_axes=(None, 0, None, None, None, None, None, None))
    batch_convolve = vmap(channel_convolve, in_axes=(None, 0, None, None, None, None, None, None))
    batch_linear_combination = vmap(geom.linear_combination, in_axes=(0, None))

    out_image_block = None

    for i,j in it.combinations_with_replacement(range(len(conv_filters[0])), 2):
        filter_a = conv_filters[0][i]
        filter_b = conv_filters[0][j]
        convolved_image = batch_convolve(layer.D, layer[0], filter_a, layer.is_torus, None, None, None, None)
        res_image = batch_convolve(layer.D, convolved_image, filter_b, layer.is_torus, None, None, None, None)

        if (out_image_block is None):
            out_image_block = res_image
        else:
            out_image_block = jnp.concatenate((out_image_block, res_image), axis=1)

    return batch_linear_combination(out_image_block, params)

def map_and_loss(params, x, y, key, train, conv_filters):
    return jnp.mean(vmap(ml.rmse_loss)(batch_net(params, x, conv_filters), y[0]))
```

Now we initialize our params as random normal, then train our model using the `train` function from `ml.py`. Train takes the input data X_layer, the target data Y_layer, a map and loss function that takes arguments (params, x, y, key, train), the params array, a random key for doing the batches, the number of epochs to run, the batch size, and the desired optax optimizer.

```
key, subkey = random.split(key)
params = random.normal(subkey, shape=(len(conv_filters) + math.comb(len(conv_filters), 2),))

filter_layer = geom.Layer.from_images(conv_filters)
X_layer = geom.BatchLayer.from_images(X_images)
Y_layer = geom.BatchLayer.from_images(Y_images)

params, _, _ = ml.train(
    X_layer,
    Y_layer,
    partial(map_and_loss, conv_filters=filter_layer),
    params,
    key,
    ml.EpochStop(500, verbose=1),
    batch_size=num_images,
    optimizer=optax.adam(optax.exponential_decay(0.1, transition_steps=1, decay_rate=0.99)),
)

print(params)
```

This should print something like:
```
Epoch 50 Train: 7.9201660
Epoch 100 Train: 1.9141825
Epoch 150 Train: 1.0414978
Epoch 200 Train: 0.6042308
Epoch 250 Train: 0.3557778
Epoch 300 Train: 0.2116257
Epoch 350 Train: 0.1265045
Epoch 400 Train: 0.2636956
Epoch 450 Train: 0.0671248
Epoch 500 Train: 0.0342868
[-8.7383251e-06  7.2533490e-05 -8.7593980e-06 -8.9773348e-06
  1.0000725e+00 -9.1719430e-06]
 ```
 and we can see that the 5th parameter is 1 and all others are tiny. Hooray!

## Features

### GeometricImage

The GeometricImage is the main concept of this package. We define a geometric image for dimension D, sidelength N, parity p, and tensor order k. Note that currently, all the sidelengths must be the same. To construct a geometric image, do: `image = GeometricImage(data, parity, D)`. Data is a jnp.array with the shape `((N,)*D + (D,)*k)`.

### Layer and BatchLayer

The Layer and BatchLayer classes allow us to group multiple images together that have the same dimension and sidelength. Layer is a dictionary where the keys are tensor order k, and the values are a image data block where the first index is the channel, then the remaining indices are the normal ones you would find in a geometric image. BatchLayer has the same structure, but the first index of the data image block is the batch, the second is the channel, and then the rest are the geometric image. You can easily construct Layers and BatchLayers from images using the `from_images` function.

## Authors
- **David W. Hogg** (NYU) (MPIA) (Flatiron)
- **Soledad Villar** (JHU)
- **Wilson Gregory** (JHU)

## License
Copyright 2022 the authors. All **text** (in `.txt` and `.tex` and `.bib` files) is licensed *All rights reserved*. All **code** (everything else) is licensed for use and reuse under the open-source *MIT License*. See the file `LICENSE` for more details of that.
