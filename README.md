Hushbox
Hushbox 是一款简洁高效的本地密码管理工具，专为加密货币玩家和注重隐私的用户设计。该软件具备强大的 AES-256 加密能力，所有数据均以加密形式存储在本地，确保您的账户信息安全。

一.功能特性
核心功能
1.主密码保护：
用户首次运行时设置主密码，所有数据均受主密码加密保护。
可通过“Set Master Password”功能随时更新主密码。
2.数据本地加密存储：
使用强大的 AES-256 加密算法，所有数据均存储在本地的 encrypted_data.json 文件中。
3.账户管理：
支持添加账户信息（AccountName、Password、Notes）。
表格中支持直接编辑账户名和备注，密码列默认隐藏，支持一键显示或隐藏。
4.实时编辑与保存：
支持双击表格直接修改账户信息。
点击 “Save Changes” 按钮保存所有更改至本地文件。

二.安装与运行

系统要求
操作系统：Windows 10 或更高版本。
依赖：不需要安装 Python 或其他库（.exe 已打包为独立文件）。

安装步骤
下载 Hushbox：
获取打包好的 Hushbox.exe 文件。

运行程序：
双击运行 Hushbox.exe，无需任何安装过程。

首次运行：
如果主密码未设置，程序将引导您设置主密码。

三.使用方法
首次运行
1.启动程序后，若未设置主密码，会弹出提示，要求设置主密码。
2.按提示输入新密码并确认，完成主密码设置。

解锁数据
1.输入您的主密码后，点击 Unlock 按钮，进入主界面。
2.若密码正确，您将看到保存的账户信息。

添加新账户
1.点击 Add Account 按钮。
2.输入以下信息：
AccountName: 账户名称（如“OKX 钱包”）。
Password: 账户密码。
Notes: 备注信息（如“我的交易账户”）。
3.点击 OK 保存。

四.编辑账户信息
双击编辑：
直接双击表格中的 AccountName 或 Notes 进行编辑。
显示/隐藏密码：
点击密码列的 👁 按钮切换密码显示状态，显示后可直接编辑密码。

五.保存更改
修改完成后，点击 Save Changes 按钮。
所有更改将加密存储到本地文件。

六.文件说明
master_password.bin：
存储加密后的主密码，无法直接读取。
salt.bin：
随机生成的加密盐值，用于密码加密，自动生成。
encrypted_data.json：
加密存储的账户数据，无法直接读取。


注意事项
忘记主密码：
如果忘记主密码，无法解密已存储的数据。建议妥善保存主密码。
首次运行建议：
若需要重新开始，您可以手动删除 master_password.bin 和 encrypted_data.json，软件会引导您重新设置主密码。
数据隐私：
所有数据均加密存储在本地，程序不会上传任何数据至网络。
杀毒软件兼容：
某些杀毒软件可能误报，请将程序加入信任列表。
版本信息
当前版本
版本号: 1.0.0
发布日期: 2024-12-04
常见问题
无法解锁，显示“Decryption failed”错误：
请检查输入的主密码是否正确。如果问题仍然存在，您可能需要删除 master_password.bin 和 encrypted_data.json，重新开始。
程序无法运行：
确保下载的 Hushbox.exe 文件完整。
检查系统是否为 Windows 10 或更高版本。
密码显示不正确或文件损坏：
如果 salt.bin 或其他文件被修改或删除，可能导致数据解密失败。建议重新初始化。
未来计划
增加云端同步功能（可选）。
添加密码生成器。
提供 Linux 和 macOS 版本支持。
版权与许可
作者: 高洋
许可: 仅限个人使用，禁止未经授权的商业用途。
如果需要进一步帮助或反馈问题，请联系作者

Hushbox
Hushbox is a simple and efficient local password manager designed for cryptocurrency enthusiasts and privacy-conscious users. It features robust AES-256 encryption to securely store all your data locally, ensuring your account information remains safe.

Features
Core Features
Master Password Protection:
Set a master password on the first run to encrypt all your data.
Update the master password anytime using the “Set Master Password” feature.
Local Data Encryption:
All data is stored locally in an encrypted format using AES-256 encryption.
Account Management:
Add accounts with AccountName, Password, and Notes fields.
Edit account names and notes directly in the table.
Passwords are hidden by default but can be toggled visible for editing.
Save Changes:
Save all modifications to the local encrypted file using the “Save Changes” button.
Installation and Usage
System Requirements
Operating System: Windows 10 or later.
Dependencies: None (the .exe file is standalone and does not require Python installation).
Installation Steps
Download Hushbox:
Obtain the Hushbox.exe file.
Run the Application:
Double-click Hushbox.exe to launch the program—no installation is required.
First-Time Setup:
If no master password is set, the program will prompt you to create one.
How to Use
First-Time Setup
On launching the program, if no master password is set, you will be prompted to create one.
Enter and confirm the new master password to complete the setup.
Unlocking Your Data
Enter your master password in the input field and click Unlock.
If the password is correct, you will access the main interface with your saved account information.
Adding a New Account
Click the Add Account button.
Provide the following details:
AccountName: Name of the account (e.g., “OKX Wallet”).
Password: Account password.
Notes: Additional information (e.g., “My trading account”).
Click OK to save.
Editing Account Information
Direct Editing:
Double-click the AccountName or Notes cell to edit directly.
Password Visibility:
Click the 👁 button in the Password column to toggle between hidden and visible states. When visible, the password can be edited directly.
Saving Changes
After making changes, click the Save Changes button.
All modifications will be securely saved to the local encrypted file.
File Descriptions
master_password.bin:
Stores the encrypted master password.
salt.bin:
Randomly generated cryptographic salt used for encryption. Automatically created.
encrypted_data.json:
Stores all account information in encrypted form.
Important Notes
Forgetting the Master Password:
If you forget your master password, it will be impossible to decrypt your data. Please store your master password securely.
First-Time Initialization:
If you wish to reset the application, delete master_password.bin and encrypted_data.json, and the program will guide you through setting a new master password.
Data Privacy:
All data is encrypted and stored locally. No information is uploaded to any server.
Antivirus Compatibility:
Some antivirus software might flag unknown .exe files. Add the file to your trusted list if flagged.
Version Information
Current Version
Version: 1.0.0
Release Date: 2024-12-04
FAQs
What happens if I enter the wrong master password?
The program will not unlock the data. Ensure you enter the correct password.
The application shows a “Decryption failed” error. What should I do?
Verify the master password. If the issue persists, delete master_password.bin and encrypted_data.json to reset.
How do I recover lost data?
Unfortunately, without the correct master password, your data cannot be recovered due to encryption.
Future Plans
Add cloud synchronization (optional).
Include a secure password generator.
Provide support for Linux and macOS platforms.
License and Credits
Author: Gao Yang
License: For personal use only. Unauthorized commercial use is prohibited.