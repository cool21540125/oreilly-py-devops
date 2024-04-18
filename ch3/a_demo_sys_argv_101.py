"""
p69
python a_demo_sys_argv_101.py --a-flag some-value 13
看看會輸出啥...
"""

import sys

if __name__ == "__main__":
    print(f"The 1 argv: '{sys.argv[0]}")
    print(f"The 2 argv: '{sys.argv[1]}")
    print(f"The 3 argv: '{sys.argv[2]}")
    print(f"The 4 argv: '{sys.argv[3]}")
