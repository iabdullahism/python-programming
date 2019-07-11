{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"Copy of bank1_data.py","version":"0.3.2","provenance":[{"file_id":"1JA96BynWHJ_FYaj_0TPcgk_2EKL7q24F","timestamp":1562775510660}],"collapsed_sections":[]},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"cuGE_h-bcVtR","colab_type":"code","colab":{}},"source":[""],"execution_count":0,"outputs":[]},{"cell_type":"markdown","metadata":{"id":"hLqqqyI7coYN","colab_type":"text"},"source":[""]},{"cell_type":"code","metadata":{"id":"g4uLDWIqdBBD","colab_type":"code","outputId":"614f619a-2cad-41af-bed7-952f7c1c53d8","executionInfo":{"status":"ok","timestamp":1562775175882,"user_tz":-330,"elapsed":2518,"user":{"displayName":"rahul pandit","photoUrl":"https://lh3.googleusercontent.com/-CdAtdDKbGYg/AAAAAAAAAAI/AAAAAAAAAA8/dcxp7PEZsbc/s64/photo.jpg","userId":"16763915785238138489"}},"colab":{"base_uri":"https://localhost:8080/","height":52}},"source":["from google.colab import drive\n","drive.mount('/content/drive')\n","\n","import os\n","os.getcwd()\n","\n","os.chdir('/content/drive/My Drive/deep-learning/day27')\n","\n","import pandas as pd\n","dataset = pd.read_csv(\"Churn_Modelling.csv\")\n","\n","dataset.shape\n"],"execution_count":0,"outputs":[{"output_type":"stream","text":["Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"],"name":"stdout"},{"output_type":"execute_result","data":{"text/plain":["(10000, 14)"]},"metadata":{"tags":[]},"execution_count":1}]},{"cell_type":"code","metadata":{"id":"XZ86zW35dh_9","colab_type":"code","colab":{}},"source":["import numpy as np\n","import matplotlib.pyplot as plt\n","import pandas as pd"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"D7iH54hkt6oH","colab_type":"code","colab":{}},"source":[""],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"HnakZo-cdtDV","colab_type":"code","colab":{}},"source":["dataset.head(5)\n"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"ApKTN5i5bAiF","colab_type":"code","colab":{}},"source":["features = dataset.iloc[:, 3:-1].values\n","labels = dataset.iloc[:, 13].values"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"cYYkC3mgeLYy","colab_type":"code","colab":{}},"source":["\n","from sklearn.preprocessing import LabelEncoder, OneHotEncoder\n","labelencoder_features_1 = LabelEncoder()\n","features[:, 1] = labelencoder_features_1.fit_transform(features[:, 1])\n","\n","labelencoder_features_2 = LabelEncoder()\n","features[:, 2] = labelencoder_features_2.fit_transform(features[:, 2])\n","\n","\n","onehotencoder = OneHotEncoder(categorical_features = [1])\n","features = onehotencoder.fit_transform(features).toarray()\n","\n","features = features[:, 1:] #dummy variable trap\n","\n","features[1]"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"MmokudxwnPAR","colab_type":"code","outputId":"6e605df2-da15-4449-dfd1-26c82bb2214d","executionInfo":{"status":"ok","timestamp":1562775177096,"user_tz":-330,"elapsed":3615,"user":{"displayName":"rahul pandit","photoUrl":"https://lh3.googleusercontent.com/-CdAtdDKbGYg/AAAAAAAAAAI/AAAAAAAAAA8/dcxp7PEZsbc/s64/photo.jpg","userId":"16763915785238138489"}},"colab":{"base_uri":"https://localhost:8080/","height":34}},"source":["labels.shape"],"execution_count":0,"outputs":[{"output_type":"execute_result","data":{"text/plain":["(10000,)"]},"metadata":{"tags":[]},"execution_count":6}]},{"cell_type":"markdown","metadata":{"id":"vVn6MfhueT_8","colab_type":"text"},"source":["\"\"\"we not take onehotencode becuse male and female is 1,0\"\"\""]},{"cell_type":"code","metadata":{"id":"Ga-x7K6YeeUw","colab_type":"code","colab":{}},"source":["from sklearn.model_selection import train_test_split\n","features_train,features_test,labels_train,labels_test=train_test_split(features,labels,random_state=0,test_size=0.2)"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"eQp70OnefLmK","colab_type":"code","outputId":"d829f542-3ae4-4298-e147-d51bfdf4c161","executionInfo":{"status":"ok","timestamp":1562775177118,"user_tz":-330,"elapsed":3604,"user":{"displayName":"rahul pandit","photoUrl":"https://lh3.googleusercontent.com/-CdAtdDKbGYg/AAAAAAAAAAI/AAAAAAAAAA8/dcxp7PEZsbc/s64/photo.jpg","userId":"16763915785238138489"}},"colab":{"base_uri":"https://localhost:8080/","height":34}},"source":["\n","features_train.size"],"execution_count":0,"outputs":[{"output_type":"execute_result","data":{"text/plain":["88000"]},"metadata":{"tags":[]},"execution_count":8}]},{"cell_type":"code","metadata":{"id":"UwW2Vmh-fZVc","colab_type":"code","colab":{}},"source":["from sklearn.preprocessing import StandardScaler\n","sc = StandardScaler()\n","features_train = sc.fit_transform(features_train)\n","features_test = sc.transform(features_test)"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"RmglKgSqg5ex","colab_type":"code","outputId":"52c55531-0506-4812-eb1c-4ddc7e06d3c8","executionInfo":{"status":"ok","timestamp":1562775178818,"user_tz":-330,"elapsed":5272,"user":{"displayName":"rahul pandit","photoUrl":"https://lh3.googleusercontent.com/-CdAtdDKbGYg/AAAAAAAAAAI/AAAAAAAAAA8/dcxp7PEZsbc/s64/photo.jpg","userId":"16763915785238138489"}},"colab":{"base_uri":"https://localhost:8080/","height":34}},"source":["# Importing the Keras libraries and packages\n","import keras\n","from keras.models import Sequential\n","from keras.layers import Dense\n"],"execution_count":0,"outputs":[{"output_type":"stream","text":["Using TensorFlow backend.\n"],"name":"stderr"}]},{"cell_type":"code","metadata":{"id":"26XffhkdhLyQ","colab_type":"code","colab":{}},"source":["classifier = Sequential()\n","\n","features.shape\n"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"tdegba7AhTxb","colab_type":"code","colab":{}},"source":["#adding the first hidden layer\n","classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))\n","#we use no of hidden 2/3 of input feature and plus ouput labels\n","#here unit=6 means 6 nodes in first hidden layer\n"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"DtecfvVAipPO","colab_type":"code","colab":{}},"source":["classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))\n"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"W8WB1nrii5xw","colab_type":"code","colab":{}},"source":["# Adding the output layer\n","classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))\n","\n","# Compiling the ANN"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"l9mvY8-ZjSxb","colab_type":"code","colab":{}},"source":["classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])\n","#adam is lago in descent gradient to perform optimization like soring algo diff\n","classifier.fit(features_train, labels_train, batch_size = 5, epochs = 20)\n"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"lx3gcipKj5LC","colab_type":"code","colab":{}},"source":["\n","labels_pred = classifier.predict(features_test)\n","labels_pred = (labels_pred > 0.5)\n","#label_pred is in % now convert into 1,0 form usinf condition\n"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"DHLOX56ekESo","colab_type":"code","outputId":"3cabf3c2-e767-45bc-e398-e7eeda6b533d","executionInfo":{"status":"ok","timestamp":1562775213941,"user_tz":-330,"elapsed":40355,"user":{"displayName":"rahul pandit","photoUrl":"https://lh3.googleusercontent.com/-CdAtdDKbGYg/AAAAAAAAAAI/AAAAAAAAAA8/dcxp7PEZsbc/s64/photo.jpg","userId":"16763915785238138489"}},"colab":{"base_uri":"https://localhost:8080/","height":34}},"source":["from sklearn.metrics import confusion_matrix,accuracy_score\n","cm=confusion_matrix(labels_pred,labels_test)\n","print(\"accuracy score of model=\",accuracy_score(labels_pred,labels_test))"],"execution_count":0,"outputs":[{"output_type":"stream","text":["accuracy score of model= 0.8465\n"],"name":"stdout"}]},{"cell_type":"markdown","metadata":{"id":"ulFt5u_chPLB","colab_type":"text"},"source":["\"\"\"\n","\n","Q1. (Create a program that fulfills the following specification.)\n","\n","Program Specification\n","\n","Use the prev. ANN model to predict if the customer with the following information will leave the bank: (Churn_Modelling.csv)\n","\n","        Geography: France\n","        Credit Score: 600\n","        Gender: Male\n","        Age: 40 years old\n","        Tenure: 3 years\n","        Balance: $60000\n","        Number of Products: 2\n","        Does this customer have a credit card? Yes\n","        Is this customer an Active Member: Yes?\n","        Estimated Salary: $50000\n","\n","So, should we say goodbye to that customer?\n","\n","\"\"\"\n"]},{"cell_type":"code","metadata":{"id":"ZGN0R3tlmEJT","colab_type":"code","colab":{}},"source":["data=[600,\"France\",\"Male\",40,3,60000,2,1,1,50000]\n","data=np.array([data])\n","\n","data[:,1]=labelencoder_features_1.transform(data[:,1]) \t\n"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"tyZ7vpPc2Voy","colab_type":"code","colab":{}},"source":["data[:,2]=labelencoder_features_2.transform(data[:,2]) \t\n"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"VOcROSs82XJV","colab_type":"code","outputId":"7d1a8672-3b88-4835-936e-b0981b33faed","executionInfo":{"status":"ok","timestamp":1562775368360,"user_tz":-330,"elapsed":3805,"user":{"displayName":"rahul pandit","photoUrl":"https://lh3.googleusercontent.com/-CdAtdDKbGYg/AAAAAAAAAAI/AAAAAAAAAA8/dcxp7PEZsbc/s64/photo.jpg","userId":"16763915785238138489"}},"colab":{"base_uri":"https://localhost:8080/","height":52}},"source":["data = onehotencoder.transform(data).toarray()\n","\n","data=data[:,1:]\n"],"execution_count":0,"outputs":[{"output_type":"execute_result","data":{"text/plain":["array([[0.e+00, 0.e+00, 6.e+02, 1.e+00, 4.e+01, 3.e+00, 6.e+04, 2.e+00,\n","        1.e+00, 1.e+00, 5.e+04]])"]},"metadata":{"tags":[]},"execution_count":27}]},{"cell_type":"code","metadata":{"id":"0blgvho63R_f","colab_type":"code","outputId":"25c667e8-3515-46b3-ad69-f68313488215","executionInfo":{"status":"ok","timestamp":1562775450683,"user_tz":-330,"elapsed":1239,"user":{"displayName":"rahul pandit","photoUrl":"https://lh3.googleusercontent.com/-CdAtdDKbGYg/AAAAAAAAAAI/AAAAAAAAAA8/dcxp7PEZsbc/s64/photo.jpg","userId":"16763915785238138489"}},"colab":{"base_uri":"https://localhost:8080/","height":34}},"source":["pred=classifier.predict(data)\n","print(\"no left because pred=\",pred[0])"],"execution_count":0,"outputs":[{"output_type":"stream","text":["no left because pred= [0.]\n"],"name":"stdout"}]}]}