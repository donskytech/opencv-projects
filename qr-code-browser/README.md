# dream-team-thesis

Thesis project

## Prerequisites

1. Install Python  
   https://www.donskytech.com/how-to-install-python-in-windows/
2. Install git bash. Choose Windows  
   https://git-scm.com/downloads
3. Install Visual Studio Code. Choose Windows System Installer x64  
   https://code.visualstudio.com/download

## Installation Procedures

1.  Open git bash  
    ![git bash](https://github.com/Jaressa/dream-team-thesis/assets/69466026/87fd9fce-c806-47c1-a066-ec8360e3bffc)

2.  Execute below command  
    `mkdir -p /c/git-repo`
3.  Next  
    `cd /c/git-repo`
4.  Clone the repository  
    `git clone https://github.com/Jaressa/dream-team-thesis.git`
5.  Change directory by executing below command
    `cd dream-team-thesis`
6.  Open the project in Visual Studio Code  
    `code .`
7.  When the Visual Studio Code opens then open a new Terminal by going to menu View -> Terminal

![VSCode Terminal](https://github.com/Jaressa/dream-team-thesis/assets/69466026/4f2a7113-5ed9-4c4a-87e4-31225511a45b)

8.  Create a virtual environment by typing below command on the terminal. Click YES when a prompt comes out.

`python -m venv .venv`

![python virtual environment](https://github.com/Jaressa/dream-team-thesis/assets/69466026/96754ab5-1102-4436-81bc-b18c90b20da4)

8. Activate the virtual environment by executing below command

`.venv\Scripts\activate`

You should see the following
![virtual environment](https://github.com/Jaressa/dream-team-thesis/assets/69466026/7f587e63-7772-4fc6-a4fb-29cb7a559472)

9. Install the project dependencies using the below command

`pip install -r requirements.txt`

If everything goes well then you should see the following information
![pip install](https://github.com/Jaressa/dream-team-thesis/assets/69466026/81aeb3be-698b-4788-81a5-08ec76bbe9e4)

10. Run your server by executing the below command

`flask run --host=0.0.0.0`
![Run flask server](https://github.com/Jaressa/dream-team-thesis/assets/69466026/88902b97-c6df-4a5e-bbc2-703523b14b95)

11. Open your Chrome browser and type the IP that is assigned to you by your network above.

For example my url

![Sample Application](https://github.com/Jaressa/dream-team-thesis/assets/69466026/48cc93be-bb4a-4762-ad3f-a4904953a6bc)

## Sample QR Code

Sample QR code is in the sample folder
