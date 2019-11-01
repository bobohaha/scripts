data=$1
echo $data
curl -H 'Content-Type: application/json; charset=utf-8' -H 'Host: m.ipalfish.com' -H 'User-Agent: okhttp/3.11.0' --data-binary $data --compressed 'https://m.ipalfish.com/klian/ugc/interactclass/classroomtime/hold'