# Quality Assurance Assessment

This project is a Quality Assurance assessment written in Python using Playwright and Behave. It is designed to automate testing scenarios and generate reports for analysis.

For detailed information about the assessment, please refer to the [e-core Test Automation Assessment](e-core_test_automation_assessment.md) document.

## Running the Tests

You have two options to run these tests: using Docker Compose or running them locally on your machine.

### 1. Docker Compose

#### Pre-requisites

- Ensure you have Docker and Docker Compose installed on your machine.

#### Steps

1. Build and run the Docker containers using Docker Compose:

   ```bash
   docker-compose up --build
   ```


Once the containers are up and running, you can access the test report by navigating to http://localhost:5252 in your web browser.

### 2. Local Setup

#### Pre-requisites

- Ensure you have Python 3.12 installed on your machine.

#### Steps

1. Install the required Python packages:

```bash
pip install -r requirements.txt
```

Install Playwright and its dependencies:

```bash
playwright install --with-deps
```

Run the tests using Behave:

```bash
behave ./features
```

This will execute the test scenarios defined in the features directory and generate the results.