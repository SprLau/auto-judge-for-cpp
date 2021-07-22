times=1
while [ $times -le "$1" ]
do
	python data.py
	g++ test.cpp -o test
	g++ std.cpp -o std
	python read.py | ./std > stdout
	python read.py | ./test > testout
	python diff.py
	let times+=1
	rm test
	rm std
	rm stdout
	rm testout
	rm data.txt
done
