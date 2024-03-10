# Add echos to this
echo Starting flask server
docker build --tag sampleflask ./sampleflask/
docker run -d -p 5000:5000 --name flaskserver --restart unless-stopped sampleflask

# Starting pihole
cd ./pihole
docker compose up -d
cd ../

# Starting nginx
docker build --tag ng ./nginx
docker run -d -p 80:80 --name nginxserver --restart unless-stopped ng

echo containers created
docker ps
echo dhcp reserve an ip. make it ur default dns server. add custom dns records in /admin