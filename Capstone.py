# Phase 1 — Business Understanding

## Business Problem Framing & Success Criteria

### Business Context - Derived from Client Interviews and other Sources of Enterprise Information

West Chester University is seeking to better understand the factors that influence university graduation rates. As a university, West Chester has both fixed and variable operating costs, and maintaining a consistent number of students through graduation helps provide greater stability when planning for tuition revenue and other university-related revenue. The university would like to compare its performance with similar regional universities in order to better understand where opportunities for improvement may exist. For this analysis, West Chester Universitys peers will primarily consist of smaller regional universities in Pennsylvania and universities located within approximately 100 miles of West Chester. Examples of potential peer institutions include Millersville University, Shippensburg University, and Slippery Rock University.


### Business Problem

West Chester University needs to identify the factors that are most relevant in explaining and predicting graduation rates. The university also wants to understand how it compares with its regional peer institutions on those factors.
Identifying these factors would help the university determine where resource investments could potentially have the greatest impact on graduation rates.

### North Star

Every student who starts with a degree, and no student is left behind because of who they are or where they started. 

### Key Decision

Based on the factors that are most strongly associated with graduation rates, which areas should West Chester University prioritize for potential investment or intervention, and how does WCU compare with its regional peer institutions in those areas?

### Analytical Objective

Identify and quantify the factors that are most strongly associated with university graduation rates, and compare West Chester University with similar regional peer institutions to determine where meaningful differences and potential opportunities for improvement exist.


### Key Analytical Questions

What characteristics are most strongly associated with higher graduation rate? 
Can graduation rates be predicted with sufficient accuracy to support resource allocation to then further increase graduation rates? 
What university traits are most strongly associated with higher graduation rates? 

### Analytical Approach

### 2.2 Load Libraries 
# Data Manipulation
import pandas as pd
import numpy as np

# Visualization
import seaborn as sns
import matplotlib.pyplot as plt

# Notebook Display
from IPython.display import display

# Notebook Settings
sns.set(style="whitegrid")

import warnings
warnings.filterwarnings("ignore")
