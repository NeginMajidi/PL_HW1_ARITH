# arith function
current_dir := ${CURDIR}

default: arith

arith: HW1.py
	echo 'python $(current_dir)/HW1.py' > arith
	chmod u+x arith

clean:
	rm -f arith

install: arith