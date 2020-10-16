#! bin/bash

mkdir DDM{1..100}

cat > time_till_now.txt <<end_text
nanoseconds since 1970-01-01 00:00:00 UTC:
$(date +%s.%N)
end_text

echo DDM{1..100}/ |xargs -n 1 cp time_till_now.txt
