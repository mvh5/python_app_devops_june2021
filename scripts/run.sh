#!/bin/bash

#echo "docker run -itd --name test_api01 --rm mauriciovh05/api_cdk_may:$1"
docker run -itd --name test_api01 -p 3000:3000  --rm mauriciovh05/api_cdk_may:$1 
