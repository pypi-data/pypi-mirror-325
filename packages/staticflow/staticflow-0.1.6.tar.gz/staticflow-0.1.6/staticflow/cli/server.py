import asyncio
from aiohttp import web
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rich.console import Console
from rich.panel import Panel
from ..core.config import Config
from ..core.engine import Engine
from ..plugins.syntax_highlight import SyntaxHighlightPlugin
from ..plugins.math import MathPlugin
from ..plugins.diagrams import MermaidPlugin
from ..plugins.notion_blocks import NotionBlocksPlugin

console = Console()

REQUIRED_DIRECTORIES = ['content', 'templates', 'static', 'public']
REQUIRED_FILES = ['config.toml']


def create_welcome_page():
    """Create welcome page and necessary files for new projects."""
    content_dir = Path('content')
    templates_dir = Path('templates')
    static_dir = Path('static/css')
    
    # Create directories if they don't exist
    content_dir.mkdir(parents=True, exist_ok=True)
    templates_dir.mkdir(parents=True, exist_ok=True)
    static_dir.mkdir(parents=True, exist_ok=True)
    
    # Create config.toml
    config_content = """site_name = "My StaticFlow Site"
base_url = "http://localhost:8000"
description = "A new StaticFlow site"
author = ""
language = "ru"

# Directories
source_dir = "content"
template_dir = "templates"
static_dir = "static"
output_dir = "public"

# Default settings
default_template = "base.html"
"""
    
    # Create welcome page
    welcome_content = """---
title: Welcome to StaticFlow
template: base.html
---
# Добро пожаловать в StaticFlow!

StaticFlow - это современный генератор статических сайтов с богатыми возможностями для создания контента.

## Возможности

### 1. Подсветка кода

```python
def hello_world():
    print("Привет, StaticFlow!")
```

### 2. Математические формулы

Inline формула: $E = mc^2$

Блочная формула:
$$
\\int_0^\\infty e^{-x} dx = 1
$$

### 3. Диаграммы

```mermaid
graph TD
    A[Начало] --> B[Создание контента]
    B --> C[Сборка сайта]
    C --> D[Публикация]
    D --> E[Конец]
```

### 4. Блоки в стиле Notion

:::info Информация
Это информационный блок. Используйте его для важных заметок.
:::

:::warning Предупреждение
Это блок с предупреждением. Обратите особое внимание!
:::

## Начало работы

1. Создание контента:
   - Добавьте Markdown файлы в директорию `content`
   - Используйте front matter для метаданных

2. Настройка шаблонов:
   - Измените шаблоны в директории `templates`
   - Добавьте свои стили в `static/css`

3. Запуск сервера разработки:
```bash
staticflow serve
```"""

    # Create base template
    base_template = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title }}</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <main>
        {{ page.content }}
    </main>
</body>
</html>"""

    # Create basic styles
    welcome_styles = """/* Base styles */
:root {
    --primary-color: #3b82f6;
    --text-color: #1f2937;
    --bg-color: #ffffff;
    --code-bg: #f8fafc;
    --border-color: #e5e7eb;
}

body {
    font-family: system-ui, -apple-system, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background: var(--bg-color);
    margin: 0;
    padding: 20px;
}

main {
    max-width: 800px;
    margin: 0 auto;
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

h1, h2, h3 {
    color: var(--primary-color);
}

h1 {
    font-size: 2.5rem;
    border-bottom: 2px solid var(--primary-color);
    padding-bottom: 0.5rem;
}

code {
    background: var(--code-bg);
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: monospace;
}

pre {
    background: var(--code-bg);
    padding: 1rem;
    border-radius: 0.5rem;
    overflow-x: auto;
}"""

    # Write files
    index_path = content_dir / 'index.md'
    template_path = templates_dir / 'base.html'
    style_path = static_dir / 'style.css'
    config_path = Path('config.toml')
    
    index_path.write_text(welcome_content)
    template_path.write_text(base_template)
    style_path.write_text(welcome_styles)
    config_path.write_text(config_content)


def validate_project_structure():
    """Validate project structure and permissions."""
    errors = []
    warnings = []
    
    # Check required directories
    for dir_name in REQUIRED_DIRECTORIES:
        dir_path = Path(dir_name)
        if not dir_path.exists():
            errors.append(f"Directory '{dir_name}' not found")
        elif not dir_path.is_dir():
            errors.append(f"'{dir_name}' exists but is not a directory")
        else:
            try:
                # Try to create a temporary file to test write permissions
                test_file = dir_path / '.write_test'
                test_file.touch()
                test_file.unlink()
            except (PermissionError, OSError):
                warnings.append(
                    f"Warning: Limited permissions on '{dir_name}' directory"
                )
    
    # Check content structure
    content_path = Path('content')
    if not content_path.exists() or not any(content_path.iterdir()):
        warnings.append("No content found - creating welcome page")
        try:
            create_welcome_page()
        except Exception as e:
            warnings.append(f"Failed to create welcome page: {str(e)}")
    
    return errors, warnings

class FileChangeHandler(FileSystemEventHandler):
    """Handler for file system changes."""
    
    def __init__(self, callback):
        self.callback = callback
        
    def on_modified(self, event):
        if not event.is_directory:
            self.callback(event.src_path)


class DevServer:
    """Development server with hot reload support."""
    
    def __init__(self, config: Config, host: str = 'localhost', port: int = 8000):
        self.config = config
        self.host = host
        self.port = port
        self.engine = Engine(config)
        
        # Initialize plugins
        self.engine.add_plugin(SyntaxHighlightPlugin())
        self.engine.add_plugin(MathPlugin())
        self.engine.add_plugin(MermaidPlugin())
        self.engine.add_plugin(NotionBlocksPlugin())
        
        # Validate project structure before starting
        errors, warnings = validate_project_structure()
        
        if errors:
            console.print(Panel(
                "\n".join([
                    "[red]Critical errors found:[/red]",
                    *[f"• {error}" for error in errors],
                    "\n[yellow]Please fix these issues before starting the server:[/yellow]",
                    "1. Make sure you're in the correct project directory",
                    "2. Check if all required directories and files exist",
                    "3. Verify file and directory permissions",
                    "\nProject structure should be:",
                    "project_name/",
                    "├── content/",
                    "│   └── pages/",
                    "├── templates/",
                    "├── static/",
                    "├── public/",
                    "└── config.toml"
                ]),
                title="[red]Project Structure Errors[/red]",
                border_style="red"
            ))
            raise SystemExit(1)
        
        if warnings:
            console.print(Panel(
                "\n".join([
                    "[yellow]Warnings:[/yellow]",
                    *[f"• {warning}" for warning in warnings]
                ]),
                title="[yellow]Project Structure Warnings[/yellow]",
                border_style="yellow"
            ))
            
        # Build the site before starting server
        self.engine.build()
        
    async def handle_request(self, request):
        """Handle incoming HTTP request."""
        path = request.path
        
        # Serve files from public directory
        if path == "/":
            path = "/index.html"
            
        file_path = Path(self.config.get("output_dir")) / path.lstrip("/")
        
        if not file_path.exists():
            return web.Response(status=404, text="Not Found")
            
        if not file_path.is_file():
            return web.Response(status=403, text="Forbidden")
            
        content_type = "text/html"
        if path.endswith(".css"):
            content_type = "text/css"
        elif path.endswith(".js"):
            content_type = "application/javascript"
            
        return web.FileResponse(file_path, headers={"Content-Type": content_type})
        
    def start(self):
        """Start the development server."""
        app = web.Application()
        app.router.add_get('/{tail:.*}', self.handle_request)
        
        web.run_app(app, host=self.host, port=self.port) 