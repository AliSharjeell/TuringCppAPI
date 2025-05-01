from fastapi import FastAPI, Query
import subprocess
import json

app = FastAPI()

@app.get("/run")
def run_cpp_program(name: str = Query(...)):
    try:
        # Run executable and send input via stdin
        result = subprocess.run(
    ["./turing", name],  # no ".exe"
    capture_output=True,
    text=True,
    check=True
)


        # Parse JSON output
        data = json.loads(result.stdout)
        return data

    except subprocess.CalledProcessError as e:
        return {"error": "Executable failed", "details": e.stderr}

    except json.JSONDecodeError:
        return {"error": "Invalid JSON from program", "raw_output": result.stdout}
