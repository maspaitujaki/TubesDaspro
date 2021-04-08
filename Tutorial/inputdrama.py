f = open("korean_drama.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

def parser(dipisah, pemisah):
    split_value = []
    tmp = ''
    for c in dipisah:
        if c == pemisah:
            split_value.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_value.append(tmp)
    return split_value

def convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(3):
    if(i == 0):
      arr_cpy[i] = int(arr_cpy[i])
    elif(i == 2):
      arr_cpy[i] = float(arr_cpy[i])
  return arr_cpy

def convert_line_to_data(line):
  raw_array_of_data = parser(line,",")
  array_of_data = [data.strip() for data in raw_array_of_data]
  return array_of_data

raw_header = lines.pop(0)
header = convert_line_to_data(raw_header)
datas = []

for line in lines:
  array_of_data = convert_line_to_data(line)
  real_values = convert_array_data_to_real_values(array_of_data)
  datas.append(real_values)

def modify_datas(idx, col, value):
  datas[idx][col] = value
# ubah rating goblin jadi 5.5

modify_datas(0, 2, 5.5)

def convert_datas_to_string():
  string_data = ",".join(header) + "\n"
  for arr_data in datas:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ",".join(arr_data_all_string)
    string_data += "\n"
  return string_data



# # misalkan kita ingin membuat entri baru pada datas
# # maka kita meminta masukan untuk entri baru
# new_drama_idx = datas[-1][0] + 1
# new_drama_name = input("What is the drama name? \n>>")
# new_drama_rating = float(input("What is your rating? \n>>"))
# new_drama = [new_drama_idx, new_drama_name, new_drama_rating]

# # setelah punya komponen untuk entri baru, kita masukkan ke datas
# datas.append(new_drama)

new_drama_name = ""
new_dramas = []
new_drama_idx = datas[-1][0] + 1
while(new_drama_name != "stop"):
    new_drama_name = input("What is the drama name? \n >>")
    if (new_drama_name == "stop"):
        continue
    new_drama_rating = float(input("What is your rating? \n>>"))
    new_drama = [new_drama_idx, new_drama_name, new_drama_rating]
    new_dramas.append(new_drama)
    new_drama_idx += 1

datas += new_dramas


datas_as_string = convert_datas_to_string()
f = open("korean_drama.csv", "w")
f.write(datas_as_string)
f.close()