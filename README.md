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

Bees provide nearly one-third of the food we eat by pollinating our fields and orchards. Bees are also a multi-billion dollar industry. The problem is that honeybee colonies are shrinking more and more each year. What we’ve done is predict honeybee colony loss over time based on key factors that help and harm honeybees. We’ve found that certain states have better survivability for their bees, and plan to look further into what these states offer bees that could be applied to other states. We also found that the bee population dips more drastically in winter when they rely heavily on their honey reserves at that time to overwinter. We plan to explore the effect of other stressors, such as Mites, Pesticides, and Disease, on overall hive health.

<a href = "https://www.canva.com/design/DAFQROGr2j4/vhxKf9p8nqg4u1fuLkqAcw/edit?utm_content=DAFQROGr2j4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton">Project Slideshow Presentation</a>

***
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Project Outline:

#### Technical Goals:

Our technical goals are to analyze honeybee colony data from Beeinformed.org and the USDA to determine if there is a statistically significant amount of loss among colonies over time, and to develop a machine learning model that accurately predicts honeybee colony loss based on significant environmental and human-driven features. We can use these predictions to make recommendations to stakeholders to minimize colony loss and improve outcomes.

#### Business Goals:

Honeybees pollinate $15 billion worth of crops in the United States each year, including more than 130 types of fruits, nuts, and vegetables. Honeybees also produce honey, worth about $3.2 million in 2017 according to USDA-National Agricultural Statistics Service (NASS).

We want to provide stakeholders with an accurate model for predicting colony loss over time, which factors affect colony loss, and which areas are most conducive to colony production and preservation. We also want to provide a way for stakeholders to test outcomes based on actions they take (or not take) to mitigate colony loss. Our overarching business goal is to influence stakeholders to make responsible and proactive decisions to help honeybees thrive.

        
### Hypothesis

Our initial hypothesis is that honeybee colony loss has increased over time and will continue to increase year after year if no measures are taken to mitigate or reverse this outcome. Some initial questions we have are:

How much have honeybee colonies diminished over time? Is this loss compounded year over year?

What significant features drive honeybee colony loss?

What time of year has the biggest loss?
- Does summer or winter have the largest loss?

What state/area suffers heaviest losses?

What are the primary factors attributing to colony loss?

Does the beekeeper to colony ratio have an effect on colony loss?
- Does a Closer to 1:1 ratio bode better for a colony's survival?

### Target variable

Our target variable is <b><u>honeybee colony loss</u></b>. We trained and evaluated several machine learning models to predict future colony loss based on significant features. 
- Starting Colony Count
- Net Gain/Loss through the year.
- Bee Keeper to Hive Ratio
We selected Our Lasso-Lars Model, with a 35% better prediction rate than baseline mean.

### Need to haves (Deliverables):

- Final Notebook: Full pipeline, hypotheses, statistical testing, markdown, code comments, three models including time series.
- wrangle.py: Docstrings and code comments.
- explore.py: Docstrings and code comments.
- modeling.py: Docstrings and code comments.
- Slide deck
- 7-10 minute presentation to a mixed technical and non-technical target audience.

### Nice to haves (With more time):

<s>Interactive map</s>
Comparision of different regions
Comparision of Stressor Data (ie. Mites, Pesticides, Diseases, etc.)
Full Comparison of Transient Bees vs. Bees exclusive to a state.

***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]

- The United States has an overall net loss in honeybee colonies each year. 2020 saw a net gain, perhaps as a result of less human activity and interference, as well as improved environmental conditions, during the pandemic.

- The beekeeper-to-colony ratio has a significant positive correlation with colony loss (76 percent).

- More colonies are lost in the winter season than in the summer season. <u>This is consistent year after year</u>.

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

- We created separate functions for preparing the data- one for time series analysis and one for linear regression modeling.
- All observations with 10 or less beekeepers were dropped because the data for those observations is protected under privacy laws.
- All strings were stripped, lowercased, and spaces were replaced with underscores.
- We engineered two columns: beekeeper_colony_ratio (colonies lost / beekeepers) and colony_net_gain (ending_colonies - starting_colonies).
- We also created dummy variables for the three categories in the season column: winter, summer, and annual.
- Multistate and non_continental data were dropped, and we isolated only observations with beekeepers exclusive to their respective states.
- We converted all numerical columns to integers or floats and the year to datetime format.


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
      Train:  2675.28  
      Validate:  1881.73

    RMSE using Median on 
      Train:  2759.24  
      Validate:  1911.84
      
Since our baseline RMSE using mean is smaller than RMSE using median, we will use RMSE mean for our baseline

We used SelectKbest and Recursive feature Selection to help us identify our most important drivers of colony loss. We picked 4 features.

- Selected features to input into models:
    - features = ['beekeepers_scaled', 'starting_colonies_scaled','ending_colonies_scaled', 'colonies_net_gain_scaled', 'beekeeper_colony_ratio_scaled']

***

### Models and RMSE Values:


- Will run the following regression models:

   OLS, Lasso Lars, Tweedie Regressor, Polynomial Features 

    
#### Model 1: Linear Regression (OLS)


- Model 1 results: 
    RMSE:
      - Train: 1089.66
      - Validate: 882.27


### Model 2 : Lasso Lars Model


- Model 2 results: 
    RMSE:
    - Train: 1089.18
    - Validate: 897.70


### Model 3 : Tweedie Regressor (GLM)

- Model 3 results:
    RMSE:
    - Train: 1674.01
    - Validate: 1950.43


### Model 4: Polynomial Regression Model

- Model 4 results: 
    RMSE:
    - Train: 1018.15
    - Validate: 1281.37


## Selecting the Best Model:

| model  | RMSE_train |RMSE_validate|
|---|--|---|
|Baseline | 2675.28 |   1881.73|
|    OLS Regressor  |1089.66  |  882|
| LASSOLARS(alpha = 1)  |1089.18  |   897.70|
|Tweedie Regressor(power=5, alpha=1)  |1674.01 |  1950.43|
| Polynomial Regression(degree = 2)   |1018.15 |  1281.37|


- The LassoLars model performed well on the train and validate sets, beating baseline RMSE on train by 1586.81 and on validate by 984.03. (The baseline difference between train and validate sets was 1079.37, and the selected model had an RMSE difference of 330.71). The OLS Regressor also performed well, but we decided overall that the Lasso Lars model is the best model for this project.


## Testing the Model
Using LassoLars, we predicted our model on test data.

|RMSE|Value|
|-|-|
|Baseline| 2675.28|
|Train|1089.18|
|Validate |897.70|
|RMSE | 1717.23|

- Model Testing Results

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]
Based on our driving features of Starting Colony, Net gain/loss, and Bee Keeper to Hive Ratio, we're able to say that it appears these features have an impact on the overall number of lost colonies, and colony survivability, as well as our time series data showing a consistent trend of increased loss of colonies during winter. With these features we can recommend an increase in the number of Beekeepers, especially in states with larger numbers of starting colonies (as they appear to have a more commercialized bee keeping operation), as well as taking precautions and mitigation steps during winter to aid in Honey Bee Colony Survival.
- Bee Keeper to Hive Ratio: It would appear that the less colonies a keeper has to tend to the more likely they are to be able to care for their bee health, and more likely to recongnize changes in the behavior of their colonies that could signal an issue or illness within it.
- Winter: Due to the colder weather bees are less likely to venture out for pollen, and instead rely more heavily upon their honey reserves for nutrition for overwintering. Abstaining from Harvesting Honey as they temperatures begin to dip could benefit a colony as it gives them the food stores they require, or even adding a sugar syrup feeder designed for bees if you need to harvest their honey.  Even if you don't have bees, putting out a feeder in your yard or winter blooming flowers can help any bee brave enough to venture out for food. Also, Bees trapped away from the hive when it's cold will sometimes burrow in dead gardens for shelter, so waiting until the thaw to start prepping your garden can greatly benefit any unlucky bee who needs some shelter.

***
###### ReadMe template by: <a href="https://github.com/mdalton87" target="_blank">Mathew Dalton</a>
</p>
