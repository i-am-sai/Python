import sys
print(sys.path)

def run_all_test():
    return 0

try:
   run_all_test()
except Exception as e:
    print(f"Test suite crashed: {e}")
    sys.exit(1)