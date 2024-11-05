Product Summarization Chatbot
Project Overview
This project implements a simple chatbot client-server solution that performs product summarization in Vietnamese. Users can send product-related queries to the server, which responds with up to 5 related products along with reasons to purchase them.

Features
Client sends a product-related text request in Vietnamese.

Server processes the request, summarizes relevant products, and returns the top 5 related products with reasons to buy.

Requirements
Python 3.8 or higher

transformers

aiofiles

asyncio

quart

quart-cors

requests

tkinter

rouge-score

Installation

Install the required packages:
pip install -r requirements.txt
Running the Server

Navigate to the server directory:
cd server

Run the server:
python app.py
Running the Client

Navigate to the client directory:
cd client

Run the client:
python main.py
Server Code Explanation
app.py
Handles requests from the client.

Summarizes product descriptions and returns the top 5 related products.

Includes ROUGE scoring for evaluation.

summarize.py
Contains functions for product summarization, category detection, and pattern detection.

Uses a pre-trained BART model for summarization.

cleaning.py
Reads product descriptions from files.

Cleans and normalizes text data.

Client Code Explanation
main.py
Sends product-related queries to the server.

Displays the summarized product information along with ROUGE scores.

Data Preparation
Organize Product Descriptions:

Place product descriptions in the server/product_data directory.

Create folders for each category (e.g., Backpacks, Clothes, Office).

Each folder should contain text files with product descriptions.

Clean Data:

Run cleaning.py to clean and normalize the product descriptions.

cd server
python cleaning.py

Evaluation
The server applies ROUGE scoring to evaluate the quality of the summaries.

ROUGE scores are returned along with the product summaries for performance assessment.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Contact
Your Name: giabao.ngoha@gmail.com