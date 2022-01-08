

<p align="center">
  <img src="https://storage.googleapis.com/kaggle-competitions/kaggle/5407/media/housesbanner.png" alt="Sublime's custom image"/>
</p>

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
![GitHub last commit](https://img.shields.io/badge/last%20commit-Dec--2021-blue)
![GitHub issues](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)
![GitHub](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)


# Washington House Price Estimator - (Web App)

Python Web Interface application that predicts price of Real Estate Property in Washington, USA. The Backend application Results estimate price of property with estimated location on map.

### Use Cases

- Interface helps user to modulate the housing requirement to alter the real Estate Budget.
- Budgeting based on user requirement.


## Model Deployment Structure

<p align="center">
  <img src="https://github.com/DSPOWER93/artifacts/blob/main/Model_Infrastructure.png" alt="Sublime's custom image"/>
</p>


## Model Visuals

### Landing Page

The user access [web interface](http://ec2-44-192-101-120.compute-1.amazonaws.com/) and enter its requirement regarding the real estate property.

<p align="center">
  <img src="https://github.com/DSPOWER93/artifacts/blob/main/Screenshot%20from%202022-01-04%2023-12-04.png" alt="Sublime's custom image"/>
</p>


### WebApp Results

Based on user inputs the application predicts Estimated price of property with location on map.

<p align="center">
  <img src="https://github.com/DSPOWER93/artifacts/blob/main/Screenshot%20from%202022-01-04%2023-13-08.png" alt="Sublime's custom image"/>
</p>


## Localhost Deployment

To reproduce API on Localhost using rest API Flask, following code to be ran on bash: 

**Creating Virtual Environment**
```bash
$virtualenv virtualenv_name
$virtualenv -p /usr/bin/python3.8 virtualenv_name
$source virtualenv_name/bin/activate
```
**Model Deployment**
```bash
(virtualenv_name)$git clone https://github.com/DSPOWER93/Washington-house-price.git
(virtualenv_name)$pip install -r requirements.txt
(virtualenv_name)$python3 app.py
```
Model Inferencing would result same at localhost, Invoke Url would local host link generated by Flask Rest API.

## FAQs

### **Why EC2 Instance is selected for model Deployment?**<br/>

➤➤**User Control:** EC2 is an easily managable infrastructure for ML Deployment which is billed on demand basis.<br/>
➤➤**Flexibility:** It gives flexibility to choose and pay for computing power based on user requirement.<br/>
➤➤**Response time:** EC2 servers have minimal response timings as servers are already spinning around the time.<br/> 
➤➤**Load Balancing:** EC2 Instance are good at handling lutiple request in parallel.  If Model is deployed on Serverless Instance like AWS Lambda, it becomes challenging to deal with high number of request as request is processed in serialized manner instead of parallel.<br/>

### **Upgrade points of application?**<br />

Based on changes price upgrade in real estate market, model weights would required to be fine tuned accordingly with updated data. If Model performance degrades over time, it'd required to be hypertuned with different parameters or re-trained again.

### Web app infrastructure Limitations?

**MLops not designed on model:** As nature of data is very dynamic. It's a necessary to upgrade model weights over time, as static model weights would degrade over period.
 
 ## About me

I am Mohammed working as Sr. Business Analyst @ Affine.ai. I am presently working gaming Industry, delivering end to end Machine Learning projects based on clients requirement. 
Github profile:
[![Mohammed](https://img.shields.io/badge/Github-white?style=flat&logo=github&labelColor=black)](https://github.com/DSPOWER93/)


#### 👀 We can connect on <br/>
[![Mohammed](https://img.shields.io/badge/Linkedin-blue?style=flat&logo=Linkedin&labelColor=blue)](https://www.linkedin.com/in/mohammed-taher-13934a51/)
[![Mohammed](https://img.shields.io/badge/Gmail-white?style=flat&logo=gmail&labelColor=white)](mailto:md786.52@gmail.com)
[![Mohammed](https://img.shields.io/badge/Instagram-white?style=flat&logo=Instagram&labelColor=white)](https://www.instagram.com/mdboy93/)
