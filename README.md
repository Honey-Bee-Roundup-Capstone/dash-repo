# <a name="top"></a>Honey Bee Round-up
![]()

by: Dashiell Bringhurst, Rajesh Lamichhane, and Jennifer Lewis

<p>
  <a href="https://github.com/dashbringhurst" target="_blank">
    <img alt="Dashiell" src="https://img.shields.io/github/followers/dashbringhurst?label=Follow_Dashiell&style=social" />
  </a>
   <a href="https://github.com/rajeshlamichhane04" target="_blank">
    <img alt="Rajesh" src="https://img.shields.io/github/followers/rajeshlamichhane04?label=Follow_Rajesh&style=social" />
  </a>
   <a href="https://github.com/JenniferMLewis" target="_blank">
    <img alt="Jennifer" src="https://img.shields.io/github/followers/JenniferMLewis?label=Follow_Jenn&style=social" />
  </a>
</p>


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___

<img src="https://cdn.discordapp.com/attachments/415980182021603329/1035270460373483610/eric-ward-qFAEHxevxVE-unsplash.jpg">

## <a name="project_description"></a>Project Description:
[[Back to top](#top)]

***
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Project Outline:

Technical Goals: 

  Our technical goals are to analyze honeybee colony data from the USDA to determine if there is a statistically significant amount of loss among colonies over time, and to develop a machine learning model that accurately predicts honeybee colony loss based on significant environmental and human-driven features. We can use these predictions to make recommendations to stakeholders to minimize colony loss and improve outcomes.

Business Goals: 

  Honeybees pollinate $15 billion worth of crops in the United States each year, including more than 130 types of fruits, nuts, and vegetables. Honeybees also produce honey, worth about $3.2 million in 2017 according to USDA-National Agricultural Statistics Service (NASS).	

  We want to provide stakeholders with an accurate model for predicting colony loss over time, which factors affect colony loss, and which areas are most conducive to colony production and preservation. We also want to provide a way for stakeholders to test outcomes based on actions they take (or not take) to mitigate colony loss. Our overarching business goal is to influence stakeholders to make responsible and proactive decisions to help honeybees thrive.

        
### Hypothesis

Our initial hypothesis is that honeybee colony loss has increased over time and will continue to increase year over year if no measures are taken to mitigate or reverse this outcome. Some initial questions we have are: 

  How much have honeybee colonies diminished over time? Is this loss compounded year over year?

  What effects do honeybee colony loss have on agricultural businesses? 
    Financial impacts? Production/crop impacts?

  What future environmental or agricultural implications can be gleaned from the data? 

  What significant features drive honeybee colony loss?
  
  What time of year is the biggest loss?

  What state/area suffers heaviest loss and primary factors attributing to that?

  Does Longitude affect colony loss? 
    Do more northern hives lose more bees?


### Target variable

Our target variable is honeybee colony loss. We are going to train and evaluate several machine learning models to predict future colony loss based on significant features. We will select the best-performing model for testing unseen data.

### Need to haves (Deliverables):

Final Notebook: Full pipeline, hypotheses, statistical testing, markdown, code comments
wrangle.py
explore.py
modeling.py
Three models including time series
Slide deck
7-10 minute presentation to a mixed technical and non-tech audience

### Nice to haves (With more time):

Interactive map

***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]




***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| year | Year Survey Data was reported for. | [DATETIME] |
| state | State Survey Data was reported for. | [OBJ64] |
| data_item breakdown 1 | These 5 are the input values | |
| data_item breakdown 2 | for the data item column, | |
| data_item breakdown 3 | we're going to take them and | |
| data_item breakdown 4 | break them into encoding so we | |
| data_item breakdown 5 | have values that work for each year. | |
| value | Instances of the data_item breakdown type for that year | [INT or FLOAT] |
| total_annual_loss | percentage (%) of bees lost among all bee keeprs in the reported state. | |
| beekeepers| Number of Bee Keepers with Colonies who operate in the reported state. | |
| beekeepers_exclusive_to_state | Percentage (%) of Bee Keepers with Colonies ONLY in the reported state. (Keepers with colonies in more than one state have their numbers added to all states they operate in.) | |
| colonies | Number of Colonies belonging to keepers who operate in the reported state.| |
| colonies_exclusive_to_state | Percentage (%) of Colonies kept by Bee Keepers who ONLY operate in the reported state.  | |

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()


### Wrangle steps: 


*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - wrangle.py 
    - explore.py
    - modeling.py


### Takeaways from exploration:


***

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]

### Stats Test 1: ANOVA Test: One Way

Analysis of variance, or ANOVA, is a statistical method that separates observed variance data into different components to use for additional tests. 

A one-way ANOVA is used for three or more groups of data, to gain information about the relationship between the dependent and independent variables: in this case our clusters vs. the log_error, respectively.

To run the ANOVA test in Python use the following import: \
<span style="color:green">from</span> scipy.stats <span style="color:green">import</span> f_oneway

- f_oneway, in this case, takes in the individual clusters and returns the f-statistic, f, and the p_value, p:
    - the f-statistic is simply a ratio of two variances. 
    - The p_vlaue is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:


#### Summary:


### Stats Test 2: T-Test: One Sample, Two Tailed
- A T-test allows me to compare a categorical and a continuous variable by comparing the mean of the continuous variable by subgroups based on the categorical variable
- The t-test returns the t-statistic and the p-value:
    - t-statistic: 
        - Is the ratio of the departure of the estimated value of a parameter from its hypothesized value to its standard error. It is used in hypothesis testing via Student's t-test. 
        - It is used in a t-test to determine if you should support or reject the null hypothesis
        - t-statistic of 0 = H<sub>0</sub>
    -  - the p-value:
        - The probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct
- We wanted to compare the individual clusters to the total population. 
    - Cluster1 to the mean of ALL clusters
    - Cluster2 to the mean of ALL clusters, etc.

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is 
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results:


#### Summary:

***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

### Baseline
    
- Baseline Results: 
    

- Selected features to input into models:
    - features = []

***

### Models and R<sup>2</sup> Values:
- Will run the following regression models:

    

- Other indicators of model performance with breif defiition and why it's important:

    
    
#### Model 1: Linear Regression (OLS)


- Model 1 results:



### Model 2 : Lasso Lars Model


- Model 2 results:


### Model 3 : Tweedie Regressor (GLM)

- Model 3 results:


### Model 4: Quadratic Regression Model

- Model 4 results:


## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation/Out of Sample RMSE | R<sup>2</sup> Value |
| ---- | ----| ---- |
| Baseline | 0.167366 | 2.2204 x 10<sup>-16</sup> |
| Linear Regression (OLS) | 0.166731 | 2.1433 x 10<sup>-3</sup> |  
| Tweedie Regressor (GLM) | 0.155186 | 9.4673 x 10<sup>-4</sup>|  
| Lasso Lars | 0.166731 | 2.2204 x 10<sup>-16</sup> |  
| Quadratic Regression | 0.027786 | 2.4659 x 10<sup>-3</sup> |  


- {} model performed the best


## Testing the Model

- Model Testing Results

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]


***
###### ReadMe template by: <a href="https://github.com/mdalton87" target="_blank">Mathew Dalton</a>
</p>
