import os

# 简单硬编码：证明自动化能创建目录
target_dir = "人工智能/WangZipeng"

# 创建目录（包括父目录）
os.makedirs(target_dir, exist_ok=True)

# 创建一个占位文件，证明目录被成功创建
placeholder = os.path.join(target_dir, "hello_from_automation.txt")
with open(placeholder, "w") as f:
    f.write("This directory was auto-created by GitHub Actions!\n")

print(f"✅ Successfully created: {target_dir}")