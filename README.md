# Khan Bank Fake Transaction Generator (Educational Use Only)

This Python script visually simulates a Khan Bank transaction confirmation screen by overlaying user input onto a predefined image template.

> ⚠️ **For educational purposes only.**
> This tool is meant to help students and developers learn about image processing with Python. Do not use it to deceive others or fabricate financial information.

---

## 📥 Clone & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Hexarion890/KhanBankFakeTransaction.git
   cd KhanBankFakeTransaction
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure the following files are present**:

   * `FakeProof.py` – the main Python script
   * `FakeProof.jpg` – the base template image (Khan Bank UI)

4. **Run the script**:

   ```bash
   python FakeProof.py
   ```

---

## 💡 How It Works

The script uses the `Pillow` library to modify an image (`FakeProof.jpg`) by inserting the following user-supplied values:

* 💰 **MONGO** – Transaction amount
* 👤 **NER** – Receiver's name
* 🔢 **DANS** – Account number
* 📝 **UTAG** – Transaction note
* 🕒 **TIME** and **TIME2** – Auto-generated timestamps

Each value is placed accurately over the base image using coordinates and fonts specified in the script config.

The image is saved with an auto-incremented filename (e.g., `output1.jpg`, `output2.jpg`) to avoid overwriting.

---

## 🧪 Example Input
```bash
Enter the MONGO (amount): 50,000.00 MNT      --better to put lower then 5,000.00
Enter the NER (name): Бат-Эрдэнэ
Enter the DANS (account number): 1234 567 890
Enter the UTAG (transaction note): Хоолны мөнгө
```

The script will embed this data on the image and show the generated transaction screen.

---

## 🛠 Configuration

You can customize:

* Font sizes, colors, and spacing
* Text positions
* Output file naming

All configurations are in the top section of `FakeProof.py`.

---

## 📌 Legal & Ethical Disclaimer

This script is intended **only for educational and illustrative purposes** such as UI demos, learning Python image editing, or practicing automation.

❗ **Misuse is strictly discouraged.** Creating fake or fraudulent documents may be illegal and could lead to serious consequences.

---

## 🔗 License

This project is provided "as is" with no warranty. Use at your own risk. Educational use only.

```
