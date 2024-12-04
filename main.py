import sys
import os
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QInputDialog, QHeaderView, QDialog
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from encryption import EncryptionManager


class PasswordDialog(QDialog):
    """Dialog for setting or updating master password."""
    def __init__(self, parent=None, has_existing_password=False):
        super().__init__(parent)
        self.setWindowTitle("Set Master Password")
        self.setGeometry(300, 300, 400, 200)
        self.has_existing_password = has_existing_password
        self.old_password = None
        self.new_password = None
        self.confirm_password = None
        self.initUI()

    def initUI(self):
        """Initialize the dialog UI."""
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Old password input (only if an existing password is set)
        if self.has_existing_password:
            self.old_password_label = QLabel("Enter Old Password:")
            self.old_password_input = QLineEdit()
            self.old_password_input.setEchoMode(QLineEdit.Password)
            self.layout.addWidget(self.old_password_label)
            self.layout.addWidget(self.old_password_input)

        # New password input
        self.new_password_label = QLabel("Enter New Password:")
        self.new_password_input = QLineEdit()
        self.new_password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.new_password_label)
        self.layout.addWidget(self.new_password_input)

        # Confirm new password input
        self.confirm_password_label = QLabel("Confirm New Password:")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.confirm_password_label)
        self.layout.addWidget(self.confirm_password_input)

        # Buttons
        self.button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        self.button_layout.addWidget(self.ok_button)
        self.button_layout.addWidget(self.cancel_button)
        self.layout.addLayout(self.button_layout)

    def get_passwords(self):
        """Return the entered passwords."""
        if self.has_existing_password:
            self.old_password = self.old_password_input.text()
        self.new_password = self.new_password_input.text()
        self.confirm_password = self.confirm_password_input.text()
        return self.old_password, self.new_password, self.confirm_password


class HushboxApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hushbox")
        self.setGeometry(100, 100, 900, 600)
        self.setWindowIcon(QIcon("icon.png"))

        self.master_password_file = "master_password.bin"
        self.encryption = EncryptionManager()
        self.data_file = "encrypted_data.json"
        self.data = {}

        self.initUI()

        # Check if master password exists, prompt user to set it if missing
        if not os.path.exists(self.master_password_file):
            QMessageBox.information(self, "Information", "No master password set. Please set it now.")
            self.set_master_password()

    def initUI(self):
        """Initialize the user interface."""
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Unlock section
        self.label = QLabel("Enter Master Password:")
        self.layout.addWidget(self.label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.unlock_button = QPushButton("Unlock")
        self.unlock_button.clicked.connect(self.unlock)
        self.layout.addWidget(self.unlock_button)

        # Setting master password button
        self.set_password_button = QPushButton("Set Master Password")
        self.set_password_button.clicked.connect(self.set_master_password)
        self.layout.addWidget(self.set_password_button)

        # Account table (hidden until unlocked)
        self.table = QTableWidget(0, 4)  # 4 columns: AccountName, Password, Notes, Show/Hide
        self.table.setHorizontalHeaderLabels(["AccountName", "Password", "Notes", "Visibility"])
        self.table.horizontalHeader().setStyleSheet("""
        QHeaderView::section {
        background-color: #F6911D;
        color: white;
        font-weight: bold;
        border: 1px solid #dddddd;
        text-align: center;
        padding: 5px;
            }
        """)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)
        self.table.hide()

        # Add Account button
        self.add_button = QPushButton("Add Account")
        self.add_button.clicked.connect(self.add_account)
        self.layout.addWidget(self.add_button)
        self.add_button.hide()

        # Save changes button
        self.save_button = QPushButton("Save Changes")
        self.save_button.clicked.connect(self.save_changes)
        self.layout.addWidget(self.save_button)
        self.save_button.hide()

    def unlock(self):
        """Unlock the app with the master password."""
        if not os.path.exists(self.master_password_file):
            QMessageBox.warning(self, "Error", "No master password set! Please set it first.")
            return

        master_password = self.password_input.text()
        if not master_password:
            QMessageBox.warning(self, "Error", "Please enter the master password!")
            return

        try:
            # Load stored master password and attempt decryption
            with open(self.master_password_file, "rb") as f:
                stored_password_encrypted = f.read().decode()

            self.encryption.set_master_password(master_password)
            stored_password = self.encryption.decrypt(stored_password_encrypted)

            if master_password != stored_password:
                QMessageBox.warning(self, "Error", "Incorrect master password!")
                return

            self.encryption.set_master_password(master_password)
            self.data = self.load_data()

            # Update UI
            self.label.hide()
            self.password_input.hide()
            self.unlock_button.hide()
            self.set_password_button.hide()
            self.table.show()
            self.add_button.show()
            self.save_button.show()
            self.refresh_table()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to unlock: {e}")

    def set_master_password(self):
        """Set a new master password."""
        has_existing_password = os.path.exists(self.master_password_file)
        dialog = PasswordDialog(self, has_existing_password)
        if dialog.exec_() == QDialog.Accepted:
            old_password, new_password, confirm_password = dialog.get_passwords()
            try:
                if has_existing_password:
                    # Validate old password
                    with open(self.master_password_file, "rb") as f:
                        stored_password_encrypted = f.read().decode()
                    self.encryption.set_master_password(old_password)
                    stored_password = self.encryption.decrypt(stored_password_encrypted)
                    if old_password != stored_password:
                        QMessageBox.warning(self, "Error", "Old master password is incorrect!")
                        return

                # Validate new passwords
                if not new_password or not confirm_password:
                    QMessageBox.warning(self, "Error", "New password cannot be empty!")
                    return
                if new_password != confirm_password:
                    QMessageBox.warning(self, "Error", "Passwords do not match!")
                    return

                # Save new master password
                self.encryption.set_master_password(new_password)
                with open(self.master_password_file, "wb") as f:
                    f.write(self.encryption.encrypt(new_password).encode())
                QMessageBox.information(self, "Success", "Master password updated successfully!")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to set new master password: {e}")

    def add_account(self):
        """Add a new account."""
        account, ok = QInputDialog.getText(self, "Add Account", "Account Name:")
        if not ok or not account:
            return

        password, ok = QInputDialog.getText(self, "Add Password", "Password:")
        if not ok or not password:
            return

        note, ok = QInputDialog.getText(self, "Add Note", "Note:")
        if not ok:
            note = ""

        self.data[account] = {"password": password, "note": note}
        self.save_data()
        self.refresh_table()

    def save_changes(self):
        """Save changes made in the table."""
        updated_data = {}
        for row in range(self.table.rowCount()):
            account = self.table.item(row, 0).text()
            password = self.table.item(row, 1).text()
            note = self.table.item(row, 2).text()

            if password == "********":
                password = self.data[account]["password"]

            updated_data[account] = {"password": password, "note": note}

        self.data = updated_data
        self.save_data()
        QMessageBox.information(self, "Success", "Changes saved successfully!")

    def refresh_table(self):
        """Refresh the account list display in the table."""
        self.table.setRowCount(0)
        for account, details in self.data.items():
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            # AccountName
            account_item = QTableWidgetItem(account)
            self.table.setItem(row_position, 0, account_item)

            # Password
            password_item = QTableWidgetItem("********")
            self.table.setItem(row_position, 1, password_item)

            # Notes
            notes_item = QTableWidgetItem(details["note"])
            self.table.setItem(row_position, 2, notes_item)

            # Visibility button
            visibility_button = QPushButton("👁")
            visibility_button.clicked.connect(lambda _, r=row_position: self.toggle_password_visibility(r))
            self.table.setCellWidget(row_position, 3, visibility_button)

    def toggle_password_visibility(self, row):
        """Toggle visibility of the password."""
        password_item = self.table.item(row, 1)
        account_name = self.table.item(row, 0).text()

        if password_item.text() == "********":
            password_item.setText(self.data[account_name]["password"])
        else:
            password_item.setText("********")

    def load_data(self):
        """Load and decrypt data from file."""
        if not os.path.exists(self.data_file):
            return {}
        with open(self.data_file, "r") as f:
            encrypted_data = f.read()
        return json.loads(self.encryption.decrypt(encrypted_data))

    def save_data(self):
        """Encrypt and save data to file."""
        encrypted_data = self.encryption.encrypt(json.dumps(self.data))
        with open(self.data_file, "w") as f:
            f.write(encrypted_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HushboxApp()
    window.show()
    sys.exit(app.exec_())



