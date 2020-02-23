# Just Caption This

![MLH tested us... and we won!](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/946/891/datas/original.jpg)

![GIFS](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/946/925/datas/original.gif)

## Inspiration

Most of the content on social media is displayed on images. Unfortunately not everybody is able to see and therefore enjoy the content that is published. Nowadays there are several screen reading solutions that allow vision-impaired individuals to listen to what is written on the web. But what about **images**?

We felt it was for the benefit of those individuals to create a real-time solution that allowed them to know what the image in question is about, without depending on someone else to describe it for them, increasing their independence, helping them to see. 

## What it does

When our twitter bot (@JustCaptionThis) is mentioned in a publication, or a thread containing an image, it will post a reply with a written description of the image. In addition to describing the objects present in the image, the tool can also recognize when there is text present and read the text out of the image into a format that is more accessible for the visually impaired.

## How we built it

We first created a Twitter profile and an app to automate the whole process.

We used Twitter's Streaming API through the Tweepy library to get a real-time feed of new tweets that mention our profile (@JustCaptionThis). We identified whether those tweets had an image, or were a response to a tweet with an image, part of a longer thread.

Using Machine Learning the image is processed and a description is generated.

That description is then posted as a response to the tweet that mentioned us (@JustCaptionThis).

## Challenges we ran into

Creating and giving permission to the Twitter app to the Twitter profile @JustCaptionThis.

Identifying the image that the user requesting a caption is referring to.

Integrating the Neural Network into the python code controlling the twitter action.

## Accomplishments that we're proud of

Creating something useful for people with impaired vision, we like to thinl we have been able to improve someone's life.

Working with the Twitter API and getting a bot to worksuccessfully. One of our hackers didn't even have a twitter account!

Combining Machine Learning with Social Media.

## What's next for Just Caption This

Train the neural network model on Twitter data and keep it up to date with advancements in image recognition!
