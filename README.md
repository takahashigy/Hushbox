# Hushbox

[English](#english-version) | [中文](#中文版本)

---

## English Version

Hushbox is a secure, lightweight, and easy-to-use local password manager designed for cryptocurrency users.

---

### Features

- **Local Encryption:** All data is securely encrypted and stored locally.
- **Master Password:** Protect your accounts with a master password.
- **Account Management:** Add, view, and edit account details like AccountName, Password, and Notes.
- **Customizable Security:** Change master passwords anytime.
- **User-Friendly Interface:** A simple GUI for all levels of users.

---

### How to Use

1. **Set Master Password:**
   - Launch the application.
   - Set your initial master password when prompted.
   - ![1](https://github.com/user-attachments/assets/dc955646-9c14-41ff-8f27-cfc01458ddf1)
   - ![3](https://github.com/user-attachments/assets/e691fa55-7f63-412c-9a23-2650e3e13908)
   - ![4](https://github.com/user-attachments/assets/a27d213c-0c49-4693-9db1-1aeff668f3c2)

2. **Unlock Application:**
   - Enter your master password to access saved accounts.
   - ![6](https://github.com/user-attachments/assets/ecb59dbc-08c8-4d62-b960-120776a65905)

3. **Manage Accounts:**
   - Add accounts by clicking the "Add Account" button.
   - Edit existing accounts directly in the table.
   - ![8](https://github.com/user-attachments/assets/62e2babd-7e07-4dec-825f-e072c12bb7d4)
   - ![9](https://github.com/user-attachments/assets/6a8b21bf-9b68-4da6-9d16-571c7eaf811e)
   - ![10](https://github.com/user-attachments/assets/aa53210f-bedc-4128-a95d-aa52e35de793)

4. **Save Changes:**
   - Click the "Save Changes" button to save all updates.

---

### Installation

```bash
git clone https://github.com/takahashigy/Hushbox.git
cd Hushbox
pip install -r requirements.txt
python main.py

```
---

## 中文版本

Hushbox 是一款轻量级、安全且易用的本地密码管理器，专为加密货币用户设计。

---

### 功能

- **本地加密：** 所有数据使用 AES-256 进行加密，并存储在本地。
- **主密码保护：** 使用主密码保护您的账号信息。
- **账号管理：** 添加、查看和编辑账号的名称、密码和备注。
- **灵活安全性：** 随时更改主密码。
- **用户友好界面：** 简单易用的图形界面。

---

### 使用方法

1. **设置主密码：**
   - 启动应用程序。
   - 按提示设置您的初始主密码。
   - ![1](https://github.com/user-attachments/assets/dc955646-9c14-41ff-8f27-cfc01458ddf1)
   - ![3](https://github.com/user-attachments/assets/e691fa55-7f63-412c-9a23-2650e3e13908)
   - ![4](https://github.com/user-attachments/assets/a27d213c-0c49-4693-9db1-1aeff668f3c2)





2. **解锁应用程序：**
   - 输入主密码以访问保存的账号。
   - ![6](https://github.com/user-attachments/assets/ecb59dbc-08c8-4d62-b960-120776a65905)


3. **管理账号：**
   - 点击 “Add Account” 按钮添加账号。
   - 在表格中直接编辑已有账号。
   - ![8](https://github.com/user-attachments/assets/62e2babd-7e07-4dec-825f-e072c12bb7d4)
   - ![9](https://github.com/user-attachments/assets/6a8b21bf-9b68-4da6-9d16-571c7eaf811e)
   - ![10](https://github.com/user-attachments/assets/aa53210f-bedc-4128-a95d-aa52e35de793)




4. **保存更改：**
   - 点击 “Save Changes” 按钮保存更新。
   - 

---

### 安装方法

```bash
git clone https://github.com/takahashigy/Hushbox.git
cd Hushbox
pip install -r requirements.txt
python main.py
```
---
**文件说明**
- master_password.bin：
  存储加密后的主密码，无法直接读取。
- salt.bin：
  随机生成的加密盐值，用于密码加密，自动生成。
- encrypted_data.json：
  加密存储的账户数据，无法直接读取。
**注意事项**
 - 忘记主密码：
   如果忘记主密码，无法解密已存储的数据。建议妥善保存主密码。
 - 首次运行建议：
   若需要重新开始，您可以手动删除 master_password.bin 和 encrypted_data.json，软件会引导您重新设置主密码。
**数据隐私**：
- 所有数据均加密存储在本地，程序不会上传任何数据至网络。
- 杀毒软件兼容：
  某些杀毒软件可能误报，请将程序加入信任列表。

**版本信息**
- 当前版本
- 版本号: 1.0.0
- 发布日期: 2024-12-04

**常见问题**
- 无法解锁，显示“Decryption failed”错误：
  请检查输入的主密码是否正确。如果问题仍然存在，您可能需要删除 master_password.bin 和 encrypted_data.json，重新开始。
- 程序无法运行：
  确保下载的 Hushbox.exe 文件完整。
- 检查系统是否为 Windows 10 或更高版本。
- 密码显示不正确或文件损坏：
  如果 salt.bin 或其他文件被修改或删除，可能导致数据解密失败。建议重新初始化。

**未来计划**
- 增加云端同步功能（可选）。
- 添加密码生成器。
- 提供 Linux 和 macOS 版本支持。

**版权与许可**
- 作者: 高洋
- 许可: 仅限个人使用，禁止未经授权的商业用途。


