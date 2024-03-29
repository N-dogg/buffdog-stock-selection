﻿Warren Buffet Stock Selection
===================


#### Coding and testing the commercial applications of academic papers and cutting edge analytical techniques.
------------------------------------------------------------------------

**Paper 1:** *A Machine Learning Framework for Stock Selection*

**Abstract:** This paper demonstrates how to apply machine learning algorithms to distinguish good stocks from the bad stocks. To this end, we construct 244 technical and fundamental features to characterize each stock, and label stocks according to their ranking with respect to the return-to-volatility ratio. Algorithms ranging from traditional statistical learning methods to recently popular deep learning method, e.g. Logistic Regression (LR), Random Forest (RF), Deep Neural Network (DNN), and the Stacking, are trained to solve the classification task. Genetic Algorithm (GA) is also used to implement feature selection. The effectiveness of the stock selection strategy is validated in Chinese stock market in both statistical and practical aspects, showing that: 1) Stacking outperforms other models reaching an AUC score of 0.972; 2) Genetic Algorithm picks a subset of 114 features and the prediction performances of all models remain almost unchanged after the selection procedure, which suggests some features are indeed redundant; 3) LR and DNN are radical models; RF is risk-neutral model; Stacking is somewhere between DNN and RF. 4) The portfolios constructed by our models outperform market average in back tests.

**Paper 2:** *Neural Network Models for Stock Selection Based on Fundamental Analysis*

**Abstract:** Application of neural network architectures for financial prediction has been actively studied in recent years. This paper presents a comparative study that investigates and compares feed-forward neural network (FNN) and adaptive neural fuzzy inference system (ANFIS) on stock prediction using fundamental financial ratios. The study is designed to evaluate the performance of each architecture based on the relative return of the selected portfolios with respect to the benchmark stock index. The results show that both architectures possess the ability to separate winners and losers from a sample universe of stocks, and the selected portfolios outperform the benchmark. Our study argues that FNN shows superior performance over ANFIS.

----------


Documents
-------------

[A Machine Learning Framework for Stock Selection](https://arxiv.org/pdf/1806.01743.pdf)

[Neural Network Models for Stock Selection Based on Fundamental Analysis](https://arxiv.org/ftp/arxiv/papers/1906/1906.05327.pdf)


----------


Hypotheses
-------------------
Overall goal is to develop a program, trained on Warren Buffett's historical trading, that can identify future opportunities of a similar nature. The following are the projects hypotheses:
 - A neaural network model will be effective at learning past patterns of stock selection and predicting similar stocks
 - A neaural network model will be effective at analysis large amounts of fundamental stock data
 - The success of Warren Buffett's stock selection will continue into the future

----------

Process
-------------
With Buffett's unique stock selection style leading to so few acquisition's, we are looking at the rare-event prediction problem. Where we have an unbalanced dataset with positively labelled data representing less that 5% of the total population. No matter how large the data, the use of Deep Learning gets limited by the amount of positively labeled samples.

![Capture](https://user-images.githubusercontent.com/43980002/65649792-5ed99e80-e04b-11e9-8cad-7493452ba0d6.JPG)

To combat this we have undersampled from the negatively labelled data and included holdings from managers who claim to use the same techniques. Coupling this with a shallower architechture we can see positive results from both the training and validation cost curves early on. We saw the best results when early-stopping was implemented to prevent overfitting.

![Figure_1](https://user-images.githubusercontent.com/43980002/65650062-939a2580-e04c-11e9-8e20-58c008027da8.png)

Although uncommon, after the model was trained, it was used to predict on the entire population. With a relatively strict early-stopping policy, the intention was to test whether the model could identify any stocks it still believed had the same characteristics as those held. 

----------


Example Results Screens
--------------------
Here we can analyse both the profiles of the stocks selected to see if they match, and just for fun, create a portfolio to test the returns. 

Profile-wise we are looking for that 'moat'. The economic barriers, patents, copyrights, legal barriers that make it difficult for competitors to steal market share. With predictions like Amazon, Intel and Carnival Corporation (the world’s largest leisure cruise company), it shows true. Diving into some of the stranger picks, Styker, Orthofix, IQVIA, IntelliPharmaCeutics are all leading medical companies with large controls of patents and research labs. Finally, we see predictions in the area of semiconductors, a must in a world of increasing computers. At a business profile level, we are seeing fantastic similarities between those stocks highlighted by our model and those held.

We can also look at the return on a evenly weighted portfolio made with the holdings predicted by the model. From the time when this model was trained (September 2018) till now (September 2019) we observed the following returns:

![Capture1](https://user-images.githubusercontent.com/43980002/65655509-d3b6d380-e05f-11e9-8a75-3f4c023c498f.JPG)

Promising returns.

----------

Next Steps
--------------------
- Perform research over the risk of the portfolio
- Put my money where my analytics is

----------

Requirements
--------------------
pandas  
keras  
matplotlib  
sklearn  

----------
