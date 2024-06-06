# MLOPS_task4
# MLOps Task - Iris Dataset

This repository demonstrates a complete MLOps pipeline for the Iris dataset, including data preprocessing, model training, evaluation, deployment, and CI/CD.

## Project Structure
- `data/`: Directory to store dataset files.
- `notebooks/`: Jupyter notebooks for exploratory data analysis.
- `scripts/`: Python scripts for preprocessing, training, and evaluation.
- `models/`: Directory to store the trained model.
- `app/`: Flask application for model serving.
- `tests/`: Unit tests for the model and API.
- `.github/workflows/`: GitHub Actions workflows for CI/CD.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation.

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/MLOps_task-iris.git
    cd MLOps_task-iris
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run data preprocessing:
    ```bash
    python scripts/data_preprocessing.py
    ```

4. Train the model:
    ```bash
    python scripts/train_model.py
    ```

5. Evaluate the model:
    ```bash
    python scripts/evaluate_model.py
    ```

6. Start the Flask app:
    ```bash
    python app/app.py
    ```

7. Run tests:
    ```bash
    python -m unittest tests/test_model.py
    ```

## CI/CD Pipeline

The CI/CD pipeline is configured using GitHub Actions and is defined in `.github/workflows/ci-cd.yml`.

