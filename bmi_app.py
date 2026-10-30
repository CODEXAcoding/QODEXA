import tkinter as tk
from tkinter import ttk, messagebox

class AdvancedBMISoftware(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Health & BMI Advisor")
        self.geometry("520x720")
        self.configure(bg="#eef2f5")
        self.resizable(False, False)

        # Header Title
        tk.Label(
            self, 
            text="Smart Health & BMI Advisor", 
            font=("Segoe UI", 18, "bold"), 
            bg="#eef2f5", 
            fg="#1a365d"
        ).pack(pady=15)

        # Input Card
        input_card = tk.Frame(self, bg="#ffffff", padx=20, pady=15, relief="flat", bd=0)
        input_card.pack(padx=20, pady=5, fill="x")

        # Input: Age
        tk.Label(input_card, text="Age (Years):", font=("Segoe UI", 10, "bold"), bg="#ffffff").grid(row=0, column=0, sticky="w", pady=6)
        self.age_entry = tk.Entry(input_card, font=("Segoe UI", 10), width=22, relief="solid", bd=1)
        self.age_entry.grid(row=0, column=1, pady=6, padx=10)

        # Input: Gender
        tk.Label(input_card, text="Gender:", font=("Segoe UI", 10, "bold"), bg="#ffffff").grid(row=1, column=0, sticky="w", pady=6)
        self.gender_combo = ttk.Combobox(input_card, values=["Male", "Female"], state="readonly", width=20)
        self.gender_combo.current(0)
        self.gender_combo.grid(row=1, column=1, pady=6, padx=10)

        # Input: Height
        tk.Label(input_card, text="Height (cm):", font=("Segoe UI", 10, "bold"), bg="#ffffff").grid(row=2, column=0, sticky="w", pady=6)
        self.height_entry = tk.Entry(input_card, font=("Segoe UI", 10), width=22, relief="solid", bd=1)
        self.height_entry.grid(row=2, column=1, pady=6, padx=10)

        # Input: Weight
        tk.Label(input_card, text="Weight (kg):", font=("Segoe UI", 10, "bold"), bg="#ffffff").grid(row=3, column=0, sticky="w", pady=6)
        self.weight_entry = tk.Entry(input_card, font=("Segoe UI", 10), width=22, relief="solid", bd=1)
        self.weight_entry.grid(row=3, column=1, pady=6, padx=10)

        # Submit Button
        btn_calc = tk.Button(
            self, 
            text="Analyze Health Profile", 
            font=("Segoe UI", 11, "bold"), 
            bg="#2b6cb0", 
            fg="white", 
            activebackground="#2c5282",
            activeforeground="white",
            bd=0, 
            pady=10, 
            cursor="hand2",
            command=self.calculate_and_analyze
        )
        btn_calc.pack(padx=20, pady=12, fill="x")

        # Output Card Setup
        self.output_card = tk.Frame(self, bg="#ffffff", padx=20, pady=15, relief="flat", bd=0)
        self.output_card.pack(padx=20, pady=5, fill="both", expand=True)

        self.lbl_bmi = tk.Label(self.output_card, text="BMI: --", font=("Segoe UI", 15, "bold"), bg="#ffffff", fg="#2d3748")
        self.lbl_bmi.pack(pady=2)

        self.lbl_status = tk.Label(self.output_card, text="Status: --", font=("Segoe UI", 12, "bold"), bg="#ffffff", fg="#718096")
        self.lbl_status.pack(pady=2)

        self.lbl_ideal = tk.Label(self.output_card, text="Ideal Weight Range: --", font=("Segoe UI", 9), bg="#ffffff", fg="#4a5568")
        self.lbl_ideal.pack(pady=2)

        self.lbl_bmr = tk.Label(self.output_card, text="Daily BMR: --", font=("Segoe UI", 9), bg="#ffffff", fg="#4a5568")
        self.lbl_bmr.pack(pady=2)

        # Risk Analysis Box
        self.lbl_risk_title = tk.Label(self.output_card, text="[ Health Risks / ক্ষতিকর দিক ]", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#e53e3e")
        self.lbl_risk_title.pack(pady=(10, 2))

        self.lbl_risk_text = tk.Label(self.output_card, text="--", font=("Segoe UI", 9), bg="#ffffff", fg="#742a2a", wraplength=440, justify="center")
        self.lbl_risk_text.pack(pady=2)

        # Actionable Advice Box
        self.lbl_advice_title = tk.Label(self.output_card, text="[ Health Recommendations / করণীয় ]", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#2b6cb0")
        self.lbl_advice_title.pack(pady=(10, 2))

        self.lbl_advice_text = tk.Label(self.output_card, text="--", font=("Segoe UI", 9), bg="#ffffff", fg="#2c5282", wraplength=440, justify="center")
        self.lbl_advice_text.pack(pady=2)

    def calculate_and_analyze(self):
        try:
            age = int(self.age_entry.get())
            height_cm = float(self.height_entry.get())
            weight_kg = float(self.weight_entry.get())
            gender = self.gender_combo.get()

            if age <= 0 or height_cm <= 0 or weight_kg <= 0:
                raise ValueError

            # 1. Standard Calculations
            height_m = height_cm / 100
            bmi = round(weight_kg / (height_m ** 2), 2)

            min_w = round(18.5 * (height_m ** 2), 1)
            max_w = round(24.9 * (height_m ** 2), 1)

            if gender == "Male":
                bmr = round((10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5)
            else:
                bmr = round((10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161)

            # 2. Dynamic Advice & Risk Assessment
            if bmi < 18.5:
                status = "Underweight (কম ওজন)"
                color = "#dd6b20" # Orange
                risks = "• রোগ প্রতিরোধ ক্ষমতা কমে যাওয়া\n• ক্লান্তি ও দুর্বলতা অনুভব করা\n• হাড় ক্ষয় ও রক্তস্বল্পতার ঝুঁকি"
                advice = "• দৈনিক ক্যালোরি ও প্রোটিন সমৃদ্ধ খাবার বাড়ান\n• শক্তিবর্ধক ব্যায়াম (Strength Training) করুন\n• নিয়মিত পুষ্টিকর স্ন্যাকস খান"

            elif 18.5 <= bmi < 24.9:
                status = "Normal Weight (সঠিক ওজন)"
                color = "#38a169" # Green
                risks = "• ঝুঁকি ন্যূনতম! স্বাস্থ্যকর লাইফস্টাইল বজায় রাখুন।"
                advice = "• বর্তমান সুষম খাদ্যাভ্যাস ধরে রাখুন\n• দৈনিক ৩০ মিনিট হাঁটা বা ব্যায়াম করুন\n• পর্যপ্ত ঘুম ও পানি পান নিশ্চিত করুন"

            elif 25 <= bmi < 29.9:
                status = "Overweight (অতিরিক্ত ওজন)"
                color = "#d69e2e" # Yellow/Amber
                risks = "• টাইপ-২ ডায়াবেটিসের ঝুঁকি বৃদ্ধি\n• রক্তচাপ ও কোলেস্টেরল বৃদ্ধি\n• ফ্যাটি লিভার ও জয়েন্টে ব্যথার সম্ভাবনা"
                advice = "• দৈনিক খাবারের ক্যালোরি ১০-২০% কমান\n• প্রসেসড খাবার ও অতিরিক্ত মিষ্টি এড়িয়ে চলুন\n• দৈনিক অন্তত ৪৫ মিনিট কার্ডিও ব্যায়াম করুন"

            else:
                status = "Obese (অতিরিক্ত স্থূলতা)"
                color = "#e53e3e" # Red
                risks = "• হৃদরোগ ও স্ট্রোকের উচ্চ ঝুঁকি\n• শ্বাসকষ্ট ও স্লিপ অ্যাপনিয়া\n• দীর্ঘমেয়াদী জয়েন্টের মারাত্মক ক্ষতি"
                advice = "• চিকিৎসকের পরামর্শে ডায়েট চার্ট তৈরি করুন\n• কার্বোহাইড্রেট ও তেল-জাতীয় খাবার কমান\n• হাঁটা দিয়ে শুরু করে ধীরে ধীরে শরীরচর্চা বাড়ান"

            # 3. Render Output
            self.lbl_bmi.config(text=f"BMI: {bmi}", fg=color)
            self.lbl_status.config(text=f"Status: {status}", fg=color)
            self.lbl_ideal.config(text=f"Ideal Weight Range: {min_w} kg - {max_w} kg")
            self.lbl_bmr.config(text=f"Daily BMR (Baseline Calories): {bmr} kcal/day")
            
            self.lbl_risk_text.config(text=risks)
            self.lbl_advice_text.config(text=advice)

        except ValueError:
            messagebox.showerror("Invalid Input", "অনুগ্রহ করে বয়স, উচ্চতা এবং ওজনের সঠিক সংখ্যা দিন।")

if __name__ == "__main__":
    app = AdvancedBMISoftware()
    app.mainloop()