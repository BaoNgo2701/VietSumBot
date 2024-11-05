# Vietnamese Product Summarization Chatbot 
## Project Overview This project aims to develop a chatbot client-server solution that performs product summarization in Vietnamese. Users can send a request searching for a product, and the server will process this request by summarizing a collection of relevant products. 
## Prerequisites Ensure you have the following installed: 
  - Python 3.8+ - pip (Python package installer)
  - Virtual environment 
## Installation 
### Clone the Repository 
```sh
  git clone https://github.com/BaoNgo2701/VietSumBot
  cd vietnamesse-product-summarization-chatbot

'''

### Create and Activate a Virtual Environment
#### Window:
\```sh
  python -m venv env
  env\Scripts\activate
\
#### Linux:
\'''sh
  python3 -m venv env
  source env/bin/activate
\

## Processing Data
### Install Dependencies
\''' sh 
  pip install -r requirement.txt
\'''

### Cleaning Data
To preprocess and clean the data, run:
\''' sh
  python server/cleaning.py
'''

### Fine-Tuning the Model
To fine-tune the model on the cleaned data, run:
\''' sh
  python fine_tune.py
'''

### Generating Summaries
To generate summaries, run:
\'''
  python server/generate_summaries.py
'''

### Evaluation
To evaluate the model using ROUGE scores, run:
\'''
  python evaluation/evaluate_model.py
'''

## Running the server
### Start the Server
\'''
  hypercorn server.app:app
'''

### Verify the Server
Open your browser and navigate to http://127.0.0.1:8000 to ensure the server is running.

## Testing the Client
### Run the Client Application
\'''sh
  python client/main.py
'''

### Interact with the Client
Enter product queries in Vietnamese in the input field and click the "Send" button to view summarized product information and reasons to buy.

