# FreeLunch
## About Us
FreeLunch is an academically oriented online magazine that hosts editorials on pertinent issues in the fields of Economics & Finanace, Science and Technology and World Affairs, contributed primarily by college students.

This is the code repository for a new website design for http://www.freelunch.co.in/
The website is built on Django framework with HTML5, CSS3, JS, Jquery and AJAX. It is currently under developement.

## Development Team
* Abhishek Gaur - [abhishekspeer](https://github.com/abhishekspeer)
* Indraneel Ghosh - [ighosh98](https://github.com/ighosh98)
* Akshay Mittal - [Ak-shay](https://github.com/Ak-shay)
* Himanshu Agarwal - [HimanshuAgarwal022](https://github.com/HimanshuAgarwal022)
* Saransh Jindal - [UnlaxedNeurotic](https://github.com/UnlaxedNeurotic)


## Contact us
Email: [**freelunch@freelunch.co.in**](mailto:freelunch@freelunch.co.in)

## Contributing to the project
If you are interested in contributing to the repository please go through the [contribution guidlines](CONTRIBUTING.md) **carefully**

### Installation
You can work on the project by cloning the repository to your local system. The url for the repository is https://github.com/BITS-Periodical-Society/freelunch.git
1. Make sure that you have git installed on your system
    * To check if you have git installed, type `git` in your command line. If you see a help menu for git, you are good to go.
    * To install git and understand how to use it briefly, you can use [this](https://www.computerhope.com/issues/ch001927.htm) resource. For a more complete and in-depth understanding, use [this](https://git-scm.com/book).
2. Create a local copy of the repository `git clone https://github.com/BITS-Periodical-Society/freelunch.git`
3. Create a virtual environment for the project <br />
`virtualenv venv`\
`source venv/bin/activate`
4. Install the necessary dependencies for the project - `pip install -r requirements.txt`
5. Now you may make changes to the project and create pull requests on github to have your changes merged in strict accordance with the [contribution guidlines](CONTRIBUTING>md)
6. Running the website
    * To run the website, go to the project directory `cd freelunch`
    * To run the local server `python manage.py runserver`

### Creating Fake data
We use the `Faker` library for creating data. Checkout the [repo](https://github.com/joke2k/faker) and [official documentation](https://faker.readthedocs.io/en/master/).
1. First create the database for the website\
`python manage.py makemigrations`\
`python manage.py migrate`
2. To create fake data, run the `populate_site.py` script\
`python populate_site.py`
3. Follow instructions as they come up
4. Check issue #157 for more info.
