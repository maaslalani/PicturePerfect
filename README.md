# PicturePerfect
Instagram photos reveal predictive markers of depression.

## Description
In a study conducted by a Harvard researcher Andrew G. Reece, it was concluded that there were key indicators of depression that lie within one's Instagram profile.
The computer trained model was able to outperform the average general practitioner whose success rate for diagnonsis was around 42%.

Picture Perfect is a piece of software which
* fetches a user's instagram profile
* downloads all the images from posts
* uses several key indicators of depression from social media to assign a *health score*
* displays the likelihood of that instagram user having depression

## Research
A 34-page research paper was written on how [Instagram photos reveal predictive markers of depression](https://arxiv.org/pdf/1608.03282.pdf).
The researchers include Andrew G. Reece who is part of the Psychology Department at Harvard University.

**Abstract**
Using Instagram data from 166 individuals, we applied machine learning tools to
successfully identify markers of depression. Statistical features were computationally extracted
from 43,950 participant Instagram photos, using color analysis, metadata components, and
algorithmic face detection. Resulting models outperformed general practitioners’ average
diagnostic success rate for depression. These results held even when the analysis was restricted
to posts made before depressed individuals were first diagnosed. Photos posted by depressed
individuals were more likely to be bluer, grayer, and darker. Human ratings of photo attributes
(happy, sad, etc.) were weaker predictors of depression, and were uncorrelated with
computationally­generated features. These findings suggest new avenues for early screening
and detection of mental illness.

## Variables and Criteria 
There were several criteria we considered when constructing the health score, mainly derived from the research paper.

* **Hue, Saturation, Brightness**

Depressed individuals were found to have a more blueish tint in their photos which is quantified through a higher value in hue. Depressed individuals were also more likely to posts photos that did not have a high saturation value nor a high brightness, meaning their photos would be on the darker side with a more blue tone.

* **Comments to Likes ratio**

It was found that depressed individuals were more likely to received more comments on their posts, while simultaneously receiving less likes. To implement this in our program we parse the meta data of the user's posts and found the number of likes and number of comments and created a ratio of `# comments / # likes`. This ratio would indicate a higher likelihood of an individual being depressed if it were closer to one.

* **Facial Detection**

There lies a relationship between the number of people in a photo and a user's mental health. Having an image where there are more people present indicates mental wellbeing. To implement this in our program, we ran each image through a facial recognition software that outputs the number of faces there are in a given image which allowed us to assign a score to the user based on this factor.

* **Number of posts**

A mentally unhealthy individual was found to post more on average and per day than a mentally healthy individual. To implement this, we found the metadata concerning number of posts user had. The higher this number the higher score they were assigned.

* **Caption Analysis**

Future Steps
Lastly, we plan to use sentiment analysis on the caption of each image which can contribute to the health score of the user.

## Usage
To get up and running with this project you need google application credentials and python3.
First clone this project.
```bash
git clone git@github.com:maaslalani/PicturePerfect.git
```

### Getting `Google_Application_Credentials`
[Google Application Credentials](https://console.cloud.google.com/projectselector/apis/credentials)

After you get you secret credentials type the following command, replace the filepath with the path to your secret credentials.
```bash
export GOOGLE_APPLICATION_CREDENTIALS=~/Documents/Projects/Hack-Harvard-2018/PicturePerfect.json
```

### Setting up dependencies
Install `python3` with homebrew
```bash
brew install python3
```

Install dependencies
```bash
pip3 install -r requirements.txt
```

### Running the project
To run the main program use the following command.
```bash
python3 main.py
```
`--help`, `--verbose`, and `--debug` are valid flags.
