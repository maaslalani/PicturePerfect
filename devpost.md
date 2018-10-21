# Inspiration
In a study conducted by a Harvard researcher Andrew G. Reece, it was concluded that there were key indicators of depression that lie within one's Instagram profile.
The computer trained model was able to outperform the average general practitioner whose success rate for diagnonsis was around 42%.
As mental health concerns are increasing and the amount of data posted on social media being more and more accessible, we set out to detect early signs of depression more accurately than a general physician using image processing, facial recognition, and sentimental analysis.

# What it does
Picture Perfect is a piece of software which
* fetches a user's instagram profile
* downloads all the images from posts
* uses several key indicators of depression from social media to assign a *health score*
* displays the likelihood of that instagram user having depression

# How we built it
We used an instagram scraper to fetch a user's instagram posts. Then, using python opencv for facial recognition, simple json parsers to retrieve number of comments and likes on each photo, and google cloud to retrieve colour values of the image.

# Challenges we ran into
We ran into several challenges especially with deciding which values to use and how to use them by basing them off the research paper this hack was inspired by.

# Accomplishments that we're proud of
We are proud of the fact that our software can potentially be usede to tackle a large human issue, which is what we believe technology should be used for.

# What we learned
We learned quite a bit after reading a 34 page research paper on this subject. It was very inspiring to see the applications of technology and then to actually implement it. We feel like we now have built a system to apply our skills to other problems.
