hdfs dfs -mkdir -p /Question5.2/input

hdfs dfs -copyFromLocal SE.txt /Question5.2/input

hadoop jar ../hadoop-streaming-2.8.1.jar \
-input /Question5.2/input/SE.txt \
-output /Question5.2/out_round_1 \
-file ./SetupMapper.py \
-mapper SetupMapper.py

declare -i n
n=30
for i in $(seq 1 30);
do
    hadoop jar ../hadoop-streaming-2.8.1.jar \
	-input /q52/out_round_$i \
	-output /q52/out_round_$((i+1)) \
	-file ./Mapper.py \
	-mapper Mapper.py \
	-file ./Reducer.py \
	-reducer Reducer.py
done

hdfs dfs -get /Question5.2/out_round_$((n+1))

cat ./Question5.2/out_round_$((n+1)) | python Sorted.py
