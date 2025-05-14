# Telegram Bot Project Template (Python + aiogram)

A clean and simple project template for building Telegram bots with Python and aiogram. This boilerplate provides a ready-to-use structure, helping you focus on writing bot logic instead of spending time on setup.

## Features
- Minimalistic and well-organized project structure
- Uses aiogram for asynchronous Telegram Bot API interaction
- Ready for scalable development
- Suitable for quick prototypes and production bots
- Easy to extend and customize

## Requirements
- Python 3.8+
- aiogram (latest version)

## Install dependencies:

```shell
uv sync
```

## Project Structure

```
app/
├── commons/         # Shared reusable logic
│   ├── services/    # Business-layer services (e.g. Telegram, payments)
│   └── utils/       # Low-level helpers and pure utility functions
├── enums/           # Enumerations for consistent value usage
├── localization/    # Language and message localization
├── models/          # SQLAlchemy ORM models
├── routes/          # aiogram routers and handlers
├── schemas/         # Pydantic models for input/output validation
```

## Quick Start
### 1. Clone this repository:

```shell
git clone https://github.com/MartyshWin/template_telegrambot.git
cd template_telegrambot
```

### 2. Install dependencies:
```shell
uv sync
```

### 3. Configure your bot token and settings in config.py.
### 4. Run the bot:
```shell
uv run python main.py
```

## Why use this template?
- Saves time on initial setup
- Encourages clean code organization
- Good starting point for both beginners and experienced developers
- Easy to maintain and scale for larger projects

## License

*This project is licensed under the MIT License.*

--- 

## 📚 Documentation
- [Architecture and design of the project](docs/architecture_and_philosophy.md)


