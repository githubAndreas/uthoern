# Uthoern

Playlist continuation recommender system.


### Installing

The only required installation step is to install [Anaconda](https://anaconda.org/anaconda/python). Uthoern needs libaries like Pandas or SciKit Learn and there are included in the Anaconda package

### Execution

1. Go into the project
2. Create there a folder named 'model_storage'
3. Open the Anaconda Prompt
4. Navigate into the project folder

**Training**

5. Replace *<Path_to_mpd_folder>* with the path to the Million Playlist Dataset and execute the statement:
```
python3 uthoern.py <Path_to_mpd_folder> 1000
```
6. The Training needs around 30 hours. If you want to see the current state, lock into the utheorn.log file inside the project.

**Prediction**

7. Now enter the following statement. *<Path_to_the_challenge_set_folder>* is the path to the challenge set. The TrainingId looks like *20180627114113583448*. You will find your id in the model_storage folder.

```
python3 uthoern_predict.py <Path_to_the_challenge_set_folder> <TrainingId>
```

This steps needs around 40h

**Prediction**

If the prediction process ist finished, you will find your playlist recommendation in the 'model_storage/TrainingId' folder named *TrainingId_TeamLuebeck__mdp_submission.csv*