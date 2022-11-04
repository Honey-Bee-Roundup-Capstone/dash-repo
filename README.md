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

Bees provide nearly one-third of the food we eat by pollinating our fields and orchards. Bees are also a multi-billion dollar industry. The problem is that honeybee colonies are shrinking more and more each year. What we aim to do is predict honeybee colony loss over time based on key factors that help and harm honeybees. We will then make recommendations to people in the business: beekeepers, farmers, the USDA, honey and wax companies, and so on, to mitigate future losses and improve the overall outlook of honeybees in general. This project provides both a financial benefit and an environmental one, and we're excited to see what solutions we can provide for this important issue.


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

What significant features drive honeybee colony loss?

What time of year is the biggest loss?

What state/area suffers heaviest loss and primary factors attributing to that?

Does summer or winter have the largest loss?

Does the beekeeper to colony ratio have an effect on colony loss?

### Target variable

Our target variable is honeybee colony loss. We trained and evaluated several machine learning models to predict future colony loss based on significant features. We selected the best-performing model for testing unseen data.

### Need to haves (Deliverables):

Final Notebook: Full pipeline, hypotheses, statistical testing, markdown, code comments wrangle.py explore.py modeling.py Three models including time series Slide deck 7-10 minute presentation to a mixed technical and non-tech audience.

### Nice to haves (With more time):

Interactive map

***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]

- The United States has an overall net loss in honeybee colonies each year. 2020 saw a net gain, perhaps as a result of less human activity and interference, as well as improved environmental conditions, during the pandemic.

- The beekeeper-to-colony ratio has a significant positive correlation with colony loss (76 percent).

- More colonies are lost in the winter season than in the summer season. This is consistent year after year.

- Florida and Wisconsin have had the highest cumulative net loss over time. Their stark differences in climate and geolocation point to factors other than location and climate affecting colony loss.

- Colonies that are exclusive to their respective states suffer less losses than colonies that travel to other states.

- California's beekeeping operation is vastly larger than any other state; they have the most colony losses per year as a result, but they have been relatively successful in replacing the lost colonies and adding new ones over time.


***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
<p>
Originally Data was found on <a href = "https://data.world/finley/bee-colony-statistical-data-from-1987-2017">Data.World</a>, then up-to-date data was pull from the Original Souces, and we narrowed down to the Bee Colony Loss Data from <a href = "https://bip2.beeinformed.org/loss-map/">BeeInformed.org</a>
</p>

#### Starting DataFrame:

---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| year | Year Survey Data was reported for. | [DATETIME] |
| state | State Survey Data was reported for. | [OBJ64] |
| total_annual_loss | Percentage (%) of bees lost among all colonies in the reported state. | |
| average_loss | Average Level of Bee Loss Experience by a Bee Keeper in the reported state. | |
| starting_colonies | Number of Colonies at the start of the reporting period for the reported state. | |
| colonies_lost | Number of Colonies lost at the end of the reporting period for the reported state. (Note: Loss rates should not be interpreted as a change in population size because beekeepers can replace lost colonies throughout the year. Therefore, colony loss rates are best interpreted as a turn-over rate, as high levels of losses do not necessarily result in a decrease in the total number of colonies managed in the United States.) | |
| ending_colonies | Number of Colonies at the end of the reporting peroid for the reported state. | |
| beekeepers| Number of Bee Keepers with Colonies who operate in the reported state. | |
| beekeepers_exclusive_to_state | Percentage (%) of Bee Keepers with Colonies ONLY in the reported state. (Keepers with colonies in more than one state have their numbers added to all states they operate in.) | |
| colonies | Number of Colonies belonging to keepers who operate in the reported state.| |
| colonies_exclusive_to_state | Percentage (%) of Colonies kept by Bee Keepers who ONLY operate in the reported state.  | |

#### Final DataFrame:

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]
<p>
Data was originally found on Data.World, and further traced back to it's source to pull the most up-to-date data on Bees.
<ul>Of the original 3 Data sets:
<li> After assessement Census Data from the USDA was deemed not to have pertinent information to the current population of bees or health of hives, as well as the fact that it is reported in 5 year gaps, was removed from our initial data set.</li>
<li> Survey Data by State from the USDA was also deemed as having less pertinent information on the trend in population of bees or health of their hives, and was left for further exploration as time permits due to a small amount of data on the environmental area of the colonies.</li>
<li> The Bee Colony Loss Data from BeeInformed.org has the most relevant data regarding current number of colonies, number of bee keepers, and loss of bees and colonies, so was the data set we initially focused on.
  <ul><li> However, due to this privacy stipulation "For the protection of privacy, losses are reported as N/A if 10 or fewer beekeepers responded in that state. These beekeepers' losses are included in the national statistics." we decided to drop all records where the number of beekeepers were 10 or less, as most of the data was Null, and therefore not contributing towards our goal. </li></ul></li></ul>

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

### Stats Test 1: Correlation Test

Correlation tests are used to check if two samples are related. They are often used for feature selection and multivariate analysis in data preprocessing and exploration.


To run the Correlation test in Python use the following import: \
<span style="color:green">from</span> scipy.stats <span style="color:green">import</span> pearsonr

- pearsonr, in this case, takes in the  and returns the correlation coefficient, corr, and the p_value, p:
    - the correlation coefficient is a unitless continuous numerical measure between -1 and 1, where 1= perfect correlation and -1 = perfect negative correlation. 
    - The p_value is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct.

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is there is no relationship between the number of colonies lost annually and the beekeeper to colony ratio.
- The alternate hypothesis (H<sub>1</sub>) is there is a relationship between the number of colonies lost annually and the beekeeper to colony ratio.

#### Confidence level and alpha value:
- I established a 95% confidence level 
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:

corr = 0.765
p = 3.51e-57

#### Summary:

We can reject the null hypothesis that there is no relationship between the number of colonies lost annually and the beekeeper to colony ratio.

### Stats Test 2: T-Test: Two Samples, Two Tailed
- A T-test allows me to compare a categorical and a continuous variable by comparing the mean of the continuous variable by subgroups based on the categorical variable
- The t-test returns the t-statistic and the p-value:
    - t-statistic: 
        - Is the ratio of the departure of the estimated value of a parameter from its hypothesized value to its standard error. It is used in hypothesis testing via Student's t-test. 
        - It is used in a t-test to determine if you should support or reject the null hypothesis
        - t-statistic of 0 = H<sub>0</sub>
    -  - the p-value:
        - The probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct
- We wanted to compare colony loss in the summer to colony loss in the winter. 

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is there is no difference between the number of colonies lost in the summer and the number of colonies lost in the winter.
- The alternate hypothesis (H<sub>1</sub>) is a difference between the number of colonies lost in the summer and the number of colonies lost in the winter.

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results:

t = 4.322
p = 1.840e-5

#### Summary:

We can reject the null hypothesis that there is no difference in colony loss between summer and winter.

***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

- We scaled the data using the MinMaxScaler with the exception of our target variable, colonies_lost. We selected two features through statistical testing: beekeeper_colony_ratio and colonies_net_gained. We ran a recursive feature elimination (RFE) and Select K Best to confirm our choices, and added three more based on the results: beekeepers_scaled, starting_colonies_scaled, and ending_colonies_scaled.

- After scaling the data, we calculated a baseline using both the mean and the median, and selected the mean because it had a lower RMSE than the median. We selected four models to fit and train and created a function to run all four models and return the RMSE for both the train and validate sets.


### Baseline
    
- Baseline Results: 
    
    RMSE using Mean on 
      Train:  2794.49 
      Validate:  1715.12

    RMSE using Median on 
      Train:  2867.69 
      Validate:  1837.86

- Selected features to input into models:
    - features = ['beekeepers_scaled', 'starting_colonies_scaled','ending_colonies_scaled', 'colonies_net_gain_scaled', 'beekeeper_colony_ratio_scaled']

***

### Models and R<sup>2</sup> Values:


- Will run the following regression models:

   OLS, Lasso Lars, Tweedie Regressor, Polynomial Features 

    
#### Model 1: Linear Regression (OLS)


- Model 1 results: 
    RMSE:
      - Train: 1212.60
      - Validate: 900.12


### Model 2 : Lasso Lars Model


- Model 2 results: 
    RMSE:
    - Train: 1213.01
    - Validate: 882.29


### Model 3 : Tweedie Regressor (GLM)

- Model 3 results:
    RMSE:
    - Train: 1557.26
    - Validate: 1614.44


### Model 4: Squared Regression Model

- Model 4 results: 
    RMSE:
    - Train: 384.35
    - Validate: 3512.81


## Selecting the Best Model:



                                 model   RMSE_train  RMSE_validate
0                             Baseline  2794.490927    1715.116523
1                        OLS Regressor  1212.600000     900.120000
2                 LASSOLARS(alpha = 1)  1213.010000     882.290000
3  Tweedie Regressor(power=1, alpha=0)  1557.260000    1614.440000
4    Polynomial Regression(degree = 2)   394.350000    3512.810000


- The LassoLars model performed well on the train and validate sets, beating baseline RMSE on train by 1581.49 and on validate by 832.83. The baseline difference between train and validate sets was 1079.37, and the selected model had an RMSE  difference of 330.71. The OLS Regressor also performed well, but we decided overall that the Lasso Lars model is the best model for this project.


## Testing the Model


- Model Testing Results

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]


***
###### ReadMe template by: <a href="https://github.com/mdalton87" target="_blank">Mathew Dalton</a>
</p>
