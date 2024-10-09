from ohms_law_jh import calcVoltage, calcCurrent, calcResistance, Drive

def test_functions():
    print("Testing standalone functions:")
    print(f"Voltage: 2A × 5Ω = {calcVoltage(2, 5)}V")
    print(f"Current: 10V ÷ 2Ω = {calcCurrent(10, 2)}A")
    print(f"Resistance: 12V ÷ 3A = {calcResistance(12, 3)}Ω")

def test_class():
    ohm = Drive()
    print("\nTesting Drive class methods:")
    print(f"Voltage: 2A × 5Ω = {ohm.calcVoltage(2, 5)}V")
    print(f"Current: 10V ÷ 2Ω = {ohm.calcCurrent(10, 2)}A")
    print(f"Resistance: 12V ÷ 3A = {ohm.calcResistance(12, 3)}Ω")

if __name__ == "__main__":
    test_functions()
    test_class()