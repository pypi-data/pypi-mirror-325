# Neural Payments -- Payments infrastructure for AI agents

## Overview
An SDK that enables your AI agent to send and receive money programmatically. You can spin up agents, fund them with USDC, and enable them to recieve and send money from any other agent that integrates the Neural Payments SDK.

The SDK comes with a template with sample agents. To use your own agents, simply replace the agent names and identities in the template with yours. 

## Features
- **Programmatic Payments**: Send and receive payments without messing with Paypal / stripe / credit card check in / check out pages.

- **Sample Agent Template**: Create and customise your own agent by replacing the agent names in the sample templates with your own agents.

- **Instant USDC Payments**: Implements near real-time USDC payments with verifiable transaction records on the USDC main net.


## Prerequisites
- **Python** (3.9 or later)
- **Node.js** (v20.17.0 or later)
- **API Keys from Circle’s Developer Console**: Obtain your API keys by visiting [Circle’s Developer Console](https://console.circle.com/).

## Environment Setup

### Python Setup
1. Install Python and create a virtual environment:
   ```bash
   mkdir ai_agents_project
   cd ai_agents_project
   python -m venv ai_agents_env
   source ai_agents_env/bin/activate  # On Windows use: ai_agents_env\Scripts\activate
   ```
2. Install necessary Python packages:
   ```bash
   pip install autogen python-dotenv
   ```

### Node.js Setup
1. Create a new Node.js project:
   ```bash
   npm init -y
   ```
2. Install Circle's Developer-Controlled Wallets SDK:
   ```bash
   npm install @circle-fin/developer-controlled-wallets --save
   ```

### Configuration
1. Create a `.env` file in the project root and add your API keys. To test in Replit, use the Replit [Secret Keys](https://docs.replit.com/replit-workspace/workspace-features/secrets) feature:
   ```
   OPENAI_API_KEY=your_openai_api_key
   CIRCLE_API_KEY=your_circle_api_key
   CIRCLE_ENTITY_SECRET=your_circle_entity_secret
   ```
2. Create an `OAI_CONFIG_LIST` file containing necessary OpenAI configurations:
   ```json
   [
       {
           "model": "gpt-4o",
           "api_key": "${OPENAI_API_KEY}"
       }
   ]
   ```

## Usage
To run the entire project, execute the following command:
```bash
python3 main.py
```

### Key Scripts
- **`ai_research.py`**: Contains logic to create and manage the AI agents in sample template.
- **`circle_payment.js`**: Implements blockchain payment processing, including wallet creation, transaction processing, and validation of payments received by AI agents.
- **`main.py`**: Orchestrates the execution of the research tasks and the payment processing.

## Key Functions
- **AI Research**: Managed by the function defined in `ai_research.py`, which initiates conversations among AI agents and collaborates on tasked workflows.
- **Blockchain Payments**: Handled by the functions in `circle_payment.js`, which encompass creating wallets, checking balances, and processing transactions.

## Running the Project
1. Execute the project by running `main.py`. It will perform AI research on the topic defined in the script and handle all wallet interactions and payments through the Circle API.
2. Monitor the logs in the terminal for real-time feedback regarding agent contributions and payment confirmations.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

---