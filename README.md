# AssicurAssistance

Insurance policy management program

The program allows the creation of a customer profile with their vehicles and respective insurance policies. It is possible to create brokers and companies to manage the distribution of insurance policies. The program will keep track of policy expiry dates, which can be either semi-annual or annual, and will notify insurers (who will have their own account to input personal information) via a GUI on the application's homepage using push notifications. Additionally, customers will be notified via email and SMS if they have consented to notifications at the time of profile creation.



## Use and functionality

BROKERS AND INSURANCE COMPANIES\
The web application is designed to archive and manage insurance policies. When creating a new policy, it's essential to associate it with an insurance company, which is managed by a broker. A broker can oversee multiple insurance companies.

CREATING A NEW INSURANCE POLICY\
Once the relevant company is established, users can proceed to create a policy linked to a specific customer. Alongside customer details, the policy includes information about the vehicle to be insured, which is stored within the customer's "garage" section. To streamline the process and enhance user experience, users can directly navigate to "Customers" -> "Create new customer" after setting up the broker and the company. This seamless transition to the customer creation page guides users through the policy issuance process.

SCRIPT.PY\
The system includes a Daemon script.py responsible for managing the delivery of frontend notifications to alert insurers about policy expirations. Additionally, it handles the removal of policies expired for more than 3 months. Upon policy expiration, the system triggers both email notifications (coming soon) and SMS alerts via an external API to notify customers.


## Software info
Server: Unix sistem (actually run on Ubuntu Server)\
Back-end: python 3.11.4 Django Rest Framework\
Front-end : Vue Framework


## Installation

## Backend
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install environment.


Create a virtual environment

```bash
pip install virtualenv 
```


```bash
virtualenv myenv 
```


```bash
source myenv/bin/activate 
```

install all necessary packages

```bash
(myenv) cd AssicurAssistance 
```

```bash
(myenv) pip install -r requirements.txt 
```

Make database migrations 

```bash
cd src/
(myenv) python3 manage.py makamigrations 
```

Migrate Database

```bash
(myenv) python3 manage.py migrate 
```

Run Django Server

```bash
(myenv) python3 manage.py runserver 
```

Run Django Notification service (optional)

```bash
docker run -p 6379:6379 -d redis:5
(myenv) python3 manage.py runscript script 
```

## Front-end

```bash
cd AssicurAssistance
cd src/vite-project/ 
```


Install all packages

```bash
npm install
```

set the variables you are interested in in the config.js file 

create project's build

 ```bash
npm run build
```

Run server
```bash
node server.js
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)
