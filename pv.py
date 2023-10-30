import streamlit as st 
from st_speckmol import spec_plot 
import glob
import pandas as pd
import subprocess
import os
import base64
import plotly.express as px
import io
import py3Dmol

st.markdown(
    ''' # 3D Structure Visualization Tool using Speckmol'''
)
 
with st.sidebar.header('Upload your XYZ FILE'):
    uploaded_file = st.sidebar.file_uploader("Upload your input xyz file", type=["xyz"])

if uploaded_file is not None:
    # Read the content of the uploaded file
    protein_data = uploaded_file.read()
    
with st.sidebar.expander("Parameters",expanded=True):
    outl = st.checkbox('Outline',value=True)
    bond = st.checkbox('Bond',value=True)
    bond_scale = st.slider('BondScale',min_value=0.0,max_value=1.0,value=0.8)
    brightness = st.slider('Brightness',min_value=0.0,max_value=1.0,value=0.4)
    relativeAtomScale = st.slider('RelativeAtomScale',min_value=0.0,max_value=1.0,value=0.64)
    bondShade = st.slider('bondShade',min_value=0.0,max_value=1.0,value=0.5)  
     
_PARAMETERS = {'outline': outl , 'bondScale': bond_scale,
                'bonds': bond ,'bondShade' : bondShade,
                'brightness': brightness, 'relativeAtomScale':relativeAtomScale,
              }
res = spec_plot(protein_data, wbox_height="800px", wbox_width="800px", scroll=True, _PARAMETERS = _PARAMETERS)

  
    


