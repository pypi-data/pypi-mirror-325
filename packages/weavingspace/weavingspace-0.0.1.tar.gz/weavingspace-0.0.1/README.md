# Geographical weaving
This is work in progress towards developing tiled geospatial data layers for symbolisation of complex multi-attribute choropleths.  

The original proof-of-concept code is in R and Rmd files in the `r-stuff` folder. Needed datasets to run the code are in the `data` folder.

## **Update** (*April 2022*) 
There is now a working version in python using `geopandas` and `shapely`. It will be more extensible in the longer run and will be the basis of any further work at this stage. The python implementation also appears less prone to topological glitches when tiles are dissolved to form tilings and does not require that we use any additional libraries to get reasonable(ish) performance when tiling large maps. The python source is in the `weavingspace` folder. 

There are several jupyter notebooks in this repo that show examples of how to use the codebase, and the API is documented [here](https://dosull.github.io/weaving-space/doc/weavingspace.html).

## Talks
An overview of the concepts assembled from the proof-of-concept _R_ code is on [this webpage](https://dosull.github.io/weaving-space/NZCS-Nov-2021/make-weave-map.html). A similar follow-up talk is [available here](https://dosull.github.io/weaving-space/Palmerston-North-Nov-2022/slides/index.html)

Slides from a more recent talk explaining the work, extended to tiled maps (of which woven maps are a special case) is available [here](https://dosull.github.io/weaving-space/Palmerston-North-Nov-2022/slides/).
