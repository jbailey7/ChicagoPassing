# Overview

Despite being one of the NFL’s oldest franchises, the Chicago Bears are the only team to never have a quarterback throw for 4,000 yards in a single season. Could there be an external, environmental related reason for this? Or (as might be suggested by fans of the rival Green Bay Packers) have the Bears just had a string of sub-par quarterbacks throughout their existence? 

The main focus of this project will be to study the effect of Soldier Field (where the Bears have played full-time since 1971) and weather on quarterback performance. I will focus on three main questions: 

1. Do temperature, wind, and precipitation impact quarterback performance? 
2. Is quarterback play at Soldier Field systematically different from other outdoor stadiums?
3. Does Soldier Field amplify the effects of poor weather conditions?

### Data

Quarterback performance is measured using EPA per dropback. EPA (Expected Points Added) is a play-by-play metric that estimates how much a given play increases or decreases a team’s expected points based on historical game situations. For example, a three-yard gain on 4th-and-2 is far more valuable than the same gain on 3rd-and-10, and EPA captures this contextual difference.

Defensive strength is also measured using season-level defensive EPA allowed per play. Because opponent quality strongly influences quarterback outcomes, defensive EPA is included as a control variable in every model.

To improve interpretability, continuous predictors such as temperature, wind speed, and defensive EPA are mean-centered.

For more detailed information about the data itself, refer to the README file in the etl/ folder. 

### Modeling

To test these questions, I will use four models. The dependent variable in all models is quarterback EPA per dropback. Models are estimated sequentially to isolate the role of stadium identity and weather.

**Model 1** will act as the baseline model. It will compare how quarterback EPA per dropback is impacted by home field advantage and opponent's defensive EPA. When later models add in weather and Soldier Field factors, we can use this model as a point of reference. 

**Model 2** will add in a Soldier Field indicator. Now we can see if playing at Soldier Field impacts quarterback play (without looking for specific causes of that impact). 

**Model 3** will add in weather. Now I can compare how the temperature, wind, and precipitation are associated with quarterback play, and if Soldier Field still has an impact with these extra factors. 

**Model 4** will add in an interaction between Soldier Field and the weather factors. This will test if Soldier Field amplifies the impact of certain weather conditions on quarterback play. 

Models 3 and 4 will both have two versions. Version one will consider temperature to be a linear variable, while version 2 will consider temperature as a categorical variable to test whether temperature effects are linear. The difference in these variables is explained further in the etl/README file. 