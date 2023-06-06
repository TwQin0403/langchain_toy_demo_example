# langchain_toy_demo_example

This repository serves as a  example for learning the Langchain framework. It facilitates the construction of a simple application designed to fetch arXiv papers using their respective arXiv IDs. Furthermore, it use the first two pages of paper to generates LaTeX slides.

## How to Use

Follow these simple steps to get the application up and running:

1. **Create a .env File**: Add a .env file to your project folder. This file should contain the following line:

```other
OPENAI_API_KEY= YOUR_OPENAI_API_KEY
```

2. **Build the Application:** Initiate the build process by entering the following command in your terminal:

```other
make build
```

3. **Run the Application:**  Once the build process completes, start the application with the following command:

```other
make run_app
```

## Demonstration

The app appears as follows:
![Image Description](app.png)
Input the Arxiv ID and initiate the process to generate the slides. Once it is completed, a download link will be displayed.
![Image Description](app_link.png)
This will produce a PDF file output.
![Image Description](output.png)
