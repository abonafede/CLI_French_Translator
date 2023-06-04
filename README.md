# CLI English to French Translator

## Description
This command line ML system utilizes the powerful Helsinki-NLP model from Hugging Face to provide accurate English-to-French translation. By leveraging the command line interface, users can effortlessly input English sentences and receive their French translations swiftly, enabling seamless communication between the two languages.

## MLOps
This ML system incorporates continuous integration using GitHub Actions, employing the main.yml file as its template. Through this CI process, every code change triggers automated testing and deployment, ensuring the system's functionality and reliability. The Makefile acts as the execution guide, orchestrating the necessary commands for translation. Additionally, the repository offers a linked GitHub Codespace, providing a collaborative and streamlined development environment for contributors to work on the project.

## How to Run
1. Navigate to souce folder of your choice (cd ~/PATH/)
2. Once in directory, git clone this repository (git clone LINK)
3. Navigate into cloned foler (cd ~/PATH/CLI_French_Translator/)
4. Set up environment (make setup)
5. Run (python translator.py)
