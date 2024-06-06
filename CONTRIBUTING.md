# Contributing to RmediatoR
Thank you for your interest in contributing to RmediatoR! We welcome contributions from the community and are excited to see what you can bring to the project. Below are some guidelines to help you get started.

## How Can You Contribute?
1. Reporting Bugs: If you find a bug, please report it by opening an issue on GitHub. Provide as much detail as possible to help us understand and reproduce the issue.

2. Feature Requests: Have an idea for a new feature? Open an issue on GitHub to discuss it. We welcome new ideas and improvements.

3. Code Contributions: We accept pull requests for bug fixes, new features, and documentation improvements. See the guidelines below for more details.

4. Documentation: Help us improve our documentation. This includes everything from fixing typos to adding new sections and improving existing content.

## Getting Started
1. Fork the Repository
Start by forking the repository to your own GitHub account.

2. Clone the Repository
Clone the forked repository to your local machine:

```sh
git clone https://github.com/your-username/rmediator.git
cd rmediator
```
3. Install Dependencies
Install the necessary dependencies using pip or poetry:

```sh
pip install -r requirements.txt
```

or

```sh
poetry install
```
4. Create a Branch
Create a new branch for your work. Use a descriptive name for the branch:

```sh
git checkout -b feature/your-feature-name
```
## Making Changes
### Coding Guidelines
Follow PEP 8 style guidelines for Python code.
Write clear, concise commit messages.
Include docstrings for all public methods and classes.
Add or update tests as needed to cover your changes.

We are using `isort` and `black` to format our code. Please run them before making your commits.

### Running Tests
Ensure all tests pass before submitting your pull request. Run the tests with:

```sh
make test
```

or

```sh
make test-coverage
```
Which will also display the test coverage statistics achieved by the code at that point.

### Commit Your Changes
Commit your changes to your branch:

```sh
git add .
git commit -m "Description of your changes"
```
### Push to GitHub
Push your changes to your forked repository:

```sh
git push origin feature/your-feature-name
```

### Submitting a Pull Request
1. Navigate to the original repository on GitHub.
2. Click the "New Pull Request" button.
3. Select the branch you created and compare it with the main branch.
4. Fill out the pull request template, providing as much detail as possible.
5. Submit your pull request.

### Code Review Process
Your pull request will be reviewed by the maintainers. They may request changes or ask for additional information. Please be responsive to feedback and make the requested changes promptly.

### Community Guidelines
- Be respectful and considerate in your interactions with others.
- Provide constructive feedback and be open to receiving it.

### Thank You!
Thank you for contributing to RmediatoR! Your efforts help make this project better for everyone. If you have any questions, feel free to reach out by opening an issue on GitHub or contacting us at fikernew.birhanu.waju@gmail.com.