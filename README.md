# TicketPrediction
How likely are you to be given a citation at a traffic stop? Prediction using spark

# Purpose
For 84.51's AI-focused hackathon, me and a friend decided to build a model that would attempt to predict the likelihood that you would receive a ticket/ citation when being pulled over for a traffic stop. This was based off of data given via the [Cincinnati Open Data Portal](https://data.cincinnati-oh.gov/Safer-Streets/Traffic-Stops-drivers/hibq-hbnj) and included features such as car type, stop location, driver age, sex, race among several other aspects.

In addition to building this model, this project also served as an opportunity to learn about the tech stack for big data applications. As we were both new to this field, we also saw this project as an opportunity to learn about various technologies such as Spark, Scala, and Zeppelin.

# Key Components
* Traffic_Stops_Drivers.csv : The set of all data used for this project
* Notebook/TicketPrediction.json : The code for this project exported from a Zeppelin notebook

# Prerequisites
* Should have Java 1.8 installed (Zeppelin and Scala require this)

# Local Setup (Install, Config, Running)
## Installation
* Install Zeppelin (link)[https://zeppelin.apache.org/docs/0.7.0/install/install.html#installation]

## Running
* At the install location, X, run X/bin/zeppelin.cmd (Windows-specific). This should launch Zeppelin as a local Web IDE on port 8080
* Open up Zeppelin on localhost via any web-browser, select 'Import note' from the home page, and then import the Notebook in this project under Notebook/TicketPrediction.json
* You can now run the whole notebook or individual paragraphs using the Zeppelin IDE

