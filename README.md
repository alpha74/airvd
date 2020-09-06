# Airvd
### Basic CRUD REST demo using Django REST Framework.


### Used:
- Python
    - Django
    - Django REST Framework
    - SQLite

-----

### Run:
- Create `virtualenv` using `requirements.txt`
- Run `python manage.py runserver` in commandline. By default, server runs on port `5000`.

-----

### Models:

#### Device
- An IoT device with properties:
    - `uid` : unique id of device
    - `name` : name of device

- A device measures humidity and temperature:
    - `HumidityReading` : one-to-many
    - `TemperatureReading` : one-to-many
    
### HumidityReading
- `device` : owner device
- `humidity` : reading
- `timestamp` : timestamp when reading was stored in db


### TemperatureReading
- `device` : owner device
- `temperature` : reading
- `timestamp` : timestamp when reading was stored in db

-----


### APIs

#### API to create a device
- Endpoint: `POST /api/devices/`
- Content-Type: `application/json`
- Request Payload
    - `uid`
    - `name`


#### API to delete a device
- Endpoint: `DELETE /api/devices/{device-uid}`
    - `device-uid` : uid of device to be deleted
    

#### API to retrieve a device
- Endpoint: `GET /api/devices/{device-uid}`
    - `device-uid` : uid of device
    
    
#### API to list all devices
- Endpoint: `GET /api/devices/`
- Response: `json`


### API to return readings for a device in given period
- Endpoint: `GET /api/devices/{device-uid}/readings/{parameter}/?start_on=yyyy-mmddTHH:MM:SS&end_on=yyyy-mm-ddTHH:MM:SS`
    - `device-uid` : uid of device
    - `parameter` : **temperature** or **humidity**
    - `start_on` and `end_on` :  query parameters which are compulsary and should be used to filter the result to only include data between `start_on` and `end_on`.
        - `yyyy-mm-ddTHH:MM:SS` : year-monthdateThour:minute:second
        
- Response: `json`

-----

#### Commit History Graph
![commit_history](https://github.com/alpha74/airvd/blob/master/FORREADME/img/commit_history.png)
