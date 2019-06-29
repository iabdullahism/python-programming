the knn algo much better to the logistic regression because 
in knn algo use distance of every point and not make liner boundry 
but the main issu eis that 
1.logistic regression draw the line at training time
but the 
2.knn predict when the data is given and find the nearest distance



#when the data is diff in ranges 
p             q    r
20000         1    .9
so we use (x-mean)/std    it is calld normalizitin data


#
when we alreday do feature_train using standerd scale in fit_transform
then now if we want to scale feature_test then direct call transform method because the
fit_transform save all the mean and std of every column so you can directly use it


#
probabiltiy column tells what is my actual data in what is prediction
actual data  prediction data

for remove these techniqe use confusion matrix
