Anomaly Detection Using Financial Ratios
===================


####Coding and testing the commercial applications of academic papers and cutting edge analytical techniques.
------------------------------------------------------------------------

**Paper 1:** *A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise*

**Abstract:** Clustering algorithms are attractive for the task of class identification in spatial databases. However, the application to large spatial databases rises the following requirements for clustering algorithms: minimal requirements of domain knowledge to determine the input parameters, discovery of clusters with arbitrary shape and good efficiency on large databases. The well-known clustering algorithms offer no solution to the combination of these requirements. In this paper, we present the new clustering algorithm DBSCAN relying on a density-based notion of clusters which is designed to discover clusters of arbitrary shape. DBSCAN requires only one input parameter and supports the user in determining an appropriate value for it. We performed an experimental evaluation of the effectiveness and efficiency of DBSCAN using synthetic data and real data of the SEQUOIA 2000 benchmark. The results of our experiments demonstrate that (1) DBSCAN is significantly more effective in discovering clusters of arbitrary shape than the well-known algorithm CLAR-ANS, and that (2) DBSCAN outperforms CLARANS by a factor of more than 100 in terms of efficiency.

**Paper 2:** *Clustering-based Anomaly Detection for Microservices*

**Abstract:** Anomaly detection is an important step in the management and monitoring of data centers and cloud computing platforms. The ability to detect anomalous virtual machines before real failures occur results in reduced downtime while operations engineers urgently recover malfunctioning virtual machines, efficient root cause analysis, and improved customer optics in the event said malfunction lead to an outage. Virtual machines could fail at any time, whether in a lab or production system. If there is no anomaly detection system, and a virtual machine in a lab environment fails, the QA and DEV team will have to switch to another environment while the OPS team fixes the failure. The potential impact of failing to detect anomalous virtual machines can result in financial ramifications, both when developing new features and servicing existing ones. This paper presents a model that can efficiently detect anomalous virtual machines both in production and testing environments.

----------


Documents
-------------

[A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise](https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf)

[Clustering-based Anomaly Detection for Microservices](https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf)


----------


Hypotheses
-------------------
 - Financial ratios are good indicators of a business and its operations
 - DBSCAN algorithm will be effective at identifying clusters of differing density, size and shape
 - Points identified as 'noise' can be the basis for further analysis of potentially risky companies

----------

Process
-------------
From paper 2, we note it is important to first separate the data into common domains to ensure we are comparing data points with common characteristics. In this case study on financial ratios, we are dividing our data into industries.

image

DBCAN can detect clusters of deferring size and shape by locating regions of high density that are separated from one another by regions of low density. The algorithm form clusters in the following way:

*“A point **a** is density connected to a point **b** with respect to ϵ and MinPts, if there is a point **c** such that, both **a** and **b** are density reachable from **c** w.r.t. to ϵ and MinPts.”*

image


----------


Example Results Screens
--------------------

----------

Next Steps
--------------------
----------

Requirements
--------------------
----------
