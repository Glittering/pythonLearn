1.pcre
	sudo ./configure --pre..
	sudo make
	sudo make install
2.apr
	sudo ./configure --pre..
	sudo make
	sudo make install
3.apr-util
	sudo ./configure --pre.. --with-apr=...
	sudo make
	sudo make install
4.apache
	sudo ./configure --pre.. --with-pcre=... --with-included-apr=...
	sudo make
	sudo make install
