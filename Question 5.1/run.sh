hdfs dfs -mkdir -p /Question5.1/input

wget http://www.textfiles.com/etext/FICTION/defoe-robinson-103.txt
hdfs dfs -copyFromLocal defoe-robinson-103.txt /q51/input

wget http://www.textfiles.com/etext/FICTION/callwild
hdfs dfs -copyFromLocal callwild /Question5.1/input

# Run round 1
hadoop jar ../hadoop-streaming-2.8.1.jar \
-input /Question5.1/input \
-output /Question5.1/out_round1 \
-file ./Round1Mapper.py \
-mapper Round1Mapper.py \
-file ./Round1Reducer.py \
-reducer Round1Reducer.py

# Run round 2
hadoop jar ../hadoop-streaming-2.8.1.jar \
-input /Question5.1/out_round1 \
-output /Question5.1/out_round2 \
-file ./Round2Mapper.py \
-mapper Round2Mapper.py \
-file ./Round2Reducer.py \
-reducer Round2Reducer.py

# Run round 3
hadoop jar ../hadoop-streaming-2.8.1.jar \
-input /Question5.1/out_round2 \
-output /Question5.1/out_round3 \
-file ./Round3Mapper.py \
-mapper Round3Mapper.py \
-file ./Round3Reducer.py \
-reducer Round3Reducer.py

hdfs dfs -get /Question5.1

cat ./Question5.1/out_round3/part-00000 | python top20.py
