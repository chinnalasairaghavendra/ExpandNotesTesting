# Advanced Selenium Python Hybrid Automation Framework

## Overview

This project is an enterprise-grade hybrid automation framework built using:

- Selenium with Python
- Pytest
- Selenium Grid
- Docker
- Jenkins CI/CD
- Allure Reporting
- API Automation using Requests
- AI-Assisted Automation using LongCat LLM

The framework automates the ExpandTesting Notes Application using:

- UI Testing
- API Testing
- Hybrid UI + API Validation
- Parallel Execution
- AI-powered quality engineering capabilities

---

# Application Under Test

## UI

https://practice.expandtesting.com/notes/app

## API

https://practice.expandtesting.com/notes/api/api-docs/

---

# Framework Features

## UI Automation

- Selenium WebDriver
- Page Object Model (POM)
- Explicit Waits
- JavaScript Executor utilities
- Reusable BasePage methods
- Screenshot capture on failure
- Structured logging

---

## API Automation

- Requests-based reusable API clients
- Authentication handling
- CRUD operations validation
- API response assertions
- Performance checks

---

## Hybrid End-to-End Testing

### UI → API Validation

Validate that notes created through the UI are immediately reflected in API responses.

### API → UI Validation

Validate that notes deleted through API disappear from the UI.

---

# Advanced Capabilities

## Parallel Execution

- pytest-xdist
- Selenium Grid
- Distributed execution using Docker

---

## CI/CD Integration

Implemented using Jenkins pipeline.

Pipeline includes:

1. Source checkout
2. Dependency installation
3. Selenium Grid startup
4. Parallel test execution
5. Allure report publishing
6. Artifact upload

---

# AI-Assisted Automation Features

## AI Failure Analysis

Automatically analyzes failed test cases using LongCat LLM.

Features:

- Root cause analysis
- Failure explanation
- AI-generated debugging suggestions
- Allure AI attachments

---

## AI Test Data Generation

Dynamic test data generation using LongCat LLM.

Example:

- Dynamic note title
- Dynamic description
- Dynamic categories

---

## AI Locator Healing

If a locator fails:

1. Framework captures page source
2. Sends DOM + failed locator to LongCat LLM
3. LLM suggests improved locator
4. Framework retries dynamically

---

# Agentic Automation Features

## Self-Healing Locators

Runtime recovery using alternate locator strategies.

---

## Intelligent Retry Engine

Automatically retries flaky Selenium actions such as:

- StaleElementReferenceException
- ElementClickInterceptedException
- TimeoutException

---

## Intelligent Wait System

Centralized reusable wait utilities:

- Wait for clickable
- Wait for visible
- Wait for presence

---

# Performance Engineering

## API Performance Validation

Validate API response time is under acceptable threshold.

---

## UI Performance Validation

Measure:

- Page load time
- DOM readiness timing

---

# Project Structure

```text
project/
│
├── ai/
│   ├── ai_locator_healer.py
│   ├── failure_analyzer.py
│   ├── intelligent_waits.py
│   ├── llm_client.py
│   ├── retry_agent.py
│   ├── self_healing.py
│   └── test_data_generator.py
│
├── api/
│   ├── auth_api.py
│   └── notes_api.py
│
├── config/
│   ├── environment.py
│   └── config_template.yaml
│
├── docker/
│   ├── docker-compose.yml
│   ├── Dockerfile.jenkins
│   └── Jenkinsfile
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── notes_page.py
│
├── tests/
│   ├── api/
│   ├── e2e/
│   ├── performance/
│   └── ui/
│
├── utils/
│   ├── logger.py
│   └── performance_utils.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

# Tech Stack

| Technology | Usage |
|---|---|
| Python | Programming Language |
| Selenium | UI Automation |
| Pytest | Test Framework |
| Requests | API Automation |
| Docker | Containerization |
| Selenium Grid | Distributed Parallel Execution |
| Jenkins | CI/CD |
| Allure | Reporting |
| LongCat LLM | AI-assisted automation |

---

# Installation & Setup

## Clone Repository

```bash
git clone https://github.com/chinnalasairaghavendra/ExpandNotesTesting
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configuration

Create:

```text
config/config.yaml
```

Example:

```yaml
base_url: "https://practice.expandtesting.com/notes"
api_url: "https://practice.expandtesting.com/notes/api"
email: "your_email"
password: "your_password"
```

---

# Environment Variables

Create:

```text
.env
```

Example:

```env
LONGCAT_API_KEY=your_api_key
```

---

# Running Tests

## Run All Tests

```bash
pytest
```

---

## Run Parallel Tests

```bash
pytest -n 2
```

---

## Run With Allure

```bash
pytest -n 2 --alluredir=allure-results
```

---

## Open Allure Report

```bash
allure serve allure-results
```

---

# Selenium Grid Execution

## Start Grid

```bash
docker compose -f docker/docker-compose.yml up -d --scale chrome=2
```

---

## Open Grid UI

```text
http://localhost:4444
```

---

# Jenkins Pipeline

The project supports Jenkins CI/CD integration.

Pipeline stages:

- Checkout Source Code
- Install Dependencies
- Start Selenium Grid
- Run Parallel Tests
- Publish Reports
- Upload Artifacts

---

# Reporting

## Allure Report

Features:

- Screenshots
- Logs
- Failure analysis
- AI debugging insights

---

## HTML Report

Generated using pytest-html.

---

# Key Highlights

- Enterprise-grade Selenium framework
- Hybrid UI + API automation
- AI-assisted automation
- Self-healing capabilities
- Dockerized Selenium Grid
- Jenkins CI/CD integration
- Distributed parallel execution
- Advanced reporting
- Intelligent retry mechanisms

---

# Future Enhancements

Potential future improvements:

- AI-based flaky test prediction
- Historical trend analysis
- Smart test prioritization
- Visual testing integration
- Cloud Selenium Grid support

---

# Author

Chinnala Sai Raghavendra

---

# Conclusion

This framework demonstrates a modern enterprise-level hybrid automation solution combining:

- Selenium
- API automation
- AI-assisted quality engineering
- CI/CD
- Distributed execution
- Resilient automation architecture

The project showcases scalable, maintainable, and intelligent automation engineering practices suitable for real-world QA environments.

