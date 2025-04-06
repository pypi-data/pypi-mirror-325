# adept algorithm -- Python implementation

This repo contains Python implementation of ADEPT method -- a fast, scalable, and accurate method for pattern segmentation in time series -- and, additionally, its extension for  walking segmentation from free-living wrist-worn sensor accelerometry data. 

Related publoshed work: 

1. Karas, M., Straczkiewicz, M., Fadel, W., Harezlak, J., Crainiceanu, C. M., & Urbanek, J.
K. (2019). Adaptive empirical pattern transformation (ADEPT) with application to walking
stride segmentation. Biostatistics, 22(2), 331–347.
[https://doi.org/10.1093/biostatistics/kxz033](https://doi.org/10.1093/biostatistics/kxz033 )

2. Karas, M., Urbanek, J. K. U., Illiano, V. P., Bogaarts, G., Crainiceanu, C. M., Dorn, J. F.
(2021). Estimation of free-living walking cadence from wrist-worn sensor accelerometry
data and its association with SF-36 quality of life scores. Physiological measurement,
42(6). [https://doi.org/10.1088/1361-6579/ac067b](https://doi.org/10.1088/1361-6579/ac067b)

The R implementation is available in R package adept ([CRAN index](https://cran.r-project.org/web/packages/adept/index.html)): 

- `segmentPattern()` -- ADEPT method implementation (paper 1 above), 
- `segmentWalking()` -- ADEPT extension for  walking segmentation from free-living wrist-worn sensor accelerometry data (paper 2 above). 

This Python implementation presented in this repo was developed by Marta Karas during her internship at Novartis @ Sensor Data Analytics Team in summer 2019 (IP not proteceted). 

# Overview of walking segmentation algorithm

The proposed algorithm for walking segmentation from free-living wrist-worn sensor accelerometry data consists of 3 main parts: 

### Step (1): Stride pattern segmentation from raw accelerometry data. 

- Input: raw vector magnitude accelerometry data, stride pattern templates, other segmentation parameters.  
- Output: List of lists, where each "inner list" has 3 elements which describe one identified data segment: 

    - 0. index of the start of the segment, 
    - 1. duration of the segment, expressed in array length, 
    - 2. correlation value between raw vector magnitude accelerometry data and stride pattern template. </br></br>

- Related implementations: 
  - `python/segment_pattern.py` -- <span style="color:magenta">**ADEPT method implementation (paper 1 above); corresponds to R's `adept::segmentPattern()`**</span>
  - `python/segment_pattern_utils.py`
  - `python/sliding_functions.py`</br></br>
  
- Corresponding tests:  
  - `python/test_segment_pattern.py`
  - `python/test_sliding_functions.py`

### Step (2): Describing each data segment obtained in Step 1. with numeric summaries of corresponding raw accelerometry data.

- Input: step (1) output, raw accelerometry data. 

- Output: List of lists, where each "inner list" has 23 elements which describe one identified data segment. 

- Related implementations: 

  - `python/describe_segments.py`

### Step (3). Identification of: (a) valid walking strides, (b) walking instances, (c) walking bouts. 

- Input: step (2) output, further algorithm parameters. 

- Output: Data frame, where each row represents one identified data segment; it has columns `'walking_instance_id'` and `'walking_bout_id'` which define walking instance and walking bout ID, respectively. There is an option to return data frame of all identified data segments contained in step (2) output, or only those if they correspond to some identified walking bout. 

- Related implementations: 

  - `python/segment_walking_bouts.py` -- <span style="color:magenta">**ADEPT extension for  walking segmentation from free-living wrist-worn sensor accelerometry data (paper 2 above); corresponds to R's `adept::segmentWalking()`**</span>

### Explanation: (a) valid walking stride, (b) walking instance, (c) walking bout

Definitions: 

- valid walking stride - identified data segment which passes certain filtering conditions; parameters of those conditions are arguments of `python/segment_walking_bouts.py` function.

- walking instance - a sequence of >=3 subsequent valid walking strides. To be a valid walking instance, those >=3 subsequent strides must also be "similar" to each other in a sense that their duration, azimuth angle median, elevation angle median are not larger (in their mean among 3 subsequent strides) than some parameter values; those parameters are arguments of `python/segment_walking_bouts.py` function.

- walking bout -  walking instance, possibly joined with another walking instance. We merge walking instances which are i.e. very close to each other and it is plausible to think they come from one walking action, but, say, something in a middle of that walking action has missed the "valid" stride criteria.  3 cases of conditions upon which the merging happens: 

    - (case 1) no break between two neighbouring walking instances, or 1-element break (bridge) between the two neighbouring walking instances, 
    - (case 2) 2-element break (bridge) between the two neighbouring walking instances, where at least 1 element of the bridge is close to passing valid stride condition; 
    - (case 3) 3-element break (bridge) between the two neighbouring walking instances, where at least 2 elements of the bridge are close to passing valid stride condition. The primary conceptual difference is that information of walking bout may be used i.e. to compute walking bout size, but only the strides from walking instance (subset of walking bout) are the ones one may want to use in analysis etc. 

### Time execution of the above steps implementation

- Step (1) is the most consuming one and takes 1-2 minutes per-subject per-dad24 with fs = 30 Hz of data collection. 
- Step (3) is the least time consuming and takes 1-2 seconds per-subject per-dad24 with fs = 30 Hz of data collection. Step (2) is also level of a few seconds. 

###  Wrapper for the above steps implementation

A wrapper code: `python/wrapper_identify_walking.py` computes Step (1) and Step (2) of the algorithm steps above and save final results to file (per subject-, per dad24-specific numpy array files). I meant it to be something close to wrapper in the pipeline, but ran out of time to prepare it to be closer. 

- Input: 3 arguments (HDF4 file path, pattern template file path, partial results dir path)
- Output: Step (2) output saved to file (precisely, per subject-, per dad24-specific numpy array files). 
