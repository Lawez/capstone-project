# EXERCISE INTENSITY RECOMMENDATION SYSTEM

![image.jpg](https://github.com/Lawez/capstone-project/blob/main/image.jpg)

## Business understanding
#### Problem statement
Develop a recommender system for exercise intensity that provides personalized recommendations on appropriate workout intensities based on individual characteristics, including age, gender, BMI, exercise duration, heart rate, calories burned, weather conditions, and desired weight goals. The goal is to guide individuals in selecting exercise intensities that optimize their fitness outcomes, taking into account their specific attributes and preferences.
#### Business context
In today's thriving fitness and wellness industry, the development of a recommender system for exercise intensity presents valuable business opportunities. Fitness centers, gyms, and personal trainers can leverage this system to offer tailored workout programs that align with individual goals, preferences, and fitness levels, ultimately attracting and retaining members. Wellness apps and platforms can integrate the recommender system to deliver personalized exercise recommendations, enhancing the user experience and setting them apart from competitors. Healthcare providers can utilize the system to promote physical activity as a means of disease prevention and management, while corporate wellness programs can leverage it to support employee well-being and productivity. By incorporating an exercise intensity recommender system, businesses can optimize workout effectiveness, increase customer satisfaction, and differentiate their offerings in a competitive market.

#### Objectives
Overall Objective: Develop a Recommender System for Personalized Exercise Intensity

1. To personalize exercise intensity recommendations. Build a recommendation system based on individual characteristics such as age, gender, body mass index (BMI), exercise duration, heart rate, calories burned, weather conditions, and desired weight goals.
2. Develop a model that can predict the optimal exercise intensity for a given individual. 
3. Identify the factors that contribute to optimal exercise intensity.
4. To develop a recommender system that can dynamically adjust exercise intensity recommendations based on changing weather conditions. The system should consider the impact of different weather conditions on workout performance and suggest appropriate exercise intensities accordingly

## Project Steps
1. **Business/Data Understanding**: Conducted a comprehensive understanding of the business requirements and identified the relevant data needed for developing the exercise intensity recommendation system.
2. **Data Preparation**: Performed data cleaning and preprocessing steps, including handling missing values, removing outliers, and transforming necessary variables.
3. **Feature Engineering**: Engineered new features to enhance the predictive power of the models.
4. **Exploratory Data Analysis (EDA)**: Conducted exploratory data analysis to gain insights into the data, visualize relationships between variables, and identify patterns and trends.
5. **Modeling and Evaluation**: Used models to predict exercise intensity based on individual characteristics and other features. Utilized RMSE (Root Mean Squared Error) as the evaluation metric to assess the performance of the models.
6. **Integration**: Integrated the trained models into the web app and mobile app, allowing users to receive real-time exercise intensity recommendations based on their input.
7. **Documentation and Write-up**: Documented the project details, including the project steps, descriptions of the models used, evaluation results, and many interesting findings as well as insights obtained throughout the project.

## Required Dependencies
* pandas
* numpy
* matplotlib
* Scikit-learn
* seaborn
### Loading Data
* df1 = pd.read_csv('exercise_datasett.csv')
### cleaning data
* cleaned(df1)

## Visualizations
![image](https://github.com/Lawez/capstone-project/assets/124572155/23bee446-71e2-4481-b597-77b14789e3c2)

![image](https://github.com/Lawez/capstone-project/assets/124572155/8a292d51-a303-496a-ae03-d67f8cd0cbab)

![image](https://github.com/Lawez/capstone-project/assets/124572155/c421d9aa-1ba8-467a-944e-61d33d4763c3)

![image](https://github.com/Lawez/capstone-project/assets/124572155/7743a1b5-101d-4548-ba11-deef8b4aba3d)


## Model Selection and Performance
The project involved evaluating multiple machine learning models for predicting exercise intensity based on individual characteristics. The following models were tested, and their RMSE values were calculated:

| Model                     | RMSE  |
|---------------------------|-------|
| Logistic Regression       | 3.83  |
| XGBoost Regressor         | 2.92  |
| Random Forest Regressor   | 2.89  |
| K-Nearest Neighbors (KNN) | 3.14  |
| Tuned Random Forest       | 2.86  |
 
Based on the performance results, it was decided to further tune and optimize the Random Forest Regressor model, as it had the lowest RMSE among the tested models. After the tuning process, the Random Forest Regressor achieved an improved RMSE of 2.86.

## Conclusion
* The model can be utilized to provide personalized exercise intensity recommendations to individuals based on their characteristics, including age, gender, BMI, exercise duration, heart rate, calories burned, weather conditions, and desired weight goals. Users can input their information into the system, and the model will generate tailored recommendations to optimize their workout effectiveness.
* Integrate the exercise intensity recommendation system into wellness apps and platforms to deliver personalized exercise guidance to users. The system can enhance the user experience by providing customized workout plans and real-time intensity recommendations based on the individual's characteristics and preferences.
*  By providing personalized exercise guidance, the system can help employees maintain a healthy lifestyle, manage stress, and improve productivity.
*  The system can assist healthcare professionals in prescribing appropriate exercise intensities for individuals with specific health conditions or goals.

## Installation and Usage
1. Clone the repository: https://github.com/Lawez/capstone-project.git 
2. Install the required dependencies
3. Start the web app
4. Access the web app in your browser 

# Acknowledgement and Contributors
We extend our heartfelt appreciation to the Moringa School community, particularly the technical mentors, for their exceptional guidance and unwavering support during the project. Their expertise and constant assistance have been pivotal in the development of the exercise intensity recommendation system. We are profoundly grateful for their commitment to fostering a collaborative learning environment, which has played a crucial role in our accomplishments.

Special thanks to the team that made this project possible.
* amos.kipkirui@student.moringaschool.com
* ian.tulienge@student.moringaschool.com
* lavender.echessa@student.moringaschool.com
* kelvin.muriuki@student.moringaschool.com
* susan.warigia@student.moringaschool.com
* eston.kamau@student.moringaschool.com

## Repository Structure

```
├── data/                      <- Directory containing datasets used in the study
├── images/                    <- Folder for storing images related to the project
├── presentation.pdf           <- PDF document containing the project presentation
├── .canvas                    <- File extension specific to the Canvas platform
├── .gitignore                 <- File specifying patterns to be ignored by Git
├── CONTRIBUTING               <- Directory containing logs and guidelines for contributions
├── LICENSE.md                 <- File containing the project's license information
├── README.md                  <- Top-level README providing an overview of the project
└── student.ipynb              <- Jupyter Notebook documenting the analysis and findings

```



