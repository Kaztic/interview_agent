# Interview Agent

An AI-powered interview agent that assists with shortlisting and interviewing process.

## Prerequisites

- Python 3.8+
- Redis
- Conda (recommended) or Virtual environment

## Setup

### Option 1: Using Conda (Recommended)

1. Clone the repository
   ```bash
   git clone https://github.com/Kaztic/interview_agent.git
   ```

2. Create and activate the Conda environment from the environment.yml file:
   ```bash
   conda env create -f environment.yml
   conda activate interview_agent
   ```

### Option 2: Using venv

1. Clone the repository
   ```bash
   git clone https://github.com/Kaztic/interview_agent.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv interview_agent_env
   source interview_agent_env/bin/activate  # On Windows: interview_agent_env\Scripts\activate
   ```
   **note: you might have to work with python or python3 based on your machine env setup.
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Environment Setup

Create a `.env` file with the following variables:
```
REDIS_URL=redis://localhost:6379/0
GEMINI_API_KEY=your_key_here
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

## Running the Application

### Option 1: Using Conda (Recommended)

#### Start Script (starts Redis and Celery worker)
```bash
# Make the script executable
chmod +x start_conda.sh

# Run the start script
./start_conda.sh
```

#### Run Script (starts FastAPI server)
```bash
# Make the script executable
chmod +x run_conda.sh

# Run the API server
./run_conda.sh
```

### Option 2: Using venv

#### Start Script (starts Redis and Celery worker)
```bash
# Make the script executable
chmod +x start.sh

# Run the start script
./start.sh
```

#### Run Script (starts FastAPI server)
```bash
# Make the script executable
chmod +x run.sh

# Run the API server
./run.sh
```

Both options will:
1. Activate the appropriate environment
2. Start Redis server with secure configuration
3. Start the Celery worker (for start scripts)
4. Start the FastAPI server on http://localhost:8000 (for run scripts)

## API Usage

### 1. Create a New Interview Task

Send a POST request to create a new interview task:

```bash
curl -X POST http://localhost:8000/api/v1/interview \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "You are an C/C++ and OOPs interviewer, give the interviewee 5 unique questions"
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
    "result": "Based on my experience..."
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

## Development

The application uses:
- FastAPI for the web server
- Celery for task queue
- Redis as message broker and result backend
- Google's Gemini AI for AI capabilities

## Security

- Redis is configured to run in protected mode
- All services are bound to localhost by default
- Environment variables are used for sensitive configuration 
