export TYPESENSE_API_KEY=xyz
    
mkdir "$(pwd)"/typesense-data

docker run -p 8108:8108 \
            -v"$(pwd)"/typesense-data:/data typesense/typesense:30.1 \
            --data-dir /data \
            --api-key=$TYPESENSE_API_KEY \
            --enable-cors

docker run -it --env-file=./.env -e "CONFIG=$(cat config.json | jq -r tostring)" typesense/docsearch-scraper:0.11.0
