import sys
import os
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton,
    QTextEdit, QLineEdit, QFileDialog, QTableWidget, QTableWidgetItem, QLabel, QMessageBox, QDialog, QInputDialog, QSizePolicy, QComboBox, QTabWidget
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, pyqtSignal, QThread
from PyQt5.QtGui import QFont, QColor, QIcon, QPixmap
from g4f.client import Client
import black  # Для форматирования кода
import keyboard  # Для обработки нажатий клавиш
from importlib.resources import files

class FileWidget(QWidget):
    def __init__(self, file_name, file_size, file_content, parent=None):
        super().__init__(parent)
        self.file_content = file_content
        self.parent_app = parent  # Сохраняем ссылку на родительский виджет
        self.initUI(file_name, file_size)

    def initUI(self, file_name, file_size):
        layout = QHBoxLayout()
        icon_label = QLabel()
        icon_label.setPixmap(QIcon.fromTheme("document").pixmap(24, 24))  # Используем стандартную иконку
        layout.addWidget(icon_label)
        file_info = QVBoxLayout()
        name_label = QLabel(file_name)
        size_label = QLabel(f"{file_size} KB")
        file_info.addWidget(name_label)
        file_info.addWidget(size_label)
        layout.addLayout(file_info)
        self.delete_button = QPushButton("Delete")
        self.delete_button.setStyleSheet("""
        QPushButton {
        background-color: #FF4500;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 5px;
        font-size: 12px;
        }
        QPushButton:hover {
        background-color: #FF6347;
        }
        """)
        self.delete_button.clicked.connect(self.delete_file)
        layout.addWidget(self.delete_button)
        self.setLayout(layout)
        self.setStyleSheet("""
        QWidget {
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        }
        QLabel {
        font-size: 12px;
        }
        """)
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.show_file_content()

    def show_file_content(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("File Content")
        dialog.setLayout(QVBoxLayout())
        if isinstance(self.file_content, pd.DataFrame):
            table_view = QTableWidget()
            table_view.setRowCount(self.file_content.shape[0])
            table_view.setColumnCount(self.file_content.shape[1])
            table_view.setHorizontalHeaderLabels(self.file_content.columns)
            for row in range(self.file_content.shape[0]):
                for col in range(self.file_content.shape[1]):
                    item = QTableWidgetItem(str(self.file_content.iat[row, col]))
                    table_view.setItem(row, col, item)
            table_view.resizeColumnsToContents()
            table_view.setStyleSheet("""
            QTableWidget {
            background-color: #f9f9f9;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            font-size: 14px;
            }
            QHeaderView::section {
            background-color: #4CAF50;
            color: white;
            padding: 0px;
            border: 1px solid #ccc;
            font-size: 28px;
            }
            """)
            dialog.layout().addWidget(table_view)
        else:
            content_display = QTextEdit()
            content_display.setReadOnly(True)
            content_display.setText(self.file_content)
            content_display.setStyleSheet("""
            QTextEdit {
            background-color: #f9f9f9;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            font-size: 14px;
            }
            """)
            dialog.layout().addWidget(content_display)
        dialog.exec_()

    def delete_file(self):
        self.parent_app.remove_file(self)

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setLayout(QVBoxLayout())
        self.initUI()

    def initUI(self):
        self.model_label = QLabel("Select Model:")
        self.model_label.setStyleSheet("font-size: 14px; padding: 5px;")
        self.layout().addWidget(self.model_label)
        self.model_selector = QComboBox()
        self.model_selector.addItems(["gpt-4o-mini", "llama-3.3-70b", "llama-3.2-90b", "gpt-4o", "qwen-2.5-1m-demo", "qwen-2.5-coder-32b", "qwen-2.5-72b", "deepseek-v3", "deepseek-r1"])
        self.model_selector.setStyleSheet("""
        QComboBox {
        background-color: #fff;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        font-size: 14px;
        }
        QComboBox::drop-down {
        border: none;
        }
        QComboBox QAbstractItemView {
        background-color: #fff;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        font-size: 14px;
        }
        """)
        self.layout().addWidget(self.model_selector)
        self.save_button = QPushButton("Save")
        self.save_button.setStyleSheet("""
        QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
        font-size: 14px;
        }
        QPushButton:hover {
        background-color: #45a049;
        }
        """)
        self.save_button.clicked.connect(self.accept)
        self.layout().addWidget(self.save_button)

    def get_selected_model(self):
        return self.model_selector.currentText()

class NeuralNetworkApp(QMainWindow):
    hide_signal = pyqtSignal()
    show_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Neural Network GUI with PyQt5")
        self.setGeometry(100, 100, 1200, 800)
        # Initialize the neural network client
        self.client = Client()
        # Store loaded database content
        self.db_contents = []
        # Store conversation history
        self.conversation_history = []
        # Load system prompts from files
        self.system_prompt = self.load_system_prompt("system_prompt.txt")
        self.script_analysis_prompt = self.load_system_prompt("script_analysis_prompt.txt")
        self.python_db_prompt = self.load_system_prompt("python_db_prompt.txt")
        # Store loaded Python script content
        self.python_script_contents = []
        # Store current model
        self.current_model = "gpt-4o-mini"
        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        # Tab widget
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)
        # Main tab
        self.main_tab = QWidget()
        self.main_layout = QHBoxLayout(self.main_tab)
        self.tab_widget.addTab(self.main_tab, "Main")
        # Chat interface
        self.chat_layout = QVBoxLayout()
        # Chat history display
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.chat_history.setStyleSheet("""
        QTextEdit {
        background-color: #f9f9f9;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
        }
        """)
        self.chat_layout.addWidget(self.chat_history)
        # Input field and send button
        self.input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message here...")
        self.input_field.setStyleSheet("""
        QLineEdit {
        background-color: #fff;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
        }
        """)
        self.input_layout.addWidget(self.input_field)
        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet("""
        QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 15px;
        font-size: 16px;
        }
        QPushButton:hover {
        background-color: #45a049;
        }
        """)
        self.send_button.clicked.connect(self.send_message)
        self.input_layout.addWidget(self.send_button)
        self.chat_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(self.chat_layout)
        # File load buttons and display area
        self.file_load_layout = QVBoxLayout()
        self.load_db_button = QPushButton("Load Database")
        self.load_db_button.setStyleSheet("""
        QPushButton {
        background-color: #008CBA;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 15px;
        font-size: 16px;
        }
        QPushButton:hover {
        background-color: #007B9A;
        }
        """)
        self.load_db_button.clicked.connect(self.load_database)
        self.file_load_layout.addWidget(self.load_db_button)
        self.load_script_button = QPushButton("Load Python Script (.py)")
        self.load_script_button.setStyleSheet("""
        QPushButton {
        background-color: #FF5733;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 15px;
        font-size: 16px;
        }
        QPushButton:hover {
        background-color: #E64A19;
        }
        """)
        self.load_script_button.clicked.connect(self.load_python_script)
        self.file_load_layout.addWidget(self.load_script_button)
        self.settings_button = QPushButton("Settings")
        self.settings_button.setStyleSheet("""
        QPushButton {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 15px;
        font-size: 16px;
        }
        QPushButton:hover {
        background-color: #2980b9;
        }
        """)
        self.settings_button.clicked.connect(self.open_settings)
        self.file_load_layout.addWidget(self.settings_button)
        self.file_display_layout = QVBoxLayout()
        self.file_display_layout.setAlignment(Qt.AlignTop)
        self.file_load_layout.addLayout(self.file_display_layout)
        self.main_layout.addLayout(self.file_load_layout)
        # Guide tab
        self.guide_tab = QWidget()
        self.guide_layout = QHBoxLayout(self.guide_tab)
        self.tab_widget.addTab(self.guide_tab, "Руководство")
        # Chat interface for guide
        self.guide_chat_layout = QVBoxLayout()
        # Chat history display for guide
        self.guide_chat_history = QTextEdit()
        self.guide_chat_history.setReadOnly(True)
        self.guide_chat_history.setStyleSheet("""
        QTextEdit {
        background-color: #f9f9f9;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
        }
        """)
        self.guide_chat_layout.addWidget(self.guide_chat_history)
        # Input field and send button for guide
        self.guide_input_layout = QHBoxLayout()
        self.guide_input_field = QLineEdit()
        self.guide_input_field.setPlaceholderText("Type your message here...")
        self.guide_input_field.setStyleSheet("""
        QLineEdit {
        background-color: #fff;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
        }
        """)
        self.guide_input_layout.addWidget(self.guide_input_field)
        self.guide_send_button = QPushButton("Send")
        self.guide_send_button.setStyleSheet("""
        QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 15px;
        font-size: 16px;
        }
        QPushButton:hover {
        background-color: #45a049;
        }
        """)
        self.guide_send_button.clicked.connect(self.send_guide_message)
        self.guide_input_layout.addWidget(self.guide_send_button)
        self.guide_chat_layout.addLayout(self.guide_input_layout)
        self.guide_layout.addLayout(self.guide_chat_layout)
        # File load button and display area for guide
        self.guide_file_load_layout = QVBoxLayout()
        self.guide_load_script_button = QPushButton("Загрузить скрипт Python")
        self.guide_load_script_button.setStyleSheet("""
        QPushButton {
        background-color: #FF5733;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 15px;
        font-size: 16px;
        }
        QPushButton:hover {
        background-color: #E64A19;
        }
        """)
        self.guide_load_script_button.clicked.connect(self.load_guide_python_script)
        self.guide_file_load_layout.addWidget(self.guide_load_script_button)
        self.guide_file_display_layout = QVBoxLayout()
        self.guide_file_display_layout.setAlignment(Qt.AlignTop)
        self.guide_file_load_layout.addLayout(self.guide_file_display_layout)
        self.guide_layout.addLayout(self.guide_file_load_layout)
        # Initialize keyboard shortcuts
        self.hide_signal.connect(self.hide)
        self.show_signal.connect(self.show)
        self.init_keyboard_shortcuts()
        # Loading animation overlay
        self.loading_overlay = QWidget(self)
        self.loading_overlay.setStyleSheet("""
        background-color: rgba(0, 0, 0, 150);
        """)
        self.loading_overlay.hide()
        self.loading_overlay.resize(self.width(), self.height())
        self.loading_label = QLabel("Loading...", self.loading_overlay)
        self.loading_label.setStyleSheet("""
        color: white;
        font-size: 24px;
        """)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setGeometry(0, 0, self.width(), self.height())

    def init_keyboard_shortcuts(self):
        keyboard.add_hotkey('ctrl + num 5', self.hide_window)
        keyboard.add_hotkey('ctrl + num 8', self.show_window)
        keyboard.add_hotkey('ctrl + num 1', self.decrease_opacity)
        keyboard.add_hotkey('ctrl + num 2', self.increase_opacity)

    def hide_window(self):
        self.hide_signal.emit()

    def show_window(self):
        self.show_signal.emit()

    def decrease_opacity(self):
        current_opacity = self.windowOpacity()
        new_opacity = max(0.05, current_opacity - 0.05)
        self.setWindowOpacity(new_opacity)

    def increase_opacity(self):
        current_opacity = self.windowOpacity()
        new_opacity = min(1.0, current_opacity + 0.05)
        self.setWindowOpacity(new_opacity)

    def open_settings(self):
        dialog = SettingsDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.current_model = dialog.get_selected_model()
            QMessageBox.information(self, "Model Changed", f"Model changed to {self.current_model}")

    def load_system_prompt(self, file_name):
        """Load system prompt from a text file."""
        try:
            resource_path = files('module_aifree').joinpath(file_name)
            with open(resource_path, "r", encoding="utf-8") as file:
                return file.read().strip()
        except Exception as e:
            QMessageBox.warning(self, "System Prompt Error", f"Failed to load system prompt: {str(e)}")
            return ""

    def format_code(self, code):
        """Format Python code using Black."""
        try:
            formatted_code = black.format_str(code, mode=black.FileMode())
            return formatted_code
        except Exception as e:
            return f"Error formatting code: {str(e)}"

    def process_response(self, response):
        """Process the response to handle code blocks and formatting."""
        if "```python" in response:
            parts = response.split("```python")
            formatted_parts = [parts[0]]
            for part in parts[1:]:
                code, *rest = part.split("```", 1)
                try:
                    formatted_code = black.format_str(code.strip(), mode=black.FileMode())
                    formatted_parts.append(f"```python\n{formatted_code}\n```")
                except Exception as e:
                    formatted_parts.append(f"```python\n# Error formatting code: {str(e)}\n{code.strip()}\n```")
                if rest:
                    formatted_parts.append(rest[0])
            response = "".join(formatted_parts)
        return response

    def save_python_script(self, script_content):
        """Prompt the user to choose a path and name to save a Python script."""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Python Script",
            "",  # Начальный путь (пустой - текущая директория)
            "Python Files (*.py);;All Files (*)",
            options=options
        )
        if file_path:
            try:
                if not file_path.endswith(".py"):
                    file_path += ".py"
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(script_content)
                QMessageBox.information(self, "Success", f"Script saved successfully at:\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save script: {str(e)}")

    def save_documentation(self, documentation_content):
        """Prompt the user to choose a path and name to save a documentation file."""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Documentation",
            "",  # Начальный путь (пустой - текущая директория)
            "Text Files (*.txt);;All Files (*)",
            options=options
        )
        if file_path:
            try:
                if not file_path.endswith(".txt"):
                    file_path += ".txt"
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(documentation_content)
                QMessageBox.information(self, "Success", f"Documentation saved successfully at:\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save documentation: {str(e)}")

    def send_message(self):
        user_message = self.input_field.text().strip()
        if not user_message:
            QMessageBox.warning(self, "Input Error", "Please enter a message.")
            return
        self.conversation_history.append({"role": "user", "content": user_message})
        self.chat_history.append(f"You: {user_message}")
        self.input_field.clear()

        # Show loading animation
        self.loading_overlay.show()

        # Prepare the full prompt for the neural network
        db_context = ""
        for db_content in self.db_contents:
            db_context += f"Database content:\n{db_content}\n\n"
        messages = [{"role": "system", "content": self.system_prompt}]
        if self.script_analysis_prompt:
            messages.append({"role": "system", "content": self.script_analysis_prompt})
        if self.python_db_prompt:
            messages.append({"role": "system", "content": self.python_db_prompt})
        if db_context:
            messages.append({"role": "system", "content": db_context})
        messages.extend(self.conversation_history)

        # Start worker thread
        self.worker = Worker(self.client, self.current_model, messages)
        self.worker.finished.connect(self.handle_response)
        self.worker.error.connect(self.handle_error)
        self.worker.start()

    def handle_response(self, bot_message):
        # Process the response to handle code formatting
        bot_message = self.process_response(bot_message)

        # Check if the response contains a Python script
        if "```python" in bot_message:
            parts = bot_message.split("```python")
            for part in parts[1:]:
                code, *_ = part.split("```", 1)
                self.save_python_script(code.strip())

        # Add bot message to conversation history
        self.conversation_history.append({"role": "assistant", "content": bot_message})

        # Display the bot's response in the chat history
        self.chat_history.append(f"Bot:\n{bot_message}")

        # Hide loading animation
        self.loading_overlay.hide()

    def handle_error(self, error_message):
        self.chat_history.append(f"Error: {error_message}")
        self.loading_overlay.hide()

    def send_guide_message(self):
        user_message = self.guide_input_field.text().strip()
        if not user_message:
            QMessageBox.warning(self, "Input Error", "Please enter a message.")
            return
        self.conversation_history.append({"role": "user", "content": user_message})
        self.guide_chat_history.append(f"You: {user_message}")
        self.guide_input_field.clear()

        # Show loading animation
        self.loading_overlay.show()

        # Prepare the full prompt for the neural network
        db_context = ""
        for db_content in self.db_contents:
            db_context += f"Database content:\n{db_content}\n\n"
        messages = [{"role": "system", "content": self.system_prompt}]
        if self.script_analysis_prompt:
            messages.append({"role": "system", "content": self.script_analysis_prompt})
        if self.python_db_prompt:
            messages.append({"role": "system", "content": self.python_db_prompt})
        if db_context:
            messages.append({"role": "system", "content": db_context})
        messages.extend(self.conversation_history)

        # Start worker thread
        self.worker = Worker(self.client, self.current_model, messages)
        self.worker.finished.connect(self.handle_guide_response)
        self.worker.error.connect(self.handle_guide_error)
        self.worker.start()

    def handle_guide_response(self, bot_message):
        # Process the response to handle code formatting
        bot_message = self.process_response(bot_message)

        # Add bot message to conversation history
        self.conversation_history.append({"role": "assistant", "content": bot_message})

        # Display the bot's response in the chat history
        self.guide_chat_history.append(f"Bot:\n{bot_message}")

        # Save the conversation history to a file
        self.save_documentation(bot_message)

        # Hide loading animation
        self.loading_overlay.hide()

    def handle_guide_error(self, error_message):
        self.guide_chat_history.append(f"Error: {error_message}")
        self.loading_overlay.hide()

    def load_database(self):
        options = QFileDialog.Options()
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, "Open Database Files", "", "All Files (*);;Excel Files (*.xlsx *.xls);;SQLite Files (*.db *.sqlite)", options=options
        )
        if file_paths:
            for file_path in file_paths:
                try:
                    if file_path.endswith(('.xlsx', '.xls')):
                        df = pd.read_excel(file_path)
                    elif file_path.endswith(('.db', '.sqlite')):
                        import sqlite3
                        conn = sqlite3.connect(file_path)
                        query = "SELECT * FROM sqlite_master WHERE type='table';"
                        tables = pd.read_sql_query(query, conn)
                        table_name = tables['tbl_name'][0]
                        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
                        conn.close()
                    else:
                        raise ValueError("Unsupported file format.")
                    self.db_contents.append(df)
                    self.display_file_widget(file_path, df)
                    QMessageBox.information(self, "Success", "Database loaded successfully!")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed to load database: {str(e)}")

    def display_file_widget(self, file_path, file_content):
        file_name = file_path.split('/')[-1]
        file_size = f"{os.path.getsize(file_path) // 1024}"  # Size in KB
        file_widget = FileWidget(file_name, file_size, file_content, self)
        self.file_display_layout.addWidget(file_widget)

    def load_python_script(self):
        options = QFileDialog.Options()
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, "Open Python Scripts", "", "Python Files (*.py)", options=options
        )
        if file_paths:
            for file_path in file_paths:
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        script_content = file.read()
                    self.python_script_contents.append(script_content)
                    self.display_file_widget(file_path, script_content)
                    QMessageBox.information(self, "Success", "Python scripts loaded successfully!")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed to load Python script: {str(e)}")

    def load_guide_python_script(self):
        options = QFileDialog.Options()
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, "Open Python Scripts", "", "Python Files (*.py)", options=options
        )
        if file_paths:
            for file_path in file_paths:
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        script_content = file.read()
                    self.python_script_contents.append(script_content)
                    self.display_guide_file_widget(file_path, script_content)
                    QMessageBox.information(self, "Success", "Python scripts loaded successfully!")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed to load Python script: {str(e)}")

    def display_guide_file_widget(self, file_path, file_content):
        file_name = file_path.split('/')[-1]
        file_size = f"{os.path.getsize(file_path) // 1024}"  # Size in KB
        file_widget = FileWidget(file_name, file_size, file_content, self)
        self.guide_file_display_layout.addWidget(file_widget)

    def remove_file(self, file_widget):
        file_content = file_widget.file_content
        if isinstance(file_content, pd.DataFrame):
            self.db_contents.remove(file_content)
        else:
            self.python_script_contents.remove(file_content)
        self.file_display_layout.removeWidget(file_widget)
        self.guide_file_display_layout.removeWidget(file_widget)
        file_widget.deleteLater()
        QMessageBox.information(self, "Success", "File removed successfully!")

class Worker(QThread):
    finished = pyqtSignal(str)  # Сигнал для передачи результата
    error = pyqtSignal(str)     # Сигнал для передачи ошибки

    def __init__(self, client, model, messages):
        super().__init__()
        self.client = client
        self.model = model
        self.messages = messages

    def run(self):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                web_search=False,
                max_tokens=8192
            )
            bot_message = response.choices[0].message.content.strip()
            self.finished.emit(bot_message)
        except Exception as e:
            self.error.emit(str(e))

def main():
    app = QApplication(sys.argv)
    window = NeuralNetworkApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()