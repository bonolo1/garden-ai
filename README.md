# Garden AI

## Table of Contents

1. [Project Description](#project_description)
2. [Installation](#installation) 
3. [Usage](#usage)
4. [Credit and Contribution](#credit_and_contribution)
5. [License](#license)

## Project Description <a name="project_description"><a>
The purpose of this AI program is to review sentences (namely garden-path sentences), use Natural Language Processing (NLP) to analyse them and display the attributes of these sentences.

## Installation <a name="installation"><a> 

There are two different ways to run the application: using Docker or a virtual environment.

### Docker

You can either use docker on your desktop or by using Docker Playground. Descriptions for using both options are included.

**Run container using Desktop**

1. If don't already have Docker installed on your desktop, install Docker on your desktop.

2. Once installed, enter the following command in the terminal:

```
docker run bonolor/garden-ai
```

**Run container using Docker Playground**

1. Go to Docker Playground at the following link and enter "Start": https://labs.play-with-docker.com/.

2. Add a new instance.
  
3. Enter the following command in the terminal:

```
docker run bonolor/garden-ai
```

### Virtual Environment

1. Download the following files in the repository: garden.py and requirements.txt

2. Create a project folder named "garden_ai".
 
3. Move and save the downloaded files to the garden_ai folder.
  
4. Open your local Integrated Development Environment (IDE) such as VSCode.
 
5. Add the garden_ai folder to your IDE.
 
6. In the same parent directory, create a virtual environment named .venv by entering the following command in the terminal (use relevant python version):
   
  ```
  python3.11 -m venv .venv
  ```
  
7. Activate the virtual environment using the following command (for macOS):
  
  ```
  source .venv/bin/activate
  ```
  
8. Once the virtual environment is created and activated, enter the following command to move into the garden_ai directory (if you are not already in the directory):
  
  ```
  cd garden_ai
  ```
 
9. Run the requirements.txt file to install all the relevant packages:
  
  ```
  pip install -r requirements.txt
  ```
  
10. If prompted to upgrade pip, enter:

   ```
  pip install --upgrade pip
  ```

11. Run the program.

## Usage <a name="usage"><a>

These the garden sentences selected to be analysed by the program:

<img width="772" alt="Screenshot 2023-05-04 at 10 51 36" src="https://user-images.githubusercontent.com/127111801/236156917-daf51da6-05b6-4fb0-a143-82a99163924e.png">

The following is a breakdown of the NLP attributes of each of the sentences in the format of **token-named entitity - named entity type** where the program indicates where there is no named entity:

<img width="772" alt="Screenshot 2023-05-04 at 10 52 26" src="https://user-images.githubusercontent.com/127111801/236161916-3bac43f0-5b89-4ef3-870d-5bf4ae41fcc4.png">

The program also displays an explanation of selected named entities:

<img width="771" alt="Screenshot 2023-05-04 at 11 10 21" src="https://user-images.githubusercontent.com/127111801/236161864-06b86085-5bef-4305-9291-3494a34392c2.png">

## Credit and Contribution <a name="credit_and_contribution"><a> 

This project has been developed by Bonolo Ramasedi.

## License <a name="license"><a> 
  
This project is not licensed and is intended for display purposes only. All rights reserved. No usage, distribution, or modification rights are granted.

