from fib import create_seq,locate_num


data = input()
seq = []
seq_mapper = {}
while data != "Stop":
    split_data = data.split()
    if split_data[0] == "Create":
        n = int(split_data[-1])
        seq = create_seq(n)
        seq_mapper = {val:idx for idx,val in enumerate(seq)}
        print(*seq)
    elif split_data[0] == "Locate":
        num = int(split_data[-1])
        print(locate_num(num,seq_mapper))
    data= input()