# 📦 aws_28_10

Welcome to the `aws_28_10` project repository!  
This repo contains Python scripts and configuration files used for hands-on learning with AWS, automation, and basic scripting tasks.

---

## 📁 Project Structure

| File / Folder       | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `basededados.py`     | Script that connects to a database using configuration from `db.yml`        |
| `db.yml`             | YAML file with database connection settings                                 |
| `exemplo.py`         | Basic Python script to handle command-line arguments                        |
| `somar2n.py`         | Script that sums two numbers provided via command-line arguments            |
| `.github/workflows/` | Contains GitHub Actions workflow to automate script execution               |
| `README.md`          | This file                                                                   |

---

## ⚙️ GitHub Actions Workflow

This project includes a basic CI/CD pipeline using **GitHub Actions**:
- Runs `somar2n.py` when triggered manually
- Useful for testing automation of Python scripts

---

## 🚀 How to Use

Make sure you have Python installed, then run:

```bash
python somar2n.py 5 7
