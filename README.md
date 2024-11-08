# ***Setup Guide for Your Offline Local AI That Knows You***
## Introduction

This Python CLI (Command Line Interface) application is designed to allow users to interact with the LLaMA (Large Language Model Meta AI) 3.2 model through a simple command-line interface. The application enables users to generate responses based on a personalized prompt, leveraging their background information to provide tailored responses.

How It Works

  User Prompt: The application prompts the user to provide their background information.
  LLaMA Model Interaction: Using the Ollama framework, the application sends the user's prompt to the LLaMA model.
  Response Generation: The model generates a response based on the input prompt and returns it to the user.

By following this guide, you'll set up everything you need to run the application successfully.


If you already have python and Ollama installed then skip to step 4

Before you start, ensure you have the following installed on your system:

  Python 3.8 or higher: Download from python.org.
  Pip: Package installer for Python (usually comes with Python installations).

## Step 1: Install Ollama

Ollama is the framework that allows you to interact with LLaMA. Follow these steps to install it:

  Open your terminal (Command Prompt, PowerShell, or Terminal).

  Run the following command to install Ollama:


    curl -sSfL https://ollama.com/download.sh | sh

  This command will download and install Ollama on your system.

  
  Or download it from the webiste:

  Link: https://ollama.com/

  Run the app and then open CMD and type ollama to see commands



## Step 2: Get the LLaMA 3.2 Model

Once Ollama is installed, you can download the LLaMA 3.2 model by running the following command in your terminal:


ollama pull llama3.2

This command will fetch the model and make it available for use in your application.

## Step 3: Clone the Python CLI Application

  Navigate to the directory where you want to save the Python CLI application.

  Clone the repository (or simply download the .py file if you are sharing it directly):

    git clone https://github.com/MegaMegaBite/Personal-Offline-AI-Assistant.git
    
  Or just download the Personal_Llama.py file, just make sure it is saved in your desired directory.

## Step 4: Create a Personal Prompt

Before running the application, you need to create a personalized prompt. You can use ChatGPT to help with this. Here’s how to create a prompt:

Open ChatGPT and ask it to generate a personal prompt based on your background and interests and how you want it to behave. For example, you can say:

"Create a personalized prompt that describes my interests, goals, and background. It should aslo make sure that the AI is the best personal asisstant it can be."

Replace the placeholder "Your prompt" in the Python code with the personalized prompt generated by ChatGPT.


def get_user_background():
    return (
       "Your prompt"
    )



## Step 5: Install Required Python Packages

Navigate to the directory where your Python CLI application is saved and run the following command to install the required packages:


    pip install requests pypdf

This command installs the necessary libraries to run your application.

## Step 6: Run the Application

Now that everything is set up, you can run your Python CLI application with the following command:


    python Personal_Assistant.py


**You have successfully set up the Python CLI application to interact with the LLaMA model! Now you can generate tailored responses based on your personalized prompt. If you have any questions or run into issues, feel free to reach out for assistance.**
