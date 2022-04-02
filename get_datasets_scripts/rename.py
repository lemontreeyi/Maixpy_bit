import os

begin_num = 0

dir_root = "./A"
dst_root = "./pic"
file_list = os.listdir(dir_root)
file_list.sort()
total_num = len(file_list)
i = begin_num
for item in file_list:
    if item.endswith('.jpg'):
        src = os.path.join(dir_root, item)
        dst = os.path.join(os.path.abspath(dst_root), str(i) + '.png')

        try:
            os.rename(src, dst)
            print("converting {} to {}".format(src, dst))
            i += 1
        except Exception as e:
            print(f"error:{e}")
            print("rename dir fail")

print("total {} to rename & converted {} pics".format(total_num, i))


