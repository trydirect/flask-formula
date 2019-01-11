#!/bin/sh
while ! pmm-admin config --client-name pg1 --server pmm-server
do
    sleep 1
done

pmm-admin add external:metrics postgresql pgexporter:9187
