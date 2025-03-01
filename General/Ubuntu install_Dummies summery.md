# Ubuntu Installation and Configuration Issues on Lenovo Ideapad 320

## 1️⃣ Checking UEFI Boot Support
- If UEFI boot options do not appear in BIOS, your laptop may not support UEFI USB boot.
- Ensure USB is formatted as **GPT** and use **Rufus** (Windows) or **Balena Etcher** (Linux) to create a bootable USB.

## 2️⃣ Fixing "System Doesn't Have Any USB Boot Option"
- Enter BIOS and ensure **Secure Boot is disabled**.
- Enable **Legacy Boot (if needed)** and select USB as **first boot priority**.
- Use a USB 2.0 port if USB 3.0 is causing issues.

## 3️⃣ Choosing the Correct Ubuntu Installation Option
- **Option 1: "Install Ubuntu alongside Windows"** → Risky if insufficient space.
- **Option 2: "Erase disk and install Ubuntu"** → Deletes Windows (not recommended).
- **✅ Option 3: "Something Else"** → Best choice for installing on pre-allocated free space.

## 4️⃣ Manual Partitioning for Ubuntu Installation
1. Select the **free space** you prepared earlier.
2. Create a **root (`/`) partition** (30GB+ Ext4 filesystem).
3. (Optional) Create a **swap partition** (same size as RAM).
4. **For UEFI:** Use existing **EFI partition (`/dev/sda1`)** as `/boot/efi` (do not format).
5. Install **GRUB bootloader** to the correct disk:
   - **UEFI:** `/dev/sda1` (EFI partition)
   - **Legacy BIOS:** `/dev/sda` (main disk)

## 5️⃣ Fixing GRUB Bootloader Issues
- If Windows is missing from GRUB after installation:
  ```bash
  sudo update-grub
  ```
- If GRUB fails during installation, manually install it:
  ```bash
  sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=ubuntu
  sudo update-grub
  ```

## 6️⃣ Changing Drive Letter Assignments in Windows
1. Open **Disk Management (`diskmgmt.msc`)**.
2. Right-click the USB or HDD partition → **"Change Drive Letter and Paths"**.
3. Assign SSD as **C, D, E, F** and USB as **G**.

## 7️⃣ Changing Installation and Download Paths in Ubuntu
- **Change APT download path:**
  ```bash
  echo 'Dir::Cache "/mnt/newdrive/apt-cache/";' | sudo tee /etc/apt/apt.conf.d/02cache
  ```
- **Move Snap apps to another drive:**
  ```bash
  sudo mv /var/lib/snapd /mnt/newdrive/snap
  sudo ln -s /mnt/newdrive/snap /var/lib/snapd
  sudo systemctl restart snapd
  ```
- **Change Flatpak installation path:**
  ```bash
  sudo mkdir -p /mnt/newdrive/flatpak
  sudo flatpak remote-add --system new-repo file:///mnt/newdrive/flatpak
  ```

## 🚀 Summary
✅ **Ensure correct boot settings in BIOS.**
✅ **Use "Something Else" to manually install Ubuntu in free space.**
✅ **Properly configure GRUB bootloader to dual boot with Windows.**
✅ **Modify download and installation paths for efficient storage management.**

---
Now your Ubuntu installation is properly configured with Windows! 🎯🔥
