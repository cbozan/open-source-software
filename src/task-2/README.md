## REST API Service
This is a REST API service built with flask
<br />

### Endpoints
  ```
  api.add_resource(DefaultParameters, "/default_parameters")
  api.add_resource(Trends, "/trends")
  ```
  <br />
  
  
## GET PARAMETERS
  ```
  http://127.0.0.1:5000/default_parameters
  ```
  ![GET](https://user-images.githubusercontent.com/71611710/199793479-e94f9621-85cf-4057-91b0-cca12c6c9218.png)
  
  <br />
  
  
## POST PARAMETERS
  ```
  http://127.0.0.1:5000/default_parameters?hl=en-US&pn=united_states&tz=360
  ```
  ![POST](https://user-images.githubusercontent.com/71611710/199794369-97732c9a-25c3-4b24-8721-d3e26754f163.png)
  
  <br />
  
  
## GET TRENDS
  ```
  http://127.0.0.1:5000/trends
  ```
  ![Screenshot 4](https://user-images.githubusercontent.com/71611710/199795770-c7e72f34-9b3b-4d39-bd5b-b13383a52716.png)
  
  <br />
  
