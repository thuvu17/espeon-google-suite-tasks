# Google Suite Manager Tool

## Project Purpose
The Google Suite Manager Tool is a web application designed to streamline the management and access to various Google Suite services including Google Meet and Google Calendar. This tool provides a centralized platform for users to engage with Google services more efficiently, offering quick access links and features tailored for enhanced productivity.

## Features
- **Home Dashboard**: A central hub from which all services can be accessed.
- **Google Meet Integration**: Direct access to Google Meet for quickly starting or scheduling meetings.
- **Google Calendar Integration**: Easy access to Google Calendar to view, manage, and schedule events.
- **Google Login**: Support login using a Google account.
- **Task List**: A dedicated section for managing daily tasks and reminders directly from the homepage.


## Installation Instructions
To set up the Google Suite Manager Tool on your local machine, follow these steps:

## Prerequisites

- Python 3.8 or higher
- PDM for Python dependency management

## Project Setup

To set up the project environment:

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd <repository-name>
   ```

3. Install PDM if you haven't already:
   ```
   pip install pdm
   ```

4. Initialize the project using PDM (if not already done):
   ```
   pdm init
   ```

5. Install project dependencies:
   ```
   pdm install
   ```
6. Install python Flask
   ```
   pip install Flask
   ```
## Running the Application

To run the application, use:
```
pdm run python src/app.py
```

Replace `src/app.py` with the path to your Python script.

## Testing

To run tests, execute:
```
pdm run pytest
```

## Usage Instructions

Once the application is running, navigate to http://127.0.0.1:5000/ in your web browser to access the Google Suite Manager Tool. From the homepage, you can access the following features:

Click on the Google Meet button to navigate to the Google Meet section.
Click on the Google Calendar button to view the calendar interface.
Manage and view tasks in the To-Do List section on the homepage.

## Contributing Guidelines

Contributions to the Google Suite Manager Tool are welcome! Here’s how you can contribute:

- Fork the Repository: Fork the project to your GitHub account.
- Clone Your Fork: Make a local clone of your fork for development.
- Create a New Branch: Create a new branch for each feature or improvement.
- Make Changes: Implement your changes and commit them to your branch.
- Push Changes: Push your changes to your fork on GitHub.
- Submit a Pull Request: Open a pull request from your fork's branch to the original repository’s main branch.

### Bug Reports & Feature Requests

Please use the issue templates provided to report any bugs or file feature requests. Navigate to the `.github/issue_template` directory to access the bug report and feature request templates. This will help us understand and address your concerns more efficiently.

### Pull Requests

Here are some guidelines for submitting pull requests:
- Navigate to the `.github/pull_request_template` directory and use the pull request template provided for your submissions.
- Provide a clear summary of what the PR achieves.
- Explain the motivation behind the changes.
- Describe any testing that has been done to ensure the changes work as expected.

By contributing, you agree that your contributions will be licensed under the project's license.

## License

This project is licensed under the Apache License 2.0 - see the `LICENSE` file for details.

## Additional Information

- This project uses GitHub Actions for continuous integration, which automatically runs tests and checks code formatting with Black.
- The `.gitignore` file is configured to ignore Python-specific files and directories, such as `__pycache__` and the `venv` directory.
- For more details on project organization and workflow management, refer to the documentation in the `docs` directory.
