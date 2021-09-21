---
title: Sưu tầm một số ý tưởng tạo obsidian
---
# Sưu tầm một số ý tưởng tạo obsidian

## Notes:
- https://joschuasgarden.com/: 
	- Trang dùng [[Obsidian]] để tạo những trích dẫn, tham khảo [[Kinh thánh]]
	- Tham khảo thêm hướng dẫn trên [obsidian forum](https://forum.obsidian.md/t/bible-study-in-obsidian-kit-including-the-bible-in-markdown/12503?u=joschua)
	- Bản dịch các ngôn ngữ ở trên trang [kinh thánh gateway](https://www.biblegateway.com/versions/Vietnamese-Bible-Easy-to-Read-Version-BPT/#booklist), tool sẽ download bản dịch tương ứng với câu lệnh
	- Trên trang gateway có [[Các bản dịch tiếng Việt Kinh Thánh trên BibleBateway]]:  ^2385af
		- BD2011: Bản dịch 2011
		- NVB: New Vietnamese Bible
		- BPT: [[Vietnamese Bible Easy-To-Read Version]]
	- Cách cài đặt, download thánh kinh ra md, tham khảo [hướng dẫn](https://github.com/mkudija/BibleGateway-to-Obsidian-Catholic)
		- vào link github, clone https://github.com/selfire1/BibleGateway-to-Obsidian
		```
	 	git clone https://github.com/selfire1/BibleGateway-to-Obsidian.git
	 	cd BibleGateway-to-Obsidian
	 	git submodule init
	 	git submodule update
		```
	 	- Copy `bg2obs.sh` và file `bg2md.rb` của submodule vào chung 1 folder
	 	- Install `ruby` trên windows, rồi install `gem`, dùng gem install một số library
		```
		gem install colorize optparse clipboard
		```
		- Mở mingwin/gitbash lên và run `bash bg2obs.sh -i -v BPT`
			- BPT là một phiên bản tiếng việt [[#^2385af]], lưu ý, trong khi download không nên can thiệp vào clipboard



