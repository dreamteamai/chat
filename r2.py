import os
# 檔案讀取
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 轉換
def convert(lines):
	person = None
	tony_word_count = 0
	fish_word_count = 0
	tony_sticker_count = 0
	fish_sticker_count = 0
	tony_image_count = 0
	fish_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'tony':
			if s[2] == '貼圖':
				tony_sticker_count += 1
			elif s[2] == '圖片':
				tony_image_count += 1
			else:
				for m in s[2:]:
					tony_word_count += len(m)
		elif name == '那芝魚':
			if s[2] == '貼圖':
				tony_sticker_count += 1
			elif s[2] == '圖片':
				fish_image_count += 1
			else:
				for m in s[2:]:
					fish_word_count += len(m)
	print('tony說了', tony_word_count, '個字')
	print('tony傳了', tony_sticker_count, '個貼圖')
	print('tony傳了', tony_image_count, '張圖片')
	print('那芝魚說了', fish_word_count, '個字')
	print('那芝魚傳了', fish_sticker_count, '個貼圖')
	print('那芝魚傳了', fish_image_count, '張圖片')

		#print(s)


# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n') 



def main():
	lines = read_file('[LINE]那芝魚.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)


main()