# 3550_Exam_2_Applied

Starting Repository for Exam #2

## Overview

For this, you'll need to complete some code to pass a few tests. Overall, you're making a class that represents an NBA player, as defined by a CSV of stats for each NBA player. Knowing about the NBA is not necessary or helpful, there are some numbers, and we need to do some manipulation with them. You'll ultimately need to generate some statistics for each player based on the data, implement some functionality for the class, and eventually create a fake game that allows us to run a simulation that compares two players, based on the excitement found in stats.

In completing this, you'll need to fill in the missing code, and add anything like other methods as needed (you may need/want some). The existing tests will call the methods in your code to try to use them, so that is the verification that you can work against. It will likely be easier for you to add some other diagnostics - print, log, debug, and/or tests to help as you develop - don't just rely on a test.

## What do I Need to do?

There are a few portions of code that you need to complete to make things work, but you'll probably want to add some other bits as well. I'd recommend starting at the beginning - can you make the object, and can you read from the data 'into' the object. Once that works, start targeting different bits of functionality one at a time. 

<ol>
    <li> Complete the NBA Player class. This will represent one player per object, and one row of data from the CSV. </li>
    <li> Add functionality - there are both instance and static things needed in the code. </li>
    <li> Create other stuff - as long as things work, you can add as you need. So if you need a different function, go for it. </li>
</ol>

The calculations that you need are as follows:

True Shooting Percentage (TS%) = PTS / (2 * (FGA + (0.44 * FTA)))

Effective Field Goal Percentage (eFG%) = (FGM + (0.5 * 3PM)) / FGA

Some important points to keep in mind:

<ul>
    <li> You do NOT need to know anything about basketball, at all, it won't help. The numbers are just measurements, and the calculations are just math. </li>
    <li> There are several ways to do things, other than what is requested, you can do as you please. Some parts are not specified, those are open to interpretation as long as things work. </li>
    <li> The logic of the different parts - the object, the loading of data, the calculations, etc... - can largely be done separately with dummy data, then combined. For example, this means that you could build the object to do __lt___, allowing things to be sorted, based on some placeholder value, like PTS. Then when you figure out the calculation stuff, just replace the PTS with the actual value and you're good. The two parts of code need each other to ultimately work towards our goal, but we can separate them to make things more simple to create them. </li>
    <li> The parts that are specified to be static should work that way, the other stuff should belong to an instance. </li>
    <li> Particularly for the last bit, if the premise/goal of what I have there isn't clear, please ask. </li>
</ul>

## Grading

The grades for the applied bits will be based on the test results that run in GitHub. The exception is that if your code doesn't run or makes mistakes, I'll look at it manually and try to adjudicate the scale of the mistake. 

## But it Doesn't Work!

The first exam notably had a mistake in the test script, which was my fault. I reused a variable name by not being careful copy/pasting, for the sole reason of giving you all a vivid lesson in how not following good practices in code style/design/readability can come back to hurt you! In general, on a test, please assume that the intent is whatever the question asks, and if something downstream of that fails, it is likely a mistake in the test. If there's something like this I will need to resolve the error in your favor, marks wise, so please don't worry about that part. If I make a mistake, or if you all do something that I didn't really expect and that causes odd results, I'll resolve it in a way that is as materially fair as possible - work on the default assumption that what was asked for is what was intended. For things like 'there is an incorrect answer' on a test script, that's a pretty simple change to do after the fact.