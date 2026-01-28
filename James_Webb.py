#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'widget')


# # This example shows how to read James Webb image
# 
# This example (loosly based on the "Read and plot an image from FITS file" on astropy https://docs.astropy.org/en/stable/generated/examples/io/plot_fits-image.html ).
# 
# Set up matplotlib and use a nicer set of plot parameters
# 
# 

# In[1]:


import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
import  astropy.visualization as asv 
from skimage.transform import resize # For resizing the images
import numpy as np
plt.style.use(astropy_mpl_style)


# Open the image

# In[3]:


from astropy.io import fits

# Image url
imUrl = '/export/work/Satdata2/jwst/MAST_2025-01-07T0756/JWST/jw01170006001_02101_00001_guider1/jw01170006001_02101_00001_guider1_cal.fits'


# We now can have a look at what the file contains
# 

# In[4]:


file = fits.open(imUrl)


# In[5]:


file.info()



# The main image is located in "SCI", which we select with ``ext=1`` when reading the file.
# 
# Now we open the files and read in the image arrays. We also resize them so that they all
# are the same size.

# In[8]:


file[2].header


# In[9]:


im = fits.getdata(imUrl, ext=1)


# The data is now stored as a 2D numpy array. Print the dimensions using the
# shape attribute:

# In[10]:


print(im.shape,im.dtype)
display(im)


# We can now have a look at a greyscale image of the selected band. 
# Here one might need to tune some of the parameters.

# In[11]:


plt.figure()
im[np.isnan(im)]=0 # Make nan pixels black
norm = asv.simple_norm(im, stretch='asinh',asinh_a=0.1, min_percent=40 ,max_percent=99.7) # How we scale the image
plt.imshow(im, norm=norm, cmap='gray') # Plotting the grayscale image
plt.grid(False)
plt.colorbar()


# In[ ]:




