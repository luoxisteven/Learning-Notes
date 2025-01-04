# Computer Vision

## Image Basic
- **Image Formation**
    1) World parameters
        - Light source
        - Surface properties 
    2) Camera parameters
        - Focal length / angle of view
        - Aperture size / depth of field
        - Lens distortion
- **Digital Image**
    - Pixel = smallest unit of an image
    -  A tensor (3D dimensional array of values)
        - Width x height x channel
        - 3 channels = RGB colour image (red, green, blue)
        - 1 channel = grayscale image
- **Image Manipulation**
    1) Crop = extract a subset of the image array (doesn’t
require resampling)
    2) Resize = change the dimensions of the image array
(**`requires resampling`**)
- **Resamling Methods**
    1) Nearest-neighbour: closest value to sample point
        - Simple, preserves hard edges
        - Smooth curves may be blocky/distorted 
    2) Bilinear: weighted average of 4 pixels around sample point
        - moother curves, but blurs hard edges
        - Slower to comput

    ![alt text](img-en/Resamling_Methods.png)

## Filter
- **Pixel Operator** computes an output value at each pixel location, based on the input pixel value  
  $$
  g(i, j) = h(f(i, j))
  $$
    - Output of image $g(i, j)$
    - Input of image $f(i, j)$
- **Local Operator** computes an output value at each
pixel location, based on a **`neighbourhood of pixels`**
around the input pixel 
- **Cross-correlation Convolution**
    $$
    g(i, j) = h(u, v) \otimes f(i, j)
    $$

    $$
    g(i, j) = \sum_{u, v} f(i + u, j + v) h(u, v)
    $$
- **Convolution**
    $$
    g(i, j) = h(u, v) * f(i, j)
    $$
    $$
    g(i, j) = \sum_{u, v} f(i - u, j - v) h(u, v)
    $$
    ![alt text](img-en/Convolution.png)


