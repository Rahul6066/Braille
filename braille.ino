#include <WiFi.h>
#include <LiquidCrystal_I2C.h>

// LCD setup: I2C address 0x27, 16 columns, 2 rows
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(115200);      // Start Serial Monitor
  lcd.init();                // Initialize LCD
  lcd.backlight();           // Turn on LCD backlight
  lcd.setCursor(0, 0);
  lcd.print("Waiting...");
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n'); // Read line from Serial
    lcd.clear();

    // Line 1: first 16 characters
    lcd.setCursor(0, 0);
    lcd.print(input.substring(0, 16));

    // Line 2: next 16 characters (if any)
    if (input.length() > 16) {
      lcd.setCursor(0, 1);
      lcd.print(input.substring(16, 32));
    }
  }
}
