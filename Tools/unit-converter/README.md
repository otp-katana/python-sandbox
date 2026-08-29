# Unit Converter Engine (Terminal Edition)

A highly polished, modular terminal application built in Python for converting a wide variety of units ranging from standard metrics to financial and digital measurements[cite: 15]. The project relies on a robust UI system utilizing ASCII box-drawing characters and cross-platform screen-clearing logic to deliver a seamless user experience[cite: 15].

## 🚀 Features

- **Advanced Terminal UI:** Features dedicated, beautifully drawn screens for the main menu, unit category selection (source/target), and result display, preventing terminal clutter[cite: 15].
- **Cross-Platform Compatibility:** The UI module dynamically clears the console using `os.system('cls' if os.name == 'nt' else 'clear')`, ensuring clean transitions on both Windows and Unix-based systems[cite: 15].
- **Broad Category Scope:** The architecture is designed to support length, weight, temperature, volume, area, time/speed, currency, fuel consumption, and digital storage conversions[cite: 15].
- **Continuous Loop:** The application runs on a `while` loop, allowing users to make consecutive calculations seamlessly without restarting the script[cite: 14].

## 🛠️ Usage

1. Ensure the `UI.py` module and the main script are in the same directory[cite: 14].
2. Run the main application script from your terminal.
3. Use numeric inputs (e.g., `01`) to navigate through the categorized menus[cite: 14, 15].

## 📌 Architecture Roadmap & Planned Fixes

The current codebase (v1.0) is transitioning from a static prototype to a dynamic engine. The following critical architectural updates are prioritized for the next iteration:

- [ ] **Base-Unit Refactoring:** Replace the exhaustive $N \times N$ `if-elif` combination blocks (`giriş_from` mapped directly to `giriş_to`) with a centralized "Base Unit" logic (e.g., mapping everything to Meters first, then to the target unit)[cite: 14]. This will eliminate repetitive code and drastically reduce bug surfaces.
- [ ] **Result UI Integration:** The core logic currently prints raw float results (e.g., `print(birim_giriş_from / 10)`)[cite: 14]. These outputs need to be routed to the pre-designed `uzunluk_dönüştürücü_result()` screen to maintain visual consistency[cite: 14, 15].
- [ ] **Data Type Validation:** Implement `try-except ValueError` wrappers around `float(input("Birim> "))` prompts to prevent the engine from crashing when non-numeric data is entered[cite: 14].
- [ ] **Dictionary-Based Configuration:** Store the conversion rates (e.g., `1000` for km, `25.4` for inches) inside Python dictionaries instead of hardcoding them into logical operators[cite: 14].
- [ ] **Module Completion:** Activate the remaining categories from the main menu (Weight, Temperature, Data, etc.) following the newly optimized Base-Unit architecture[cite: 15].