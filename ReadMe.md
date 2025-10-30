# ACME Load API

## Deployment Instructions

### 1. Access the Deployment

**Base URL**  
https://acme-load-api.fly.dev


**Authentication**  
All endpoints require an API key sent in the `x-api-key` header.

**Endpoints**  
- `GET /loads` → List all loads  
- `GET /loads/{id}` → Fetch details for a specific load  
- `POST /search` → Search loads by JSON body filters (`origin`, `destination`, `equipment_type`, etc.)

**Usage examples**  

- Get load with `load_id` **L1001**:
```bash
curl -H "x-api-key: sk_test_9f8c6e12b3a04c57a2d44e89c1a7d9c4" \
https://acme-load-api.fly.dev/loads/L1001
```

- Get loads with origin Dallas:
```bash
curl -X POST -H "Content-Type: application/json" \
-H "x-api-key: sk_test_9f8c6e12b3a04c57a2d44e89c1a7d9c4" \
-d '{"origin":"Dallas"}' \
https://acme-load-api.fly.dev/search
```

### 2. How to Reproduce the Deployment

#### Manual Steps

1. **Clone the repo / project structure**  
   The repository contains:
   - `app/main.py` → FastAPI app  
   - `app/loads.json` → mock data  
   - `requirements.txt`  
   - `Dockerfile`

2. **Install Fly.io CLI**  
   - **Mac**  
     ```bash
     brew install flyctl
     ```
   - **Linux**  
     ```bash
     curl -L https://fly.io/install.sh | sh
     ```
   - **Windows**  
     ```powershell
     iwr https://fly.io/install.ps1 -useb | iex
     ```

3. **Authenticate**  
   ```bash
   flyctl auth login

4. **Initialize the app**

flyctl launch

You will be prompted to choose, among other parameters, the app name.
By default, it should be acme-load-api.

5. **Set API key as a secret**

flyctl secrets set API_KEY="replace_with_your_api_key"

6. **Deploy**
flyctl deploy

7. Verify
curl -H "x-api-key: <your-key>" https://<app-name>.fly.dev/loads
Replace with your API key (step 5) and the app name defined at step 4.

## Project Structure

```plaintext
.
├── app/
│   ├── main.py        # FastAPI app entrypoint
│   └── loads.json     # Mock load data
├── requirements.txt   # Python dependencies
├── Dockerfile         # Containerization instructions
```
