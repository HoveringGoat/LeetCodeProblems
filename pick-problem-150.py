import random

def main():
    problems = [6, 135, 58, 68, 30, 76, 48, 73, 289, 383, 205, 290, 202, 219, 128, 228, 57, 452, 71, 150, 224, 141, 138, 92, 25, 82, 61, 86, 146, 101, 105, 106, 117, 114, 112, 129, 124, 173, 222, 236, 199, 637, 102, 103, 530, 230, 98, 130, 133, 399, 207, 210, 909, 433, 127, 208, 211, 212, 77, 52, 79, 108, 148, 427, 918, 74, 162, 153, 502, 373, 295, 67, 190, 191, 137, 201, 172, 149, 198, 139, 322, 300, 120, 64, 63, 97, 72, 123, 188, 221]

    num = random.randint(0, len(problems) - 1)

    print(f"You should do problem: {problems[num]}")
if __name__ == '__main__':
    main()

