
# Svaasthy-AI Based Patient Health Monitoring System 

# Introduction:

The IoT-based Patient Health Management System is a technology solution that aims to improve the healthcare experience for patients by leveraging the power of the Internet of Things (IoT). The system is designed to record patient temperature, oxygen levels, and diagnoses in a smart and efficient manner. Additionally, the system has its own website portal, which allows patients and healthcare providers to access and manage patient information in real-time

# Material Required
The system comprises of three main components: IoT devices, a cloud-based server, and a website portal.
* Iot devices :- Arduino Uno, Esp32 nodemcu , temperature sensor , pulse oximeter sensors, Rfid Sensor , Touch sensor
* Cloud-Based Server:The cloud-based server is responsible for storing and processing patient data. The server is designed to be highly scalable, allowing it to handle large amounts of data and support a large number of users. Additionally, the server uses advanced algorithms and machine learning techniques to analyze patient data and provide insights that can be used to improve patient care.
* Website Portal:The website portal is the interface through which patients and healthcare providers can access and manage patient information. The portal is designed to be user-friendly and easy to navigate, making it easy for patients and healthcare providers to access the information they need. Additionally, the portal provides real-time access to patient data, allowing healthcare providers to make quick and informed decisions about patient care.

# Scientific Principle Involved
* Data Science: Data science is the study of how to extract insights from data. AI-based health monitoring systems rely heavily on data science techniques to analyze patient data and generate insights.

# Construction And Working
* Hardware Setup: The hardware components required for the system include sensors for measuring the vital signs such as heart rate, blood pressure, and temperature, as well as a NodeMCU board for data transmission.
* Data Collection: The sensor data is collected by the NodeMCU board and transmitted to the Django server through Wi-Fi.
* Data Processing: The Django server processes the data using machine learning algorithms to detect anomalies and predict potential health risks. The server then generates alerts and sends them to the appropriate medical personnel.
* User Interface: The system provides a user-friendly interface for patients to view their health data and receive alerts on their mobile devices or through a web application.
# Advantages
* Early Detection of Health Problems: The AI-based system can detect anomalies in patient data and alert medical personnel, allowing for early detection and treatment of potential health problems.
* Personalized Care: The system can provide personalized care to patients based on their individual health data and medical history, allowing for more targeted treatment plans.
* Improved Efficiency: The system can automate many tasks such as data collection and processing, freeing up medical personnel to focus on more critical tasks.
* Remote Monitoring: The system allows for remote monitoring of patients, reducing the need for hospital visits and improving access to care for patients in remote locations.
* Predictive Analytics: The system can use machine learning algorithms to analyze patient data and predict potential health risks, allowing for proactive interventions and preventive care.
* Cost Savings: The system can reduce healthcare costs by improving efficiency, reducing hospital stays, and preventing expensive medical procedures.

# References
* "Artificial intelligence in healthcare: past, present and future" by N. van Loon et al., Journal of Medical Systems, 2020.
* "A Review of Artificial Intelligence in Healthcare" by S. Mathur et al., Journal of Family Medicine and Primary Care, 2019.
* "Artificial Intelligence in Healthcare: A Comprehensive Review" by S. Shickel et al., Artificial Intelligence in Medicine, 2018.
* "A Comparative Study of Artificial Intelligence Techniques in Healthcare" by R. Chakraborty et al., International Journal of Advanced Computer Science and Applications, 2019.
* "Healthcare data analytics and artificial intelligence: A survey" by V. Tripathi et al., Proceedings of the International Conference on Computing and Communications Technologies, 2018.










# Dashboard

* ![Logo](https://i.ibb.co/s9KN2m9/homescreen.jpg)
# Patient List

* ![Logo](https://i.ibb.co/sywgJjv/1.png)

# Patient Temperature And Data

* ![Logo](https://i.ibb.co/NxwTXtP/2.png)

# IOT DEVICE

* ![Logo](https://i.ibb.co/6X7dXbW/3.png)

# FlowChart
* ![logo](https://i.ibb.co/QMDYw26/image-005.jpg)

## Badges


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)




## Authors

- [@Shashank-shekharr](https://www.github.com/shashank-shekharr)


## Deployment

To deploy this project run

```bash
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py makemigrations
  python manage.py createsuperuser
  python manage.py runserver
```


## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shashank-shekhar-93263b283/)



