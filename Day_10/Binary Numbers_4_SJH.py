if __name__ == '__main__':
    n = int(input())
    binary_number = bin(n)[2:]
    # 10진수를 2진수로 변환, 이때 2진수로 변환된 숫자 앞에 0b가 붙기 때문에 2번째 자리부터 숫자를 나타내면 된다.
   
    bin_num_list = []
    for num in binary_number:
        bin_num_list.append(num)

    ones_counter = 0
    count_number_list = []
    for i in range(0, len(bin_num_list)):
        if bin_num_list[i] == '1':
            ones_counter += 1
        else:
            count_number_list.append(ones_counter)
            ones_counter =0
    count_number_list.append(ones_counter)

    print(max(count_number_list))
