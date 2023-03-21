Tool to detect Financial Fraud 

Current Situation- As it has become easier to get connected to people across the world, we are vulnerable to online frauds, scam, putting our money and hard work in vain. The worst part is that the scammer is always at an advantage to impersonate or conceal his actual identity and status.

>>> Key Outcomes Expected:
Develop a machine learning algorithm that predicts and detects instances of financial fraud and cybercrime in real-time, enabling faster response times and reducing losses.



 The increased accuracy of machine learning algorithms provides financial firms with a significant reduction in the number of false positives (where transactions are incorrectly flagged as declined and fraudulent) and false negatives (where genuine instances of fraud are missed).

 Ho The transaction is Fraudulent
 H1 The transaction is genuine.

 Classification problem:

 Decrease: FP --> (where transactions are incorrectly flagged as declined and fraudulent)\
 Decrease: FN --> ( where the transactions are fraud but detect as not)
 
 Detecting method: 
 ML algorithm  works by comparing every new transaction with the previous (personal information, data, IP address, location, etc) one and detecting suspicious cases. As a result, financial units can prevent fraud related to payment or credit cards.

 Task : Monitoring user behaviour
    user suddenly starts accessing their account from a different location or device.,
    user logging in from multiple locations within short period of time
    Identify patterns that are indicative


    Algo Logistic regression
    Decision trees
    Random Forests
    SVM
    DNN
    
### Software and account Requirement.

1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com/download)
3. [GIT cli](https://git-scm.com/downloads)
4. [GIT Documentation](https://git-scm.com/docs/gittutorial)

downloading dataset
-----------------
chmod 600 ~/.kaggle/kaggle.json




Creating conda environment
```
conda create -p venv python==3.8
BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```



```
python setup.py install
