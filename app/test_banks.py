from project.banks import banks_data, get_bank_info

print("🔹 All Banks Data:")
print(banks_data)

print("\n🔹 Test 1: Get SBI")
print(get_bank_info("SBI"))

print("\n🔹 Test 2: Get HDFC")
print(get_bank_info("HDFC"))

print("\n🔹 Test 3: Invalid Bank")
print(get_bank_info("XYZ"))