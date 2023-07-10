# alfis_last_blockbot
Telegram bot that writes the number of the last block in the alfis blockchain
```
 export BOT_API_TOKEN=<API_TOKEN>
```
```
git clone https://github.com/RNDpacman/alfis_last_blockbot.git
cd ./alfis_last_blockbot
docker buildx build -t alfis_last_block .
docker compose up -d
docker compose logs -f alfis_last_block
```
