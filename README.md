# Interview Agent

An AI-powered interview agent that assists with shortlisting candidates and interviewing them.

## Project Structure

```
interview_agent/
├── api/                    # API endpoints and routing
│   ├── endpoints.py       # API route definitions
│   └── __init__.py
├── core/                  # Core application logic
│   ├── agents/           # Different agent implementations
│   │   ├── interview_agent.py
│   │   └── __init__.py
│   ├── prompts/          # System prompts for different agents
│   │   └── interview_prompt.py
│   ├── main.py          # Main application logic
│   ├── config.py        # Configuration settings
│   └── schemas.py       # Data models and schemas
├── tasks/                # Celery task definitions
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
├── environment.yml      # Conda environment file
└── README.md
```

## Prerequisites

- Python 3.8+
- Redis
- Conda (Recommended)

### Installing Conda

1. Download the Miniconda installer:
   ```bash
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   ```

2. Make the installer executable:
   ```bash
   chmod +x Miniconda3-latest-Linux-x86_64.sh
   ```

3. Run the installer:
   ```bash
   ./Miniconda3-latest-Linux-x86_64.sh
   ```

4. Follow the prompts:
   - Press Enter to review the license agreement
   - Type "yes" to accept the license terms
   - Press Enter to confirm the installation location (or specify a different path)
   - Type "yes" when asked if you want the installer to initialize Miniconda3

5. Close and reopen your terminal, or run:
   ```bash
   source ~/.bashrc
   ```

6. Verify the installation:
   ```bash
   conda --version
   ```

## Setup

1. Clone the repository

2. Set Up the Environment:

   ### Option 1: Using environment.yml (Recommended)
   ```bash
   # Create and activate the environment
   conda env create -f environment.yml
   conda activate interview_agent
   ```

   ### Option 2: Manual Conda Installation (If option 1 is not working)
   ```bash
   # Create a new conda environment for the project
   conda create -n interview_agent python=3.8
   conda activate interview_agent

   # Install required packages
   conda install -c conda-forge fastapi uvicorn celery redis python-dotenv requests pydantic pydantic-settings google-generativeai
   ```

   ### Option 3: Using Virtual Environment (Optional)
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file with the following variables:
   ```bash
   REDIS_URL=redis://localhost:6379/0
   GEMINI_API_KEY=your_key_here
   # Get your API key from https://makersuite.google.com/app/apikey
   CELERY_BROKER_URL=redis://localhost:6379/0
   CELERY_RESULT_BACKEND=redis://localhost:6379/0
   ```

## Running the Application 

### With Conda (Recommended)
### Step 1: Start Celery worker and Redis

This script starts both Redis and Celery worker in the background:

```bash
# Make the script executable
chmod +x start_conda.sh

# Run the start script
./start_conda.sh
```

This will:
1. Activate the Conda environment
2. Start Redis server with secure configuration
3. Start the Celery worker

### Step 2: Start the API Server

This script starts the FastAPI server:

```bash
# Make the script executable
chmod +x run_conda.sh

# Run the API server
./run_conda.sh
```

This will:
1. Activate the Conda environment
2. Start the FastAPI server on http://localhost:8000


### With Venv
### Step 1: Start Celery worker and Redis

This script starts both Redis and Celery worker in the background:

```bash
# Make the script executable
chmod +x start.sh

# Run the start script
./start.sh
```

This will:
1. Activate the virtual environment
2. Start Redis server with secure configuration
3. Start the Celery worker

### Step 2: Start the API Server

This script starts the FastAPI server:

```bash
# Make the script executable
chmod +x run.sh

# Run the API server
./run.sh
```

This will:
1. Activate the virtual environment
2. Start the FastAPI server on http://localhost:8000

## API Usage

### 1. Create a New Interview Task

Send a POST request to create a new interview task:

```bash
curl -X POST http://localhost:8000/api/v1/interview \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Full stack developer with 5 years of experience in Python and JavaScript"
  }'
```

Response:
```json
{
    "task_id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "queued"
}
```

### 2. Get Task Result

Use the task_id from the previous response to check the status and get the result:

```bash
curl http://localhost:8000/api/v1/tasks/123e4567-e89b-12d3-a456-426614174000
```

Response:
```json
{
    "task_id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "SUCCESS",
    "result": "Interview questions and evaluation..."
}
```

Possible status values:
- `queued`: Task is waiting to be processed
- `STARTED`: Task is being processed
- `SUCCESS`: Task completed successfully
- `FAILURE`: Task failed
- `PENDING`: Task is waiting to be picked up by a worker

## API Endpoints

- `POST /api/v1/interview`: Create a new interview task
  - Request body: `{"prompt": "your question here"}`
  - Returns: task_id and initial status
- `GET /api/v1/tasks/{task_id}`: Get the result of a specific task
  - Returns: task_id, current status, and result (if completed)

## Components

### Agents

The `core/agents` directory contains different agent implementations:
- `interview_agent.py`: Implements the InterviewAgent class that handles interview interactions using the Gemini AI model

### Prompts

The `core/prompts` directory contains system prompts:
- `interview_prompt.py`: Defines the interview system prompt and formatting functions

### Main Application

The `core/main.py` file contains:
- FastAPI application setup
- Endpoint definitions
- Agent initialization and management

## Development

The application uses:
- FastAPI for the web server
- Celery for task queue
- Redis as message broker and result backend
- Google's Gemini AI for AI capabilities
- System prompts stored locally for better management and versioning

## Security

- Redis is configured to run in protected mode
- All services are bound to localhost by default
- Environment variables are used for sensitive configuration
