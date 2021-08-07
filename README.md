# Braingraphgeo

Braingraphgeo is a package for performing analysis on structural brain networks
using random geometric surrogate graphs.

Data and examples stem from a manuscript currently under review at NeuroImage:

Trinkle, S., Foxley, S., Wildenberg, G., Kasthuri, N., La Riviere, P., “The role
of spatial embedding in mouse brain networks constructed from diffusion
tractography and tracer injections,” *Under review at NeuroImage, 2021.*

For more information, see [my blog
post](http://scotttrinkle.com/news/brain-networks/)

## Installation

For local installation, first clone the repo:

`git clone https://github.com/scott-trinkle/braingraphgeo.git`

`cd` into the directory:

`cd braingraphgeo`

and run (preferably in a virtual environment): 

`pip install -e .`

and install requirements:

`pip install -r requirements.txt`

## Data

Example data represent weighted structural brain graphs derived from neural
tracer imaging and diffusion MRI tractography. Graphs are stored as weighted
adjacency matrices in `.csv` files. Nodes are defined as anatomical regions
detailed in the [Allen Mouse Brain
Atlas](https://mouse.brain-map.org/static/atlas). "XXX-I" and "XXX-C" in the
column and index titles of the data files represent ipsilateral and
contralateral nodes, respectively. For access to the Allen brain atlas acronyms
and structure masks, I recommend using the
[allensdk](https://allensdk.readthedocs.io/en/latest/):

```
from allensdk.core.mouse_connectivity_cache import MouseConnectivityCache

mcc = MouseConnectivityCache()
tree = mcc.get_structure_tree()
```

Edge weights for the tracer data (`data/tracer.csv`) are defined using the
normalized connection density metric from the [Knox computational
model](https://direct.mit.edu/netn/article/3/1/217/2194/High-resolution-data-driven-model-of-the-mouse)
(code available
[here](https://github.com/AllenInstitute/mouse_connectivity_models)). 

Edge weights for the dense (`data/tract_dense_n*.csv`) and endpoint
(`data/tract_endpoint_n*.csv`) tractography graphs represent raw streamline
counts between nodes, normalized by the product of the two node volumes.

For fair comparison between tractography (based on an inherently symmetric
diffusion metric) and tracers (based on injections to a single hemisphere),
graphs have been made undirected and have enforced hemispheric symmetry: `W =
W.T`.

Distances between nodes are available in the same format in
`data/fiber_distances.csv`.  Distances are measured in mm and represent the
shortest streamline connecting each pair of nodes averaged across all
tractography datasets.
