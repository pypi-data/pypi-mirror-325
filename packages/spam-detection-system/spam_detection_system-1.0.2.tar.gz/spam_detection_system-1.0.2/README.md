# 🚀 Spam Detection System

## 💻 Tech Stack

| Programming | Web | ML & Data | DevOps | Tools | Shell |
|:---:|:---:|:---:|:---:|:---:|:---:|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) | ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) | ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white) | ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white) |
| ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) | ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) | ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) | ![Railway](https://img.shields.io/badge/Railway-0B0B0B?style=for-the-badge&logo=railway&logoColor=white) | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) | ![Shell Script](https://img.shields.io/badge/Shell%20Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white) |

## 🔧 Version Control Workflow

### Git Branching Strategy
- **Main Branch**: `main` (primary development branch)
- **Workflow**: Feature-based branching
- **Commit Conventions**: Descriptive, atomic commits

### Key Git Commands Used
```bash
# Clone the repository
git clone https://github.com/bniladridas/spam-detection-system.git

# Create a new feature branch
git checkout -b feature/new-model-improvement

# Stage changes
git add .

# Commit with a descriptive message
git commit -m "Add comprehensive model performance metrics"

# Push to remote repository
git push origin feature/new-model-improvement

# Merge feature branch (via Pull Request)
git checkout main
git merge feature/new-model-improvement
```

### Version Control Best Practices
- Atomic commits
- Descriptive commit messages
- Regular code reviews
- Branch protection rules
- Continuous integration checks

### Repository Insights
![GitHub commits](https://img.shields.io/github/commit-activity/m/bniladridas/spam-detection-system?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/bniladridas/spam-detection-system/main?style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/bniladridas/spam-detection-system?style=flat-square)

## 📚 Key Libraries Used
- **Data Processing**: NumPy, Pandas
- **Machine Learning**: scikit-learn (MultinomialNB)
- **Web**: Flask, Gunicorn
- **Visualization**: Matplotlib
- **Logging**: Python logging module
- **Serialization**: joblib

## 🔗 Quick Links
- **Live Demo**: [Spam Detection Web App](https://web-production-4569.up.railway.app)
- **Repository**: [GitHub Project](https://github.com/bniladridas/spam-detection-system)

## 🌐 LinkedIn Showcase

### Project Announcement Post

[![LinkedIn Post](https://img.shields.io/badge/View%20LinkedIn%20Post-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/feed/update/urn:li:activity:7292445054487392256/)

**Key Highlights from the Post:**
- 🚀 95% Spam Detection Accuracy
- ⚡ Real-time Email Classification
- 🔬 Machine Learning Innovation
- 🌐 Open-Source Collaboration

*Note: For the full interactive post, please visit the LinkedIn link above.*

## 📝 License
MIT License

## 📦 Package Installation

### PyPI
[![PyPI version](https://badge.fury.io/py/spam-detection-system.svg)](https://pypi.org/project/spam-detection-system/)

Install the latest version from PyPI:
```bash
pip install spam-detection-system
```

### Specific Versions
- [PyPI Project Page v1.0.0](https://pypi.org/project/spam-detection-system/1.0.0/)
- [PyPI Project Page v1.0.1](https://pypi.org/project/spam-detection-system/1.0.1/)
- [PyPI Project Page v1.0.2](https://pypi.org/project/spam-detection-system/1.0.2/)

### GitHub Package Installation
```bash
# Authenticate with GitHub Packages
pip install \
  -i https://maven.pkg.github.com/bniladridas/spam-detection-system \
  spam-detection-system
```

### GitHub Package Publishing
1. **Create a Personal Access Token**:
   Please follow the instructions below to create a token.

### 🔑 Creating a Personal Access Token

1. **Go to GitHub Token Creation Page**:
   [https://github.com/settings/tokens/new](https://github.com/settings/tokens/new)

2. **Token Scopes Needed**:
   - `repo` (Full control of private repositories)
   - `write:packages` (Upload packages to GitHub Packages)
   - `read:packages` (Download packages from GitHub Packages)

3. **Best Practices**:
   - Set an expiration date
   - Use a descriptive name
   - Limit token scope to specific repositories
   - Store token securely

⚠️ **Security Warning**: 
- Never share your token publicly
- Use GitHub Secrets in Actions
- Rotate tokens periodically

2. Set the token as an environment variable:
```bash
export GITHUB_TOKEN=your_personal_access_token
```

3. Build and publish the package:
```bash
python -m build
twine upload \
  --repository-url https://maven.pkg.github.com/bniladridas/spam-detection-system \
  dist/*
```

### GitHub Package Publishing Workflow

#### 1. Create GitHub Secrets

Go to your repository:
1. Settings → Secrets and variables → Actions
2. Click "New repository secret"

Create these secrets:
- `PYPI_API_TOKEN`: PyPI upload token
- `GITHUB_TOKEN`: Personal Access Token

#### 2. Trigger Package Publish

Publish methods:
1. **Manual Release**:
   ```bash
   # Create and push a new tag
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. **GitHub Release**:
   - Go to your repository
   - Click "Releases"
   - "Draft a new release"
   - Select a tag
   - Publish release

#### 3. Verify Package

After publishing:
```bash
# Install from GitHub Packages
pip install \
  -i https://maven.pkg.github.com/bniladridas/spam-detection-system \
  spam-detection-system
```

### 🔍 Troubleshooting

- Ensure all GitHub Actions permissions are correctly set
- Verify token scopes
- Check workflow logs for specific errors

### 📋 Checklist

- [x] Create Personal Access Token
- [ ] Set up GitHub Secrets
- [ ] Configure package metadata
- [ ] Test package locally
- [ ] Publish package

## Package Features
- Easy installation via pip
- Supports Python 3.9+
- Lightweight machine learning package
- Comprehensive spam detection algorithms

## Git Operations

### Clone Repository
```bash
git clone https://github.com/bniladridas/spam-detection-system.git
cd spam-detection-system
```

### Push Changes
```bash
# Add changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to repository
git push origin main
```

## Running with Docker

### Start Server
```bash
docker-compose up --build
```
- Access the application at [http://localhost:5001/](http://localhost:5001/).

### Stop Server
```bash
docker-compose down
```

### View Server Logs
```bash
docker-compose logs spam-detection-app
```

Example Server Logs:
```
spam-detection-app-1  | [2025-02-04 05:28:45 +0000] [1] [INFO] Starting gunicorn 20.1.0
spam-detection-app-1  | [2025-02-04 05:28:45 +0000] [1] [INFO] Listening at: http://0.0.0.0:5001
spam-detection-app-1  | [2025-02-04 05:28:45 +0000] [1] [INFO] Using worker: sync
```

## Running with Flask Backend

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Application
```bash
python app.py
```
- Access the application at [http://127.0.0.1:5001/](http://127.0.0.1:5001/).

## Using the API
Send a POST request to `/predict` with JSON:
```json
{
  "email_text": "Your email content here"
}
```

#### Response Format
```json
{
  "is_spam": true/false,
  "spam_probability": 0-100,
  "message": "Spam detected!" or "Not spam."
}
```

## 🚀 Deployment

### Railway Deployment
For a detailed guide on deploying this project on Railway.app, check out our [Railway Deployment Guide](/docs/railway_deployment_guide.md).

### Live Demo
- **Platform**: Railway
- **URL**: https://web-production-4569.up.railway.app
- **Endpoint**: `/predict`

### Deployment Methods

#### Local Deployment

##### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

##### Installation
1. Clone the repository
```bash
git clone https://github.com/bniladridas/spam-detection-system.git
cd spam-detection-system
```

2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

## Model Details
- **Algorithm**: Multinomial Naive Bayes
- **Features**: Text classification
- **Performance**: 95% accuracy on test dataset

## Project Structure
- `app.py`: Main Flask application
- `spam_dataset.csv`: Training dataset
- `requirements.txt`: Python dependencies
- `Dockerfile`: Docker configuration
- `docker-compose.yml`: Docker Compose setup

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to branch
5. Create pull request

## PyPI Token Creation

### 🔑 Creating PyPI API Token

1. **Log in to PyPI**:
   - Go to [https://pypi.org/account/login/](https://pypi.org/account/login/)

2. **Navigate to Account Settings**:
   - Click on your username
   - Select "Account settings"

3. **Create API Token**:
   - Scroll to "API tokens" section
   - Click "Add API token"
   - Give token a descriptive name
   - Select appropriate scopes
   - Copy the generated token

4. **Add Token to GitHub Secrets**:
   - In your GitHub repository
   - Go to Settings → Secrets → Actions
   - Create a new repository secret
   - Name: `PYPI_API_TOKEN`
   - Paste your PyPI token

⚠️ **Security Tips**:
- Never share your PyPI token
- Use scoped tokens
- Rotate tokens periodically