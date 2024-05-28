# Wine Quality Prediction with AWS SageMaker
By: Leticia Genao
Course: N.U. ANA680

## Overview
This notebook demonstrates building, training, and testing a linear regression model to predict wine quality, using both Docker containers and without them in AWS SageMaker.

## Contents
- `wine_quality_no_docker.ipynb`: Notebook for deployment without using Docker.
- `wine_quality_docker.ipynb`: Notebook for deployment with Docker.
- `Dockerfile`: Docker configuration file.
- `requirements.txt`: Dependencies for the Docker container.

## Dataset Description
Same as described in Part 1.

## Methodology
### Model Building
The model was developed using SageMaker's Jupyter environment, leveraging linear regression algorithms available in Scikit-learn.

### Model Evaluation
Evaluation was based on the same metrics as in Part 1, ensuring consistency across different deployment strategies.

## Results
- Final Test MSE: 0.0182
- Final Test R2 Score: 0.205

## Discussion
The non-container approach in SageMaker simplifies the setup but may limit the control over the computing environment compared to using Docker containers.

## Deployment Overview
Two approaches are illustrated:
1. **Without Docker**: Directly using SageMaker's Jupyter notebooks.
2. - SageMaker Notebook: `wine_quality_no_docker.ipynb`
3. **With Docker**: Utilizing a custom Docker container within SageMaker.
4. - SageMaker Notebook: `wine_quality_ocker.ipynb`

## Troubleshooting Deployment Issues
During the deployment phase, especially with AWS Cloud services, I encountered several errors. Specific issues included problems deploying the Docker container in AWS. The actions taken to troubleshoot included:

* Verifying IAM permissions to ensure the SageMaker role had adequate access to the necessary AWS resources.
* Checking the Docker container logs for errors indicating potential configuration issues.
* Validating the Dockerfile and requirements.txt to ensure all dependencies were correctly specified and compatible.
Despite these efforts, the errors persisted, indicating a deeper issue possibly related to network configurations or compatibility between the container setup and AWS SageMaker. I also still believe I need to revisit the IAM permissions as well as my S3 bucket setup. I will continue to debug and update the deployment process accordingly.

## Conclusion
This project verifies the feasibility of deploying machine learning models directly within cloud environments and highlights the challenges associated with containerization, offering valuable insights into cloud-based model deployment strategies.


## Reference
Cortez, Paulo, Cerdeira,A., Almeida,F., Matos,T., and Reis,J.. (2009). Wine Quality. UCI Machine Learning Repository. https://doi.org/10.24432/C56S3T.