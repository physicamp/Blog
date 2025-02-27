# Legacy vs. UEFI Boot Modes: Definitions and Differences

## 1️⃣ What is Legacy BIOS?
**Legacy BIOS (Basic Input/Output System)** is the traditional firmware used to initialize hardware and boot an operating system.

### 🔹 **Characteristics of Legacy BIOS:**
- Uses **MBR (Master Boot Record)** for boot management.
- Can only boot from drives **up to 2TB** in size.
- Supports a maximum of **4 primary partitions**.
- **No Secure Boot** (less security).
- Loads bootloader from the **first sector** of the boot disk.
- **Slower boot process** compared to UEFI.

---

## 2️⃣ What is UEFI?
**UEFI (Unified Extensible Firmware Interface)** is the modern replacement for BIOS, offering more features and better performance.

### 🔹 **Characteristics of UEFI:**
- Uses **GPT (GUID Partition Table)** instead of MBR.
- Supports **drives larger than 2TB**.
- Allows **128 primary partitions** (vs. 4 in MBR).
- Supports **Secure Boot**, preventing unauthorized OS booting.
- Can boot from **EFI partitions** instead of the first disk sector.
- **Faster boot times** than Legacy BIOS.

---

## 3️⃣ Differences Between Legacy and UEFI
| Feature        | Legacy BIOS | UEFI |
|--------------|------------|------|
| Boot Method  | Uses MBR | Uses GPT |
| Max Disk Size | 2TB | 9ZB+ |
| Partitions | 4 Primary | 128+ |
| Secure Boot | ❌ No | ✅ Yes |
| Speed | Slower | Faster |
| Compatibility | Older Systems | Modern Systems |

---

## 4️⃣ How to Check if Your System is Using UEFI or Legacy
### ✅ **Windows (CMD/PowerShell Method)**
1. Open **Command Prompt** as Administrator.
2. Run:
   ```sh
   bcdedit /enum | find "Firmware"

