# Movie Recommendation AI

Movie Recommendation AI is a Streamlit web application that suggests movies to users based on their favorite genres and movies. It uses OpenAI's GPT-3.5-turbo model to generate personalized movie recommendations.

## Table of Contents

- Features
- Installation
- Usage
- Configuration
- Contributing

## Features

- Users can select their favorite movie genres.
- Users can input their top 3 favorite movies.
- The app provides 5 movie recommendations based on the user's preferences.
- The recommendations are displayed in a table format with the movie name, genre, and a short summary.

## Installation

### Prerequisites

- Python 3.7 or higher
- [pip](https://pip.pypa.io/en/stable/) package manager

### Clone the Repository

```bash
git clone https://github.com/efdalerdem17/movie-recommendation-ai.git
cd movie-recommendation-ai
Create a Virtual Environment
It is recommended to create a virtual environment to manage your dependencies.
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the Dependencies
pip install -r requirements.txt
Usage

Setting Up the API Key
Create a .env file in the project root directory.
Add your OpenAI API key to the .env file:
OPENAI_API_KEY=your-api-key-here
Running the Application
To run the Streamlit application, use the following command:
streamlit run film_oneri_sistemi.py
This will start the web application in your browser.

